# 🧠 DataFlowHub – Lightweight ETL System (Django + Celery + Redis)

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
✅ Automatic **transformation and normalization** of JSON with **pandas.json_normalize()**  
✅ Execution logging and statuses (`pending`, `running`, `success`, `failed`)  
✅ **Pagination** of results  
✅ Modular architecture – separation between `core/` and `etl/` apps

---

## 🧩 Planned Features

🔹 ETL from **databases** (PostgreSQL, MySQL, etc.)  
🔹 ETL from **file sources** (CSV, Excel, JSON)  
🔹 **Authentication and Role-based access** – different users with different permissions  
🔹 **Filtering, searching, throttling** in API  
🔹 **Docker** containerization  
🔹 **.env configuration** for production  
🔹 **CI/CD pipeline** (GitHub Actions)  
🔹 **Flake8 / Ruff** for linting  
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
| Database        | SQLite (dev) → PostgreSQL (prod) |
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
pip install -r requirements.txt

# 4️⃣ Run Redis (Docker example)
docker run -d -p 6379:6379 redis

# 5️⃣ Start Celery worker
celery -A dataflowhub worker -l info

# 6️⃣ Run Django server
python manage.py runserver
```

Swagger Docs → [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

---

## 🗺️ Roadmap (Next Steps)

| Step                          | Description                               |
| ----------------------------- | ----------------------------------------- |
| 🧩 Add DB/File source support | Create specialized tasks and transformers |
| 🔒 Add Authentication         | JWT or DRF Token-based system             |
| 🧮 Add Filtering & Searching  | Via DRF filters and query params          |
| 🐳 Add Docker setup           | docker-compose for web + redis + celery   |
| ⚙️ Add CI/CD                  | GitHub Actions workflow                   |
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
