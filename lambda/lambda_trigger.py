import boto3
import json

def lambda_handler(event, context):
    glue = boto3.client('glue')
    
    # Trigger the Glue ETL job
    response = glue.start_job_run(JobName='your-glue-job')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Glue job triggered!')
    }
