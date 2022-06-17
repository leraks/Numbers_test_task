from django.shortcuts import render
from .secondary_functions.data_sheets import data_sheets
from django.core.paginator import Paginator

def view_static(request , page = 0):
    data = data_sheets()
    if page != 0:
        p = Paginator(data, 15)
        count_p = p.count
        page_obj = p.get_page(page)
        summ = 0
        for i in page_obj:
            summ += int(i[2])

        return render(request, 'siteApp/viewStatic.html', {'data': page_obj , 'summ':summ,'count_p':count_p})
    else:
        summ = 0
        for i in data:
            summ += int(i[2])

        context = {"data":data,"summ":summ}
        return render(request,"siteApp/viewStatic.html", context)


