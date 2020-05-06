from unittest import TestCase
from trip_sorter.boarding_card import boarding_card_factory, BoardingCardBase, \
    AirplaneBoardingCard, TrainBoardingCard, AirportBusBoardingCard


class BoardingCardTest(TestCase):

    def test_boarding_card_factory_returns_boarding_card(self):
        transportation = 'airplane'
        origin = 'Stockholm'
        destination = 'New York JFK'

        raw_boarding_card_data = {'transportation': transportation, 'origin': origin, 'destination': destination}

        boarding_card = boarding_card_factory(raw_boarding_card_data)

        self.assertIsInstance(boarding_card, BoardingCardBase)
        self.assertEqual(boarding_card.transportation, transportation)
        self.assertEqual(boarding_card.origin, origin)
        self.assertEqual(boarding_card.destination, destination)

    def test_boarding_card_factory_returns_airplane_boarding_card(self):
        transportation = 'airplane'
        origin = 'Girona Airport'
        destination = 'Stockholm'
        flight = 'SK455'
        seat = '3A'
        gate = '45B'
        ticket_counter = '344'
        automatic_baggage_transfer = True

        raw_boarding_card_data = {
            'transportation': transportation,
            'origin': origin,
            'destination': destination,
            'flight': flight,
            'seat': seat,
            'gate': gate,
            'ticket_counter': ticket_counter,
            'automatic_baggage_transfer': automatic_baggage_transfer
        }

        boarding_card = boarding_card_factory(raw_boarding_card_data)

        self.assertIsInstance(boarding_card, AirplaneBoardingCard)
        self.assertEqual(boarding_card.transportation, transportation)
        self.assertEqual(boarding_card.origin, origin)
        self.assertEqual(boarding_card.destination, destination)
        self.assertEqual(boarding_card.flight, flight)
        self.assertEqual(boarding_card.seat, seat)
        self.assertEqual(boarding_card.gate, gate)
        self.assertEqual(boarding_card.ticket_counter, ticket_counter)
        self.assertEqual(boarding_card.automatic_baggage_transfer, automatic_baggage_transfer)

    def test_boarding_card_factory_returns_airport_bus_boarding_card(self):
        transportation = 'airport bus'
        origin = 'Barcelona'
        destination = 'Girona Airport'
        seat = '44'

        raw_boarding_card_data = {
            'transportation': transportation,
            'origin': origin,
            'destination': destination,
            'seat': seat
        }

        boarding_card = boarding_card_factory(raw_boarding_card_data)

        self.assertIsInstance(boarding_card, AirportBusBoardingCard)
        self.assertEqual(boarding_card.transportation, transportation)
        self.assertEqual(boarding_card.origin, origin)
        self.assertEqual(boarding_card.destination, destination)
        self.assertEqual(boarding_card.seat, seat)

    def test_boarding_card_factory_returns_train_boarding_card(self):
        transportation = 'train'
        origin = 'Madrid'
        destination = 'Barcelona'
        seat = '45B'

        raw_boarding_card_data = {
            'transportation': transportation,
            'origin': origin,
            'destination': destination,
            'seat': seat
        }

        boarding_card = boarding_card_factory(raw_boarding_card_data)

        self.assertIsInstance(boarding_card, TrainBoardingCard)
        self.assertEqual(boarding_card.transportation, transportation)
        self.assertEqual(boarding_card.origin, origin)
        self.assertEqual(boarding_card.destination, destination)
        self.assertEqual(boarding_card.seat, seat)
