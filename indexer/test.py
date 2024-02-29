# This file contains unit tests to verify that the file pulled from the fetch.py script is a json file, with a valid schema, a fileanme that matches its height, and a height that is positive

#required libraries
import unittest
import json
import os
from jsonschema import validate


class TestJSONValidation(unittest.TestCase):
  def setUp(self):
    # Replace with the actual folder path
    self.folder_path = "C:/Users/lmhmo/indexer/blocks"
    self.error_file = "error_log.txt"


  def test_valid_json_files_exist(self):
    # Get a list of all files in the directory
    all_files = os.listdir(self.folder_path)
    if not all_files:
      self.fail("No files found in the specified directory.")
      self.write_error("No files found in the specified directory.")


  def test_json_file_extension(self):
    for filename in os.listdir(self.folder_path):
      with self.subTest(filename=filename):
        self.assertTrue(filename.lower().endswith(".json"))
        if not filename.lower().endswith(".json"):
          self.write_error(f"{filename} does not have a .json extension.")
  def test_height_positive_integer(self):
    for filename in os.listdir(self.folder_path):
      height = os.path.splitext(filename)[0]
      with self.subTest(filename=filename):
        self.assertTrue(height.isdigit() and int(height) > 0)
        if not (height.isdigit() and int(height) > 0):
          self.write_error(f"{filename} has an invalid height value.")

        def write_error(self, message):
          with open(self.error_file, "a") as err_file:
            err_file.write(message + "\n")

  def test_validate_json_files(self):
    # Load your JSON schema (replace with your actual schema)
    with open("schema.json") as schema_file:
      schema = json.load(schema_file)

  # Validate each JSON file in the folder
    for filename in os.listdir(self.folder_path):
      if filename.lower().endswith(".json"):
        with open(os.path.join(self.folder_path, filename)) as data_file:
          json_data = json.load(data_file)
          try:
            validate(instance=json_data, schema=schema)
          except Exception as e:
            self.fail(f"Validation failed for {filename}: {e}")


if __name__ == "__main__":
  # Run the tests
  unittest.main()
  # If all tests pass, write a success message to log.txt
  with open("log.txt", "w") as log_file:
    log_file.write("All tests passed successfully!")
