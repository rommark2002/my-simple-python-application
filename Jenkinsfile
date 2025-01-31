pipeline {
    environment {
        registry = 'rommark2002/class-17-repo'
        image = 'class17-docker-build-publish-pipeline'
        repo = 'https://github.com/rommark2002/my-simple-python-application.git'
    }
   agent {
       label 'my-node'    
            }

    stages {
        stage('Git Checkout/clone repo') {
            steps {
                git credentialsId: 'jenkins-github-access-token2', url: "$repo", branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $image .' 
            }
        }
        stage('Docker tag image') {
            steps {
                sh 'docker tag $image:latest $registry:latest'
                sh 'docker tag $image:latest $registry:$BUILD_NUMBER'
            }
        }
        stage('Push docker image to repo') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'jenkins-docker-access-token', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
                  sh "echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin"
                  sh 'docker push $registry:latest'
                  sh 'docker push $registry:$BUILD_NUMBER'
                }
            }
        }
    }
    post {
    success {
    // One or more steps need to be included within each condition's block.
    slackSend   color: 'good',
                message: 'Docker image pushed successfully',
                channel: '#class17',
                tokenCredentialId: 'slack-jenkins-integration'
    }
    failure {
    // One or more steps need to be included within each condition's block.
    slackSend   color: 'danger',
                message: 'Docker pipeline failed terribly',
                channel: '#class17',
                tokenCredentialId: 'slack-jenkins-integration'
  }
}
}
