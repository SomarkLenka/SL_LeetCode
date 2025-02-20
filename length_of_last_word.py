class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Reverse the string such that we gain access to the last word, first.
        s = s[::-1]

        # Boolean flag to identify once we begin reading a word, ignores whitespace.
        word=False

        # Our counter to keep track of word length
        count=0

        # Loop through each character in the string. We enumerate to keep track of our position in the string, ensuring we return count when we reach the end of the string.
        for i, c in enumerate(s):

            # Check if the character is a letter, if so increment the counter, and set the word Bool to True such that the exit conditions can be triggered upon ceasing to read our current word.
            if c.isalpha():
                count+=1
                word=True

            # If we are reading our word and the char is not a letter, we are no longer reading a word. Exit and return most recent count.
            if word and not c.isalpha():
                return count

            # If the word is the only word in the string, terminate the loop upon reaching the end of the string and hence the word.
            if word and i==len(s)-1:
                return count
