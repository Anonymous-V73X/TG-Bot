from client import bot
from pyrogram import Client, filters
import json


# Specify the JSON file path
json_file = "file_data.json"

# Dictionary to store the file details
file_data = {}


# Handler for file messages
@bot.on_message(filters.document)
def handle_file(client, message):
    # Get the file name and ID
    file_name = message.document.file_name
    file_id = message.document.file_id

    # Add the file details to the dictionary
    file_data[file_name] = [file_id]

    # Save file details to JSON if the number of files reaches a threshold
    if len(file_data) >= 100:
        save_files()

    


# Function to save file details to JSON
def save_files():
    try:
        # Load existing data from JSON or create an empty dictionary
        with open(json_file, "r") as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = {}

    # Update the existing data with the new file details
    existing_data.update(file_data)

    # Write the updated data to the JSON file
    with open(json_file, "w") as file:
        json.dump(existing_data, file, indent=4)

    # Clear the file_data dictionary
    file_data.clear()


# get sticker id
@bot.on_message(filters.sticker)
def handle_sticker(client, message):
    print(message)


# Start the bot
bot.run()
