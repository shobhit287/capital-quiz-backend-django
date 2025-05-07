# city-quiz-backend-django

This repository hosts the backend of the **Capital City Quiz** application, built using Django.  
The backend handles quiz logic, serves random countries, and verifies user-submitted capital guesses.

---

## 🛠️ Prerequisites

- Python 3.9+ (recommended: 3.12)
- `pip` package manager

---

## 🚀 Setup Instructions

### 1. Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate it (use the command for your OS)
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

---

### 2. Install Dependencies

```bash
pip install -r req.txt
```

---

### 3. Set Environment Variables

Create a `.env` file in the root directory and add the following:

```env
HOST=localhost
PORTAL_URL=http://localhost:3000
```

> ℹ️ Make sure your Django project loads environment variables from the `.env` file, using something like [`python-dotenv`](https://pypi.org/project/python-dotenv/) or `django-environ`.

---

### 4. Run the Development Server

```bash
python manage.py runserver
```

Your server will be running at `http://127.0.0.1:8000` by default.

---

## 🧼 Deactivate the Virtual Environment

```bash
deactivate
```