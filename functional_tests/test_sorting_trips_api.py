from unittest import TestCase
from app import create_app
import json
from random import shuffle


class SortingTripAPITest(TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_sorting_trip_request(self):
        # We are preparing data with aur boarding cards
        data_to_send = [
            {'transportation': 'train', 'origin': 'Madrid', 'destination': 'Barcelona',
             'seat': '45B'},
            {'transportation': 'airport bus', 'origin': 'Barcelona', 'destination': 'Girona Airport',
             'seat': None},
            {'transportation': 'airplane', 'origin': 'Girona Airport', 'destination': 'Stockholm',
             'flight': 'SK455', 'seat': '3A', 'gate': '45B', 'ticket_counter': '344'},
            {'transportation': 'airplane', 'origin': 'Stockholm', 'destination': 'New York JFK',
             'flight': 'SK22', 'seat': '7B', 'gate': '22', 'automatic_baggage_transfer': True},
        ]

        # Now, they are randomly shuffled
        shuffle(data_to_send)

        # We want them in order, and in human language
        response = self.client.post(
            url_for('api.trip_sorter'),
            data=json.dumps(data_to_send)
        )

        expected_result = "1. Take train 78A from Madrid to Barcelona. Sit in seat 45B.\n" \
                          "2. Take the airport bus from Barcelona to Girona Airport. No seat assignment.\n" \
                          "3. From Girona Airport, take flight SK455 to Stockholm. Gate 45B, seat 3A." \
                          "Baggage drop at ticket counter 344.\n" \
                          "4. From Stockholm, take flight SK22 to New York JFK. Gate 22, seat 7B." \
                          "Baggage will we automatically transferred from your last leg.\n" \
                          "5. You have arrived at your final destination.\n"

        self.assertTrue(response.status_code, 200)
        self.assertEqual(response.data, expected_result)
