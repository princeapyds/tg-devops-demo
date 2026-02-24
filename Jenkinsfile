pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-demo-app"
        CONTAINER_NAME = "devops-demo-container"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Stop Old Container') {
            steps {
                echo "Stopping old container if exists..."
                sh """
                docker rm -f ${CONTAINER_NAME} || true
                """
            }
        }

        stage('Run New Container') {
            steps {
                echo "Starting new container..."
                sh """
                docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}
                """
            }
        }
    }

    post {
        success {
            echo "Deployment successful!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
