create_venv:
	python3 -m venv venv
install:
	pip3 install -r requirements.txt
freeze:
	pip3 freeze > requirements.txt
start_server:
	docker-compose up --build
test_data_extractor:
	python3 data_exporter/data_extractor/data_extractor.py