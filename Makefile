start_server:
	docker-compose up --build
test_data_extractor:
	python3 data_exporter/data_extractor/data_extractor.py