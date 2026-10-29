
pipeline {
    agent {
        label 'instagram-docker'
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        timeout(time: 20, unit: 'MINUTES')
    }

    environment {
        CI_IMAGE = 'instagram-clone:ci'
        CI_SECRET_KEY = 'temporary-ci-secret-for-tests-only'
        WEB_DOMAIN = 'localhost,127.0.0.1'
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
                    docker build -t "$CI_IMAGE" .
                '''
            }
        }

        stage('Django System Check') {
            steps {
                sh '''
                    set -eu
                    docker run --rm \
                        --entrypoint python \
                        -e SECRET_KEY="$CI_SECRET_KEY" \
                        -e WEB_DOMAIN="$WEB_DOMAIN" \
                        "$CI_IMAGE" \
                        manage.py check
                '''
            }
        }

        stage('Automated Tests') {
            steps {
                sh '''
                    set -eu
                    docker run --rm \
                        --entrypoint python \
                        -e SECRET_KEY="$CI_SECRET_KEY" \
                        -e WEB_DOMAIN="$WEB_DOMAIN" \
                        "$CI_IMAGE" \
                        manage.py test accounts api --verbosity 2
                '''
            }
        }
    }

    post {
        success {
            echo 'CI pipeline passed: Docker build, Django check, and automated tests!'
        }

        failure {
            echo 'CI pipeline failed. Review the stage logs.'
        }

        always {
            sh 'docker image rm "$CI_IMAGE" || true'
        }
    }
}
