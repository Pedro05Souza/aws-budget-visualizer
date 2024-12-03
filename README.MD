# ⚙️ AWS Budget Display Tool  

A simple, user-friendly solution to monitor and manage your AWS budgets effortlessly! This tool provides a clear snapshot of your budget status, removing the hassle of navigating through the AWS Console.  

---

## ⚠️ Warning  

This project requires the **AWS CLI** to be installed and properly configured on your system.  

---

### 📥 AWS CLI Installation  

Follow the official guide to install the AWS CLI:  
[Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)  

---

### 🔧 Setting Up AWS CLI Credentials  

Once installed, configure the AWS CLI with your credentials:  
[AWS CLI Quickstart Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html)  

---

> **Note**: Without the AWS CLI and configured credentials, this project will not function as intended. Ensure your setup is complete before proceeding.

---

## 🚀 Features  

- **Real-Time Insights**: Instantly view your AWS budgets and spending limits.  
- **Time-Efficient**: Focus on your priorities with quick access to budget data.
- **API Integration**: Seamlessly integrate with other applications for enhanced functionality.
- **CLI Support**: Execute commands directly from your terminal for a more efficient workflow.  

---

## 🛠️ Getting Started  

Follow the steps below to set up the project and get it running in no time.  

### 1️⃣ Setting Up a Virtual Environment  

#### Create a Virtual Environment  

Run the following command in the root directory of the project:  

```bash
python -m venv venv
```

----

### 2️⃣ Activate the Virtual Environment

### Windows

  ```bash
  venv/Scripts/activate
 ```

Note: If you encounter a permission issue, execute the following command in PowerShell:

  ```bash
 Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
 ```

### macOS/Linux

  ```bash
source venv/bin/activate
 ```

### 📦 Installing Dependencies

 After activating the virtual environment, install the necessary dependencies with:

  ```bash
pip install -r requirements.txt
 ```

---

### 🖥️ Running the Application

There are two main ways to run the application:

- [API](docs/API.MD)
- [CLI](docs/CLI.MD)
