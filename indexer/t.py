import unittest
import json
import os
import logging

class TestJSONValidation(unittest.TestCase):
    def setUp(self):
        # Replace with the actual folder path
        self.folder_path = "C:/Users/lmhmo/indexer/blocks"

    def test_valid_json_files_exist(self):
        # Get a list of all files in the directory
        all_files = os.listdir(self.folder_path)
        self.assertTrue(all_files, "No files found in the specified directory.")

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

    def test_json_file_extension(self):
        for filename in os.listdir(self.folder_path):
            with self.subTest(filename=filename):
                self.assertTrue(filename.lower().endswith(".json"))

    def test_height_positive_integer(self):
        for filename in os.listdir(self.folder_path):
            height = os.path.splitext(filename)[0]
            with self.subTest(filename=filename):
                self.assertTrue(height.isdigit() and int(height) > 0)

    def tearDown(self):
        # Set up logging for successful tests
        logger = logging.getLogger("test_logger")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("log.txt")
        logger.addHandler(handler)

        # Get the name of the current test
        test_name = self.id().split(".")[-1]

        # Log the test name as passed
        logger.info(f"Test '{test_name}' passed")

if __name__ == "__main__":
    unittest.main()