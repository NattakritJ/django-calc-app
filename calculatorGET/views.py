from django.shortcuts import render
from .forms import CalcForm
from .models import CalcGET
# Create your views here.
def main(request):
    checksubmit = False
    if request.GET.get('clearall'):
        CalcGET.objects.all().delete()
    allobject = CalcGET.objects.all()
    objectsize = CalcGET.objects.count()
    result = "0.0"
    if objectsize > 10:
        CalcGET.objects.all()[:1].get().delete()
    if request.method == "GET":
        form = CalcForm(request.GET)
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
    return render(request, 'mainget.html', {'form': form,
                                            'allobject': allobject,
                                            'result':result,
                                            'checksubmit':checksubmit})