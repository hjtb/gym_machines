import csv
import os

base_directory = os.path.abspath(os.path.dirname(__file__))
path_to_data = os.path.join(base_directory,"output_no_git","images.csv")
with open(path_to_data, "r", encoding="utf-8") as file:
    lines = file.readlines()
path_to_new_data = os.path.join(base_directory,"output_no_git","test_images.csv")
number_required = 100
number_processed = 0
with open(path_to_new_data, "w") as file:
    file.write("uniq_id, image_url\n")
for line_index,line in enumerate(lines):
    entries = line.split(',')
    unique_id = entries[0]
    images = entries[1:]
    for image in images:
        image = image.strip()
        image = image.replace('"','')
        image = image.replace('[','')
        image = image.replace(']','')
        image = image.replace("'",'')
        line = f"{unique_id},{image}\n"
        with open(path_to_new_data, "a") as file:
            file.write(line)
        print(line)
