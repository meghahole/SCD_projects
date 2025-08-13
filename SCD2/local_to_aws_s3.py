import boto3
import os
print(os.getcwd())

# Connecting to AWS S3
s3_resource  = boto3.resource('s3', 'us-east-2') # remember to add your own region of aws s3

# Function to upload file in S3
def s3_upload(file_name,fold,bkt):
    
    s3_bucket = s3_resource.Bucket(name=bkt)

    if True:
        s3_bucket.upload_file(
            Filename = file_name,
            Key = fold + '/' + file_name
            )
        return True


if __name__ == '__main__':

    file_name = 'SCD2\Product_Dim_1.csv'
    s3_folder = 'raw_data'
    bucket = 'bucket-scd2-megha'

    status = s3_upload(file_name, s3_folder, bucket)

    if(status):
        print('Data is saved')
    else:
        print('Error while loading data...')