import csv
import json

# Open the CSV file and read it
with open('resources\csv\school_data.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Prepare a list to store the filtered questions and answers
    filtered_data = []

    # Loop through each row and check the category
    for row in reader:
        # Print each row to check the data
        print(row)
        filtered_data.append({
                "id": row["id"].strip(),
                "first_name": row["first_name"].strip(),
                "last_name": row["last_name"].strip(),
                "email": row["email"].strip(),
                "class": row["class"].strip(),
                "grade": row["grade"].strip(),
                
                
                
            })
    
    # Write the filtered data to a JSON file
    with open('resources/json/school_data.json', mode='w', encoding='utf-8') as json_file:
        json.dump(filtered_data, json_file, indent=4)

print("Data filtered and saved to school_data.json")

