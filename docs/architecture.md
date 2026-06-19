# Architecture Document

## Architecture Overview

The Enterprise Access Management Portal uses a modular authentication architecture that separates user interface, API routing, authentication utilities, service logic, data models, and database persistence.

## High-Level Architecture

```text
User
↓
Streamlit Dashboard
↓
Authentication Workflow
↓
User Service
↓
SQLite Database
```
## API Architecture

```text
API Consumer
↓
FastAPI Authentication Endpoint
↓
Auth Service Layer
↓
Password / JWT / Role Utilities
↓
SQLite Database
```
## Authentication Flow

```text
User Registration
↓
Validate Username
↓
Hash Password
↓
Store User Record
↓
Login Request
↓
Verify Password
↓
Generate JWT Token
↓
Validate Role Access
```
## Folder Structure

```text
enterprise-access-management-portal/
├── data/
│   └── enterprise_access.db
├── docs/
│   └── images/
├── src/
│   ├── api/
│   ├── auth/
│   ├── dashboard/
│   ├── database/
│   ├── models/
│   └── services/
├── tests/
├── README.md
├── main.py
└── requirements.txt
```
## Design Principles
* Separation of concerns
* Secure password handling
* Token-based authentication
* Role-based authorization
* Database-backed access control
* Test-driven validation
* Portfolio-ready architecture