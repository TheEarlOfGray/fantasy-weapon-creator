pipeline{
    agent any
    environment{
        DOCKERHUB_LOGIN=credentials('DOCKERHUB_LOGIN')
    }
    stages{
        stage('Testing app'){
            steps{
                sh "bash scripts/tests.sh"
            }
        }
        stage('Install dependencies'){
            steps{
                sh "bash scripts/dependencies.sh"
            }
        }
        stage('Build containers'){
            steps{
                sh "docker login -u ${DOCKERHUB_LOGIN_USR} -p ${DOCKERHUB_LOGIN_PSW}"
                sh "bash scripts/containers.sh"
            }
        }
        stage('Running ansible tasks'){
            steps{
                sh "bash scripts/ansible.sh"
            }
        }
    }
}