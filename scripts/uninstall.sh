#!/bin/bash

set -xe

SYSTEMD_DIR=/etc/systemd/system

systemctl stop route53_cdk_dyndns.timer || true
systemctl disable route53_cdk_dyndns.timer || true
rm -f $SYSTEMD_DIR/route53_cdk_dyndns.service
rm -f $SYSTEMD_DIR/route53_cdk_dyndns.timer
