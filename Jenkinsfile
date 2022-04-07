pipeline {

  agent any
  
  stages {
    
    stage("build") {
      sh'python3 manage.py migrate'
      }
    }
    
    stage("test") {
      echo 'testing'
    }
  }
}
