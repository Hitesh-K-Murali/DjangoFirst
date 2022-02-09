from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def shopHome ( request ):
    silkCollection = [
        "Banaras",
        "Pochampalle",
        "Uppada",
        "Venkatagiri",
        "Kaanchipuram",
        "Dharmavaram",
    ]
    return render ( request, "shopsilk/shopHome.html", { 'silkCollections' : silkCollection } )