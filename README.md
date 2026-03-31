# RoboHelper: Professional AI Robotics Assistant

RoboHelper is a production-ready, full-stack application that leverages Machine Learning to suggest robotics project ideas based on available electronics components.

---

## 🏗️ Architecture Overview

The system is fully containerized and architected for security and scalability:

- **Frontend**: Vanilla JS SPA served via **Nginx**.
- **Backend**: **Django REST Framework** handling ML logic and data management.
- **Orchestration**: **Docker Compose** managing services, strictly routing all traffic through Nginx (Port 8080).
- **Security**: Backend services are private to the Docker network; only the Nginx proxy is exposed to the host.

---

## 🚀 Quick Start with Docker

Ensure you have **Docker Desktop** installed.

### 1. Build and Launch
From the root directory, run:
```bash
docker-compose up --build
```
This command automatically:
- Builds optimized images.
- Runs database migrations.
- Starts both services in a connected network.

### 2. Access the Application
- **Frontend Hub**: [http://localhost:8080](http://localhost:8080)
- **API Browser**: [http://localhost:8080/api/](http://localhost:8080/api/)
- **Admin Panel**: [http://localhost:8080/admin/](http://localhost:8080/admin/)

---

## ⚠️ Important Notes

### SQLite in Docker
This project currently uses **SQLite** for simplicity. 
> [!WARNING]
> While convenient for development, SQLite has limitations in containerized production:
> - **Concurrency**: Limited support for simultaneous writes.
> - **Persistence**: Ensure the container has persistent volume mounts for the `db.sqlite3` file to avoid data loss.
> - **Recommendation**: For production scaling, switch to **PostgreSQL**.

### Windows Compatibility
The setup is optimized for **Windows (WSL2)**. If you encounter line-ending issues with shell scripts, ensure your Git configuration handles `LF` correctly.

---

## 🛠️ Scalability Recommendations

1. **Database**: Migrate to **PostgreSQL** for robust data handling and concurrency.
2. **WSGI Server**: Use **Gunicorn** or **Uvicorn** instead of the Django development server for handling production traffic.
3. **Environment Variables**: Use `.env` files for secrets and configuration instead of hardcoding values in `settings.py`.
4. **Static Files**: Use `collectstatic` and serve them via Nginx for better performance.
