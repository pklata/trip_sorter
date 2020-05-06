from unittest import TestCase
from trip_sorter.boarding_pass import boarding_pass_factory, BoardingPassBase, \
    AirplaneBoardingPass, TrainBoardingPass, AirportBusBoardingPass


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

    def test_boarding_pass_factory_returns_airplane_boarding_pass(self):
        transportation = 'airplane'
        origin = 'Girona Airport'
        destination = 'Stockholm'
        flight = 'SK455'
        seat = '3A'
        gate = '45B'
        ticket_counter = '344'
        automatic_baggage_transfer = True

        raw_boarding_pass_data = {
            'transportation': transportation,
            'origin': origin,
            'destination': destination,
            'flight': flight,
            'seat': seat,
            'gate': gate,
            'ticket_counter': ticket_counter,
            'automatic_baggage_transfer': automatic_baggage_transfer
        }

        boarding_pass = boarding_pass_factory(raw_boarding_pass_data)

        self.assertIsInstance(boarding_pass, AirplaneBoardingPass)
        self.assertEqual(boarding_pass.transportation, transportation)
        self.assertEqual(boarding_pass.origin, origin)
        self.assertEqual(boarding_pass.destination, destination)
        self.assertEqual(boarding_pass.flight, flight)
        self.assertEqual(boarding_pass.seat, seat)
        self.assertEqual(boarding_pass.gate, gate)
        self.assertEqual(boarding_pass.ticket_counter, ticket_counter)
        self.assertEqual(boarding_pass.automatic_baggage_transfer, automatic_baggage_transfer)

    def test_boarding_pass_factory_returns_airport_bus_boarding_pass(self):
        transportation = 'airport bus'
        origin = 'Barcelona'
        destination = 'Girona Airport'
        seat = '44'

        raw_boarding_pass_data = {
            'transportation': transportation,
            'origin': origin,
            'destination': destination,
            'seat': seat
        }

        boarding_pass = boarding_pass_factory(raw_boarding_pass_data)

        self.assertIsInstance(boarding_pass, AirportBusBoardingPass)
        self.assertEqual(boarding_pass.transportation, transportation)
        self.assertEqual(boarding_pass.origin, origin)
        self.assertEqual(boarding_pass.destination, destination)
        self.assertEqual(boarding_pass.seat, seat)

    def test_boarding_pass_factory_returns_train_boarding_pass(self):
        transportation = 'train'
        origin = 'Madrid'
        destination = 'Barcelona'
        seat = '45B'

        raw_boarding_pass_data = {
            'transportation': transportation,
            'origin': origin,
            'destination': destination,
            'seat': seat
        }

        boarding_pass = boarding_pass_factory(raw_boarding_pass_data)

        self.assertIsInstance(boarding_pass, TrainBoardingPass)
        self.assertEqual(boarding_pass.transportation, transportation)
        self.assertEqual(boarding_pass.origin, origin)
        self.assertEqual(boarding_pass.destination, destination)
        self.assertEqual(boarding_pass.seat, seat)
