import collections

Car = collections.namedtuple('Car', ['Make', 'Model'])

class CarCollection:
    makes = ['Toyota', 'Ford', 'Honda', 'BMW']

    models = {
        'Toyota': ['Camry', 'Corolla', 'Prius'],
        'Ford': ['F-150', 'Mustang', 'Focus'],
        'Honda': ['Civic', 'Accord', 'CR-V'],
        'BMW': ['X5', 'M3', 'i8']
    }

    def __init__(self):
        self._cars = [Car(make, model) for make in self.makes for model in self.models[make]]

    def len(self):  # Corrected the variable name
        return len(self._cars)

    def __getitem__(self, position):
        return self._cars[position]

# Create an instance
cars = CarCollection()

# Call len() correctly
print(cars.len())  # Output: 12 (since 4 makes × 3 models each = 12 cars)
print(cars.__getitem__(3))