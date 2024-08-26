import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # print(cls.all_results)
        for d in list(cls.all_results):
            print({d:cls.all_results[d].name})

    def test_run1(self):
        tournament = Tournament(90, self.usein, self.nik)
        TournamentTest.all_results = tournament.start()
        keys = list(TournamentTest.all_results.keys())
        self.assertTrue(keys[len(keys) - 1], 'Ник')

    def test_run2(self):
        tournament = Tournament(90, self.andrey, self.nik)
        TournamentTest.all_results = tournament.start()
        keys = list(TournamentTest.all_results.keys())
        self.assertTrue(keys[len(keys) - 1], 'Ник')

    def test_run3(self):
        tournament = Tournament(90, self.usein, self.andrey, self.nik)
        TournamentTest.all_results = tournament.start()
        keys = list(TournamentTest.all_results.keys())
        self.assertTrue(keys[len(keys) - 1], 'Ник')



if __name__ == '__main__':
    # TournamentTest.run()
    unittest.main()