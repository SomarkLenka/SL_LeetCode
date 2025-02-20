# SL_LeetCode
A repository consisting of LeetCode solutions.

Solutions to problems are located in /Problems/ where each folder is titled per its leetcode problem number and given name.



Within each folder for /#N NAME OF PROBLEM/ where #N is the problem number and NAME OF PROBLEM is the name of the problem:
  - A .md file detailing the problem in question Ex. - NAME_OF_PROBLEM.md
  - A .py file containing the solution Ex. - NAME_OF_PROBLEM.py
  - A .py file containing a test case generator for the problem Ex. - #N_testcase_gen.py
  - A .json file containing test cases from the in-house generator, where SEED=999999 for random component of test cases Ex. - test_cases.json
  - A .py file testing test cases against our solution, supports .json or re-generates testcases if .json does not exist Ex. - test_#N.py



To run the code yourself, simply download desired problem folder and execute test_#N.py
Each script can be run individually.
Optionally, run "python test_#N.py -s 999999" where 999999 can be replaced with any number, as a seed, to generate and test new test cases. Doing so will overwrite the current test_cases.json file. Flag is optional.

Ensure to have args module installed if receiving errors in running the scripts. As well, if getting "basestring" error, use the 2to3 module to update, or manually update, line 37 of python/site-packages/args.py from basestring to str
