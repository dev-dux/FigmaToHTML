import os
import json
jsonfolder = sorted(os.listdir('dataset'))
odir = os.listdir('output')
j= 0
for dataset in jsonfolder :
    # print(datase)
    if dataset !='ten':

        jsn = f'dataset/{dataset}/train/json/{dataset}.json'
        with open(jsn, 'r') as f:
            data = json.load(f)
        keys = data['nodes'].keys()
    #         j = 0
    #         htmlfol = os.listdir(f'output/{dataset}')
        for i in keys:
            print(f'folder : {dataset} \nnode   : {dataset}_output_node_{i}\n\n')
        j+=1
        print(j)
    #             before_html = f'output/{dataset}/{html}'
    #             after_html = f'output/{dataset}/{html}_node_{i}.html'
    #             print(f'html before:',before_html)
    #             print(os.rename(before_html, after_html))
    #             print(f'html after:',after_html)

    #             j+=1
    