# ⚙️ AWS Budget Display Tool  

A simple, user-friendly solution to monitor and manage your AWS budgets effortlessly! This tool provides a clear snapshot of your budget status, removing the hassle of navigating through the AWS Console.  

---

## 🚀 Features  
- **Real-Time Insights**: Instantly view your AWS budgets and spending limits.  
- **Time-Efficient**: Focus on your priorities with quick access to budget data.  

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

### Windows:

  ```bash
  venv/Scripts/activate
 ```

Note: If you encounter a permission issue, execute the following command in PowerShell:


  ```bash
 Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
 ```

### macOS/Linux:
  ```bash
source venv/bin/activate
 ```

 ### 📦 Installing Dependencies
 After activating the virtual environment, install the necessary dependencies with:

  ```bash
pip install -r requirements.txt
 ```

 ### 🖥️ Running the Application
 Once the environment is set up and dependencies are installed, you're ready to go! Start the application with:

   ```bash
python app.py
 ```