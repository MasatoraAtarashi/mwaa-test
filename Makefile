export AIRFLOW_HOME=/Users/s15227/ghq/github.com/MasatoraAtarashi/mwaa-test

create-user:
	airflow users create --username admin --firstname Peter --lastname Parker --role Admin --email user@example.com

init-db:
	airflow db init

reset-db:
	airflow db reset

up-web:
	airflow webserver -p 8080

up-scheduler:
	airflow scheduler
