pipeline {
    agent any

    stages {
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
    pipeline {
    agent any

    stages {

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

        stage('Archive HTML Report') {
            steps {
                archiveArtifacts artifacts: 'reports/report.html', fingerprint: true
            }
        }
    }
}
}