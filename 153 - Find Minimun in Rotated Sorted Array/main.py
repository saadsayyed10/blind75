def minInRotatedSortedArray(nums: list[int]) -> int:
    # Define left and right
    l = 0
    r = len(nums) - 1

    # While left is less than right
    while l < r:
        # Compute mid
        m = l + (r - l) // 2

        # Check if nums[mid] is less than nums[right]
        if nums[m] < nums[r]:
            # Search in left (move right to mid)
            r = m
        
        # Other search in right
        else:
            l = m + 1
        
        # When loop ends, left points to the smallest element. Return nums[left]
    return nums[l]


def main():
    nums = [3, 4, 5, 6, 1, 2]
    print(f"Input: {nums}")

    res = minInRotatedSortedArray(nums)
    print(f"Output: {res}")

if __name__ == "__main__":
    main()