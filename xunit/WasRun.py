from xunit.TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.log = None
        self.wasSetUp = None
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def run(self):
        method = getattr(self, self.name)
        method()

    def testBrokenMethod(self):
        raise Exception
