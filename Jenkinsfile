pipeline {
    agent any
   
    stages {

        stage('Run Selenium Tests with pytest') {
            steps {
                    echo "Running Selenium Tests using pytest"

                    // Install Python dependencies
                    bat 'pip install -r requirements.txt'

                    // ✅ Start Flask app in background
                    bat 'start /B python app.py'

                    // ⏱️ Wait a few seconds for the server to start
                    bat 'ping 127.0.0.1 -n 5 > nul'

                    // ✅ Run tests using pytest
                    //bat 'pytest tests\\test_bookmyshow.py --maxfail=1 --disable-warnings --tb=short'
                    bat 'pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t airbnb:v1 ."
            }
        }
        stage('Docker Login') {
            steps {
                  bat 'docker login -u smeghana55 -p Megh@3551'
                }
            }
        stage('push Docker Image to Docker Hub') {
            steps {
                echo "push Docker Image to Docker Hub"
                bat "docker tag airbnb:v1 smeghana55/air:airbnbimage"               
                    
                bat "docker push smeghana55/air:airbnbimage"
                
            }
        }
        stage('Deploy to Kubernetes') { 
            steps {
                bat '''
                    kubectl --kubeconfig="C:\\Users\\megha\\.kube\\config" apply -f deployment.yaml --validate=false
                    kubectl --kubeconfig="C:\\Users\\megha\\.kube\\config" apply -f service.yaml
                '''
            } 
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}