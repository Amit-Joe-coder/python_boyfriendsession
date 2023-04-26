from django.shortcuts import render
from mainapp.forms import *
# Create your views here.
def index_view(request):
    return render(request,'index.html')

def form_view(request):
    form=my_form()
    if request.method=='POST':
        bf_name=request.POST['bname']
        bage=request.POST['age']
        gf_name=request.POST['gname']
        request.session['bname']=bf_name
        request.session['age']=bage
        request.session['gname']=gf_name
        return index_view
    return render(request,'form.html',{'form':form})
    

def result_view(request):
    return render(request,'info.html',)
    
    
