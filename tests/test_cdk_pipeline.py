import boto3
import json
import time
import unittest
import aws_cdk as core
from aws_cdk import (
    App,
    Stack,
    aws_lambda as _lambda,
    aws_codepipeline as pipelines,
)
from cdk_workshop.pipeline import Pipeline
from constructs import Construct

class TestPipelineStatus(unittest.TestCase):
    
    def setUp(self):
        self.pipeline_name = 'Pipeline-pipelinerefresh32Pipeline0E8A7B49-1T1G0N7WS0B5U'
        self.client = boto3.client('codepipeline')

   
    def test_source_stage_succeed(self):
        stage_name = 'Source'
        response = self.client.get_pipeline_state(name=self.pipeline_name)
        stage_state = next((x for x in response['stageStates'] if x['stageName'] == stage_name), None)
        while stage_state and stage_state['latestExecution']['status'] == 'InProgress':
            time.sleep(10)
            response = self.client.get_pipeline_state(name=self.pipeline_name)
            stage_state = next((x for x in response['stageStates'] if x['stageName'] == stage_name), None)
        if stage_state is not None:
            self.assertEqual(stage_state['latestExecution']['status'], 'Succeeded')

    def test_build_stage_succeed(self):
        stage_name = 'Build'
        response = self.client.get_pipeline_state(name=self.pipeline_name)
        stage_state = next((x for x in response['stageStates'] if x['stageName'] == stage_name), None)
        while stage_state and stage_state['latestExecution']['status'] == 'InProgress':
            time.sleep(10)
            response = self.client.get_pipeline_state(name=self.pipeline_name)
            stage_state = next((x for x in response['stageStates'] if x['stageName'] == stage_name), None)
        if stage_state is not None:
            self.assertEqual(stage_state['latestExecution']['status'], 'Succeeded')

    def test_deploy_stage_succeed(self):
        stage_name = 'Deploy'
        response = self.client.get_pipeline_state(name=self.pipeline_name)
        stage_state = next((x for x in response['stageStates'] if x['stageName'] == stage_name), None)
        while stage_state and stage_state['latestExecution']['status'] == 'InProgress':
            time.sleep(10)
            response = self.client.get_pipeline_state(name=self.pipeline_name)
            stage_state = next((x for x in response['stageStates'] if x['stageName'] == stage_name), None)
        if stage_state is not None:
            self.assertEqual(stage_state['latestExecution']['status'], 'Succeeded')
        
if __name__ == '__main__':
    unittest.main()