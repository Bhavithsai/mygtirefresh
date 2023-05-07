import os

import aws_cdk as core
import aws_cdk.assertions as assertions

import aws_cdk as Matchmodule

from aws_cdk.assertions import Template

from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack



def test_codecommit():
    app = core.App()
    stack1 = CdkWorkshopStack(app,"cdk-workshop")
    template_dynamo = assertions.Template.from_stack(stack1)
    
def test_dynamodb():
    app = core.App()
    stack1 = CdkWorkshopStack(app,"cdk-workshop")
    template_dynamo = assertions.Template.from_stack(stack1)
    
    template_dynamo.resource_count_is("AWS::DynamoDB::Table", 1)
