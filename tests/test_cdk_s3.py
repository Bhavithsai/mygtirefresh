import aws_cdk as core
import aws_cdk.assertions as assertions
import aws_cdk as Matchmodule

from aws_cdk.assertions import Template

from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack

def test_s3bucket():
    app = core.App()
    stack1 = CdkWorkshopStack(app,"cdk-workshop")
    template = assertions.Template.from_stack(stack1)
    
    template.has_resource_properties("AWS::Lambda::Function",{
        "Runtime": "python3.9",
        "Handler": "lambda.lambda_handler",
    })
    
 
    
    
   