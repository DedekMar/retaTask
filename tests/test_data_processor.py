import unittest
from webapp.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        # Ideally a test xml file would be used here, but the purpose of this demo, let's just use the downloaded export_full file in the /xml_data directory (when it is downloaded)
        self.data_processor = DataProcessor('./xml_data/export_full.xml')

    # Test if open_xml_file returns the root element when the file is valid
    def test_open_xml_file_success(self):        
        root = self.data_processor.open_xml_file(self.data_processor.file_path)
        self.assertIsNotNone(root)

    # Test we get an exception and None as return when the path is invalid
    def test_open_xml_file_invalid_file(self):
        try:
            root = self.data_processor.open_xml_file("invalid_path")
            self.assertIsNone(root)
        except Exception as e:
            self.assertIn("failed to load external entity", str(e))

    # Check the method returns the correct number of items in the test xml
    def test_get_all_items(self):
        all_items = self.data_processor.get_all_items()
        self.assertIsInstance(all_items, list)
        self.assertEqual(len(all_items), 28066)

    # Check the method return the corrent amount of items
    def test_count_all_items(self):
        item_count = self.data_processor.count_all_items()
        expected_count = 28066
        self.assertEqual(item_count, expected_count)

    # Check the method returns a list
    def test_get_all_item_names(self):
        all_item_names = self.data_processor.get_all_item_names()
        self.assertIsInstance(all_item_names, list)

    # Test if get_items_with_category_parts method returns a list of dicts of items with parts
    def test_get_items_with_category_parts(self):
        category_id = "1"
        items_with_parts = self.data_processor.get_items_with_category_parts(category_id)
        self.assertIsInstance(items_with_parts, list)
        self.assertEqual(len(items_with_parts), 1249)
        self.assertIsInstance(items_with_parts[0], dict)


if __name__ == '__main__':
    unittest.main()