pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Kod cekiliyor'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t devops-app:ci .'
            }
        }
    }
}
