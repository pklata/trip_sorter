from unittest import TestCase
from trip_sorter.boarding_card import boarding_card_factory
from trip_sorter.journey_organizer import JourneyOrganizer


class JourneyOrganizerTestTest(TestCase):

    def test_can_add_boarding_card_to_journey_organizer(self):
        origin = 'Girona Airport'
        destination = 'Stockholm'
        data = {
            'transportation': 'airplane',
            'origin': origin,
            'destination': destination,
            'flight': 'SK455',
            'seat': '3A',
            'gate': '45B',
            'ticket_counter': '344'
        }
        boarding_card = boarding_card_factory(data)
        journey_organizer = JourneyOrganizer()
        journey_organizer.add(boarding_card)
        self.assertIn(destination, journey_organizer._items_by_destination)
        self.assertIn(origin, journey_organizer._items_by_origin)

    def test_journey_organizer_sorts_boarding_cards(self):
        data1 = {
            'transportation': 'airplane',
            'origin': 'Girona Airport',
            'destination': 'Stockholm',
            'flight': 'SK455',
            'seat': '3A',
            'gate': '45B',
            'ticket_counter': '344'
        }
        boarding_card1 = boarding_card_factory(data1)
        data2 = {
            'transportation': 'airplane',
            'origin': 'Stockholm',
            'destination': 'New York JFK',
            'flight': 'SK22',
            'seat': '7B',
            'gate': '22',
            'automatic_baggage_transfer': True
        }
        boarding_card2 = boarding_card_factory(data2)
        journey_organizer = JourneyOrganizer()
        journey_organizer.add(boarding_card1)
        journey_organizer.add(boarding_card2)
        organized_boarding_cards = journey_organizer.sorted()
        self.assertIs(organized_boarding_cards[0], boarding_card1)
        self.assertIs(organized_boarding_cards[1], boarding_card2)

    def test_journey_organizer_returns_journey_plan(self):
        data = [
            {'transportation': 'train', 'origin': 'Madrid', 'destination': 'Barcelona', 'number': '78A',
             'seat': '45B'},
            {'transportation': 'airport bus', 'origin': 'Barcelona', 'destination': 'Girona Airport'},
            {'transportation': 'airplane', 'origin': 'Girona Airport', 'destination': 'Stockholm',
             'flight': 'SK455', 'seat': '3A', 'gate': '45B', 'ticket_counter': '344'},
            {'transportation': 'airplane', 'origin': 'Stockholm', 'destination': 'New York JFK',
             'flight': 'SK22', 'seat': '7B', 'gate': '22', 'automatic_baggage_transfer': True},
        ]
        journey_organizer = JourneyOrganizer()
        for item in data:
            boarding_card = boarding_card_factory(item)
            journey_organizer.add(boarding_card)

        expected_plan = "1. Take train 78A from Madrid to Barcelona. Sit in seat 45B.\n" \
            "2. Take the airport bus from Barcelona to Girona Airport. No seat assignment.\n" \
            "3. From Girona Airport, take flight SK455 to Stockholm. Gate 45B, seat 3A. " \
            "Baggage drop at ticket counter 344.\n" \
            "4. From Stockholm, take flight SK22 to New York JFK. Gate 22, seat 7B. " \
            "Baggage will we automatically transferred from your last leg.\n" \
            "5. You have arrived at your final destination."

        self.assertEqual(expected_plan, journey_organizer.get_journey_plan())
