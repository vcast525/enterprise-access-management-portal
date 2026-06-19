# Technical Design Document

## Solution Overview

The Enterprise Access Management Portal is a Python-based authentication and authorization application that demonstrates secure user registration, login, password hashing, JWT token generation, protected API routes, and role-based access control.

## Technology Stack

- Python
- FastAPI
- Streamlit
- SQLite
- JWT
- Password Hashing Utilities
- Pytest
- Git
- GitHub

## Solution Components

### API Layer

Located in:

```text
src/api/auth_api.py
```
Responsible for exposing authentication-related endpoints.

### Authentication Layer

Located in:

```text
src/auth
```
Responsible for:

* Password hashing
* Password verification
* JWT creation
* JWT validation
* Role validation

### Dashboard Layer

Located in:

```text
src/dashboard/access_dashboard.py
```
Provides a Streamlit interface for access management workflows.

### Database Layer

Located in:

```text
src/database/database.py
```
Responsible for SQLite database connection and persistence.

### Model Layer

Located in:

```text
src/models/user_model.py
```
Defines the user data model.

### Service Layer

Located in:

```text
src/services/
```
Responsible for user registration, login validation, and database-backed user operations.

### Testing Layer

Located in:

```text
tests/
```
Validates user models, password utilities, JWT logic, role validation, database behavior, login functionality, and user services.
## Data Flow

```text
User
↓
Streamlit Dashboard / FastAPI API
↓
Authentication Service
↓
Password Hashing / JWT Utilities
↓
SQLite User Database
↓
Role-Based Access Result
```

