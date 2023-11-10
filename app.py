#!/usr/bin/env python3
import os
import sys

from aws_cdk import App

from route53_cdk_dyndns.route53_cdk_dyndns_stack import Route53CdkDyndnsStack


def get_env_var_or_break(env_var):
    try:
        return os.environ[env_var]
    except KeyError:
        print("Environment variable %s must be set" % env_var)
        sys.exit(1)


app = App()
Route53CdkDyndnsStack(
    app,
    "route53-cdk-dyndns",
    hosted_zone_id=get_env_var_or_break("R53_HOSTED_ZONE_ID"),
    zone_name=get_env_var_or_break("R53_ZONE_NAME"),
    record_name=get_env_var_or_break("R53_RECORD_NAME"),
)

app.synth()
