#!/usr/bin/env python3

import aws_cdk as cdk

from crpdcloudresume.crpdcloudresume_stack import CrpdcloudresumeStack


app = cdk.App()
CrpdcloudresumeStack(app, "crpdcloudresume")

app.synth()
