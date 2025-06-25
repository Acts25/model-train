pipeline {
  agent any 
  stages {
    stage('Checkout') {
       steps {
         git branch: 'main', url: 'https://github.com/Acts25/model-train.git'
       }
    }
    stage('Install Dependencies') {
       steps {
         sh 'python3 -m pip install pipx'
         sh 'python3 -m pip install -r requirements.txt'
       }
    }
    stage('Train Model') {
       steps {
         sh 'python3 train.py'
       }
    }
    stage('Test Model') {
       steps {
         sh 'python3 test.py'
       }
    }
    stage('Archive Model') {
       steps {
         archiveArtifacts artifacts: 'model.pkl', fingerprint: true
       }
    }

    }
}
