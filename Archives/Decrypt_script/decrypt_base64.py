# This program read a json file, and isolates the txs special key, then checks to see if the txs key empty or contains characters. If the key is empty, then the program will return an a message saying "no transactions found", if the program contains a transaction, then it will remove any unnecessary characters and then assign the transaction to variable "code"
def process_transaction_data(file_path):
# Reads a JSON file containing transaction data and processes it.
#Args:file_path (str): Path to the JSON file.
#Returns:str: Concatenated transaction data or an empty string if no transactions found.
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            transaction = data['block']['data']['txs']

            if len(transaction) > 0:
                return ''.join(map(str, transaction)) # remove unnecessary symbols
            else:
                return "No transactions found."
    except FileNotFoundError:
        return "File not found."

# Example usage
file_path = '../../blocks/3102393.json'
code = process_transaction_data(file_path)
print(code)

# this program send the encrypted transaction information contained in variable "code" to a url address that will decrypt the transaction and return the translated information
import requests
import json
def decode_transactions(tx):
    url = "https://phoenix-lcd.terra.dev/cosmos/tx/v1beta1/decode"
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"tx_bytes": tx})

    response = requests.post(url, headers=headers, data=data) #send to be decoded
    return response.json()

# if $code contain multiple elements(transactions), split it
code = code.split()
many = len(code)
print(many)

for i in range(many):
    # let decoded_response be the decoded string
    decoded_response = decode_transactions(code[i])

    # Print it in JSON type-
    print(f'Here is number {i+1} transaction\n')
    print(json.dumps(decoded_response, indent=2))