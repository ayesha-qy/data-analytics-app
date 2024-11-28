pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'  // Install dependencies
                }
            }
        }
        stage('Test') {
            steps {
                // Run Pytest tests here
                sh 'pytest'
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    docker.build('my-python-app:latest')  // Build Docker image
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Deploy application using kubectl
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
