import os
import json
import args
import argparse

from length_of_last_word import Solution
from _53_testcase_gen import TestCases


def parse_arguments():
    #Parse command-line arguments for setting a custom seed
    SEED = 999999
    parser = argparse.ArgumentParser(description="Pass -s 999999 replacing 999999 with your desired seed")
    parser.add_argument("-s", "--seed", type=int, default=SEED, help="Specify a seed if desired, default is 999999")
    return parser.parse_args()

class Test:
    def __init__(self):
        self.solution = Solution()
    
    def load_test_cases(self, seed):
        #Load test cases either from JSON file if it exists, or generate new ones
        if os.path.exists("test_cases.json"):
            with open("test_cases.json", "r") as file:
                test_data = json.load(file)
                seed_used = test_data["seed"]
                test_cases = test_data["test_cases"]
                print(f"Running tests with seed: {seed_used}")
                return test_cases, seed_used
        else:
            test_cases = TestCases.generate_test_cases(seed)
            print(f"Running tests with generated seed: {seed}")
            return test_cases, seed
    
    def run_test_case(self, test_input, expected):
        #Run a single test case and return the result
        result = self.solution.lengthOfLastWord(test_input)
        return result == expected, result
    
    def run_tests(self, seed, verbose=True):
        #Run all test cases and report results
        test_cases, seed_used = self.load_test_cases(seed)
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
        


if __name__ == "__main__":
    args = parse_arguments()
    test_instance = Test()
    test_instance.run_tests(args.seed)
