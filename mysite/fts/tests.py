from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PollsTest(LiveServerTestCase):
	fixtures = ['admin_user.json']

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

		# She types in her username and password and hits return
		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys('admin')

		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('adm1n')
		password_field.send_keys(Keys.RETURN)

		# her username and password are accepted and she is taken to
		# the Site Administration page
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration', body.text)

		# She now sees a couple of hyperlinks that say "Polls"
		polls_links = self.browser.find_elements_by_link_text('Polls')
		self.assertEquals(len(polls_links), 2)

		# TODO: use the admin site to create a Poll
		self.fail('finish this test')
