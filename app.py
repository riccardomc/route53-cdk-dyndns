#!/usr/bin/env python3

from aws_cdk import core

from route53_cdk_dyndns.route53_cdk_dyndns_stack import Route53CdkDyndnsStack


app = core.App()
Route53CdkDyndnsStack(app, "route53-cdk-dyndns")

app.synth()
