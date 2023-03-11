import boto3, csv, logging, coloredlogs
from dangerous_permissions import check_dangerous_permission

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")


def format_potential_list(input):
    if isinstance(input, list):
        return " ".join(input)
    return input


def get_and_write_statements(statement, entity, entity_name, policy_name):
    if not isinstance(statement, list):
        statement = [statement]
    for elt in statement:
        action = format_potential_list(elt["Action"])
        resource = format_potential_list(elt["Resource"])
        dangerous = check_dangerous_permission(action, resource, policy_name)
        writer.writerow(
            [entity, entity_name, elt["Effect"], action, resource, policy_name, dangerous,]
        )


def extract_attached_policies(attached_policies, entity, entity_name):
    res = []
    for pol in attached_policies:
        pol_version = client.get_policy(PolicyArn=pol["PolicyArn"])["Policy"]["DefaultVersionId"]
        statement = client.get_policy_version(PolicyArn=pol["PolicyArn"], VersionId=pol_version)["PolicyVersion"][
            "Document"
        ]["Statement"]
        policy_name = pol["PolicyName"]
        get_and_write_statements(statement, entity, entity_name, policy_name)

    return res


def extract_inline_policies(inline_policies, client, entity, entity_name):
    res = []
    for pol in inline_policies["PolicyNames"]:
        statement = []
        if entity == "user_policy":
            statement = client.get_user_policy(UserName=entity_name, PolicyName=pol)["PolicyDocument"]["Statement"]
        elif entity == "group_policy":
            statement = client.get_group_policy(GroupName=entity_name, PolicyName=pol)["PolicyDocument"]["Statement"]
        elif entity == "role_policy":
            statement = client.get_role_policy(RoleName=entity_name, PolicyName=pol)["PolicyDocument"]["Statement"]

        get_and_write_statements(statement, entity, entity_name, "inline")

    return res


def parse_user_groups(username, groups):
    logger.info(f"found {len(groups)} groups for user {username}")
    for gp in groups:
        entity_name = username
        attached_policies = client.list_attached_group_policies(GroupName=gp["GroupName"])["AttachedPolicies"]
        extract_attached_policies(attached_policies, "group_policy", entity_name)
        inline_policies = client.list_group_policies(GroupName=gp["GroupName"])
        extract_inline_policies(inline_policies, client, "group_policy", entity_name)


def check_users(client):
    logger.info("extracting users")
    users = client.list_users()["Users"]
    logger.info(f"Got {len(users)} users")
    for user in users:
        entity_name = user["UserName"]
        logger.info(f"extracting permissions for {entity_name}")
        attached_policies = client.list_attached_user_policies(UserName=user["UserName"])["AttachedPolicies"]
        extract_attached_policies(attached_policies, "user_policy", entity_name)
        inline_policies = client.list_user_policies(UserName=user["UserName"])
        extract_inline_policies(inline_policies, client, "user_policy", entity_name)

        response = client.list_groups_for_user(UserName=entity_name)
        if len(response["Groups"]) > 0:
            parse_user_groups(user["UserName"], response["Groups"])


def check_roles(client):
    logger.info("extracting roles")
    roles = client.list_roles()["Roles"]
    logger.info(f"Got {len(roles)} roles")
    for role in roles:
        entity_name = role["RoleName"]
        if entity_name.startswith("AWSServiceRole"):
            continue
        logger.info(f"extracting permissions for {entity_name}")
        attached_policies = client.list_attached_role_policies(RoleName=role["RoleName"])["AttachedPolicies"]
        extract_attached_policies(attached_policies, "role_policy", entity_name)
        inline_policies = client.list_role_policies(RoleName=role["RoleName"])
        extract_inline_policies(inline_policies, client, "role_policy", entity_name)


def get_caller_identity():
    return boto3.client("sts").get_caller_identity()


if __name__ == "__main__":
    f = open("res.csv", "w")
    writer = csv.writer(f)
    writer.writerow(["Type", "Name", "Effect", "Actions", "Resources", "Policy", "Is dangerous"])

    identity = get_caller_identity()
    logger.info(f"Using {identity['Arn']}")
    client = boto3.client("iam")
    check_roles(client)
    check_users(client)

    f.close()
