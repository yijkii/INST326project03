class PayReport:
    def __init__(self, caregivers):
        self.caregivers = caregivers

    def generate_report(self):
        total_weekly_pay = 0
        for caregiver in self.caregivers:
            weekly_pay = caregiver.calculate_weekly_pay()
            total_weekly_pay += weekly_pay
            print(f"{caregiver.name}: ${weekly_pay:.2f}")

        print(f"Total Weekly Pay: ${total_weekly_pay:.2f}")
