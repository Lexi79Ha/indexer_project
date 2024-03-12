# This python script uses python version 3.12.0 to pull an object with encrypted transaction data, then assigns that object to variable code.
# The variable code is then sent to an api that uses base64 to decrypt the transactions
# After the decrypted data is return it is assigned to a new json file in the decrypted_files directory
# The json file is then pull from the directory to be cleaned and prepared for postgres migration
# The attributes with the json file are pulled and isolated using pandas
import json
import requests
import shutil
def process_transaction_data(file_path): # Assign encrypted object to variable
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            transaction = data['block']['data']['txs']

            if len(transaction) > 0:
                return ''.join(map(str, transaction))  # Remove unnecessary symbols
            else:
                return "No transactions found."
    except FileNotFoundError:
        return "File not found."


# Example usage
block_number = '5904853'  # Change this number if you want to load a different file
file_path = f'C:/Users/lmhmo/indexer/blocks/{block_number}.json'
code = process_transaction_data(file_path)
print(code)
# %%
# Decrypt transaction using base64 api
def decode_transactions(tx, block, i):
    url = "https://phoenix-lcd.terra.dev/cosmos/tx/v1beta1/decode"
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"tx_bytes": tx})

    response = requests.post(url, headers=headers, data=data)  # Send to be decoded
    decoded_response = response.json()

    # Save the decoded data to a JSON file
    filename = f"{block}_{i + 1}.json"
    with open(filename, "w") as json_file:
        json.dump(decoded_response, json_file, indent=2)

    print(f"Transaction {i + 1} decoded and saved to {filename}") # Assign to json file
    return filename

# Example usage
code = code.split()
many = len(code)
block = block_number

print(f"Number of transactions: {many}")

# Store generated filenames in a list
generated_filenames = []
for i in range(many):
    filename = decode_transactions(code[i], block, i)
    generated_filenames.append(filename)

print(filename)
# This section of code will send the new decrypted json file to the decrypted_files directory

# Specify the target directory
target_directory = "C:/Users/lmhmo/indexer/Decrypted_files"
# Move the file
shutil.move(filename, target_directory)
print(f"File '{filename}' moved to '{target_directory}'.")
