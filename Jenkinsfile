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
                // 1. Report Unit Test results
                if (fileExists('python-results.xml')) {
                    junit 'python-results.xml'
                }
                
                // 2. Report Code Coverage (using Cobertura for Python)
                // This requires the Cobertura plugin to be installed in Jenkins
                if (fileExists('coverage.xml')) {
                    cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
                }
            }
        }
        success {
            echo 'Build Successful!'
            // 3. Send Email notification upon success
            // Requires SMTP configuration in Manage Jenkins -> System
            // mail to: 'your-email@example.com',
            //      subject: "SUCCESS: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
            //      body: "The build was successful. Check results at ${env.BUILD_URL}"
        }
        failure {
            echo 'Build Failed!'
            // 3. Send Email notification upon failure
            // mail to: 'your-email@example.com',
            //      subject: "FAILURE: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
            //      body: "The build failed. Review the logs at ${env.BUILD_URL}"
        }
    }
}



