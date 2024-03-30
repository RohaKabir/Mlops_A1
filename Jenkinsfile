pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t your_image_name:latest .'
                }
            }
        }
        stage('Tag Docker Image') {
            steps {
                script {
                    bat 'docker tag your_image_name:latest roha922/your_image_name:latest'
                }
            }
        }
        stage('Authenticate with Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    bat 'docker push roha922/your_image_name:latest'
                }
            }
        }
    }
}
