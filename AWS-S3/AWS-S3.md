# AWS S3 with Python Boto3

## What is AWS S3?

S3 storage refers to blob storage on AWS.

* S3 stands for Simple Storage Service
* Should be accessible from anywhere anytime for any type of data in a unstructured way - dumping it into a bucket (AWS) or container (Azure)
* Can use to host a static website (can't change anything on the page, not dynamic or receiving data from a database) on the cloud
* Blobs need to be stored inside of a bucket
* Default setting - everything is private
* If blobs are public, then you will have a URL/endpoint to access them from anywhere
* Redundancy built-in , back ups available
* Can be accessed from the AWS Console, AWS CLI, Python Boto3

## Setting up our own S3 bucket

### Step 1.

Start by launching a new instance on AWS only need to allow ssh for the security group and use the image Ubuntu 22.04.

Now ssh into your instance and update then upgrade with the below commands as usual

```
sudo apt update
sudo apt upgrade -y
```

Next we can check our python version with the below command we need this to be 3.0 or above.

```
python3 --version
```

If Python isn't already installed for whatever reason you can use the below command to get it.

```
sudo apt-get install python3
```

Now we need to install pip the Python package manager.

```
sudo apt-get install-python3-pip -y
```

Next we will install the AWS CLI using the below command.

```
sudo pip install awscli
```

We can also use a useful command to not have to type in this example python3 each time for python commands.

```
alias python=python3
```

Now we need to authenticate rights to AWS by running the below command and entering the necessary details.

```
aws configure
  access key id: "paste id"
  secret access key: "paste key"
  default region name: eu-west-1
  default output format: json
```

We need to check to make sure we can now access the buckets available by using the below command.

```
aws s3 ls
```

## AWS CLI commands

# make bucket
aws s3 mb s3://tech258-lewis-first-bucket

# check in bucket aws 
aws s3 ls s3://tech258-lewis-first-bucket

# copy file into the bucket
aws s3 cp test.txt s3://tech258-lewis-first-bucket 

# create text file with this text in it
echo This is the first line in a test file > test.txt

# download files from bucket in current directory
aws s3 sync s3://tech258-lewis-first-bucket .

# remove file from bucket without asking for confirmation (dangerous)
aws s3 rm s3://tech258-lewis-first-bucket/test.txt

# delete all files in a bucket without asking for confirmation (Very dangerous :warning:)
aws s3 rm s3://tech258-lewis-first-bucket --recursive

# dangerous deletes bucket if there are no files in it
aws s3 rb s3://tech258-lewis-first-bucket

# very dangerous deletes bucket and all file in it
aws s3 rb s3://tech258-lewis-first-bucket --force

# help on s3 commands or a specific one
aws s3 help
aws s3 rb help

## Python Boto3 commands

Using Python boto3 (separate Python scripts for each)... 

First we need to install Boto3 by using the below command

```
sudo pip install boto3
```

List all the S3 buckets 
```
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
```

Create an S3 bucket (named tech257-ramon-test-boto3 or similar) 

```
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Bucket name
bucket_name = 'tech258-lewis-test-boto3'

# Specify the region where the bucket will be created
region = 'eu-west-1'  


# Create S3 bucket with the specified region
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})

print(f"Bucket '{bucket_name}' created successfully in region '{region}'.")
```

Upload data/file to the S3 bucket 

```
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Bucket name
bucket_name = 'tech258-lewis-test-boto3'

# Local file path
local_file_path = '/home/ubuntu/test.txt'

# S3 object key (file name in S3)
s3_object_key = 'test.txt'

# Upload file to S3 bucket
s3.upload_file(local_file_path, bucket_name, s3_object_key)

print(f"File '{local_file_path}' uploaded to bucket '{bucket_name}' as '{s3_obj>
```

Download/retrieve content/file from the S3 bucket 

```
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Bucket name
bucket_name = 'tech258-lewis-test-boto3'

# S3 object key (file name in S3)
s3_object_key = 'test.txt'

# Local file path to save downloaded file
local_file_path = '/home/ubuntu/test/test.txt'

# Download file from S3 bucket
s3.download_file(bucket_name, s3_object_key, local_file_path)

print(f"File '{s3_object_key}' downloaded from bucket '{bucket_name}' to '{local_file_path}'.")
 
```

Delete content/file from the S3 bucket 

```
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Bucket name
bucket_name = 'tech258-lewis-test-boto3'

# S3 object key (file name in S3)
s3_object_key = 'test.txt'

# Delete file from S3 bucket
s3.delete_object(Bucket=bucket_name, Key=s3_object_key)

print(f"File '{s3_object_key}' deleted from bucket '{bucket_name}'.")
```

Delete the bucket 

```
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Bucket name
bucket_name = 'tech258-lewis-test-boto3'

# Delete bucket
s3.delete_bucket(Bucket=bucket_name)

print(f"Bucket '{bucket_name}' deleted successfully.")
```








