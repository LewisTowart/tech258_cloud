import boto3

# Create an S3 client
s3_client = boto3.client('s3')

# List all S3 buckets
response = s3_client.list_buckets()

# Extract bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print bucket names
for bucket in buckets:
    print(bucket)