def productArrayExceptSelf(nums: list[int]) -> list[int]:
    # Declare n as the length of the array
    n = len(nums)

    # Declare 3 three arrays as size of n
    res = [0] * n
    pref = [0] * n
    suff = [0] * n

    # Set prefix and suffix arrays such that there are no elements to the left and right of the index
    pref[0] = suff[n - 1] = 1

    # Build the prefix array
    for i in range(1, n):
        pref[i] = nums[i - 1] * pref[i - 1]

    # Build the suffix array
    for i in range(n - 2, -1, -1):
        suff[i] = nums[i + 1] * suff[i + 1]

    # Build the result array
    for i in range(n):
        res[i] = pref[i] * suff[i]

    # Return result array
    return res

def main():
    arr = [1, 2, 4, 8]
    print(f"Input: {arr}")

    res = productArrayExceptSelf(arr)
    print(f"Output: {res}")

if __name__ == "__main__":
    main()