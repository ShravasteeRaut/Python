test_dict = {
    'Codingal': 'a',
    'is': 'a',
    'best': 'a',
    'for': 'a',
    'Coding': 'b'
}

print(test_dict)

K = 'a'

res = 0
for key in test_dict:
    if test_dict[key] == K:
        res += 1

print("Frequency of K is:", res)