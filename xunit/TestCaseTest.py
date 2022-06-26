from xunit.TestCase import TestCase
from xunit.WasRun import WasRun


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testSetUp(self):
        self.test.run()
        assert ("setUp " == self.test.log)
