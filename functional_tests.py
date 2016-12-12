from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest

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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )
        
        #She types "Buy peacock feathers" into a text box (Edit's hobby
        #is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        
        #When she hits enter, the page updates, and now the page lists
        #"1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        
        #There is still a text box inviting her to add another item. She
        #enters "Use peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        #The page updates again and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])
        
        #Edith wonders whether the site will remember her list. Then she sees
        self.fail('Finish the test!')
        #that the site has generated a unique URL for her -- there is some
        #explanatory text to that effect.
        
        #She visits that URL - her to-do lists is still there.
        
        #Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
