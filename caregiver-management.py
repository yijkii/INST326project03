class Caregiver:
    def __init__(self, name, phone, email, pay_rate, availability=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.availability = availability if availability else self.initialize_availability()
        self.hours_worked = 0

    def initialize_availability(self):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]
        shifts = ['AM', 'PM']
        return {day: {shift: 'available' for shift in shifts} for day in days}
    
    def update_availability(self, day, shift, status):
        if day not in self.availability:
            raise ValueError(f"Invalid day: {day}")
        if shift not in self.availability[day]:
            raise ValueError(f"Invalid shift: {shift}")
        if status not in ['preferred', 'available', 'unavailable']:
            raise ValueError(f"Invalid status: {status}")
        self.availability[day][shift] = status

    def get_availability(self):
        return self.availability

    def add_hours(self, hours):
        self.hours_worked += hours

    def reset_hours(self):
        self.hours_worked = 0

    def calculate_weekly_pay(self):
        return self.hours_worked * self.pay_rate
    
    def __str__(self):
        return f"Caregiver: {self.name}, Phone: {self.phone}, Email: {self.email}, Pay Rate: ${self.pay_rate}/hr"
    
class CaregiverManager:
    def __init__(self):
        self.caregivers = []

    def add_caregiver(self, caregiver):
        self.caregivers.append(caregiver)

    def remove_caregiver(self, name):
        self.caregivers = [cg for cg in self.caregivers if cg.name != name]

    def find_caregiver(self, name):
        for caregiver in self.caregivers:
            if caregiver.name == name:
                return caregiver
        return None
    
    def display_all_caregivers(self):
        for caregiver in self.caregivers:
            print(caregiver)

if __name__ == "__main__":
    manager = CaregiverManager()
    caregiver1 = Caregiver("Kiki", "123-456-7890", "kiki@example.com", 20.0)
    caregiver2 = Caregiver("Bob", "987-654-3210", "bob@example.com", 18.5)

    manager.add_caregiver(caregiver1)
    manager.add_caregiver(caregiver2)

    print("All Caregivers:")
    manager.display_all_caregivers()

    caregiver1.update_availability("Monday", "AM", "preferred")
    print("\nUpdated Availability for Kiki:")
    print(caregiver1.get_availability())
