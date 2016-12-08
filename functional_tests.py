import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class NewVisitor(unittest.TestCase):

    def setUp(self):
        binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
        self.browser = webdriver.Firefox(firefox_binary=binary)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heared about a cool new online to-do app. She goes
        #to check out its homepage
        self.browser.get('http://localhost:8000')

        #She notices that the browser title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


        #She is invited to enter a to-do item straight away
        
        #She types "Buy peacock feathers" into a text box (Edit's hobby
        #is tying fly-fishing lures)
        
        #When she hits enter, the page updates, and now the page lists
        #"1: Buy peacock feathers" as an item in a to-do list
        
        #There is still a text box inviting her to add another item. She
        #enters "Use peacock feathers to make a fly" (Edith is very methodical)
        
        #The page updates again and now shows both items on her list
        
        #Edith wonders whether the site will remember her list. Then she sees
        #that the site has generated a unique URL for her -- there is some
        #explanatory text to that effect.
        
        #She visits that URL - her to-do lists is still there.
        
        #Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
