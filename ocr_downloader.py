import os
import requests
import argparse
from tqdm import tqdm

API_URL_TEMPLATE = "https://pero-ocr.fit.vutbr.cz/api/download_results/{}/{}/{}"
API_KEY = "" #ENTER VALID DEFAULT API KEY

# Get input from user for each argument
api_key = input("Enter your API key (leave empty for default): ")
folder_name = input("Enter folder name to save the response files: ")
identifier = input("Enter the process ID: ")
file_type = input("Enter the type of file you wish to recieve: ").lower()

file_extension = "txt"
if file_type.lower() == "alto":
    file_extension = "xml"

if not api_key:
    api_key = API_KEY

# Create the folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Read the requests from the file
with open("requests.txt", "r") as file:
    requests_list = file.read().splitlines()

# Send requests and save responses with progress tracking
for request in tqdm(requests_list, desc="Processing"):
    url = API_URL_TEMPLATE.format(identifier, request, file_type)
    headers = {"api-key": api_key}
    response = requests.get(url, headers=headers)

    # Save response to a file in the specified folder
    file_name = os.path.join(folder_name, "{}.{}".format(os.path.splitext(request)[0], file_extension))
    with open(file_name, "wb") as file:
        file.write(response.content)

    tqdm.write("Saved response for {} as {}".format(request, file_name))
