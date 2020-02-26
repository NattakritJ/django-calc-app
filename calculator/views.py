from django.shortcuts import render
from .forms import CalcForm
from .models import calc
# Create your views here.
def main(request):
    resultallobject = []
    xallobject = []
    yallobject = []
    op_allobject = []
    allobject = calc._meta.model.objects.all()
    for result in allobject:
        xallobject.append(result.x)
        yallobject.append(result.y)
        op_allobject.append(result.operations)
        resultallobject.append(result.result)
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
            form.save()
            resultallobject = []
            xallobject = []
            yallobject = []
            op_allobject = []
            allobject = calc._meta.model.objects.all()
            for result in allobject:
                xallobject.append(result.x)
                yallobject.append(result.y)
                op_allobject.append(result.operations)
                resultallobject.append(result.result)
    else:
        form = CalcForm()
    return render(request, 'main.html', {'form': form,
                                         'allobject': allobject,
                                         'xallobject': xallobject,
                                         'yallobject': yallobject,
                                         'op_allobject': op_allobject,
                                         'x': '1',
                                         'resultallobject': resultallobject})