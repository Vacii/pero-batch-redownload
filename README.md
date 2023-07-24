# Code for Downloading Results from PERO OCR API

This repository contains a Python script to download OCR results from the PERO OCR API. The script reads a list of requests from a file, sends API requests, and saves the responses to files in a specified folder.

## Prerequisites

- Python 3.x
- `requests` library
- `tqdm` library

## Getting Started

1. Clone this repository to your local machine.
2. Install the required libraries using the following command:

```shell
pip install requests tqdm
```

## Usage

1. Make sure you have obtained a valid API key from PERO OCR API (modify `API_KEY` variable).
2. Create a file named `requests.txt` in the repository root and add one process ID per line, representing the OCR requests you want to download the results for.
3. Open a terminal or command prompt and navigate to the cloned repository folder.
4. Run the script using the following command:

```shell
python ocr_downloader.py
```

The script will prompt you for the API key (you can leave it empty for the default key), the folder name to save the response files, and the type of file you wish to receive (either 'txt' or 'alto').

## Example

Suppose you have the following `requests.txt` file with process IDs:

```
process_id_1
process_id_2
process_id_3
```

Running the script and providing the required inputs will download the OCR results for each process ID and save them in the specified folder.

## Note

- If you wish to receive the OCR results in 'txt' format, enter 'txt' as the file type when prompted.
- If you wish to receive the OCR results in 'alto' format, enter 'alto' as the file type when prompted. The results will be saved with a '.xml' extension.

Please make sure to handle the downloaded data according to the terms and conditions of the PERO OCR API.

**Important**: Ensure that you have proper permissions and comply with the API provider's terms of use while using this script.

Happy OCR downloading! :rocket: