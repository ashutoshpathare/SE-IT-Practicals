def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    result = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            result.append(i)

    return result


text = input("Enter text: ")
pattern = input("Enter pattern: ")

res = naive_search(text, pattern)

if len(res) == 0:
    print("Pattern not found")
else:
    print("Pattern found at index:", *res)
