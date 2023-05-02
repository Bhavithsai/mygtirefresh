from constructs import Construct
import aws_cdk as cdk
from aws_cdk import (
    Stage
)
from .cdk_workshop_stack import CdkWorkshopStack

class StageFile(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        
        
        service = CdkWorkshopStack(self, 'RefreshwebStack',env=cdk.Environment(account='353120526419' , region='ap-northeast-1'))