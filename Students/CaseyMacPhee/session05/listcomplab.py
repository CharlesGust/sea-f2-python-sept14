
def count_evens(nums):
    return len([i for i in nums if i % 2 == 0])
y = count_evens([2,3,4])
print y




x = range(16)

new_list = [hex(i) for i in x]

z = {i:j for i, j in zip(x, new_list)}
print z


y = {i: hex(i) for i in x}
print y
