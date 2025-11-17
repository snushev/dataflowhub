# 🧠 DataFlowHub – Lightweight ETL System (Django + Celery + Redis)

[![DRF](https://github.com/yourusername/dataflowhub/actions/workflows/DRF.yml/badge.svg)](https://github.com/yourusername/dataflowhub/actions/workflows/DRF.yml)

## 📘 Overview

**DataFlowHub** is a lightweight ETL (Extract–Transform–Load) backend built with **Django REST Framework**, designed to automate data extraction and processing tasks.  
The project supports **asynchronous execution via Celery**, using **Redis** as a broker and backend for tasks.

The goal is to build a flexible foundation for ETL jobs that can be defined and triggered via API – from various sources (APIs, databases, files).

---

## ⚙️ Features (so far)

✅ REST API for defining and triggering ETL jobs  
✅ Execution of ETL processes via **Celery tasks**  
✅ **Redis** broker for asynchronous processing  
✅ **Swagger/OpenAPI** documentation  
✅ ETL jobs from **API sources**  
✅ **Filtering** and **searching** in API  
✅ Automatic **transformation and normalization** of JSON with **pandas.json_normalize()**  
✅ Execution logging and statuses (`pending`, `running`, `success`, `failed`)  
✅ **Pagination** of results  
✅ JWT Authentication
✅ Modular architecture – separation between `core/`, `users/` and `etl/` apps
✅ **Throttling** for request limitation
✅ **Permissions** basic IsAuthenticated permissions
✅ **Docker** and **Docker-compose** for quick start
✅ **Flake8** for linting
✅ **GitHub Actions** for basic CI/CD

---

## 🧩 Planned Features

🔹 ETL from **databases** (PostgreSQL, MySQL, etc.)  
🔹 ETL from **file sources** (CSV, Excel, JSON)
🔹 **Pytest** for unit and integration tests  
🔹 Full ETL configuration via **frontend interface** (optional)

---

## 🧱 Tech Stack

| Component       | Technology                       |
| --------------- | -------------------------------- |
| Backend         | Django 5 + Django REST Framework |
| Async Tasks     | Celery                           |
| Message Broker  | Redis                            |
| Data Processing | Pandas                           |
| Database        | PostgreSQL (prod)                |
| API Docs        | drf-spectacular                  |
| Environment     | Python 3.12+                     |

---

## 🚀 Installation & Run (Local Dev)

```bash
# 1️⃣ Clone repository
git clone https://github.com/yourusername/dataflowhub.git
cd dataflowhub

# 2️⃣ Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt  # or: uv pip install -r requirements.txt

# 4️⃣ Run Redis (Docker example)
docker run -d -p 6379:6379 redis

# 5️⃣ Start Celery worker
celery -A dataflowhub worker -l info

# 6️⃣ Run Django server
python manage.py runserver
```

## 🚀 Quick Start with Docker

```bash
# Clone repo
git clone https://github.com/snushev/dataflowhub.git
cd dataflowhub

# Start everything
docker-compose up -d

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Visit
http://localhost:8000/api/schema/swagger-ui/
```

Done! 🎉

Swagger Docs → [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

---

## 🗺️ Roadmap (Next Steps)

| Step                          | Description                               |
| ----------------------------- | ----------------------------------------- |
| 🧩 Add DB/File source support | Create specialized tasks and transformers |
| 🧪 Add Tests                  | With Pytest and Factory Boy               |
| 🎯 Finalize Production Setup  | Environment configs, logs, and monitoring |

---

## 📂 Project Structure

```
dataflowhub/
│
├── core/                  # Core configurations and shared utilities
├── etl/                   # Main ETL logic (models, tasks, transformers)
│   ├── models.py
│   ├── tasks.py
│   ├── transformer.py
│   └── views.py
├── users/                 # Main logic for login and register users
│   ├── models.py
│   ├── serializers.py
│   └── views.py
│
├── dataflowhub/           # Django project config
│
└── README.md
```

---

## 🧠 Author & Vision

This project is built as a practical path toward a **production-ready Django REST backend**, with a real-world ETL use case.  
Once fully completed, it can be used as a foundation for:

- automated integrations between systems
- data synchronization
- backend for analytical dashboards

---

## 📜 License

MIT License © 2025
