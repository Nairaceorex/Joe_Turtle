import teamcity
from teamcity.unittestpy import TeamcityTestRunner

if __name__ == '__main__':
    if teamcity.is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()

    unittest.main(testRunner=runner)

def fib(n):
    if n>1:
        return fib(n-1)+fib(n-2)
    else:
        return n