from django.shortcuts import render, HttpResponse, redirect
from django.conf.urls import url
import random

#not in session
def index(request):
    if 'totalgold' not in request.session or 'activities' not in request.session:
        request.session['totalgold'] = 0
        request.session['activities'] = []
    return render(request, 'ninja_gold/index.html')

def process_money(request):
    if request.method == 'POST':
        print request.method
        print "*" * 50

        if request.POST['building'] == 'farm':
            newgold = random.randint(10,10)
        #print newgold

        elif request.POST['building'] == 'cave':
            newgold = random.randint(5,10)
        elif request.POST['building'] == 'house':
            newgold = random.randint(2, 5)
        elif request.POST['building'] == 'casino':
            newgold = random.randint(0, 25)

        request.session[ 'totalgold' ] += newgold
        request.session['activities'].append("You've earned " + str(newgold))
        return redirect('/')
