#!/usr/bin/env python3

import aws_cdk as cdk

from cdk.stockmark_stack import StockmarkStack


app = cdk.App()
StockmarkStack(app, "stockmark-stack-dev")

app.synth()
