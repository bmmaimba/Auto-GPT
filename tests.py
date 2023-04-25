import unittest
import coverage
import os
import openai
 
openai.api_key = os.environ["OPENAI_API_KEY"]

if __name__ == "__main__":
    # Start coverage collection
    cov = coverage.Coverage()
    cov.start()

    # Load all tests from the 'autogpt/tests' package
    suite = unittest.defaultTestLoader.discover("./tests")

    # Run the tests
    unittest.TextTestRunner().run(suite)

    # Stop coverage collection
    cov.stop()
    cov.save()

    # Report the coverage
    cov.report(show_missing=True)
