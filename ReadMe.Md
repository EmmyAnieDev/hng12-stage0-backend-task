# HNG Stage 0 Task - Basic Information API

This is a simple REST API built with Python Flask that returns basic information including an email address, current datetime, and GitHub repository URL.

## Description

This API provides a single endpoint that returns:

- The developer's email address
- Current datetime in ISO 8601 format (UTC timezone)
- GitHub repository URL containing the project codebase

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/EmmyAnieDev/hngx-stage0-basic-information-api.git
   cd hngx-stage0-basic-information-api
   ```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install flask flask-cors
```

4. Run the application:

```bash
python app.py
```

The API will be available at `http://localhost:5001`

## API Documentation

### Endpoint

- URL: `GET /`
- Method: `GET`

### Response Format

```json
{
  "email": "emmanuelekwere19@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/EmmyAnieDev/hngx-stage0-basic-information-api.git"
}
```

### Example Usage

You can test the endpoint using curl:

```bash
curl http://localhost:5001/
```

Or in your browser: http://localhost:5001/

## Deployment

This API is deployed at: https://hng12-stage0-backend-task.onrender.com

## Related Links

- [Python Developers](https://hng.tech/hire/python-developers)
- [C# Developers](https://hng.tech/hire/csharp-developers)
- [Golang Developers](https://hng.tech/hire/golang-developers)
- [PHP Developers](https://hng.tech/hire/php-developers)
- [Java Developers](https://hng.tech/hire/java-developers)
- [NodeJS Developers](https://hng.tech/hire/nodejs-developers)