import aws_cdk as core
import aws_cdk.assertions as assertions
import aws_cdk as Matchmodule


from aws_cdk import integ_tests_alpha as integ_tests_alpha

from aws_cdk.assertions import Template
from aws_cdk import aws_lambda as _lambda
from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack


def test_s3bucket():
    app = core.App()
    stack1 = CdkWorkshopStack(app,"cdk-workshop")
    template = assertions.Template.from_stack(stack1)
    
    template.has_resource_properties("AWS::Lambda::Function",{
        "Runtime": "python3.9",
        "Handler": "lambda.lambda_handler",
    })

def test_lambda_integ():
    app = core.App()
    stack1 = CdkWorkshopStack(app,"cdk-workshop")
    template = assertions.Template.from_stack(stack1)
    lambdaintgtest = _lambda.Function(
            stack1, 'lambdaintgtest',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambda'),
            handler='lambda.lambda_handler',
        )
    integtest = integ_tests_alpha.IntegTest(app, "IntegTest",
    test_cases=[stack1]
    )
    
    invoke = integtest.assertions.invoke_function(
        function_name=lambdaintgtest.function_name
    )
    invoke.expect(integ_tests_alpha.ExpectedResult.object_like({
    "Payload": "200"
}))
   