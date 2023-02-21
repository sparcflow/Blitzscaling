import boto3, logging, coloredlogs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")


def list_records(client, zone_id, is_private):
    zone_type = "private" if is_private else "public"

    # use paginator to automatically loop over all objects return by the api
    paginator = client.get_paginator("list_resource_record_sets")

    try:
        source_zone_records = paginator.paginate(HostedZoneId=zone_id, MaxItems="300")
        for record_set in source_zone_records:
            for record in record_set["ResourceRecordSets"]:
                if not record["Type"] in ("A", "CNAME", "AAAA"):
                    continue
                name = record["Name"]
                value = record.get("ResourceRecords", [{"Value": ""}])[0]["Value"]
                print(f"{name}, {value}, {zone_type}")
    except Exception as error:
        print(f"An error occurred getting source zone records:{error}")


def run():
    client = boto3.client("route53")
    response = client.list_hosted_zones()
    logger.info(f'Got {len(response["HostedZones"])} zones')

    print("name, IP/Alias, visibility")
    for zone in response["HostedZones"]:
        list_records(client, zone["Id"], zone["Config"]["PrivateZone"])


if __name__ == "__main__":
    run()
