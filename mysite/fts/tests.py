from django.test import LiveServerTestCase
from selenium import webdriver

class PollsTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_create_new_poll_via_admin_site(self):
		# Gertrude opens her web browser, and goes to the admin page
		self.browser.get(self.live_server_url + '/admin/')

		# She sees the familiar 'Django administration' heading
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		# TODO: use the admin site to create a Poll
		self.fail('finish this test')
