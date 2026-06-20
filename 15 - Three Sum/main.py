def isThreeSum(nums: list[int]) -> list[list[int]]:
    # Create an empty list to store triplet result
    res = []

    # Sort the input list to handle two pointer logic and skip duplicates
    nums.sort()

    # Loop through the input list using index i
    for i, a in enumerate(nums):
        
        # Break because all number are positive
        if a > 0:
            break 
        
        # Continue because not all numbers are positive
        if i > 0 and a == nums[i - 1]:
            continue

        # Declare l, r pointers
        l = i + 1
        r = len(nums) - 1

        while l < r:
            # Declare threeSum
            threeSum = a + nums[l] + nums[r]

            # If threeSum is greater than 0, shift r to left
            if threeSum > 0:
                r -= 1
            
            # If threeSum is less than 0, shift l to right
            elif threeSum < 0:
                l += 1

            # If threeSum is 0
            else:
                # Add triplet to the result list
                res.append([a, nums[l], nums[r]])

                # Move both pointers inward
                l += 1
                r -= 1

                # Skip duplicate at l pointer
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    # Return triplet result list
    return res

def main():
    nums = [-1,0,1,2,-1,-4]
    print(f"Input: {nums}")

    res = isThreeSum(nums)
    print(f"Output: {res}")

if __name__ == "__main__":
    main()