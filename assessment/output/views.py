from django.shortcuts import render, get_object_or_404
from .models import Data, MetadataCountries

# Create your views here.
def data_list(request):
    data = Data.objects.all()
    return render(request, 'output/data_list.html', {'data' : data})

def data_detail(request, tableName):
    metadata = MetadataCountries.objects.filter(tableName=tableName)
    return render(request, 'output/data_detail.html', {'metadata' : metadata})
