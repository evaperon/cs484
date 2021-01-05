# generate .dot files to give as input to gephi

import pygraphviz as pgv
import openpyxl
import sys

def main():
    args = sys.argv
    filename =  args[1]
    fname = "xlsxs/"+filename
    split_name = filename.split('-')
    last_part = split_name[3]
    last_split = last_part.split('.')
    label = int(last_split[0])
    print("File: {f} , label = {l}".format(f=filename, l=label))

    # graph_data is an array of edges (dictionaries)
    graph_data = []
    wb = openpyxl.load_workbook(fname)
    sheet = wb.active

    for row in sheet.iter_rows(values_only=True):
        temp_dict = {}
        temp_dict['source']=row[0]
        temp_dict['dest']=row[1]
        temp_dict['weight']=row[2]
        temp_dict['label']=label
        graph_data.append(temp_dict)

    # print("Source = {s}, Destination = {d}. Weight = {w}".format(s=graph_data[0]['source'], d=graph_data[0]['dest'], w=graph_data[0]['weight']))

    # create a directed graph
    graph = pgv.AGraph(directed=True)
    for edge in graph_data:
        graph.add_edge(str(edge['source']), str(edge['dest']), weight=edge['weight'], label=edge['label'])

    graph.write("dots/"+filename+'.dot')
    # graph.layout(prog='dot')
    # graph.draw("example.png")




if __name__ == "__main__":
    main()