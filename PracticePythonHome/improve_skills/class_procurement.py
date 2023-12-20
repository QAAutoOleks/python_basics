class OpenProcedure:
    id_tender = 0

    def __init__(self, name, classifier):
        self.name = name
        self.classifier = classifier
        OpenProcedure.id_tender += 1

    def __str__(self):
        str_out = "Number of tender: " + str(OpenProcedure.id_tender) + "\nName of procurement: " + self.name + "\nClassifier: " + str(self.classifier) + "\n"
        return str_out


class SimpleProcurement(OpenProcedure):
    pass

first_tender = OpenProcedure("Elektricity", 9004)
print(first_tender)

simple_first_tender = SimpleProcurement("Сhemical reagent", 7005)
print(simple_first_tender)