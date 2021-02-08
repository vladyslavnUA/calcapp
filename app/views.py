from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *

@csrf_exempt
def index(request):
    context = {}

    tocalc = request.POST.get('whatis')

    if ('+' in str(tocalc)):
        ans = int(tocalc.split('+')[0]) + int(tocalc.split('+')[1])
        finale = str(tocalc), " = ", str(ans)
        context['ans'] = ans
        tb = Answers.objects.create(final=finale)
        tb.save()
        context['tocalc'] = tocalc
        # context['tb'] = tb

    elif ('-' in str(tocalc)):
        ans = int(tocalc.split('-')[0]) - int(tocalc.split('-')[1])
        finale = str(tocalc), " = ", str(ans)
        tb = Answers.objects.create(final=finale)
        tb.save()
        context['ans'] = ans
        context['tocalc'] = tocalc

    elif ('*' in str(tocalc)):
        ans = int(tocalc.split('*')[0]) * int(tocalc.split('*')[1])
        finale = str(tocalc), " = ", str(ans)
        tb = Answers.objects.create(final=finale)
        tb.save()
        context['ans'] = ans
        context['tocalc'] = tocalc

    elif ('/' in str(tocalc)):
        ans = int(tocalc.split('/')[0]) / int(tocalc.split('/')[1])
        finale = str(tocalc), " = ", str(ans)
        tb = Answers.objects.create(final=finale)
        tb.save()
        context['ans'] = ans
        context['tocalc'] = tocalc

    last = Answers.objects.all().order_by('-final')[:10]
    context['last'] = last
    return render(request, 'app/index.html', context)