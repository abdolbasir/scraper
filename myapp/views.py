import requests
from bs4 import BeautifulSoup
from myapp.models import Link
from django.shortcuts import render

# Create your views here.
def scrape_data(request):
    if request.method == "POST":
        url = request.POST.get("site")
    else:
        url = ""
        
    Link.objects.all().delete()

    if url:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            for link in soup.find_all('a'):
                link_address = link.get('href')
                link_name = link.string
                Link.objects.create(name=link_name, address=link_address)
            data = Link.objects.all()
        except requests.RequestException:
            pass  # Optionally, handle/log the error


        return render(request, "myapp/result.html", {"data": data})
    else:
        return render(request, "myapp/result.html", {"data": []})

