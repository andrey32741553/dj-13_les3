import csv
from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'
    with open("inflation_russia.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=";")
        inflation_list = list(rows)
    titles = inflation_list[0]
    info_list = inflation_list[1:]
    for item in info_list:
        for i, info in enumerate(item):
            if '.' in item[i]:
                item[i] = float(info)
            elif '.' not in item[i] and item[i] != '':
                item[i] = int(info)
            elif item[i] == '':
                item[i] = '-'
    context = {'titles': titles,
               'info_list': info_list}

    return render(request, template_name,
                  context=context)
