def upd_wordlst(wdlst):
    miss_words = ['I','A',' ']
    updt_wdlst = set(wdlst + miss_words)
    return updt_wdlst

def read_wdlst(fn):
    with open(fn, 'r') as file:
        wdlst = file.read().splitlines()
    return wdlst

def wrt_wdlst(fn, wdlst):
    with open(fn,'w') as file:
        file.write('\n'.join (wdlst))

if __name__ == "__main__":
    wdlst_fn = "words.txt"
    org_wdlst = read_wdlst(wdlst_fn)
    updt_wdlst = upd_wordlst(org_wdlst)
    wrt_wdlst(wdlst_fn, list(updt_wdlst))

    print("wordlist updated")