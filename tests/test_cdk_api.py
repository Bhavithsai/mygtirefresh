import aws_cdk as core
import aws_cdk.assertions as assertions
import aws_cdk as Matchmodule

from aws_cdk import aws_apigateway as apigw

from aws_cdk.assertions import Template

from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack

def test_apigw():
    app = core.App()
    stack = CdkWorkshopStack(app,"cdk-workshop")
    template = assertions.Template.from_stack(stack)
    
    template.has_resource_properties(
        "AWS::ApiGateway::RestApi",
        {
            "Name":"refreshapi"
        })
    template.has_resource("AWS::ApiGateway::Stage", {
        "Properties": {
           "StageName": "prod"
        }
    })
integration_responses=[
                apigw.IntegrationResponse(
                    status_code='200',
                    response_parameters={
                        'method.response.header.Access-Control-Allow-Headers': "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                        'method.response.header.Access-Control-Allow-Methods': "'OPTIONS,GET,POST'",
                        'method.response.header.Access-Control-Allow-Origin': "'*'"
                    }
                )
            ]