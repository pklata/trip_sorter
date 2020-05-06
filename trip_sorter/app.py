from flask import Flask, request
import json
from trip_sorter.journey_organizer import JourneyOrganizer
from trip_sorter.boarding_card import boarding_card_factory


def create_app(name):
    app = Flask(name)

    @app.route('/trip_sorter', methods=['POST'])
    def trip_sorter():
        data = json.loads(request.data)
        journey_organizer = JourneyOrganizer()
        for item in data:
            journey_organizer.add(boarding_card_factory(item))
        return journey_organizer.get_journey_plan()

    return app


if __name__ == '__main__':
    app = create_app(__name__)
    app.run(debug=True)
