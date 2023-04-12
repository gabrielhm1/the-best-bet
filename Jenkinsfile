pipeline {

    agent any
    
    stages {
        stage("build") {
            steps {
                script {
                    dockerImage = docker.build_registry
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