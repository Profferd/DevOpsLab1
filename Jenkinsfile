pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('Test') {
      steps {
        git branch: 'main', url: 'https://github.com/Profferd/DevOpsLab1.git'
        bat 'python testMain.py'
      }
    }
  }
}