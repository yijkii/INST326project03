import unittest
from caregiver_management import Caregiver
from class PayReport import PayReport
from class ScheduleExporter import ScheduleExporter

class TestCaregiver(unittest.TestCase):
    def test_log_hours(self):
        caregiver = Caregiver("Kiki", "123-456-7890", "Kiki@example.com", 20)
        caregiver.log_hours(8)
        self.assertEqual(caregiver.hours_worked, 8)

    def test_calculate_weekly_pay(self):
        caregiver = Caregiver("Kiki", "123-456-7890", "Kiki@example.com", 20)
        caregiver.log_hours(40)
        self.assertEqual(caregiver.calculate_weekly_pay(), 800)

if __name__ == "__main__":
    unittest.main()
