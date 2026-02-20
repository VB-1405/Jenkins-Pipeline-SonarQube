pipeline {
    agent any

    environment {
        // Define SonarQube scanner tool name (as configured in Jenkins Global Tool Configuration)
        SCANNER_HOME = tool 'SonarScanner'
    }

    stages {
        stage('Python: Setup & Test') {
            steps {
                dir('Basic Python') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install pytest pytest-cov
                        # Run tests with coverage
                        python3 -m pytest --junitxml=../python-results.xml --cov=. --cov-report=xml:../coverage.xml
                    '''
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') { // 'SonarQube' is the name of the server in Jenkins config
                    sh "${env.SCANNER_HOME}/bin/sonar-scanner"
                }
            }
        }

        stage('Artifact Generation') {
            steps {
                sh 'zip -r mathutils-python.zip "Basic Python" -x "**/venv/**" -x "**/__pycache__/**"'
                archiveArtifacts artifacts: 'mathutils-python.zip', fingerprint: true
            }
        }
    }

    post {
        always {
            junit 'python-results.xml'
        }
        success {
            echo 'Build Successful! Sending notification...'
            // Example email notification (requires Mailer plugin)
            // mail to: 'your-email@example.com', subject: "Build Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}", body: "Check it out at ${env.BUILD_URL}"
        }
        failure {
            echo 'Build Failed! Sending notification...'
            // mail to: 'your-email@example.com', subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}", body: "Review the logs at ${env.BUILD_URL}"
        }
    }
}

