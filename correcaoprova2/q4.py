#funcao recursiva

def soma(nums: list):

    if len(nums) == 1:
        return nums.pop()

    return nums.pop()+soma(nums)
