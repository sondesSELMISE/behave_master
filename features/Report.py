import os
import unittest

from HTMLTestRunner import HTMLTestRunner

from features.steps import draganddrop

direct=os.getcwd()




class MyTestSuite(unittest.TestCase):
    def test_Issue(self):
        suite_smoke_test=unittest.TestSuite()
        suite_smoke_test.addTests([

            unittest.defaultTestLoader.loadTestsFromTestCase(draganddrop),

        ])
        chemin=open(direct+"\SmokeTest.html","w")

        runner1=HTMLTestRunner.HTMLTestRunner(
            stream=chemin,
            title='Test Report',
            description='Smoke Tests'

        )
        runner1.run(suite_smoke_test)

if __name__ == '__main__':
    unittest.main()
