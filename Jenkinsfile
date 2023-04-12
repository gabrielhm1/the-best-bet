pipeline {

    agent any
    
    stages {
        stage("build") {
            steps {
                script {
                    dockerapp = docker.build("app/tbb:latest","-f ./Dockerfile .")
                } 
            }
        }

        stage("test") {
            steps {
                echo "Testing the app..."
            }
            
        }

        stage("Deploy") {
            steps {
                echo "Deploying the app..."
            }
        }
    }
}