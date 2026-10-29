
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
                    echo "Checking installed tools..."
                    git --version
                    python3 --version
                    docker version
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    set -eu
                    docker build -t instagram-clone:ci .
                '''
            }
        }

        stage('Django System Check') {
            steps {
                sh '''
                    set -eu
                    docker run --rm \
                        --entrypoint python \
                        -e SECRET_KEY=ci-only-temporary-secret-not-for-production \
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
