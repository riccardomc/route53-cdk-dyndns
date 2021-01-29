# AWS Route53 CDK Dyndns

Recently I bought a small [single-board
computer](https://www.notebookcheck.net/Odyssey-Blue-A-powerful-x86-and-Arduino-machine-that-supports-Windows-10-and-Linux.485011.0.html)
to use at home. I wanted to play around with the [AWS Python
CDK](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html) and I had a
very simple usecase: I wanted to update a Route53 A record set with my home IP address so
I can connect to it wherever I am.

There are other, more simple [ways](https://en.wikipedia.org/wiki/Dynamic_DNS) to achieve
this. Your router might support DynDNS out of the box even. But, meh.

## Prerequisites

I use [Debian](https://www.debian.org/). So, here's a quick way to get the AWS Python CDK
to work on a fresh install:

```
curl -sL https://deb.nodesource.com/setup_12.x | sudo bash -
sudo apt update
sudo apt install nodejs npm python3-pip python3-venv
sudo npm install -g aws-cdk
```

## Installation

Clone this repository:

```
git clone git@github.com:riccardomc/route53-cdk-dyndns.git 
cd route53-cdk-dyndn
```

Install python dependencies:

```
sudo pip3 install -r requirements.txt
```

Fill in the values in `./scripts/run.sh`:

```
export AWS_DEFAULT_REGION=
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export R53_HOSTED_ZONE_ID=
export R53_ZONE_NAME=
export R53_RECORD_NAME=
```

Then install the systemd service and timer by:

```
sudo ./scripts/install.sh
```

You can uninstall by:

```
sudo ./scripts/uninstall.sh
```

## Security

### systemd

The installation mechanism provided is a quick and dirty way to schedule a script to run
at an interval using [systemd](https://en.wikipedia.org/wiki/Systemd). If you are
concerned about security, the executable should be in a proper location as well as the
configuration variables: a user can indeed modify the `run.sh` script to execute
arbitrary code with root privileges. Make sure you are cloning the repository somewhere
safe. 

### AWS

You should avoid using your root AWS credentials for this. Create an IAM user with
restricted actions on the specific services (cloudformation, s3, route53). There's a
policy document in `iam-policy.json` that does this.

## What does it do?

Every 30 minutes (or whatever interval you specify in
`./scripts/systemd/route53_cdk_dyndns.timer`) the stack is redeployed with the external
IP fetched from [api.ipify.org](https://api.ipify.org).

Upon update you should see something like this in your system logs:

```shell
$ sudo journalctl -f
[...]
Jan 29 12:23:48 bluebot systemd[1]: Reloading.
Jan 29 12:23:48 bluebot systemd[1]: Started Route53 Dyndns Timer.
Jan 29 12:23:48 bluebot systemd[1]: Starting Route53 Dyndns Service...
Jan 29 12:23:51 bluebot run.sh[29473]: route53-cdk-dyndns: deploying...
Jan 29 12:23:52 bluebot run.sh[29473]: route53-cdk-dyndns: creating CloudFormation changeset...
Jan 29 12:24:02 bluebot run.sh[29473]:  0/2 | 12:23:57 | UPDATE_IN_PROGRESS   | AWS::CloudFormation::Stack | route53-cdk-dyndns User Initiated
Jan 29 12:24:07 bluebot run.sh[29473]:  0/2 | 12:24:03 | UPDATE_IN_PROGRESS   | AWS::Route53::RecordSet | ExternalIP (ExternalIP007FBEBD)
Jan 29 12:24:38 bluebot run.sh[29473]:  2/2 | 12:24:35 | UPDATE_COMPLETE      | AWS::Route53::RecordSet | ExternalIP (ExternalIP007FBEBD)
Jan 29 12:24:38 bluebot run.sh[29473]:  2/2 | 12:24:37 | UPDATE_COMPLETE_CLEA | AWS::CloudFormation::Stack | route53-cdk-dyndns
Jan 29 12:24:38 bluebot run.sh[29473]:  2/2 | 12:24:38 | UPDATE_COMPLETE      | AWS::CloudFormation::Stack | route53-cdk-dyndns
Jan 29 12:24:38 bluebot run.sh[29473]:  ✅  route53-cdk-dyndns
Jan 29 12:24:38 bluebot run.sh[29473]: Stack ARN:
Jan 29 12:24:38 bluebot run.sh[29473]: arn:aws:cloudformation:eu-west-1:17622514440:stack/route53-cdk-dyndns/afb743a0-60e8-11cb-9b2d-01bbb121180
Jan 29 12:24:38 bluebot systemd[1]: route53_cdk_dyndns.service: Succeeded.
Jan 29 12:24:38 bluebot systemd[1]: Started Route53 Dyndns Service.
[...]
```
