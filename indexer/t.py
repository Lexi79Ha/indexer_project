import unittest
import json
import os
import logging

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

    def test_valid_json_format(self):
        for filename in os.listdir(self.folder_path):
            full_path = os.path.join(self.folder_path, filename)
            with self.subTest(filename=filename):
                try:
                    with open(full_path, "r") as f:
                        json_data = json.load(f)
                        # If we reach here, the file contains valid JSON data
                        self.assertTrue(True)
                except (ValueError, FileNotFoundError):
                    self.fail(f"{filename} is not a valid JSON file.")
                    self.write_error(f"{filename} is not a valid JSON file.")

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

    def test_height_matches_filename(self):
        for filename in os.listdir(self.folder_path):
            height_from_filename = os.path.splitext(filename)[0]
            with self.subTest(filename=filename):
                try:
                    with open(os.path.join(self.folder_path, filename), "r") as f:
                        json_data = json.load(f)
                        actual_height = json_data["block"]["header"]["height"]
                        self.assertEqual(int(height_from_filename), int(actual_height),
                                         f"{filename} height does not match filename.")
                        # Write error message if assertion fails
                except (ValueError, FileNotFoundError):
                    self.fail(f"{filename} is not a valid JSON file or does not match its height.")
                    self.write_error(f"{filename} height does not match filename.")

    def validate_json_schema(self):
        # Define your JSON schema (replace with your actual schema)
        schema = {
            "type": "object",
            "properties": {
                "block_id": {
                    "type": "object",
                    "properties": {
                        "hash": {"type": "string"},
                        "part_set_header": {
                            "type": "object",
                            "properties": {
                                "total": {"type": "integer"},
                                "hash": {"type": "string"}
                            }
                        }
                    }
                },
                # Add other properties as needed
            },
            "required": ["block_id"]
        }

        for filename in os.listdir(self.folder_path):
            full_path = os.path.join(self.folder_path, filename)
            with self.subTest(filename=filename):
                try:
                    with open(full_path, "r") as f:
                        json_data = json.load(f)
                        validate(instance=json_data, schema=schema)
                except (ValueError, FileNotFoundError):
                    self.fail(f"{filename} is not a valid JSON file.")
                    self.write_error(f"{filename} does not have a valid schema.")
    def write_error(self, message):
        with open(self.error_file, "a") as err_file:
            err_file.write(message + "\n")

if __name__ == "__main__":
    unittest.main()