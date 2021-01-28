#!/bin/bash

ROUTE53_CDK_DYNDNS_PATH=./route53-cdk-dyndns

export AWS_DEFAULT_REGION=
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export R53_HOSTED_ZONE_ID=
export R53_ZONE_NAME=
export R53_RECORD_NAME=

cd $ROUTE53_CDK_DYNDNS_PATH || exit
cdk deploy
