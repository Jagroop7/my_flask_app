from flask import Flask, request, jsonify, render_template
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
    region_name='ca-central-1'
)

BUCKET_NAME = 'my-flask1-bucket'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    s3.upload_fileobj(file, BUCKET_NAME, file.filename)
    return jsonify({'message': f'{file.filename} uploaded successfully!'})

@app.route('/list-files')
def list_files():
    files = s3.list_objects_v2(Bucket=BUCKET_NAME)
    file_list = [file['Key'] for file in files.get('Contents', [])]
    return jsonify({'files': file_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)





