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
            script {
                // 1. Report Unit Test results (Works fine)
                if (fileExists('python-results.xml')) {
                    junit 'python-results.xml'
                }
                
                // 2. Archive Coverage Report (Since Cobertura plugin is broken)
                // This makes the coverage.xml available in the Jenkins UI
                if (fileExists('coverage.xml')) {
                    archiveArtifacts artifacts: 'coverage.xml', fingerprint: true
                }
            }
        }
        success {
            echo 'SUCCESS: Build and SonarQube Analysis completed.'
            // If you have a real email server, uncomment the line below:
            // mail to: 'your-email@example.com', subject: 'Build Success', body: '...'
        }
        failure {
            echo 'FAILURE: The build has failed.'
        }
    }
}




