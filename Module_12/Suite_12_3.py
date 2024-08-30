import unittest
import Tests_12_3

calcTS = unittest.TestSuite()
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests_12_3.RunnerTest))
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTS)