def isValidPalindrone(s: str) -> bool:
    # Create an empty
    newStr = ""

    # Loop through each character in input string
    for c in s:

        # Check if c is alpha-numeric character
        if c.isalnum():

            # If yes, then lower-case it and add it to newStr
            newStr += c.lower()
        
        # If reversed string is same as normal string, return true else return false
        return newStr == newStr[::-1]

def main():
    s = "Was it a car or a cat I saw?"
        
    res = isValidPalindrone(s)
    print(res)

if __name__ == "__main__":
    main()