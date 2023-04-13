from django.shortcuts import render
from openpyxl import Workbook, load_workbook
from .models import Sales, Predictions
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.
def home(request):

    totalsales = Sales.objects.aggregate(Sum('sales'))
    print(totalsales)

    highest_query = Sales.objects.values('region').annotate(total_sales=Sum('sales'))
    highest = highest_query[0]['total_sales']
    highest_region = highest_query[0]['region']
    
    for i in range(len(highest_query)):
        if highest_query[i]['total_sales'] > highest:
            highest_region = highest_query[i]['region']
            highest = highest_query[i]['total_sales']

    highest_query = Sales.objects.values('model').annotate(total_sales=Sum('sales'))
    mhighest = highest_query[0]['total_sales']
    highest_model = highest_query[0]['model']
    
    for i in range(len(highest_query)):
        if highest_query[i]['total_sales'] > mhighest:
            highest_model = highest_query[i]['model']
            mhighest = highest_query[i]['total_sales']

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

    # Historical Data - Color wise Sales

    color_wise_query = Sales.objects.values('color').annotate(total_sales=Sum('sales'))
    color_wise = []
    for i in range(0,3):
        color_wise.append(color_wise_query[i]["total_sales"])

    # Historical Data - Yearly Sales 2013 -2021

    yearly_query = Sales.objects.values('month').annotate(total_sales=Sum('sales'))
    yearly_dict = dict()
    for i in range(len(yearly_query)):
        if yearly_query[i]['month'][-4:] not in yearly_dict:
            yearly_dict[yearly_query[i]['month'][-4:]] = yearly_query[i]['total_sales']
        else:
            yearly_dict[yearly_query[i]['month'][-4:]] += yearly_query[i]['total_sales']
    year_wise = list(yearly_dict.values())
    
    data = {
        'region_wise' : region_wise,
        'color_wise' : color_wise,
        'year_wise' : year_wise,
        'totalsales':totalsales['sales__sum'],
        'highest':highest,
        'highest_region':highest_region,
        'mhighest':mhighest,
        'highest_model':highest_model
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

def modelpage(request, model):
    sales = Sales.objects.filter(model = model).values('model').annotate(total_sales=Sum('sales'))

    predicted_sales = Predictions.objects.filter(model = model).values('model').annotate(total_sales=Sum('prediction'))

    total_sales = sales[0]['total_sales']
    predicted_sales = predicted_sales[0]['total_sales']

    highest_query = Predictions.objects.filter(model = model).values('month').annotate(total_sales=Sum('prediction'))
    highest = highest_query[0]['total_sales']
    highest_month = '01'

    for i in range(len(highest_query)):
        if highest_query[i]['total_sales'] > highest:
            highest_month = highest_query[i]['month'][3:5]
            highest = highest_query[i]['total_sales']

    helper = {
        '01':"January",'02':"February",'03':"March",'04':"April",'05':"May",'06':"June",'07':"July",'08':"August",'09':"September",'10':"October",'11':"November",'12':"December"}
    data = {
        "model":model,
        "total_sales":total_sales,
        "predicted_sales":predicted_sales,
        "highest":highest,
        "highest_month":helper[highest_month]
    }
    context= {
        "data":data
    }
    return render(request,"alto.html", context)

def modelinsights(request, model):
    # Maruti Suzuki Alto 800 - Color-wise

    color_wise_query = Sales.objects.filter(model = model).values('color').annotate(total_sales=Sum('sales'))
    color_wise = []
    for i in range(0,3):
        color_wise.append(color_wise_query[i]["total_sales"])
    print(color_wise)

    # Maruti Suzuki Alto 800 - Year-wise

    yearly_query = Sales.objects.filter(model = model).values('month').annotate(total_sales=Sum('sales'))
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
        region_wise_query = Sales.objects.filter(model = model, region = r).values('month').annotate(total_sales=Sum('sales'))
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
        "year_wise":year_wise,
        "model":model
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


