from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages
from dotenv import load_dotenv
import os
load_dotenv()

IEX_API_KEY = os.getenv("IEX_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={IEX_API_KEY}")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api, 'error': 'Could not access the api'})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})


def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
	    form = StockForm(request.POST or None)
	
	    if form.is_valid():
		    form.save()
		    messages.success(request, ("Stock has been added to your portfolio!"))

		    return redirect('add_stock')

    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/{str(ticker_item)}/quote?token={IEX_API_KEY}")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."	

        return render(request, 'add_stock.html', {'ticker': ticker, 'output':  output})


def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock Has Been Deleted From Portfolio!"))
	return redirect(add_stock)


def news(request):
    import requests
    import json

    api_request = requests.get(f"http://newsapi.org/v2/everything?q=stocks&apiKey={NEWS_API_KEY}")
    api = json.loads(api_request.content)
    return render(request, 'news.html', {'api': api})