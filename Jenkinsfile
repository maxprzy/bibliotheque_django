pipeline {
	agent any

	stages {

		stage("build") {
			
			steps {
				sh 'python manage.py migrate'
			}
		}

		stage("testing") {

			steps {
				echo "testing"
			}
		}
	}
}
