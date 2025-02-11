# Rocket App

[![FastAPI](https://img.shields.io/badge/FastAPI-%23121011.svg?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

**Rocket App** is a modern, FastAPI-based API designed to send templated emails using a minimal yet robust codebase. The application is containerized with Docker, making it easy to deploy and scale. Leveraging FastAPI-Mail and Jinja2 for HTML templating, Rocket App provides an efficient solution for sending visually appealing email notifications.

---

## Features

- **Email Templating:** Uses Jinja2 to render HTML email templates.
- **FastAPI Integration:** Robust API endpoints built with FastAPI.
- **Dockerized:** Ready for containerized deployment using Docker.
- **Configurable:** Uses environment variables for secure configuration.
- **Visual Attachments:** Supports image attachments in emails.
- **Simple & Minimal:** Clean codebase designed for easy maintenance and scalability.

---

## Visual Overview

### Architecture Diagram

Below is an example diagram that illustrates the overall architecture of Rocket App. *(Replace `assets/architecture_diagram.png` with your actual diagram image if available.)*



### Email Preview

Here’s a sample screenshot of the email template generated by the app:

![Email Template Screenshot](assets/rocket.png)

---

## Directory Structure

```plaintext
altech001-rocket_app/
├── Dockerfile
├── main.py
├── model.py
├── rocket.py
├── requirements.txt
├── assets/
└── templates/
    └── rocket_feed.html
```