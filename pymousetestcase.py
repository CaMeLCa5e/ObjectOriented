# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class pymousetestcase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://www.google.com/")
        self.selenium.start()
    
    def test_pymousetestcase(self):
        sel = self.selenium
        sel.open("about:home")
        sel.type("id=searchText", "pymouse")
        sel.click("id=searchSubmit")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
