import csv
import os

base_directory = os.path.abspath(os.path.dirname(__file__))
path_to_data = os.path.join(base_directory,"output_no_git","flipkart_com-ecommerce_sample.csv")
with open(path_to_data, "r", encoding="utf-8") as file:
    lines = file.readlines()
path_to_new_data = os.path.join(base_directory,"output_no_git","test.csv")
number_required = 10
number_processed = 0
with open(path_to_new_data, "a") as file:
    for line in lines:
        try:
            line = line.replace(",false,",",0,")
            line = line.replace(",true,",",1,")
            file.write(f"{line}")
            number_processed = number_processed + 1
            if number_processed > number_required:
                break
        except:
            pass
1/0
