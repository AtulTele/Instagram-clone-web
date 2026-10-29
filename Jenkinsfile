
pipeline {
    agent {
        label 'instagram-docker'
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        timeout(time: 20, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Tooling') {
            steps {
                sh '''
                    set -eu
                    git --version
                    python3 --version
                    docker version
                '''
            }
        }

        stage('Django System Check') {
            steps {
                sh '''
                    set -eu
                    docker build -t instagram-clone:ci .
                    docker run --rm \
                        --entrypoint python \
                        instagram-clone:ci \
                        manage.py check
                '''
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }
        failure {
            echo 'CI pipeline failed. Review the stage logs.'
        }
        always {
            sh 'docker image rm instagram-clone:ci || true'
        }
    }
}
