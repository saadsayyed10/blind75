def validAnagram(s: str, t: str) -> bool:
    # If both string have different lengths, return False
    if (len(s) != len(t)):
        return False

    # Init two hash maps to store character frequencies for both string
    countS, countT = {}, {}

    for i in range(len(s)):
        # Iterate through both string and increase character count in both map
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    # If frequencies of both maps match return True, else False
    return countS == countT

def main():
    s = "racecar"
    t = "carrace"

    res = validAnagram(s, t)
    print(res)

if __name__ == "__main__":
    main()