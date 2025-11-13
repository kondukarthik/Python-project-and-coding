def meg_f(f1,f2,mg):
    try:
        with open(f1,'r') as f1, open(f2,'r') as f2:
            c1=f1.read()
            c2=f2.read()

            with open(mg,'w') as mg:
                mg.write(c1+" "+c2)
                print("merged success")

    except FileNotFoundError as e:
        print(f"Error:{e.filename} not found")

meg_f('f1.txt','res.txt','r.txt')
