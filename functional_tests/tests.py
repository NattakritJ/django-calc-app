from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

class AllTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_user_can_use_calculator(self):
        self.browser.get(self.live_server_url)
        title = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Calculator POST Method',title)
        x_input = self.browser.find_element_by_name('x')
        y_input = self.browser.find_element_by_name('y')
        operation = Select(self.browser.find_element_by_name('operations'))
        submit_btn = self.browser.find_element_by_name('submit')
        result = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('result : 0.0', result)
        x_input.send_keys('2')
        y_input.send_keys('2')
        operation.select_by_value('+')
        submit_btn.click()
        time.sleep(1)
        result = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('result : 4.0', result)
        x0_table = self.browser.find_element_by_name('x0').text
        self.assertIn('2.0', x0_table)
        y0_table = self.browser.find_element_by_name('y0').text
        self.assertIn('2.0', y0_table)
        op0_table = self.browser.find_element_by_name('op0').text
        self.assertIn('+', op0_table)
        result0_table = self.browser.find_element_by_name('result0').text
        self.assertIn('4.0', result0_table)
        x_input = self.browser.find_element_by_name('x')
        y_input = self.browser.find_element_by_name('y')
        operation = Select(self.browser.find_element_by_name('operations'))
        submit_btn = self.browser.find_element_by_name('submit')
        x_input.send_keys('42.3')
        y_input.send_keys('56.6')
        operation.select_by_value('*')
        submit_btn.click()
        time.sleep(1)
        result = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('result : 2394.18', result)
        x1_table = self.browser.find_element_by_name('x1').text
        self.assertIn('42.3', x1_table)
        y1_table = self.browser.find_element_by_name('y1').text
        self.assertIn('56.6', y1_table)
        op1_table = self.browser.find_element_by_name('op1').text
        self.assertIn('*', op1_table)
        result1_table = self.browser.find_element_by_name('result1').text
        self.assertIn('2394.18', result1_table)
        clear_btn = self.browser.find_element_by_name('clearall')
        clear_btn.click()
        ip1_header = self.browser.find_element_by_name('ip1').text
        ip2_header = self.browser.find_element_by_name('ip2').text
        op_header = self.browser.find_element_by_name('op_header').text
        result_header = self.browser.find_element_by_name('result_header').text
        self.assertIn('Input 1', ip1_header)
        self.assertIn('Input 2', ip2_header)
        self.assertIn('Operation', op_header)
        self.assertIn('Result', result_header)
        GET_link = self.browser.find_element_by_name('linktoget')
        GET_link.click()
        title = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Calculator GET Method', title)
        time.sleep(2)

    def test_user_can_use_calculator_in_GET_method(self):
        self.browser.get(self.live_server_url+ '/get')
        title = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Calculator GET Method',title)
        x_input = self.browser.find_element_by_name('x')
        y_input = self.browser.find_element_by_name('y')
        operation = Select(self.browser.find_element_by_name('operations'))
        submit_btn = self.browser.find_element_by_name('submit')
        result = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('result : 0.0', result)
        x_input.send_keys('2')
        y_input.send_keys('2')
        operation.select_by_value('+')
        submit_btn.click()
        time.sleep(1)
        result = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('result : 4.0', result)
        x0_table = self.browser.find_element_by_name('x0').text
        self.assertIn('2.0', x0_table)
        y0_table = self.browser.find_element_by_name('y0').text
        self.assertIn('2.0', y0_table)
        op0_table = self.browser.find_element_by_name('op0').text
        self.assertIn('+', op0_table)
        result0_table = self.browser.find_element_by_name('result0').text
        self.assertIn('4.0', result0_table)
        x_input = self.browser.find_element_by_name('x')
        y_input = self.browser.find_element_by_name('y')
        operation = Select(self.browser.find_element_by_name('operations'))
        submit_btn = self.browser.find_element_by_name('submit')
        x_input.send_keys('42.3')
        y_input.send_keys('56.6')
        operation.select_by_value('*')
        submit_btn.click()
        time.sleep(1)
        result = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('result : 2394.18', result)
        x1_table = self.browser.find_element_by_name('x1').text
        self.assertIn('42.3', x1_table)
        y1_table = self.browser.find_element_by_name('y1').text
        self.assertIn('56.6', y1_table)
        op1_table = self.browser.find_element_by_name('op1').text
        self.assertIn('*', op1_table)
        result1_table = self.browser.find_element_by_name('result1').text
        self.assertIn('2394.18', result1_table)
        clear_btn = self.browser.find_element_by_name('clearall')
        clear_btn.click()
        ip1_header = self.browser.find_element_by_name('ip1').text
        ip2_header = self.browser.find_element_by_name('ip2').text
        op_header = self.browser.find_element_by_name('op_header').text
        result_header = self.browser.find_element_by_name('result_header').text
        self.assertIn('Input 1', ip1_header)
        self.assertIn('Input 2', ip2_header)
        self.assertIn('Operation', op_header)
        self.assertIn('Result', result_header)
        POST_link = self.browser.find_element_by_tag_name('a')
        POST_link.click()
        title = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Calculator POST Method', title)
        time.sleep(2)


