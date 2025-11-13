def fst_wd(str):
    return ' '.join(word.capitalize() for word in str.split())
print(fst_wd('hello world how are yoe'))
