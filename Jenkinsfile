pipeline {
	agent any

	stages {

		stage("build") {
			
			steps {
				sh 'python -m pip install -r requirements.txt'
				sh 'export $(cat ./.env | xargs)'
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
