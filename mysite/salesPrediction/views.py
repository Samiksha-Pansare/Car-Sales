from django.shortcuts import render
from openpyxl import Workbook, load_workbook
from .models import Sales, Predictions
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.
def home(request):

    # Historical Data - Region wise Sales

    models = ["Maruti Suzuki Alto 800","Maruti Suzuki Alto K10","Maruti Suzuki S-Presso","Maruti Suzuki Eeco","Maruti Suzuki Celerio","Maruti Suzuki Swift","Maruti Suzuki Grand Vitara","Maruti Suzuki XL6","Maruti Suzuki Brezza","Maruti Suzuki Dzire"]
    regions = ['Mumbai','Pune','Nagpur','Nashik']
    region_wise = dict()
    for r in regions:
        region_wise_query = Sales.objects.filter(region = r).values('model').annotate(total_sales=Sum('sales'))
        sv = []
        for i in range(len(region_wise_query)):
            sv.append(region_wise_query[i]['total_sales'])
        region_wise[r] = sv
    print(region_wise)

    # Historical Data - Color wise Sales

    color_wise_query = Sales.objects.values('color').annotate(total_sales=Sum('sales'))
    color_wise = []
    for i in range(0,3):
        color_wise.append(color_wise_query[i]["total_sales"])
    print(color_wise)

    # Historical Data - Yearly Sales 2013 -2021

    yearly_query = Sales.objects.values('month').annotate(total_sales=Sum('sales'))
    yearly_dict = dict()
    for i in range(len(yearly_query)):
        if yearly_query[i]['month'][-4:] not in yearly_dict:
            yearly_dict[yearly_query[i]['month'][-4:]] = yearly_query[i]['total_sales']
        else:
            yearly_dict[yearly_query[i]['month'][-4:]] += yearly_query[i]['total_sales']
    year_wise = list(yearly_dict.values())
    print(year_wise)
    
    data = {
        'region_wise' : region_wise,
        'color_wise' : color_wise,
        'year_wise' : year_wise,
    }
    context = {
        "data":data
    }
    return render(request,'home.html', context)
    
     
def forecast(request):
    if request.method == "POST":
        color = request.POST.get('color')
        region = request.POST.get('region')
        model = request.POST.get('model')
        sales_query = Predictions.objects.filter(color = color, region = region, model = model).all()
        sales = []
        for s in sales_query:
            sales.append(s.prediction)
        print(sales)
        data = {
        'sales' : sales,
        }
        context = {
            "data":data
        }
        return render(request,'filter.html', context)
    return render(request,'filter.html')



def modelview(request):
    return render(request,"model.html")

def modelpage(request, model):
    data = {
        "model":model
    }
    context= {
        "data":data
    }
    return render(request,"alto.html", context)

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


def modelinsights(request):
    # Maruti Suzuki Alto 800 - Color-wise

    color_wise_query = Sales.objects.filter(model = "Maruti Suzuki Alto 800").values('color').annotate(total_sales=Sum('sales'))
    color_wise = []
    for i in range(0,3):
        color_wise.append(color_wise_query[i]["total_sales"])
    print(color_wise)

    # Maruti Suzuki Alto 800 - Year-wise

    yearly_query = Sales.objects.filter(model = "Maruti Suzuki Alto 800").values('month').annotate(total_sales=Sum('sales'))
    yearly_dict = dict()
    for i in range(len(yearly_query)):
        if yearly_query[i]['month'][-4:] not in yearly_dict:
            yearly_dict[yearly_query[i]['month'][-4:]] = yearly_query[i]['total_sales']
        else:
            yearly_dict[yearly_query[i]['month'][-4:]] += yearly_query[i]['total_sales']
    year_wise = list(yearly_dict.values())
    print(year_wise)

    # Maruti Suzuki Alto 800 Yearly Region-wise

    regions = ['Mumbai','Pune','Nagpur','Nashik']
    region_wise = dict()
    for r in regions:
        region_wise_query = Sales.objects.filter(model = "Maruti Suzuki Alto 800", region = r).values('month').annotate(total_sales=Sum('sales'))
        yearly_dict = dict()
        for i in range(len(region_wise_query)):
            if region_wise_query[i]['month'][-4:] not in yearly_dict:
                yearly_dict[region_wise_query[i]['month'][-4:]] = region_wise_query[i]['total_sales']
            else:
                yearly_dict[region_wise_query[i]['month'][-4:]] += region_wise_query[i]['total_sales']
        region_wise[r] = list(yearly_dict.values())
    print(region_wise)

    data = {
        "region_wise":region_wise,
        "color_wise": color_wise,
        "year_wise":year_wise
    }
    context = {
        "data":data
    }
    return render(request, 'alto-insights.html', context)


def modelforecast(request):
    return render(request, 'alto-forecast.html')


def groupingdata(request):

    # Prediction Data Month-wise

    prediction_data_month_wise_query = Predictions.objects.values('month').annotate(total_sales=Sum('prediction'))
    prediction_data_month_wise = []
    for i in range(0,12):
        prediction_data_month_wise.append(prediction_data_month_wise_query[i]["total_sales"])
    print(prediction_data_month_wise)

    # Prediction Data Color-wise

    prediction_data_color_wise_query = Predictions.objects.values('color').annotate(total_sales=Sum('prediction'))
    prediction_data_color_wise = []
    for i in range(0,3):
        prediction_data_color_wise.append(prediction_data_color_wise_query[i]["total_sales"])
    print(prediction_data_color_wise)

    # Prediction Data Region-wise

    prediction_data_region_wise_query = Predictions.objects.values('region').annotate(total_sales=Sum('prediction'))
    prediction_data_region_wise = []
    for i in range(0,4):
        prediction_data_region_wise.append(prediction_data_region_wise_query[i]["total_sales"])
    print(prediction_data_region_wise)

    # Prediction Data Model-wise Color-wise Region-wise Month-wise

    m = 0
    c = 0
    r = 0
    models = ["Maruti Suzuki Alto 800","Maruti Suzuki Alto K10","Maruti Suzuki S-Presso","Maruti Suzuki Eeco","Maruti Suzuki Celerio","Maruti Suzuki Swift","Maruti Suzuki Grand Vitara","Maruti Suzuki XL6","Maruti Suzuki Brezza","Maruti Suzuki Dzire"]
    regions = ['Mumbai','Pune','Nagpur','Nashik']
    colors = ["Black","Grey","White"]
    prediction_query = Predictions.objects.filter(model = models[m], color = colors[c], region = regions[r]).all()
    prediction = []
    for i in range(0,12):
        prediction.append(prediction_query[i].prediction)
    print(prediction)

    # Prediction Data Region-wise Month-wise

    prediction_region_month_wise = []
    for r in regions:
        prediction_region_month_wise_query = Predictions.objects.filter(region = r).values('month').annotate(total_sales=Sum('prediction'))
        p = []
        for i in range(0,12):
            p.append(prediction_region_month_wise_query[i]["total_sales"])
        prediction_region_month_wise.append(p)
    print(prediction_region_month_wise)

    # Prediction Data Color-wise Month-wise

    prediction_color_month_wise = []
    for c in colors:
        prediction_color_month_wise_query = Predictions.objects.filter(color = c).values('month').annotate(total_sales=Sum('prediction'))
        p = []
        for i in range(0,12):
            p.append(prediction_color_month_wise_query[i]["total_sales"])
        prediction_color_month_wise.append(p)
    print(prediction_color_month_wise)

    # Historical Data - Region wise Sales

    region_wise_query = Sales.objects.values('region').annotate(total_sales=Sum('sales'))
    region_wise = []
    for i in range(0,4):
        region_wise.append(region_wise_query[i]["total_sales"])
    print(region_wise)

    # Historical Data - Color wise Sales

    color_wise_query = Sales.objects.values('color').annotate(total_sales=Sum('sales'))
    color_wise = []
    for i in range(0,3):
        color_wise.append(color_wise_query[i]["total_sales"])
    print(color_wise)

    # Historical Data - Yearly Sales 2013 -2021

    yearly_query = Sales.objects.values('month').annotate(total_sales=Sum('sales'))
    yearly_dict = dict()
    for i in range(len(yearly_query)):
        if yearly_query[i]['month'][-4:] not in yearly_dict:
            yearly_dict[yearly_query[i]['month'][-4:]] = yearly_query[i]['total_sales']
        else:
            yearly_dict[yearly_query[i]['month'][-4:]] += yearly_query[i]['total_sales']
    year_wise = list(yearly_dict.values())
    print(year_wise)

    return HttpResponse("Done")

# last_year_data_ungroup = Sales.objects.filter(date__iregex=r'2021$').all()
    # lyd_group_date = last_year_data_ungroup.values('date').annotate(total_sales=Sum('sales'))
    # sales_2021 = []
    # for i in range(0,12):
    #     sales_2021.append(lyd_group_date[i]["total_sales"])
    # total_sales_2021 = sum(sales_2021)
    # current_year_data_ungroup = Predictions.objects.all()
    # cyd_group_date = current_year_data_ungroup.values('month').annotate(total_sales=Sum('prediction'))
    # sales_2022 = []
    # for i in range(0,12):
    #     sales_2022.append(cyd_group_date[i]["total_sales"])