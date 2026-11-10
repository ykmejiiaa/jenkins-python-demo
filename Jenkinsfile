pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Python application'
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running Python unit tests'
                sh 'python3 -m unittest -v'
            }
        }
    }
}