import xlsxwriter
# from xlwt import Workbook
import sys

def main():
    args = sys.argv
    filename =  args[1]
    fname = "txts/"+filename
    
    # parse file
    lines=[]
    with open(fname, 'r') as txt:
        for line in txt:
            lines.append(line)
    splitLines=[]
    for line in lines:
        newLine = []
        for s in line:
            k = s.replace('\n','')
            newLine.append(k)
        splitLines.append(line.split(' '))
    # print(splitLines[0][0])
    # print(splitLines[0][1])
    # print(splitLines[0][2])
    
    xlsxname = "xlsxs/"+filename+".xlsx"

    wb = xlsxwriter.Workbook(xlsxname)
    sheet = wb.add_worksheet()

    for i in range(len(splitLines)):
        sheet.write(i, 0, splitLines[i][0])
        sheet.write(i, 1, splitLines[i][1])
        sheet.write(i, 2, splitLines[i][2].replace('\n',''))

    
    wb.close()


if __name__ == "__main__":
    main()