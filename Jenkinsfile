pipeline {
    agent none
    stages {
        stage('Build') {
            agent none
            steps {
                echo "Stage build"
            }
        }
        stage('Test') {
            agent none
            steps {
                echo "Stage Test"
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
            agent none
            steps {
                echo "Stage Deliver"
            }
        }
    }
}
