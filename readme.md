# App Success prediction service

This repository is backend web-app based on FastAPI, that leverages several ML algorithms (Random Forest, Clustering) to predict and analyze the impact of the app metrics on its success, based on a large dataset provided by Google Play Store.

## Setup

#### 1. Make sure you are using python v3.12.5:

```bash
python --version
Python 3.12.5
```

#### 2. Clone the repository

```bash
git clone https://github.com/hady-awayda/hackathon-backend.git hackathon-backend
```

#### 3. Navigate into the cloned directory

```bash
cd hackathon-backend
```

#### 4. Install dependencies:

```bash
pip install fastapi uvicorn scikit-learn pydantic joblib python-jose python-dotenv sqlalchemy email-validator passlib pymysql bcrypt pandas cryptography
```

#### 5. Start the application:

```bash
python -m app.main
```

#### 6. Now the application is running on:

```bash
http://localhost:8000
```

#### 7. For the Redocly API Documentation from OpenAPI, in your browser, navigate to:

```bash
http://localhost:8000/redoc
```

#### 8. For the OpenAPI Specification 3.0 API Documentation (Swagger UI), in your browser, navigate to:

```bash
http://localhost:8000/docs
```

# Testing the APIs

### Register as a new user

# Help & Support

- This app is distributed as an open source project and is free to use for educational purposes
- If you need any help or stumble upon any issues, please don't hesitate to create a pull request, or contact me at hady.awayda@gmail.com.
