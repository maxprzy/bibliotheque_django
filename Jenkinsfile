pipeline {

  agent any
  
  stages {
    
    stage('setup') {
      sh 'python3 -m pip install -r requirements.txt'
    }
    
    stage("build") {
      sh'python3 manage.py migrate'
    }
    
    stage("test") {
      echo 'testing'
    }
  }
}
