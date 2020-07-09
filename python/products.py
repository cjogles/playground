class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return (f"name = {self.name}, price = {self.price}")

# read csv file with csv module to read file so each record is imported into a Product instance.
# return the list of product instances from the function.
product_list = []
# note that the first line of the csv is header that describes the fileds and should not be loaded into a product object

import csv
# print the list of products, 1 record per line
def productreader(your_list):
    with open("products.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            current_row = (''.join(row).split(','))
            if (current_row[0] == "name"):
                pass
            else:
                your_list.append(Product(current_row[0], current_row[1]))
        for i, x in enumerate(your_list):
            print(i, x)

productreader(product_list)
