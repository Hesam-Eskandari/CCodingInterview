import unittest
from ArraysAndStrings import check_permutation 

def execute_all_tests(tests_folder):
    suites = unittest.TestLoader().discover(tests_folder)
    unittest.TextTestRunner().run(suites)

if __name__ == "__main__":
  #execute_all_tests("ArraysAndStrings")
  check = check_permutation.CheckPermutation("12341","54321")
  print(check())
  