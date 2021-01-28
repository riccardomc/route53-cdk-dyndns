from aws_cdk import core
import aws_cdk.aws_route53 as route53
from requests import get


class Route53CdkDyndnsStack(core.Stack):
    def __init__(
        self,
        scope: core.Construct,
        construct_id: str,
        hosted_zone_id: str,
        zone_name: str,
        record_name: str,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ip = get("https://api.ipify.org").text

        zone = route53.HostedZone.from_hosted_zone_attributes(
            self,
            "MyZone",
            zone_name=zone_name,
            hosted_zone_id=hosted_zone_id,
        )

        route53.ARecord(
            self,
            "ExternalIP",
            record_name=record_name,
            zone=zone,
            target=route53.RecordTarget.from_ip_addresses(ip),
        )
