import unittest
from django.test import TestCase, LiveServerTestCase
from django.test.client import Client
from django.contrib.auth.models import User
from selenium.webdriver.firefox.webdriver import WebDriver

from django.db import IntegrityError

from social.models import Post, PostForm

class SocialTest(unittest.TestCase):
    """Perform general unit tests on the models within the Social app."""
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testman', 'testman@test.com', 'testtest')

    def tearDown(self):
        self.client.logout()
        self.user.delete()

    def test_post_form_valid(self):
        """Perform basic tests on the PostForm to ensure that the form accepts
        various inputs.
        """
        form = PostForm()
        # Ensure that an empty form is not valid.
        self.assertFalse(form.is_valid())

        # Ensure that an empty body still results in a valid form.
        body = "This is the body of the post."
        post_dict = { 'body': body }
        form = PostForm(post_dict)
        self.assertTrue(form.is_valid())

        # Ensure that a standard body input makes the form valid.
        body = "This is the body of the post."
        post_dict = { 'body': body }
        form = PostForm(post_dict)
        self.assertTrue(form.is_valid())

        post = form.save(commit=False)
        post.author = User.objects.get(id=self.user.id)
        post.save()
        self.assertIsInstance(Post.objects.get(id=post.id), Post)

class SocialSeleniumTests(LiveServerTestCase):
    """Use Selenium to test the full functionality of the site, in pieces.
    Eg. test user creation, then login, then login+post.
    """
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SocialSeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(SocialSeleniumTests, cls).tearDownClass()
        cls.selenium.quit()

    def test_join(self):
        """Test the page where a user can enter their information for a new
        account.
        """
        self.selenium.get('{}{}'.format(self.live_server_url, '/join/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('selenium_testman')
        password_input = self.selenium.find_element_by_name("password1")
        password_input.send_keys('testtest')
        password_input = self.selenium.find_element_by_name("password2")
        password_input.send_keys('testtest')
        self.selenium.find_element_by_xpath('//input[@value="Join!"]').click()

    def test_login(self):
        """Test the login page."""
        self.selenium.get('{}{}'.format(self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('selenium_testman')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('testtest')
        self.selenium.find_element_by_xpath('//input[@value="Login!"]').click()

    def test_new_post(self):
        """Test a the creation of a new post. Note that this requires the user
        to first be logged in.
        """
        # Create a new user.
        user = User.objects.create_user('test_new_post_full_user', 'sel_test@test.com', 'testtest')

        # Log in.
        self.selenium.get('{}{}'.format(self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('test_new_post_full_user')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('testtest')
        self.selenium.find_element_by_xpath('//input[@value="Login!"]').click()
        
        # Then attempt to post. The fields will not be visible otherwise.
        self.selenium.get('{}{}'.format(self.live_server_url, '/'))
        post_input = self.selenium.find_element_by_name("body")
        post_input.send_keys('THIS IS A TEST POST')
        self.selenium.find_element_by_xpath('//input[@value="Post!"]').click()
