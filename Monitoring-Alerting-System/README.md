# 🛡️ Monitoring and Alerting System (AWS Project)

This project demonstrates a cloud-native monitoring and alerting system using **AWS services** including CloudWatch, SNS, Lambda, and CloudTrail. It automatically monitors key AWS resources (EC2, RDS, ALB), generates alarms, sends notifications, and even performs automatic remediation actions.

## 🔧 Tools & Services Used

- **Amazon EC2** – Hosted a simple portfolio site
- **Amazon CloudWatch** – Monitoring and custom dashboards
- **Amazon SNS** – Email notifications
- **AWS Lambda** – Automatically restarts EC2 instance when alarm is triggered
- **AWS CloudTrail** – Logs user/API activity for auditing

## ✅ Features

- 📊 Monitor EC2, RDS, and ALB metrics
- 📈 Create custom CloudWatch dashboards
- 🚨 Set up CloudWatch Alarms to detect high CPU usage
- ✉️ Use SNS to send email notifications when alarms trigger
- 🤖 Lambda function automatically reboots the EC2 instance
- 🕵️ CloudTrail used to track all AWS activities

## 🧪 How It Works

1. **EC2 instance** is launched with a portfolio website hosted.
2. **CloudWatch Alarm** is created to monitor CPU utilization.
3. **SNS Topic** is subscribed to by email.
4. **Lambda function** is triggered by the alarm to reboot EC2.
5. **CloudTrail** records every action for compliance and auditing.

## 📂 Project Structure

```
Monitoring-Alerting-System/
│
├── lambda-function/
│   └── restart-ec2.py           # Lambda to auto-reboot EC2
│
├── portfolio/
│   └── index.html               # Sample portfolio hosted on EC2
│
├── screenshots/                 # Screenshots showing monitoring setup and results
└── README.md
```

## 🖼️ Recommended Screenshots to Include

- EC2 instance running portfolio site
- CloudWatch dashboard with metrics (EC2, RDS, ALB)
- CloudWatch alarm configuration
- SNS topic and subscription
- Notification email from SNS
- Lambda function config and CloudWatch logs
- CloudTrail logs of triggered events

## 🧹 Cost-Saving Note

All AWS resources were **deleted after testing and screenshot capture** to avoid unnecessary billing.

---

## 📌 Author

**Madhusudhan Anand** 
— Cloud Engineer | AWS Enthusiast  
https://github.com/madhusudhan-anand
