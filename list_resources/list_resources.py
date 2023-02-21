import boto3, logging, coloredlogs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")


def get_region(arn):
    region = arn.split(":")[3]
    return region if len(region) > 0 else "global"


def get_service(arn):
    return arn.split(":")[2]


def get_account(arn):
    return arn.split(":")[4]


def run():
    print("service, region, account, arn")
    client = boto3.client("resourcegroupstaggingapi")

    # use paginator to automatically loop over all objects return by the api
    paginator = client.get_paginator("get_resources")
    paginations = paginator.paginate()
    for res in paginations:
        for r in res["ResourceTagMappingList"]:
            service = get_service(r["ResourceARN"])
            region = get_region(r["ResourceARN"])
            account = get_account(r["ResourceARN"])
            print(f"{service},{region},{account},{r['ResourceARN']}")


if __name__ == "__main__":
    run()
