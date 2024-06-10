def sum_two(nums, target):
    checked = []
    for idx in range(len(nums)):
        if idx not in checked:
            for index in range(idx + 1, len(nums)):
                if nums[idx] + nums[index] == target:
                    checked.append(idx)
                    checked.append(index)
    return checked

nums = [7, 3, 4, 2, 5, 9]
target = 11
print(sum_two(nums, target))