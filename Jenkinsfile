pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
    steps {
        bat "docker build -t log-monitor:${env.BUILD_NUMBER} -t log-monitor:latest ."
    }
}

        stage('Run Container') {
            steps {
                bat '''
                if not exist reports mkdir reports
                docker run --rm ^
                -v "%WORKSPACE%\\reports:/app/reports" ^
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

    post {

        success {
            emailext(
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
Hello Mohith,

Your DevOps Log Monitoring pipeline completed successfully.

Project : ${env.JOB_NAME}
Build   : #${env.BUILD_NUMBER}
Status  : SUCCESS

View Build:
${env.BUILD_URL}

Regards,
Jenkins CI/CD
""",
                to: "YOUR_GMAIL@gmail.com"
            )
        }

        failure {
            emailext(
                subject: "FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
Hello Mohith,

Your DevOps Log Monitoring pipeline has FAILED.

Project : ${env.JOB_NAME}
Build   : #${env.BUILD_NUMBER}

View Build:
${env.BUILD_URL}

Please check the Jenkins Console Output.

Regards,
Jenkins CI/CD
""",
                to: "mohithk990@gmail.com"
            )
        }

    }
}