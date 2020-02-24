from django.shortcuts import render
from .forms import CalcForm
from .models import calc
# Create your views here.
def main(request):
    x = None
    y = None
    showresult = ""
    if request.method == "POST":
        form = CalcForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data.get('x')
            y = form.cleaned_data.get('y')
            operations = form.cleaned_data.get('operations')
            getobject = calc.objects.get(x=x, y=y,operations=operations)
            if getobject.operations == '+':
                showresult = getobject.result = x+y
            if getobject.operations == '-':
                showresult = getobject.result = x-y
            if getobject.operations == '*':
                showresult = getobject.result = x*y
            if getobject.operations == '/':
                showresult = getobject.result = x/y

    else:
        form = CalcForm()
    return render(request, 'main.html', {'form': form,'showresult':showresult})