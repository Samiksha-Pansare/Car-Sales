from django.shortcuts import render

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
