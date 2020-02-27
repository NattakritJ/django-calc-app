from django.shortcuts import render
from .forms import CalcForm
from .models import Calc
# Create your views here.
def main(request):
    checksubmit = False
    if request.POST.get('clearall'):
        Calc.objects.all().delete()
    allobject = Calc.objects.all()
    objectsize = Calc.objects.count()
    result = "0.0"
    if objectsize > 10:
        Calc.objects.all()[:1].get().delete()
    if request.method == "POST":
        form = CalcForm(request.POST)
        if form.is_valid():
            data = form.save()
            x = form.cleaned_data.get('x')
            y = form.cleaned_data.get('y')
            if form.cleaned_data.get('operations') == '+':
                data.result = x+y
            if form.cleaned_data.get('operations') == '-':
                data.result = x-y
            if form.cleaned_data.get('operations') == '*':
                data.result = x*y
            if form.cleaned_data.get('operations') == '/':
                data.result = x/y
            result = data.result
            form.save()
            form = CalcForm()
            checksubmit = True
    else:
        form = CalcForm()
    return render(request, 'main.html', {'form': form,
                                         'allobject': allobject,
                                         'result':result,
                                         'checksubmit':checksubmit})

def aboutme(request):
    return render(request, 'aboutme.html')