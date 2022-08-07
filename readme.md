# HAD-GOOGLE-SHEET-EXPORT V3.0.0

## Description

```
This program contains 3 funtions:
1. export data from wrike into google sheets (tasks, folders, contacts and workflows)
2. export all products from the H&D hubspot portal and export them to google sheets
3. export all portal ids that are contained within the MicroApp database and there collection name (table name)
```

## Requirments for running the porject locally

Create a .env file

```
# Global
SENTRY_DSN = ""
GOOGLE_APPLICATION_CREDENTIALS = ""
FLASK_ENV = "development"
FLASK_DEBUG = "true"
HOST = "localhost"
PORT = "8080"

# WRIKE TASKS, FOLDERS, CONTACTS, WORKFLOWS, PROJECTS
WRIKE_KEY=""
WRIKE_FILE = ""

# HUBSPOT MICRO APPS
DATABASE_URL = ""
MONGO_DB = ""
CA_CERT = ""
MICROAPP_FILE = ""
MICROAPP_SHEET = ""

# HUBSPOT PRODUCTS
PRIVATE_APP_KEY = ""
GOOGLE_WORKBOOK = ""
GOOGLE_SHEET = ""

```
