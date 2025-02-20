import os
import json

from length_of_last_word import Solution
from 53_testcase_gen import TestCases

class Test:
    def __init__(self):
        self.solution = Solution()
    
    def load_test_cases(self):
        """Load test cases either from JSON file if it exists, or generate new ones"""
        if os.path.exists("test_cases.json"):
            with open("test_cases.json", "r") as file:
                return json.load(file)
        return TestCases.generate_test_cases()
    
    def run_test_case(self, test_input, expected):
        """Run a single test case and return the result"""
        result = self.solution.lengthOfLastWord(test_input)
        return result == expected, result
    
    def run_tests(self, verbose=True):
        """Run all test cases and report results"""
        test_cases = self.load_test_cases()
        passed = 0
        failed = 0
        
        for test_input, expected in test_cases:
            success, result = self.run_test_case(test_input, expected)
            
            if success:
                passed += 1
                if verbose:
                    print(f"✓ Test passed: Input: '{test_input}' -> Expected: {expected}, Got: {result}")
            else:
                failed += 1
                print(f"✗ Test failed: Input: '{test_input}' -> Expected: {expected}, Got: {result}")
        
        total = passed + failed
        print(f"\nTest Summary:")
        print(f"Total tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Success rate: {(passed/total)*100:.2f}%")
        
        return passed == total
Test.run_tests()
