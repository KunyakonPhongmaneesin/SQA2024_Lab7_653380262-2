# Lab#7 - Whitebox testing
# SC353201 Software Quality Assurance
# Semester 1/2567
# Instructor: Chitsutha Soomlek

class CountClump:
  """
  This class provides a method to count the number of "clumps" in a list of integers.
  A clump is a run of 2 or more of the same adjacent numbers.
  """

  @staticmethod
  def count_clumps(nums):
    """
    Counts the number of "clumps" in a list of integers.
    A clump is a run of 2 or more of the same adjacent numbers.

    Args:
      nums: A list of integers.

    Returns:
      The number of clumps in the list.
    """
    if nums is None or len(nums) == 0:    #Block1
      return 0                             #Block2

    count = 0                               #Block3
    prev = nums[0]
    in_clump = False

    for i in range(1, len(nums)):           #Block4
      if nums[i] == prev and not in_clump:  #Block5
        in_clump = True                     #Block6
        count += 1
      elif nums[i] != prev:                 #Block7
        prev = nums[i]                      #Block8
        in_clump = False

    return count                            #Block9

# Example usage:
nums = [1, 2, 2, 3, 3, 4, 4, 4, 1]
clump_count = CountClump.count_clumps(nums)
print(f"Number of clumps: {clump_count}")  # Output: Number of clumps: 3
