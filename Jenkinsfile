pipeline {
    agent any

    environment {
        IMAGE = 'ghcr.io/tutyln/devops-app'
        REGISTRY = 'ghcr.io'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    test -f Dockerfile
                    test -f index.html
                    grep -q "v3" index.html
                    echo "Tests passed"
                '''
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                    docker build -t ${IMAGE}:v3 .
                '''
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'ghcr-credentials',
                        usernameVariable: 'GH_USER',
                        passwordVariable: 'GH_TOKEN'
                    )
                ]) {
                    sh '''
                        echo "$GH_TOKEN" | docker login ghcr.io \
                          -u "$GH_USER" --password-stdin

                        docker push ${IMAGE}:v3
                        docker logout ghcr.io
                    '''
                }
            }
        }

        stage('Update GitOps Repository') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'github-git-credentials',
                        usernameVariable: 'GIT_USER',
                        passwordVariable: 'GIT_TOKEN'
                    )
                ]) {
                    sh '''
                        git config user.name "Jenkins"
                        git config user.email "jenkins@localhost"

                        git add deployment.yaml kustomization.yaml

                        git commit -m "Deploy application v3 [skip ci]" || true

                        cat > /tmp/git-askpass.sh <<'SCRIPT'
#!/bin/sh
case "$1" in
  *Username*) echo "$GIT_USER" ;;
  *Password*) echo "$GIT_TOKEN" ;;
esac
SCRIPT
                        chmod 700 /tmp/git-askpass.sh

                        GIT_ASKPASS=/tmp/git-askpass.sh \
                        GIT_TERMINAL_PROMPT=0 \
                        git push origin HEAD:main

                        rm -f /tmp/git-askpass.sh
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'V3 image pushed. GitOps deployment updated!'
        }
        failure {
            echo 'Pipeline failed. Check stage logs.'
        }
    }
}
