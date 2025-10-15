# 🧾 sample-python-sec-review

## 📘 Project Overview
This project is a simple Python Flask web app created for a **Security Code Review Lab**.  
It shows how insecure coding (like storing plain passwords) can be improved with better security practices.  
The project has two versions:
- **Main branch:** vulnerable version (insecure code)  
- **Feature/auth-module branch:** fixed version (secure code)

---

## 📁 Project Structure
```
sample-python-sec-review/
│
├── app.py                 # Main Flask app
├── auth.py                # Authentication functions
├── requirements.txt       # Python dependencies
├── .env (optional)        # Environment variables (for secret key)
└── README.md              # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites
Make sure you have:
- Python 3.8 or newer  
- pip (Python package installer)  
- Git (for cloning and managing branches)

---

### 2️⃣ Clone the repository
```bash
git clone url
cd sample-python-sec-review
```

---

### 3️⃣ Create and activate a virtual environment
**Windows (PowerShell):**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

### 5️⃣ (Optional) Create an `.env` file for your secret key
In the project folder, create a file named `.env` and add:
```
SECRET_KEY=your_strong_secret_key_here
```

---

### 6️⃣ Run the Flask app
```bash
python app.py
```

If Flask starts correctly, you’ll see:
```
 * Running on http://127.0.0.1:5000/
```

Now open your browser and go to:
👉 http://127.0.0.1:5000/

---

## 🧠 How to Use
1. Go to `/register` to create a new user.  
2. Then go to `/login` and sign in.  
3. The homepage will show your logged-in username.  
4. Use the secure branch to test the safer version of authentication.

---

## 🔐 Security Improvements in the Secure Branch
- Passwords are **hashed using bcrypt** instead of stored as plain text.  
- The Flask `secret_key` is loaded from an **environment variable**.  
- **Debug mode** is turned off.  
- Basic **input validation** added to registration and login.

---

## 🧩 Branches
| Branch | Description |
|--------|--------------|
| `main` | Vulnerable version (insecure baseline) |
| `feature/auth-module` | Secure version (bcrypt, env vars, no debug) |

---

## 🧾 License
This project is for **educational purposes only**.  
It is not meant for production use.
