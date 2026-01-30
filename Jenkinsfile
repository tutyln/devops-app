pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Kod GitHub uzerinden guncellendi.'
            }
        }

        stage('Docker Build') {
            steps {
                // DNS hatasini cozen kritik hamle
                sh 'docker build --network host -t devops-app:ci .'
            }
        }
        
        stage('Cleanup') {
            steps {
                echo 'Eski Docker imagelari temizleniyor...'
                sh 'docker image prune -f'
            }
        }
    }
}
