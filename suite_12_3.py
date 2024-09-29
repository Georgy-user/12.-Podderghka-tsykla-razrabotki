import unittest
import tests_12_3

run_lover = unittest.TestSuite()
run_lover.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
run_lover.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(run_lover)
