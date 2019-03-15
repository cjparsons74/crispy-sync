import unittest
from crispysync.main.LambdaHandler import LambdaHandler

class LambdaHandler_test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Returns_Request(self):
        victim = LambdaHandler()
        result = victim.handle(None, None)
        self.assertEqual(result, "I'm a Lambda!", 'Expected other value...')
