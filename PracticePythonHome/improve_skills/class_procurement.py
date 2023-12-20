class OpenProcedure:
    id_tender = 0
    result_of_tender = ""

    def __init__(self, name, classifier, expected_value):
        self.name = name
        self.classifier = classifier
        self.expected_value = expected_value
        OpenProcedure.result_of_tender = "Procedure is successful"
        OpenProcedure.id_tender += 1

    def __str__(self):
        str_out = "Number of tender: " + str(OpenProcedure.id_tender)
        str_out += "\nName of procurement: " + self.name + "\nClassifier: "
        str_out += str(self.classifier) + "\n"
        str_out += OpenProcedure.result_of_tender + "\n"
        return str_out


class SimpleProcurement(OpenProcedure):
    
    def __init__(self, name, classifier, expected_value):
        self.name = name
        self.classifier = classifier
        self.expected_value = expected_value
        OpenProcedure.id_tender += 1
        if self.expected_value > 100000:
            OpenProcedure.result_of_tender = "Procedure is not successful"
        else:            
            OpenProcedure.result_of_tender = "Procedure is successful"


first_tender = OpenProcedure("Elektricity", 9004, 150000)
print(first_tender)

simple_first_tender = SimpleProcurement("Сhemical reagent", 7005, 110000)
print(simple_first_tender)