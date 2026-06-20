def containerWithMostWater(heights: list[int]) -> int:
    # Declare two pointers, l and r
    l = 0
    r = len(heights) - 1

    # Declare res to store maximum area
    res = 0

    while l < r:
        # Compute area
        area = min(heights[l], heights[r]) * (r - l)

        # Store the maximum area value in res
        res = max(area, res)

        # Move the pointer at the shorter height
        if (heights[l] <= heights[r]):
            l += 1 # Move l to right
        else:
            r -= 1 # Move r to left

    # Return result
    return res

def main():
     height = [1,7,2,5,4,7,3,6]
     print(f"Input: {height}")

     res = containerWithMostWater(height)
     print(f"Output: {res}")

if __name__ == "__main__":
    main()