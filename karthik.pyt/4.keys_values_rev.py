def invert_dictionary(d):
    return {v : k for k, v in d.items()}
print(invert_dictionary({'karthik' : 7393, 'viany' : 1450, 'keerthi' : 1354}))