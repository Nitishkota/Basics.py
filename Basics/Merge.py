#Write a function dict_merge_sum that takes two dictionaries d1 and d2 as parameters. 
#The values of both dictionaries are numerical. The function should return the merged sum dictionary m of those dictionaries.
# If a key k is both in d1 and d2, the corresponding values will be added and included in the dictionary m If k is only contained in one of the dictionaries, the k and the corresponding value will be included in m


def dict_merge_sum(d1, d2):
    """ Merging and calculating the sum of two dictionaries: 
    Two dicionaries d1 and d2 with numerical values and
    possibly disjoint keys are merged and the values are added if
    the exist in both values, otherwise the missing value is taken to
    be 0"""
    
    merged_sum = d1.copy()
    for key, value in d2.items():
        if key in d1:
            d1[key] += value
        else:
            d1[key] = value
            merged_sum.update(d2)
    
    return merged_sum

d1 = dict(a=4, b=5, d=8)
d2 = dict(a=1, d=10, e=9)

print(dict_merge_sum(d1, d2))
