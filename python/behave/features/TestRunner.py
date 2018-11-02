import sys
from behave import __main__ as test_runner

if __name__ == '__main__':
    sys.stdout.flush()
    test_runner.main()
