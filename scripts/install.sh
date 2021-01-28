#!/bin/bash

set -xe

SYSTEMD_DIR=/etc/systemd/system

sed -i "s|^ROUTE53_CDK_DYNDNS_PATH=.*$|ROUTE53_CDK_DYNDNS_PATH=$(pwd)|" ./scripts/run.sh
sed -i "s|^ExecStart=.*$|ExecStart=$(pwd)/scripts/run.sh|" ./scripts/systemd/route53_cdk_dyndns.service
ln -sf "$(pwd)/scripts/systemd/route53_cdk_dyndns.timer" $SYSTEMD_DIR
ln -sf "$(pwd)/scripts/systemd/route53_cdk_dyndns.service" $SYSTEMD_DIR
systemctl daemon-reload
systemctl enable route53_cdk_dyndns.timer
systemctl start route53_cdk_dyndns.timer
