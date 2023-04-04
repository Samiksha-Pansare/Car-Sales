from django.shortcuts import render
from openpyxl import Workbook, load_workbook
from .models import Sales, Predictions
from django.http import HttpResponse

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
    return render(request,'index.html')

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
