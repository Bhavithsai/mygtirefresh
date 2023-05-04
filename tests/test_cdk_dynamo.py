import aws_cdk as core
import aws_cdk.assertions as assertions
import aws_cdk as Matchmodule

from aws_cdk.assertions import Template

from cdk_workshop.pipeline import Pipeline



def test_codecommit():
    app = core.App()
    stack1 = core.Stack(app, 'Pipeline', env={'region': 'ap-northeast-1'})
    template = assertions.Template.from_stack(stack1)
    
    template.has_resource("AWS::CodeCommit::Repository", {
        "Name": "refreshcommit32"
   }),