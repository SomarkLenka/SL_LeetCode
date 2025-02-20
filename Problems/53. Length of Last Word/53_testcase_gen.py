import random
import string
import json

# Define a constant seed value to ensure reproducibility across test case generations.
SEED = "999999"

class TestCases:
    def generate_test_cases(seed=SEED):
        # Set the random seed for consistent output across multiple runs.
        random.seed(seed)  
        
        # List of manually defined test cases to cover common edge cases and typical scenarios.
        test_cases = [
            ("Hello World!", 5),  # Normal case with two words
            ("   Lorem  ipsum    dolerem   yarr  ", 4),  # String with multiple spaces between words
            ("how poco fool cow ? by laughs", 6),  # Sentence with various word lengths
            ("a", 1),  # Single character word case
            ("   ", 0),  # String containing only whitespace characters
            ("word", 4),  # A single word with no spaces
            ("word   ", 4),  # Single word followed by multiple spaces
            ("   word", 4),  # Single word preceded by spaces
            ("", 0),  # Empty string case
            ("words wordy worded", 6),  # String with multiple words of varying lengths
            ("wordy, wordo,,,", 5),  # Words separated by punctuation marks
        ]
        
        # Generating additional random test cases to enhance coverage.
        for _ in range(5):
            # Create a list of randomly generated words, each having a random length between 1 and 10 characters.
            words = ["".join(random.choices(string.ascii_letters, k=random.randint(1, 10))) for _ in range(random.randint(1, 5))]
            
            # Introduce a random selection of punctuation marks to add complexity to the test cases.
            punctuations = "".join(random.choices(string.punctuation, k=random.randint(0, 3)))
            
            # Construct the final test case string by joining words with spaces, appending punctuation, and adding trailing spaces.
            s = " ".join(words) + punctuations + " " * random.randint(0, 5)
            
            # Compute the expected output by determining the length of the last valid word.
            expected = len(words[-1]) if words else 0
            
            # Append the generated test case to the list.
            test_cases.append((s, expected))
        
        # Save the test cases to a JSON file for external use in another program.
        test_data = {"seed": seed, "test_cases": test_cases}
        with open("test_cases.json", "w") as file:
            json.dump(test_data, file, indent=4)
        
        # Return the list of test cases.
        return test_cases
