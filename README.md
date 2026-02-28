# Flask S3 File Upload App

A simple web app built with Python Flask that lets users upload files to AWS S3.

---

## What This App Does

- Upload files from your browser to AWS S3
- View a list of all uploaded files
- Runs on AWS EC2 server

---

## Technologies Used

- Python & Flask
- AWS EC2 (to host the app)
- AWS S3 (to store files)
- AWS IAM Role (for secure access)
- boto3 (Python library for AWS)
- HTML / CSS / JavaScript
- Git & GitHub

---

## How to Run Locally

1. Clone the repo
```bash
git clone https://github.com/Jagroop7/my_flask_app.git
cd my_flask_app
```

2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages
```bash
pip install flask boto3 python-dotenv
```

4. Create a `.env` file and add your details
```
AWS_BUCKET_NAME=your-bucket-name
AWS_REGION=ca-central-1
```

5. Run the app
```bash
python app.py
```

Open your browser and go to `http://localhost:8080`

---

## Deployed On

- AWS EC2 — Ubuntu 22.04, t2.micro
- S3 Bucket — ca-central-1 region
- IAM Role attached to EC2 for secure S3 access (no hardcoded credentials)

---

## Author

**Jagroop Kaur**  
[LinkedIn](https://www.linkedin.com/in/jagroopk) | [GitHub](https://github.com/Jagroop7)

