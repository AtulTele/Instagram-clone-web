# Instagram Clone — DevOps Engineering Project

A Django-based Instagram clone used as a foundation for hands-on DevOps engineering, containerization, CI/CD automation, and deployment practice.

**Original application developer:** [morikeli](https://github.com/morikeli)  
**Original repository:** [morikeli/instagram-clone](https://github.com/morikeli/instagram-clone)  
**DevOps project repository:** [AtulTele/Instagram-clone-web](https://github.com/AtulTele/Instagram-clone-web)

> **Attribution:** The original application was developed by [morikeli](https://github.com/morikeli). This repository builds on that application to practice and demonstrate DevOps engineering. Original application code, design, and assets remain attributable to their respective creators. Please review the original repository's license and applicable attribution requirements.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Original Application Features](#original-application-features)
- [Technology Stack](#technology-stack)
- [DevOps Implementation](#devops-implementation)
- [Architecture and CI/CD Workflow](#architecture-and-cicd-workflow)
- [Project Screenshots](#project-screenshots)
- [Run Locally with Docker](#run-locally-with-docker)
- [Useful Docker Commands](#useful-docker-commands)
- [Roadmap](#roadmap)
- [Acknowledgements](#acknowledgements)

---

## Project Overview

The original project is an Instagram-inspired social media application built with Django and a web frontend.

I am using this application as a practical workload to develop and demonstrate DevOps skills, focusing on containerization, image management, automated testing, Jenkins pipelines, security scanning, and deployment workflows.

The primary learning objective is to build a repeatable, reliable, and security-conscious delivery process around an existing application.

## Original Application Features

The original application includes the following features:

- User authentication: login, signup, and logout
- Follow and unfollow users
- Like and unlike posts
- Comment on posts
- Update user profiles and posts
- Send and receive direct messages
- Receive notifications

## Technology Stack

### Original application

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5, HTMX
- **Database:** SQLite in the current local setup

### DevOps tooling

| Tool | Purpose |
|---|---|
| Docker | Containerize the Django application |
| Docker Compose | Configure and run the application container |
| Docker Hub | Store and distribute the container image |
| Jenkins | Planned CI/CD pipeline automation |
| Git and GitHub | Version control and source-code hosting |
| Trivy | Planned container image security scanning |

Tools marked as planned will be integrated as the project progresses.

## DevOps Implementation

### Completed

- [x] Created a Docker image for the Django application
- [x] Configured Docker Compose for local execution
- [x] Published the application image to Docker Hub

### Planned

- [ ] Configure Jenkins and connect it to GitHub
- [ ] Create a declarative `Jenkinsfile`
- [ ] Automate Django checks and application tests
- [ ] Automate Docker image builds
- [ ] Integrate Trivy image security scanning
- [ ] Push versioned images to Docker Hub through Jenkins
- [ ] Automate deployment to a server
- [ ] Add deployment health checks
- [ ] Integrate monitoring and logging

Only mark a task complete after verifying it works.

## Architecture and CI/CD Workflow

The target workflow is:

```text
Developer
   |
   v
GitHub Repository
   |
   v
Jenkins Pipeline
   |
   +--> Django Checks and Tests
   |
   +--> Docker Image Build
   |
   +--> Trivy Security Scan
   |
   v
Docker Hub
   |
   v
Deployment Server
   |
   v
Application Health Verification
```

This workflow will evolve as additional automation and deployment stages are implemented.

## Project Screenshots

The screenshots below document the **original application interface**.

### Login and Signup

| Login page | Signup page |
|---|---|
| ![Login page](https://github.com/morikeli/Instagram_clone/assets/78599959/cb99eb64-28e1-4ef9-9d64-9b3a5705e7ca) | ![Signup page](https://github.com/user-attachments/assets/077eea84-6b70-4bb3-880a-7801aee7152b) |

### Homepage and User Profile

| Homepage | User profile page |
|---|---|
| ![Homepage](https://github.com/morikeli/Instagram_clone/assets/78599959/285542a1-a1fa-4c23-ad34-9ec91dc4161f) | ![User profile page](https://github.com/user-attachments/assets/647ef183-cc60-4dee-af54-db6cd01941eb) |

### Direct Messages

| Messages page | Messages screen on scroll |
|---|---|
| ![Messages page](https://github.com/user-attachments/assets/d6830ee3-d648-45d8-9da7-d4bfd7415c42) | ![Messages screen on scroll](https://github.com/user-attachments/assets/4ec915cf-794f-43fc-be95-0574082f5150) |

## Run Locally with Docker

### Prerequisites

Install the following:

- Git
- Docker Engine
- Docker Compose plugin

### 1. Clone this repository

```bash
git clone https://github.com/AtulTele/Instagram-clone-web.git
cd Instagram-clone-web
```

### 2. Configure environment variables

Create a local `.env` file based on the environment variables required by the project. Use a strong, private Django `SECRET_KEY` and configure settings appropriate for your environment.

Do not commit `.env` or other secrets to GitHub.

### 3. Build and start the application

```bash
docker compose up -d --build
```

### 4. Check the container status

```bash
docker compose ps
```

### 5. View application logs

```bash
docker compose logs -f web
```

### 6. Open the application

Visit:

http://localhost:8000/auth/login/

The exact environment configuration depends on the current `docker-compose.yml` and Django settings.

**Data note:** The SQLite database and uploaded media are intentionally excluded from Git. A fresh clone may therefore require database initialization and media setup before the application is fully usable. Do not overwrite an existing database or media directory when working with an existing local installation.

## Useful Docker Commands

Rebuild the image:

```bash
docker compose build
```

Start the application:

```bash
docker compose up -d
```

Stop the application:

```bash
docker compose down
```

View logs:

```bash
docker compose logs -f web
```

Run Django checks:

```bash
docker compose exec web python manage.py check
```

Run database migrations:

```bash
docker compose exec web python manage.py migrate
```

Collect static files:

```bash
docker compose exec web python manage.py collectstatic --noinput
```

## Docker Hub

The application image is published under the following repository:

- **Docker Hub image:** [`atultele/instagram-clone:v1`](https://hub.docker.com/r/atultele/instagram-clone)

Pull the image:

```bash
docker pull atultele/instagram-clone:v1
```

This image is a containerized application build. It does not replace the need to configure environment variables, database persistence, uploaded media storage, and other deployment-specific settings.

## Roadmap

My next goals for this project are:

1. Build a Jenkins declarative pipeline.
2. Automate testing and Docker image builds.
3. Add Trivy security scanning.
4. Publish versioned Docker images automatically.
5. Deploy the application to a remote server.
6. Implement monitoring, logging, and health verification.
7. Document operational procedures and troubleshooting.

The goal is to gain practical experience with the same delivery principles used in production DevOps environments.

## Acknowledgements

Special thanks to **[morikeli](https://github.com/morikeli)** for creating the original Instagram clone application that serves as the foundation for this project.

This repository focuses on the DevOps engineering work built around that application. Please visit and star the [original repository](https://github.com/morikeli/instagram-clone) to support the original developer.

---

**Maintainer:** [AtulTele](https://github.com/AtulTele)  
**Project focus:** DevOps, Docker, Jenkins CI/CD, container security, and deployment automation.
