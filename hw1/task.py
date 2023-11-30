# Bubble sort (imperative style)
def sort_list_imperative(numbers): 
    flag = True
    while flag:
        flag = False
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                flag = True
    return numbers

# Declarative style
def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers


print(f"Imperative style -> {sort_list_imperative([41, 6, 2, 7, -3, 2, 8, 56])}")
print(f"Declarative style -> {sort_list_imperative([41, 6, 2, 7, -3, 2, 8, 56])}")

