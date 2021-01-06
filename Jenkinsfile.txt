pipeline {
    agent any
    stages {
        stage('prepare') {
             steps {
                git credentialsId: 'git-cred', url: 'https://github.com/nada809/DockerProject.git'
                stash name:'scm', includes:'*'
            }
        }
        stage('Build') {
             steps {
                 sh "docker-compose build"
            }
        }
        stage('Test') {
            
            
            steps {
            unstash 'scm'
            script{
                docker.image('python:3.8-slim-buster').inside{ 
                    sh 'pip install -r app/requirements.txt'
                    sh 'python app/unittests.py'
                    
                }
            }
        }
            
        }
       
            
            
        }
    }
