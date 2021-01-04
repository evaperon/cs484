import glob

with open('generateall.sh', 'w') as script:
    script.write("#! /bin/bash\n")

    all_txts = []
    for txt in glob.iglob("*.txt"):
        all_txts.append(txt)
    
    for txt in all_txts:
        script.write("python txtToXls.py {file}\n".format(file=txt))