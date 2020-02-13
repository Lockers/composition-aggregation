class Store:
    def __init__(self, name):
        self.name = name
        self.departments = ['Bikes', 'cars', 'arrows']
        self.department = Department(self.departments)

        def getDept(self):
            return self.department

class Department:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

store1 = Store('Harrods')

print(store1.department)       