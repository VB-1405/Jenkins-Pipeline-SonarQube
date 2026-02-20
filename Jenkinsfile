pipeline {
    agent any

    stages {
        stage('Python: Setup & Test') {
            steps {
                dir('Basic Python') {
                    // Use python3 -m pip to ensure it's the correct environment
                    sh 'pip install pytest'
                    sh 'pytest --junitxml=../python-results.xml'
                }
            }
        }

        stage('Java: Build & Test') {
            steps {
                script {
                    // Check if the Java directory exists before attempting to run tests
                    if (fileExists('JavaProject')) {
                        dir('JavaProject') {
                            echo '--- Building and Testing Java ---'
                            // This assumes Maven is configured and available in the environment
                            sh 'mvn clean test'
                        }
                    } else {
                        echo 'JavaProject directory not found. Skipping Java tests.'
                    }
                }
            }
        }
    }

    post {
        always {
            // Collect test results for Jenkins reporting
            junit 'python-results.xml'
            script {
                if (fileExists('JavaProject/target/surefire-reports')) {
                    junit 'JavaProject/target/surefire-reports/*.xml'
                }
            }
        }
    }
}
