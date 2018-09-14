pipeline {
    agent {
        docker {
            image 'python:alpine3.7'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'apk update && apk upgrade && apk add --no-cache git'
                sh 'rm -rf lambda-project'
                sh 'git clone https://github.com/bot-TempsModernes/lambda-project.git'
                sh 'cd lambda-project'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest -v tests/test_generator.py'
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
