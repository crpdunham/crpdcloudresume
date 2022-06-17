from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_s3_deployment as s3deploy,
    aws_s3 as s3
)

from hitcounter import HitCounter


class CrpdcloudresumeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # defines and AWS lambda resource
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
        )

        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda,
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter._handler,
        )

# documentation here: https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_s3_deployment/BucketDeployment.html
        website_bucket = s3.Bucket(
            self, "WebsiteBucket",
            website_index_document="index.html",
            public_read_access=True
        )

        s3deploy.BucketDeployment(
            self, "DeployWebsite",
            sources=[s3deploy.Source.asset(
                "./website-dist")],
            destination_bucket=website_bucket,
            destination_key_prefix="web/static"
        )

# Pyhton Refrence for CDK https://docs.aws.amazon.com/cdk/api/v1/python/index.html
