import unittest


def execute_all_tests(tests_folder):
    suites = unittest.TestLoader().discover(tests_folder)
    unittest.TextTestRunner().run(suites)


if __name__ == "__main__":
    execute_all_tests("ArraysAndStrings")
    execute_all_tests("LinkedLists")

