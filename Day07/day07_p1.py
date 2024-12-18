FILE_NAME = 'day07.txt'

lines = [line.strip() for line in open(FILE_NAME, 'r').readlines()]

# going from the end of the numbers to the front
def operate(nums, target):

    # check if first number is the target (after reduced)
    if len(nums) == 1:
        return target == nums[0]

    # check if the target is divisible by the last number
    if target % nums[-1] == 0 and operate(nums[:-1], target // nums[-1]):
        return True

    # check if the target is greater than the last number
    if target > nums[-1] and operate(nums[:-1], target - nums[-1]):
        return True


# getting total of all targets that can be reduced
total = 0
for line in lines:
    target, nums = line.split(':')
    target = int(target)
    nums = [int(n) for n in nums.strip().split()]
    if operate(nums, target):
        total += target

print(total)
