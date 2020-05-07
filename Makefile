# Makefile

build:
	virtualenv -p python3.8 virtualenv
	./virtualenv/bin/pip install -r requirements.txt
	echo "export PYTHONPATH=$PYTHONPATH:$(pwd)" >> ./virtualenv/bin/activate

run:
	./virtualenv/bin/python trip_sorter/app.py

test:
	./virtualenv/bin/python -m unittest discover -v

sample_request:
	curl -H "Content-Type: application/json" -X POST -d '[{"transportation": "airplane", "origin": "Stockholm", "destination": "New York JFK", "flight": "SK22", "seat": "7B", "gate": "22", "automatic_baggage_transfer": true}, {"transportation": "airplane", "origin": "Girona Airport", "destination": "Stockholm", "flight": "SK455", "seat": "3A", "gate": "45B", "ticket_counter": "344"}, {"transportation": "airport bus", "origin": "Barcelona", "destination": "Girona Airport"}, {"transportation": "train", "origin": "Madrid", "destination": "Barcelona", "number": "78A", "seat": "45B"}]'