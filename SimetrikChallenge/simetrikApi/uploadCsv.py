import boto3
import os
from dotenv import load_dotenv
import wget

load_dotenv(verbose=True)

ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')
AWS_BUCKET_NAME = os.getenv('BUCKET_NAME')

bucket_name = 'alkemy-ong'
path_fileDownloaded = '../simetrikApi'

def aws_session(region_name = os.getenv('AWS_REGION')):
  return boto3.session.Session(aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
                              aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'))


bucket_name = 'alkemy-ong'

def upload_file(file_path):
    session = aws_session()
    s3_resource = session.resource('s3')
    file_dir, file_name = os.path.split(file_path)
    
    file = wget.download(file_path, path_fileDownloaded)

    bucket = s3_resource.Bucket(bucket_name)
    bucket.upload_file(
      Filename=file,
      Key=file_name,
      ExtraArgs={'ACL': 'public-read'}
    )

    os.remove(file)

    s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
    return s3_url


