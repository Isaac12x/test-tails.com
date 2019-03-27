import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FunctionalTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_start_app(self):
        # We just heard there is a new postcode finder in the block
        # So we just go check it out
        #
        # We get to the home page
        self.driver.get("http://localhost:5000")

        # And notice it says tails.com. Weird, thought they were selling dog
        # food. Seems I don't know that much about them really.
        self.assertIn("Tails.com - All stores", self.driver.title)

        # and now we see a huge amount of postcodes [this should be another test]
        rows = self.driver.find_elements_by_tag_name("tr")
        self.assertGreater(len(rows), 90)

        # and now should go on and test lat and long

    def test_render_add_stores(self):
        # He became quite enthused when he discovered there was a secret
        # way to add more stores to the array
        self.driver.get("http://localhost:5000/add-store")
        self.assertIn("Tails.com - Add store", self.driver.title)

    def test_add_store_failed(self):
        self.driver.get("http://localhost:5000/add-store")

        # she goes and writes a new store location
        name = self.driver.find_element_by_id("name")
        name.send_keys("Richmond")
        self.assertEqual(
            "Richmond", self.driver.find_element_by_id("name").get_attribute("value")
        )

        # next she adds a postcode
        postcode = self.driver.find_element_by_id("postcode")
        postcode.send_keys("g5suds23")
        self.assertEqual(
            "g5suds23",
            self.driver.find_element_by_id("postcode").get_attribute("value"),
        )

        # she goes and clicks on the submit button waiting
        # for her lovely new store to be added, soon she will be
        # selling amazing dog food.
        self.driver.find_element_by_name("submit").send_keys(Keys.ENTER)
        self.assertEqual(self.driver.current_url, "http://localhost:5000/add-store")

        # can assert many other things, like the flash failure message shown

    def test_add_store_successful(self):
        pass

    # And we should keep writing endless functional tests as it's where all
    # pieces come together. If this breaks, all breaks, so need to check all
    # edge cases.


if __name__ == "__main__":
    unittest.main()
