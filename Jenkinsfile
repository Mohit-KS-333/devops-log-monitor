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
        bat '''
        if not exist reports mkdir reports
        docker run --rm ^
        -v "%cd%\\reports:/app/reports" ^
        log-monitor
        '''
    }
}

        stage('Archive HTML Report') {
            steps {
                archiveArtifacts artifacts: 'reports/report.html', fingerprint: true
            }
        }
    }
}