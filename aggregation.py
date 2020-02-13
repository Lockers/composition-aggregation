class Store:
    def __init__(self, name, department):
        self.name = name
        self.departments = department

        # def getDept(self):
        #     return f'{self.department}'


class Department:
    def __init__(self):
        self.name = ['Bikes', 'cars', 'arrows']

    def __str__(self):
        return f'{self.name}'

departments = Department()
store1 = Store('Harrods', departments)

print(store1.departments)
