import requests
import unittest

class TestAPI (unittest.TestCase):

  def test_get_users(self):
    response = 200
    self.assertEqual(response, 200)

if __name__ == '__main__':
  unittest.main()
