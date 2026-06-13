def longestConsecutiveSequence(nums: list[int]) -> int:
    # Convert array into a set
    numSet = set(nums)

    # Init longest var to track length
    longest = 0

    # For each num in numset
    for num in numSet:
        # Check if num - 1 is not not in the set
        if (num - 1) not in numSet:
            # If true, init length = 1
            length = 1

            # While num + length exist in set, increase length
            while(num + length) in numSet:
                length += 1
            
            # Update longest as the max. among length and longest
            longest = max(length, longest)
    # Return the number of elements in the longest sequence
    return longest
        
def main():
    nums = [2,20,4,10,3,4,5]
    print(f"Input array {nums}")

    res = longestConsecutiveSequence(nums)
    print(f"Longest consecutive sequence: {res}")

if __name__ == "__main__":
    main()

