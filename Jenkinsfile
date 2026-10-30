
pipeline {
    agent {
        label 'instagram-docker'
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        timeout(time: 30, unit: 'MINUTES')
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
                    trivy --version
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    set -eu

                    echo "Building Django application image..."
                    docker build -t "$CI_IMAGE" .
                '''
            }
        }

        stage('Django System Check') {
            steps {
                sh '''
                    set -eu

                    echo "Running Django system checks..."

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

                    echo "Running account and API tests..."

                    docker run --rm \
                        --entrypoint python \
                        -e SECRET_KEY="$CI_SECRET_KEY" \
                        -e WEB_DOMAIN="$WEB_DOMAIN" \
                        "$CI_IMAGE" \
                        manage.py test accounts api --verbosity 2
                '''
            }
        }

        stage('Trivy Security Report') {
            steps {
                sh '''
                    set -eu

                    echo "Generating complete vulnerability report..."

                    trivy image \
                        --scanners vuln \
                        --format json \
                        --output trivy-report.json \
                        --no-progress \
                        "$CI_IMAGE"

                    echo "Displaying HIGH and CRITICAL vulnerabilities..."

                    trivy image \
                        --scanners vuln \
                        --severity HIGH,CRITICAL \
                        --exit-code 0 \
                        --no-progress \
                        "$CI_IMAGE"

                    echo "Security report generated successfully."
                '''
            }
        }
    }

    post {
        success {
            echo 'CI passed: Docker build, Django checks, tests, and security report generation.'
        }

        failure {
            echo 'CI failed. Review the stage logs and archived reports.'
        }

        always {
            archiveArtifacts(
                artifacts: 'trivy-report.json',
                allowEmptyArchive: true
            )

            sh '''
                docker image rm "$CI_IMAGE" || true
            '''
        }
    }
}
