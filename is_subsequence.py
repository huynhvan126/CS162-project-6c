# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 11/06/2024
# Description: Write a recursive function that takes two string parameters and returns True if the first string is a subsequence of the second string, but returns False otherwise.
def is_subsequence(str1, str2):
    """
    This function checks whether str1 is a subsequence of str2.
    """
    if not str1:
        return True
    if not str2:
        return False

    # Check if 1st characters match. If yes, continue searching in the remaining str2.
    if str1[0] == str2[0]:
        return is_subsequence(str1[1:], str2[1:])
    else:
        # If 1st character don't match, continue searching
        return is_subsequence(str1, str2[1:])
