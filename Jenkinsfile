pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('main') {
      steps {
        git branch: 'main', url: 'https://github.com/Profferd/DevOpsLab1.git'
        sh 'python3 main.py'
      }
    }
  }
}
