from django.shortcuts import render
from openpyxl import Workbook, load_workbook
from .models import Sales, Predictions
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.
def home(request):
    # if 'username' in request.session:
    #     context = {
    #         'username':request.session['username']
    #     }
    # else:
    #     context = {
    #         'username':None
    #     }
    last_year_data_ungroup = Sales.objects.filter(date__iregex=r'2021$').all()
    lyd_group_date = last_year_data_ungroup.values('date').annotate(total_sales=Sum('sales'))
    sales_2021 = []
    for i in range(0,12):
        sales_2021.append(lyd_group_date[i]["total_sales"])
    total_sales_2021 = sum(sales_2021)
    current_year_data_ungroup = Predictions.objects.all()
    cyd_group_date = current_year_data_ungroup.values('month').annotate(total_sales=Sum('prediction'))
    sales_2022 = []
    for i in range(0,12):
        sales_2022.append(cyd_group_date[i]["total_sales"])
    context = {
        'sales_2021' : sales_2021,
        'total_sales_2021' : total_sales_2021,
        'sales_2022' : sales_2022
    }
    return render(request,'model.html', context)

def modelview(request):
    return render(request,"model.html")

def addhistorydata(request):
    # Load the entire workbook.
    wb = load_workbook("data/monthly-car-sales-v3.xlsx", data_only=True)
    # Load one worksheet.
    ws = wb['Worksheet']
    all_rows = list(ws.rows)

    # Pull information from specific cells.
    for row in all_rows[1:]:
        model = row[0].value
        month = row[1].value
        sales = row[2].value
        color = row[3].value
        region = row[4].value
        date = row[5].value
        db = Sales(model = model, month = month, sales = sales, color= color, region = region, date = date)
        db.save()
    print("Sales Data Added")
    return HttpResponse("Sales Data Added")


def addpredictions(request):
    # Load the entire workbook.
    wb = load_workbook("data/Predictions-2022.xlsx", data_only=True)
    # Load one worksheet.
    ws = wb['Worksheet']
    all_rows = list(ws.rows)

    # Pull information from specific cells.
    for row in all_rows[1:]:
        model = row[0].value
        color = row[1].value
        region = row[2].value
        month = row[3].value
        prediction = row[4].value
        db = Predictions(model = model, month = month, prediction = prediction, color= color, region = region)
        db.save()
    print("Prediction Data Added")
    return HttpResponse("Prediction Data Added")
