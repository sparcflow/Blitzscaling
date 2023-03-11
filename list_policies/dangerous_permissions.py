import boto3, csv, logging, coloredlogs


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")

# the following are just examples and need to be more carefully tuned.

write_actions = [":put", ":insert", ":update", ":add", ":create", ":attach", ":pass"]
read_actions = [":get", ":describe", ":decrypt"]

read_sensitive_services = ["secretsmanager:", "ssm:", "kms:"]
write_sensitive_services = ["iam:", "secretsmanager:", "ssm:", "kms:", "dynamodb:", "rds:", "eks:", "lambda:"]

admin_policy_names = ["fullaccess", "admin"]


def check_dangerous_permission(action, resource, policy_name):
    action, resource, policy_name = action.lower(), resource.lower(), policy_name.lower()

    # default policies
    if any(key in policy_name for key in admin_policy_names):
        return True

    # admin access
    if action == "*" or any(key in action for key in [" *", "* "]):
        return True

    # wildcard iam:*, etc.
    if any(f"{key}*" in action for key in write_sensitive_services):
        return True

    if any(key in action for key in write_actions) and any(key in action for key in write_sensitive_services):
        return True

    if any(action.startswith(key) for key in read_actions) and (
        resource == "*" or any(key in resource for key in [" *", "* "])
    ):
        return True

    return False

