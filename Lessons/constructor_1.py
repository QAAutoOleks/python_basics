class Shopworker:
    count_workers = 0
    def __init__(self, name1 = "", age1 = 0):
        #  self.count_workers += 1
        Shopworker.count_workers += 1
        self.name = name1
        self.age = age1
    def add_year(self, quantity):
        self.age += quantity

print("Quantity workers: ", Shopworker.count_workers)

work1 = Shopworker('Ivan', 25)
print("Employee 1: ", work1.name, "", work1.age, ", quantity employees: ", work1.count_workers)
work1.add_year(3)
print("Employee 1: ", work1.name, "", work1.age, ", quantity employees: ", work1.count_workers)

work2 = Shopworker('Petro', 25)
print("Employee 2: ", work2.name, "", work2.age, ", quantity employees: ", work2.count_workers)