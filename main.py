from xunit.WasRun import WasRun

test = WasRun("testTemplateMethod")
print(test.wasRun)
test.testFailedResultFormatting()
print(test.wasRun)
