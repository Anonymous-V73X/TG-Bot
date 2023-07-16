import json

def remove_duplicate_ids():
    # Load file data from JSON
    file_data = load_file_data()

    # Iterate over each file in the file data
    for file_name, file_ids in file_data.items():
        if len(file_ids) == 2:
            # Remove one of the duplicate IDs
            file_ids = [file_ids[0]]

        # Update the file IDs in the file data
        file_data[file_name] = file_ids

    # Save the modified file data back to JSON
    save_file_data(file_data)

def load_file_data():
    try:
        with open("file_data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return data

def save_file_data(file_data):
    with open("file_data.json", "w") as file:
        json.dump(file_data, file)

# Call the function to remove duplicate IDs
remove_duplicate_ids()
