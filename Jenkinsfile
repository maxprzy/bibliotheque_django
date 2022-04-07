pipeline {
	agent any

	stages {

		stage("build") {
			
			steps {
				sh 'python3 manage.py migrate'
			}
		}

		stage("testing") {

			steps {
				echo "testing"
			}
		}
	}
}
