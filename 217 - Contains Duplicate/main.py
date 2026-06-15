def containsDuplicate(nums: list[int]) -> bool:
    # Init an empty set to store seen values
    seen = set()
    
    for num in nums:
        # For each number return True if num is seen again
        if num in seen:
            return True
        # If not then add num to the set
        seen.add(num)
    
    # If not duplicate not found, return False
    return False

def main():
    nums = [1, 2, 3, 3]
    print(nums)

    res = containsDuplicate(nums)

    print(res)

if __name__ == "__main__":
    main()