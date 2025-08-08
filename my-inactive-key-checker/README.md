# 🔐 Inactive Access Key Notifier (AWS Lambda)

This project uses an AWS Lambda function to monitor IAM users' access keys and alerts when any keys are inactive. Alerts are sent via SNS.

## 📁 Files

| File                   | Description                          |
| ---------------------- | ------------------------------------ |
| `lambda_function.py`   | Main AWS Lambda function logic that checks IAM users' access key activity |
| `README.md`            | Project overview, setup instructions, and architecture explanation |
| `iam-role-policy.json` | IAM policy that allows the Lambda to list IAM users, update access keys, and send SNS alerts |
| `trust-policy.json`    | Trust relationship policy to allow Lambda to assume the execution role |

## 🏗️ Architecture

Add an architecture diagram here (e.g., `assets/architecture.png`).

## ✅ Setup Steps

1. Create a new IAM Role with the provided policies
2. Deploy Lambda with the Python code
3. Set SNS topic ARN as an environment variable
4. Schedule Lambda using EventBridge (e.g., daily trigger)

## 📝 License

This project is licensed under the MIT License. See `LICENSE` for details.