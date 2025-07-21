nums = []
for _ in range(5):
    nums.append(int(input()))

total = sum(nums)
average = total / len(nums)

print("ผลรวม =", total)
print("ค่าเฉลี่ย =", average)
