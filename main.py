from xunit.WasRun import WasRun

test = WasRun("testSetUp")
print(test.wasRun)
test.testMethod()
print(test.wasRun)
