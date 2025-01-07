import csv
import json

# Open the CSV file and read it
with open('resources/csv/testdatatype.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Prepare a list to store the filtered questions and answers
    filtered_data = []

    # Define the categories we are interested in
    valid_categories = ["boolean", "string", "number"]
    
    # Loop through each row and check the category
    for row in reader:
        category = row["data type"].strip().lower()  # Ensure category is in lower case
        if category in valid_categories:
            filtered_data.append({
                "question": row["question"].strip(),
                "answer": row["answer"].strip()
            })
    
    # Write the filtered data to a JSON file
    with open('resources/json/testdatatype.json', mode='w', encoding='utf-8') as json_file:
        json.dump(filtered_data, json_file, indent=4)

print("Data filtered and saved to filtered_data.json")

