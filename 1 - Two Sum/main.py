def twoSum(nums: list[int], target: int) -> list[int]:
    # Init a hash map to store values and index of each element in the array
    prevMap = {}

    # Iterate through the array
    for i, n in enumerate(nums):
        # Compute complement of the current element
        diff = target - nums[i]

        # Check if complement exists in the hash map
        if diff in prevMap:
            # If yes, then return the indices of current element and compliment, else return empty array
            return [prevMap[diff], i]

        # Continue loop
        prevMap[n] = i

def main():
    nums = [3, 4, 5, 7]
    target = 7

    print(f"Array: {nums}\nTarget: {target}")

    res = twoSum(nums, target)
    print(f"Output: {res}")

if __name__ == "__main__":
    main()