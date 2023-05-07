from constructs import Construct
import unittest
import pytest
from unittest.mock import MagicMock
from aws_cdk.assertions import Template
from aws_cdk import aws_lambda as _lambda
from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack


def test_refresh_count():
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
       
        # Set up mock event and context objects
        event = {}
        context = MagicMock()
        
        my_lambda = _lambda.Function(
            self, 'refreshlambda32',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambda'),
            handler='lambda.lambda_handler',
        )

        # Call the Lambda function handler
        response = my_lambda(event, context)

        # Verify that the response is a dictionary with a "count" key
        self.assertIsInstance(response, dict)
        self.assertIn('count', response)

        # Verify that the "count" value is initially zero
        self.assertEqual(response['count'], 0)

        # Call the Lambda function handler again to simulate a page refresh
        response = my_lambda(event, context)

        # Verify that the "count" value has increased by one
        self.assertEqual(response['count'], 1)
