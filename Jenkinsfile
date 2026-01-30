pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Jenkins Pipeline SCM ayarlarından dolayı otomatik çeker
                // ama loglarda görmek iyidir
                echo 'Kod GitHub üzerinden güncellendi.'
            }
        }

        stage('Docker Build') {
            steps {
                // --network host parametresini buraya ekledik
                sh 'docker build --network host -t devops-app:ci .'
            }
        }
        
        stage('Cleanup') {
            steps {
                echo 'Eski (dangling) image'lar temizleniyor...'
                sh 'docker image prune -f'
            }
        }
    }
}
