
# Docker GitHub Actions Deployment

This project demonstrates how to automate CI/CD for a Dockerized Python Flask application using GitHub Actions. The project uses tools like Git, GitHub, Python, Flask, Pytest, Docker, and Docker Hub to create a seamless deployment pipeline.

---

## 📋 Project Overview

The goal of this project is to set up a complete CI/CD pipeline that automates the build, test, and deployment process for a Dockerized Python Flask application whenever code changes are pushed to the `main` branch.

---

## 🛠️ Tools & Technologies Used

- **Python**: Programming language for developing the Flask application.
- **Flask**: Lightweight web framework for building the web application.
- **Pytest**: Testing framework for writing unit tests.
- **Git & GitHub**: Version control and source code management.
- **GitHub Actions**: Automates CI/CD workflows.
- **Docker**: Containerizes the application for consistent deployment.
- **Docker Hub**: Repository for storing and distributing Docker images.
- **Anaconda**: Manages Python environments.
- **Visual Studio Code (VS Code)**: Code editor for development.

---

## 📋 Pre-requisites

Before you begin, ensure you have the following installed on your system:

1. [Python 3.9](https://www.python.org/downloads/)
2. [Anaconda](https://www.anaconda.com/products/distribution) (for managing Python environments)
3. [Git](https://git-scm.com/downloads) (for version control)
4. [Docker](https://www.docker.com/products/docker-desktop) (for containerization)
5. [Visual Studio Code (VS Code)](https://code.visualstudio.com/download) (recommended code editor)
6. [Docker Hub Account](https://hub.docker.com/) (for pushing Docker images)

---

## 🗂️ Project Structure

```
DOCKERGITHUBACTIONSDEPLOYMENT/
├── .github/
│   └── workflows/
│       └── cicd.yml          # GitHub Actions workflow configuration
├── venv/                     # Virtual environment (typically ignored in version control)
├── .gitignore                # Specifies files to ignore in Git (e.g., venv, temporary files)
├── app.py                    # Main application code (Flask app)
├── Dockerfile                # Docker configuration for containerizing the application
├── LICENSE                   # License for the project
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies required by the project
└── test_app.py               # Unit tests for the Flask application
```

---

## 🗺️ Architecture Diagram

```plaintext
           +-----------------+
           |  Developer      |
           +-----------------+
                   |
                   | 1. Push Code (GitHub)
                   v
           +-----------------+
           |  GitHub Repo    |
           | (Source Control)|
           +-----------------+
                   |
                   | 2. Trigger GitHub Actions
                   v
           +--------------------------+
           |  GitHub Actions         |
           |  (CI/CD Pipeline)       |
           +--------------------------+
            |        |          |
  (Build)   |   (Test)    (Dockerize)
            |        |          |
            v        v          v
  +-------------------------------+
  |       Docker Image Build      |
  +-------------------------------+
                   |
                   | 3. Push Docker Image
                   v
           +-----------------+
           |  Docker Hub     |
           +-----------------+
                   |
                   | 4. Deploy Container
                   v
           +-----------------+
           |  Local/Cloud    |
           |  Environment    |
           +-----------------+
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kala-techies/MLOPS.git
cd DOCKERGITHUBACTIONSDEPLOYMENT
```

### 2. Set Up Local Environment

1. **Create and Activate Conda Environment**:
   - Open **Anaconda Prompt** or **Terminal** in VS Code.
   - Create and activate a new environment:
     ```bash
     conda create -n flaskapp python=3.9 -y
     conda activate flaskapp
     ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Application Locally**:
   ```bash
   python app.py
   ```
   - Open your browser and navigate to [http://localhost:5000](http://localhost:5000).

4. **Run Unit Tests**:
   ```bash
   pytest
   ```

---

## 📦 Dockerization

### Manual Way to Build and Publish Docker Image

The manual process is useful for development and testing purposes, allowing you to control each step before automating the pipeline.

1. **Build Docker Image**:
   ```bash
   docker build -t flaskapp .
   ```

2. **Run Docker Container**:
   ```bash
   docker run -p 5000:5000 flaskapp
   ```
   - Open your browser and go to [http://localhost:5000](http://localhost:5000).

3. **Push Docker Image to Docker Hub**:
   ```bash
   docker tag flaskapp:latest yourdockerhubusername/flaskapp:latest
   docker push yourdockerhubusername/flaskapp:latest
   ```
   - This step allows you to share your Docker image with others via Docker Hub.

### Automated Way (CI/CD Pipeline)

The automated process uses GitHub Actions to handle the build, test, and deployment steps whenever changes are pushed to the repository. This ensures consistency and saves time by eliminating manual steps.

---

## 🔄 CI/CD Pipeline (GitHub Actions)

### Pipeline Stages Explained

1. **Build Stage**:
   - **Purpose**: Checks out the code and builds a Docker image to ensure the application is containerized correctly.
   - **Why**: This step verifies that the Dockerfile is correctly configured and the application can be packaged.

2. **Test Stage**:
   - **Purpose**: Sets up Python, installs dependencies, and runs unit tests using Pytest.
   - **Why**: Ensures the application is functioning as expected before deployment.

3. **Publish Stage**:
   - **Purpose**: Logs into Docker Hub, builds a fresh Docker image, and pushes it to Docker Hub.
   - **Why**: Automates the deployment process, allowing others to pull and use the Docker image.

### GitHub Actions Workflow (`.github/workflows/cicd.yml`):

```yaml
name: CI/CD for Dockerized Flask App

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  dockerbuild:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build Docker Image
        run: docker build . --file Dockerfile --tag workflow-test:$(date +%s)

  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest

  build-and-publish:
    needs: build-and-test
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Login to DockerHub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      - name: Build and push Docker image
        uses: docker/build-push-action@v4
        with:
          context: .
          file: ./Dockerfile
          push: true
          tags: ${{ secrets.DOCKER_USERNAME }}/flaskapp:latest
```

---

## 📌 Usage

This project is ideal for:

- **Learning CI/CD**: Understand how to automate build, test, and deployment processes using GitHub Actions.
- **Dockerization**: Learn how to containerize Python applications using Docker.
- **Testing**: Get hands-on experience with writing and running tests using Pytest.
- **Deployment**: Automate deployment to Docker Hub and run containers in a consistent environment.

---

## 🤝 Contributing

We welcome contributions to improve this project! If you're interested in adding features, fixing bugs, or improving documentation:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit:
   ```bash
   git commit -m 'Add new feature'
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

For any questions or suggestions, reach out at **connectwithkala@gmail.com**.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---
