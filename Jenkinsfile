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
            /*    sh 'git clone https://github.com/bot-TempsModernes/lambda-project.git' */
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Linter') {
            steps {
                sh "flake8 ."
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest -v'
            }
        }
        stage('Deliver') {
            agent none
            steps {
		 script {
                    if (currentBuild.result == null || currentBuild.result == 'SUCCESS') {
                        timeout(time: 3, unit: 'MINUTES') {
                            // you can use the commented line if u have specific user group who CAN ONLY approve
                            //input message:'Approve deployment?', submitter: 'it-ops'
                            input message: 'Approve deployment?'
                        }
                    }
                 }
                 echo "Stage Deliver"
            }
        }
        post {
            always {
                echo 'One way or another, I have finished'
                deleteDir() /* clean up our workspace */
            }
        }
}
