arr = list(map(int, input("Enter numbers separated by space: ").split()))

seen = set()
next_num = max(arr) + 1
result = []

for x in arr:
    if x not in seen:
        result.append(x)
        seen.add(x)
    else:
        while next_num in seen:
            next_num += 1
        result.append(next_num)
        seen.add(next_num)

print("Modified array:", result)