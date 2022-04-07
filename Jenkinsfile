pipeline {

  agent any
  
  stages {
    
    stage('setup') {
      steps {
        sh 'python3 -m pip install -r requirements.txt'
      }
    }
    
    stage("build") {
      steps {
        sh'python3 manage.py migrate'
      }
    }
    
    stage("test") {
      steps {
        echo 'testing'
      }
    }
  }
}
