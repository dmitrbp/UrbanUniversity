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
        '''
        Ощибка в коде: 
        Список, по которому происходит итерация for, изменяется в этом самом цикле for.
        Из-за этого после удаления элемента списка происходит пропуск следующей по порядку итерируемой величины
        (следующий participant пропускает ход, а participant после него получает преимущество) 
        '''
        # while self.participants:
        #     for participant in self.participants:
        #         participant.run()
        #         if participant.distance >= self.full_distance:
        #             finishers[place] = participant
        #             place += 1
        #             self.participants.remove(participant)
        while len(finishers) < len(self.participants):
            for participant in self.participants:
                if participant.name in [value.name for value in finishers.values()]:
                    continue
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = Runner('Walker')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Runner')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walker = Runner('Walker')
        runner = Runner('Runner')
        for i in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.all_results_sum = []

    def setUp(self):
        self.usein = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for dict_element in list(cls.all_results_sum):
            dic_result = {}
            for key in dict_element:
                dic_result[key] = dict_element[key].name
            print(dic_result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        tournament = Tournament(90, self.usein, self.nik)
        self.all_results = tournament.start()
        self.all_results_sum.append(self.all_results)
        keys = list(self.all_results.keys())
        self.assertTrue(self.all_results[keys[len(keys) - 1]] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        tournament = Tournament(90, self.andrey, self.nik)
        self.all_results = tournament.start()
        self.all_results_sum.append(self.all_results)
        keys = list(self.all_results.keys())
        self.assertTrue(self.all_results[keys[len(keys) - 1]] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        tournament = Tournament(90, self.usein, self.andrey, self.nik)
        self.all_results = tournament.start()
        self.all_results_sum.append(self.all_results)
        keys = list(self.all_results.keys())
        self.assertTrue(self.all_results[keys[len(keys) - 1]] == 'Ник')


if __name__ == '__main__':
    unittest.main()
