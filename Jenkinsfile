pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python3 --version'
      }
    }
    stage('main') {
      steps {
        git branch: 'main', url: 'https://github.com/Profferd/DevOpsLab1.git'
        bat 'python3 main.py'
      }
    }
  }
}
