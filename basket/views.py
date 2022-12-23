from django.shortcuts import render

# Create your views here.
def basket_summery(request):
    return render(request, 'basket/summery.html')