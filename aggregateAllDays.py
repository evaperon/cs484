import sys
import glob
import openpyxl
import pygraphviz as pgv


def main():
    # the argument is the type of graph: retweet, quote, mention, reply
    args = sys.argv
    relationship =  args[1]
    fname = "xlsxs/"+relationship+"*"
    
    graph_data = []

    for file in glob.iglob(fname):

        split_name = file.split('-')
        last_part = split_name[3]
        last_split = last_part.split('.')
        label = int(last_split[0])
        print("File: {f} , label = {l}".format(f=file, l=label))

        
        wb = openpyxl.load_workbook(file)
        sheet = wb.active

        for row in sheet.iter_rows(values_only=True):
            temp_dict = {}
            temp_dict['source']=row[0]
            temp_dict['dest']=row[1]
            temp_dict['weight']=row[2]
            temp_dict['label']=label
            graph_data.append(temp_dict)

    graph = pgv.AGraph(directed=True, strict=False)
    for edge in graph_data:
        graph.add_edge(str(edge['source']), str(edge['dest']), weight=edge['weight'], label=edge['label'])

    graph.write("dots/"+relationship+'.dot')


    
    


if __name__ == "__main__":
    main()