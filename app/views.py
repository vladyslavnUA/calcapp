import arithmaticpy
from arithmaticpy import vlad
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    context = {}
    # if request.method == 'POST':
    tocalc = request.POST.get('whatis')
    allans = []

    if ('+' in str(tocalc)):
        ans = int(tocalc.split('+')[0]) + int(tocalc.split('+')[1])
        final = str(tocalc), " = ", str(ans)
        context['ans'] = ans
        context['final'] = final
        context['tocalc'] = tocalc
    elif ('-' in str(tocalc)):
        ans = int(tocalc.split('-')[0]) - int(tocalc.split('-')[1])
        context['ans'] = ans
        context['tocalc'] = tocalc
    elif ('*' in str(tocalc)):
        ans = int(tocalc.split('*')[0]) * int(tocalc.split('*')[1])
        context['ans'] = ans
        context['tocalc'] = tocalc
    elif ('/' in str(tocalc)):
        ans = int(tocalc.split('/')[0]) / int(tocalc.split('/')[1])
        context['ans'] = ans
        context['tocalc'] = tocalc

    return render(request, 'app/index.html', context)