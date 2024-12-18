FILE_NAME = 'day07.txt'

lines = [line.strip() for line in open(FILE_NAME, 'r').readlines()]

# same approach as part 1, with one addition
def operate(nums, target):
    if len(nums) == 1:
        return target == nums[0]

    if target % nums[-1] == 0 and operate(nums[:-1], target // nums[-1]):
        return True

    if target > nums[-1] and operate(nums[:-1], target - nums[-1]):
        return True

    # checking if we can concatenate the last number
    # check the length of the target and the last number
    # check if target ends with the last number
    if len(str(target)) > len(str(nums[-1])) and str(target).endswith(str(nums[-1])) and operate(nums[:-1], int(str(target)[:-len(str(nums[-1]))])):
        return True


total = 0
for line in lines:
    target, nums = line.split(':')
    target = int(target)
    nums = [int(n) for n in nums.strip().split()]
    if operate(nums, target):
        total += target

print(total)
