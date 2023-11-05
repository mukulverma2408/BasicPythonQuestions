#Python program to check whether the string is Symmetrical or Palindrome

def CheckPalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

print(CheckPalindrome("mukullukum"))
