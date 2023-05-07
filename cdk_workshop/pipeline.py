from aws_cdk import (aws_codecommit as codecommit,
 pipelines as pipelines,
 Stack)

from constructs import Construct
from .Stage_file import StageFile

class Pipeline(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        repo = codecommit.Repository(self, 'CodeCommitRepository32',repository_name= "refreshcommit32")
        pipeline = pipelines.CodePipeline(
            self, 'pipelinerefresh32',
            cross_account_keys=True, 
            
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.code_commit(repo, "main"),
                

            # Builds our source code outlined above into a could assembly artifact
                commands=[
                    'npm install -g aws-cdk', # Installs the cdk cli on Codebuild
                    #'cd cdk.out',
                    'pip install -r requirements.txt',
                    "npx cdk synth",
                    # Instructs codebuild to install required package
                ],
                
                primary_output_directory = './cdk.out' 
            ),
        )
        
        test =  StageFile(self, "test")
        test_stage = pipeline.add_stage(test)
        
        
        deploy = StageFile(self, "website")
        deploy_stage = pipeline.add_stage(deploy)
        