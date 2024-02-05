import json
from datetime import datetime

#Question 1

## Create a base class with: 
###  Three properties initialized at construction 
###  One empty classmethod 
###  One empty instance method 


class BaseClass:
    def __init__(self, prop1, prop2, prop3):
        self.prop1 = prop1
        self.prop2 = prop2
        self.prop3 = prop3
    
    @classmethod
    def class_method(cls):
        pass
    
    def instance_method(self):
        pass

# Question 2

## Create a derived class from the base class 
###  Inherits all properties and methods from the base class 
###  Initialize the properties differently from the base class 
###  Add code to the empty methods 


class DerivedClass(BaseClass):
    def __init__(self, prop1, prop2, prop3, prop4):
        super().__init__(prop1, prop2, prop3)
        self.prop4 = prop4
    
    @classmethod
    def class_method(cls):
        print("Class Method")
    
    def instance_method(self):
        print(f"Instance Method with properties: {self.prop1}, {self.prop2}, {self.prop3}, {self.prop4}")

# Question 3

## Use list comprehension and a lambda function to extract all of the even integers out of a list of integers 

def extract_even_integers(integers_list):
    return list(filter(lambda x: x % 2 == 0, integers_list))

integers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
question_3 = extract_even_integers(integers_list)


# Question 4

## Use the next() function to find the first element in a list of dictionaries whose attribute ‘x’ = 5.
## Default to an empty dictionary if not found. 


def find_equal_to_5(list_of_dicts):
    try:
        return next(item for item in list_of_dicts if item.get('x') == 5)
    except StopIteration:
        return {}


list_of_dicts = [
    {'x': 1, 'y': 2},
    {'x': 3, 'y': 4},
    {'x': 5, 'y': 6},
    {'x': 7, 'y': 8}
]

question_4 = find_equal_to_5(list_of_dicts)


# Question 5

import json
from datetime import datetime

def read_json_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def write_json_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def format_datetime_fields(data):
    fields_to_format = ['claimDateTime', 'fileDateTime', 'receivedDateTime']
    for field in fields_to_format:
        data[field] = datetime.fromtimestamp(data[field] / 1e3).strftime('%Y-%m-%dT%H:%M:%S')
    return data

def main():
    input_file = 'input.json'
    output_file = 'output.json'
    document = read_json_from_file(input_file)
    payee_id = document['payee']['id']

    print("Payee ID:", payee_id)

    invoices_with_583 = [invoice_id for invoice_id in document['invoiceIds'] if '583' in invoice_id]

    print("Invoices containing '583':", invoices_with_583)

    document = format_datetime_fields(document)

    write_json_to_file(document, output_file)

if __name__ == "__main__":
    main()


# Logs

print("\nQuestion 3 Example : ")
print(question_3)

print("\nQuestion 4 Example : ")
print(question_4)



    
