from unittest import TestCase
from trip_sorter.boarding_pass import boarding_pass_factory, BoardingPassBase


class BoardingPassTest(TestCase):

    def test_boarding_pass_factory_returns_boarding_pass(self):
        transportation = 'airplane'
        origin = 'Stockholm'
        destination = 'New York JFK'

        raw_boarding_pass_data = {'transportation': transportation, 'origin': origin, 'destination': destination}

        boarding_pass = boarding_pass_factory(raw_boarding_pass_data)

        self.assertIsInstance(boarding_pass, BoardingPassBase)
        self.assertEqual(boarding_pass.transportation, transportation)
        self.assertEqual(boarding_pass.origin, origin)
        self.assertEqual(boarding_pass.destination, destination)
