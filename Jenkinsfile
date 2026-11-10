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

    post {
        success {
            withCredentials([
                string(credentialsId: 'webex-token', variable: 'WEBEX_TOKEN'),
                string(credentialsId: 'webex-room-id', variable: 'WEBEX_ROOM_ID')
            ]) {
                sh '''
                    curl -sS -X POST https://webexapis.com/v1/messages \
                      -H "Authorization: Bearer $WEBEX_TOKEN" \
                      -H "Content-Type: application/json" \
                      --data-binary @- <<EOF
{"roomId":"$WEBEX_ROOM_ID","text":"Jenkins build SUCCESS: ${JOB_NAME} #${BUILD_NUMBER}"}
EOF
                '''
            }
        }

        failure {
            withCredentials([
                string(credentialsId: 'webex-token', variable: 'WEBEX_TOKEN'),
                string(credentialsId: 'webex-room-id', variable: 'WEBEX_ROOM_ID')
            ]) {
                sh '''
                    curl -sS -X POST https://webexapis.com/v1/messages \
                      -H "Authorization: Bearer $WEBEX_TOKEN" \
                      -H "Content-Type: application/json" \
                      --data-binary @- <<EOF
{"roomId":"$WEBEX_ROOM_ID","text":"Jenkins build FAILED: ${JOB_NAME} #${BUILD_NUMBER}"}
EOF
                '''
            }
        }
    }
}