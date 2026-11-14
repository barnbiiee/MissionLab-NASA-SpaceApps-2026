import unittest
from mission_logic import evaluate

class MissionTests(unittest.TestCase):
    def test_basic_design_is_feasible(self):
        r=evaluate('Basic camera','Compact solar panels','Basic radio','Economy rideshare')
        self.assertTrue(r['feasible'])
        self.assertGreater(r['score'], 0)
    def test_advanced_sensor_needs_better_power_and_comms(self):
        r=evaluate('High-resolution camera','Compact solar panels','Basic radio','Economy rideshare')
        self.assertFalse(r['feasible'])
        self.assertFalse(r['checks']['Power']['passed'])
        self.assertFalse(r['checks']['Communications']['passed'])
    def test_advanced_build_can_be_feasible(self):
        r=evaluate('High-resolution camera','Expanded solar panels','High-rate radio','Economy rideshare')
        self.assertTrue(r['feasible'])
    def test_over_budget_possible(self):
        r=evaluate('High-resolution camera','Expanded solar panels','High-rate radio','Heavy rideshare')
        self.assertGreater(r['cost'], 130)
        self.assertFalse(r['checks']['Budget']['passed'])

if __name__ == '__main__':
    unittest.main()
