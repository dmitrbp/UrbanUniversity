import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner('Walker')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)
        # assert walker.distance == 50

    def test_run(self):
        runner = Runner('Runner')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        walker = Runner('Walker')
        runner = Runner('Runner')
        for i in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)


if __name__ == '__main__':
    # RunnerTest().run()
    unittest.main()
