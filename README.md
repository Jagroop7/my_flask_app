# 🚀 Flask S3 File Upload App

A Python Flask web application that allows users to upload files directly to **AWS S3** through a simple browser interface. Deployed on **AWS EC2** with IAM Role-based authentication.

---

## 🌐 Live Demo

> App is live at: `http://99.79.42.68:8080`

---

## 📋 Features

- Upload files to AWS S3 from the browser
- List all uploaded files stored in S3
- Secure AWS authentication using **IAM Role** (no hardcoded credentials)
- Deployed on AWS EC2 (Ubuntu 22.04)
- Clean and simple UI

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python / Flask | Backend web framework |
| AWS EC2 | Cloud server hosting |
| AWS S3 | File storage |
| AWS IAM Role | Secure, credential-free authentication |
| boto3 | AWS SDK for Python |
| python-dotenv | Environment variable management |
| HTML / CSS / JavaScript | Frontend UI |
| Git / GitHub | Version control |
| Linux (Ubuntu 22.04) | Server OS |

---

## 📁 Project Structure

```
my_flask_app/
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Frontend UI
├── .env                # Environment variables (not committed to GitHub)
├── .gitignore          # Ignores .env and venv
└── requirements.txt    # Python dependencies
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.x
- AWS Account with S3 bucket created
- EC2 instance (Ubuntu 22.04 recommended)

### 1. Clone the repository
```bash
git clone https://github.com/Jagroop7/my_flask_app.git
cd my_flask_app
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install flask boto3 python-dotenv
```

### 4. Configure environment variables
Create a `.env` file in the root directory:
```
AWS_BUCKET_NAME=your-bucket-name
AWS_REGION=ca-central-1
```
> ⚠️ **Note:** If running on EC2 with an IAM Role attached, AWS credentials are handled automatically — no access keys needed in `.env`!

### 5. Run the app
```bash
python app.py
```

Visit `http://localhost:8080` in your browser.

---

## ☁️ AWS Deployment (EC2)

This app is deployed on AWS EC2. Here's the deployment setup:

- **Instance:** t2.micro (Ubuntu 22.04 LTS)
- **Security Group:** HTTP (port 8080) open to the internet, SSH restricted to My IP
- **IAM Role:** `my-flask-app-role` with `AmazonS3FullAccess` policy attached to EC2
- **S3 Bucket:** `my-flask1-bucket` (ca-central-1 region)

---

## 🔒 Security

- AWS credentials are **never hardcoded** in the code
- IAM Role attached to EC2 instance for secure, automatic S3 access
- `.env` file is listed in `.gitignore` and never pushed to GitHub
- SSH access restricted to authorized IP only

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Home page with upload UI |
| POST | `/upload` | Upload a file to S3 |
| GET | `/list-files` | List all files in S3 bucket |

---

## 👩‍💻 Author

**Jagroop Kaur**  
[LinkedIn](https://linkedin.com/in/jagroopkaur) | [GitHub](https://github.com/Jagroop7)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
