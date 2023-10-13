pipeline {
    environment {
        registry = 'cmuriukin/class17-repo'
        image = 'class17-docker-build-publish-pipeline'
        repo = 'https://github.com/cmuriukin/my-simple-python-application.git' 
    }
    agent any
    stages {
        stage('Git Checkout/clone repo') {
            steps {
                git credentialsId: 'jenkins-github-access-token', url: "$repo", branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $image .'
            }
        }
        stage('Docker tag image') {
           steps {
               sh 'docker tag $image:latest $registry:latest '
               sh 'docker tag $image:latest $registry:$BUILD_NUMBER'
           } 
        }
        stage('Push docker image to repo') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-access-token', passwordVariable: 'docker_hub_password', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
                  sh "echo $docker_hub_password | docker login -u $DOCKER_HUB_USERNAME --password-stdin"
                  sh 'docker push $registry:latest'
                  sh 'docker push $registry:$BUILD_NUMBER'
                }
            }
        }
    }
}
