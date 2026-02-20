pipeline {
    agent any

    stages {
        stage('Python: Setup & Test') {
            steps {
                dir('Basic Python') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install pytest pytest-cov
                        python3 -m pytest --junitxml=../python-results.xml --cov=. --cov-report=xml:../coverage.xml
                    '''
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('MySonarQubeServer') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
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
            // Only run junit if the file exists to avoid further errors
            script {
                if (fileExists('python-results.xml')) {
                    junit 'python-results.xml'
                }
            }
        }
        success {
            echo 'Build Successful!'
        }
        failure {
            echo 'Build Failed!'
        }
    }
}


