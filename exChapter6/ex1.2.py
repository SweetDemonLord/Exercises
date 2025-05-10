def pairwise_product_sum(list1, list2):
    if len(list1) < len(list2):
        list1 = list1 * ((len(list2) // len(list1))+1)
    elif len(list2) < len(list1):
        list2 = list2 * ((len(list1) // len(list2))+1)
    result = sum(x * y for x, y in zip(list1, list2))
    return result
list1 = [10,20,30]
list2 = [10,20]
result = pairwise_product_sum(list1, list2)
print("The pairwise product sum: ", result)