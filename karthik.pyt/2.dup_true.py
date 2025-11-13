def has_duplicates(lst):
    return any(lst.count(i) > 1 for i in lst)
print(has_duplicates([1,2,3,1,1]))