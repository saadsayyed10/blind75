def encode(strs: list[str]) -> str:
    # If encoded string is empty string empty string
    if not strs:
        return ""
    
    # Create an empty list to store the sizes of each string(word)
    sizes, res = [], []

    # Append length of the size of each string
    for s in strs:
        sizes.append(len(s))
    
    # Build a single comma separated string
    for sz in sizes:
        res.append(str(sz))
        res.append(",")
    
    # Add "#" to mark the end of the word and append the actual string in order
    res.append("#")
    res.extend(strs)

    # Return final encoded string
    return ''.join(res)

def decode(s: str) -> list[str]:
    # If encoded string is empty string empty list
    if not s:
        return []
    
    # Create empty list to read and parse the encoded string and a variable to increment
    sizes, res, i = [], [], 0

    # Read characters from the start until reaching '#' to extract all recorded sizes
    while s[i] != '#':
        j = i

        # Parse each size until reading a ','
        while s[j] != ',':
            j += 1
        sizes.append(int(s[i:j]))
        i = j + 1
    
    i += 1

    # After '#' extract substring according to list size
    for sz in sizes:
        # Append substring to the result by reading characters
        res.append(s[i:i + sz])
        i += sz
    
    return res

def main():
    strs = ["I", "love", "Leet", "code"]
    print(f"Original list: {strs}")

    encodedStr = encode(strs)
    print(f"Encoded string is: {encodedStr}")

    decodedList = decode(encodedStr)
    print(f"Decoded list is: {decodedList}")

if __name__ == "__main__":
    main()
