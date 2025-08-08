# aws-iam-key-cleanup
# 🛡️ AWS IAM Access Key Cleanup Automation

This project is an AWS serverless solution to automatically detect and disable stale IAM access keys. It helps organizations improve their security posture by enforcing best practices around key rotation and cleanup.
![architecture](https://github.com/user-attachments/assets/2184c627-87e2-48c3-b8e5-b60d14accee2)


---

## 🚀 Features

- Detects IAM users with access keys older than 90 days
- Disables old keys automatically
- Sends notification via Amazon SNS
- Runs daily using EventBridge Scheduler
- 100% Serverless (Lambda + Python + IAM + SNS)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/github/license/jaythagreat1/aws-iam-key-cleanup) 
![Python](https://img.shields.io/badge/python-3.12%2B-blue)

---

## 🧰 Architecture

- **AWS Lambda (Python)**: Main logic to evaluate and disable old keys
- **Amazon EventBridge**: Triggers Lambda daily
- **Amazon SNS**: Sends notification emails
- **IAM**: Roles and policies for access control

---

## 📆 Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone (https://github.com/jaythagreat1/aws-iam-key-cleanup).git
cd aws-iam-key-cleanup
```
<!-- ✅ Replace `johnathanhorner` with your GitHub username -->

### 2. Edit Lambda Script

- Update `lambda_function.py` with your **SNS topic ARN** and key age threshold (default: 90 days)
![lambda-script](https://github.com/user-attachments/assets/07cebf8f-a3fd-49ed-870f-c7adb6441d53)

### 3. Zip and Upload Lambda Code

```bash
zip function.zip lambda_function.py
```

- Go to AWS Console → Lambda → Create Function
  - Runtime: Python 3.12 or latest supported version
  - Upload the `function.zip` file

### 4. Create IAM Role for Lambda

#### Trust Policy (`trust-policy.json`):
![inline-policy](https://github.com/user-attachments/assets/6d5a9c81-27dd-4784-98c2-6558e06e3963)

#### Permissions Policy (`iam-role-policy.json`):
![InactiveAccessKeysAlertPolicy ](https://github.com/user-attachments/assets/b9c9e5bd-84a0-47e8-b9b9-4ca2e8bd5bac)

- Attach both policies to the IAM role
- Attach this IAM role to your Lambda function as its **Execution Role**

📌  This Lambda execution role provides the permissions required for the function to:
- List IAM users and access keys

- Get last used dates for keys

- Disable access keys

- Publish notifications to SNS


### 5. Create SNS Topic and Subscribe

- Go to Amazon SNS
  - Create a topic (e.g., `iam-key-alerts`)
   ![sns-topic](https://github.com/user-attachments/assets/04f9ffd8-6c6e-4243-a885-9739c47ef477)
  - Add your email as a subscriber
  - Confirm the subscription via email
    ![email-confirm](https://github.com/user-attachments/assets/a5519185-ad40-47e8-9c64-f2bbded43136)


### 6. Create EventBridge Scheduler

- Go to **Amazon EventBridge > Scheduler**
- Create a new schedule:
  - **Schedule type**: `rate(1 day)`
  - **Target**: your Lambda function
  - **Flexible time window**: 5 Mins
  ![eventbridge-rule](https://github.com/user-attachments/assets/2104e4a9-102a-47b0-89ea-5391757bb51d)
  - **Target**: your Lambda function
  ![lambda-func2](https://github.com/user-attachments/assets/f6c0a3fb-e770-460f-b92b-d2e6f18f0748) 

---

## 📧 Email Sample
![email-sample](https://github.com/user-attachments/assets/aebebe96-d42f-404c-80a1-f50126b5e568)

---

## 📁 Files

| File                   | Description                          |
| ---------------------- | ------------------------------------ |
| [`lambda_function.py`](./lambda_function.py)| Main AWS Lambda function logic that checks IAM users' access key activity |
| [`README.md`](./README.md)| Project overview, setup instructions, and architecture explanation |
| [`iam-role-policy.json`](./iam-role-policy.json) | IAM policy that allows the Lambda to list IAM users, update access keys, and send SNS alerts |
| [`trust-policy.json`](./trust-policy.json)| Trust relationship policy to allow Lambda to assume the execution role |
| [`LICENSE`](./LICENSE) | MIT License for this project |

## 🏗️ Architecture
![sys-desi2](https://github.com/user-attachments/assets/56fdd6c1-d42a-4dd2-b44c-9209d309722a)

## ✅ Setup Steps

1. Create a new IAM Role with the provided policies
2. Deploy Lambda with the Python code
3. Set SNS topic ARN as an environment variable
4. Schedule Lambda using EventBridge (e.g., daily trigger)

---

## 🤔 Why This Matters

Outdated IAM keys pose a serious security risk. This project enforces a proactive, automated cleanup to stay compliant with AWS security best practices and protect against unauthorized access.


## 🙌 Contributing

Pull requests and suggestions are welcome!

---

## 🔗 Author

**Johnathan Horner**  
[LinkedIn](https://www.linkedin.com/in/johnathan-horner-99b37782/)  
[GitHub](https://github.com/jaythagreat1/)

 



  
