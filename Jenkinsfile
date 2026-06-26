pipeline {
    agent any

    stages {
        stage('Use Docker Context') {
            steps {
                bat 'docker context use desktop-linux'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t log-monitor .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run --rm log-monitor'
            }
        }
    }
}