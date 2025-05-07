# Docker Image Optimization and Security

## 🚀 Project Overview
This project focuses on containerizing a Node.js or Python application using Docker within a VirtualBox-based Ubuntu environment. The goal is to build **lightweight**, **optimized**, and **secure** Docker images using best practices.

## 🎯 Key Objectives
- Set up Docker on Ubuntu (inside VirtualBox)
- Create and containerize a sample Node.js/Python app using Docker
- Optimize the image using:
  - Alpine base images
  - Multi-stage builds
  - `.dockerignore` to exclude unnecessary files
- Improve security by:
  - Avoiding root users
  - Scanning images with tools like **Trivy** or **Docker Scan**

## ⚙️ Technologies Used
- Ubuntu (inside VirtualBox)
- Docker & Docker CLI
- Trivy or Docker Scan (for security)
- Dive (for image analysis)
- Visual Studio Code (for development)

## 📦 Key Docker Commands Used
```bash
cd /mnt/c/Users/kaviy/Downloads/Myproject/Myproject
docker build -t myproject-image .
docker run -d -p 8080:80 myproject-image
docker images
dive my-static-site
trivy image my-static-site
