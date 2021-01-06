import glob

with open('generatdots.sh', 'w') as script:
    script.write("#! /bin/bash\n")

    all_xlsxs = []
    for xlsx in glob.iglob("xlsxs/*"):
        no_prefix = xlsx.replace('xlsxs/','')
        all_xlsxs.append(no_prefix)
    
    for xlsx in all_xlsxs:
        script.write("python generateSmallDots.py {file}\n".format(file=xlsx))