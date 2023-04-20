from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from libgen_api import LibgenSearch
import requests
# Create your views here.



#http://127.0.0.1:8000/?id=978-0262033848 how to pass


from django.http import HttpResponse, JsonResponse

@api_view()
@permission_classes([AllowAny])

def index(request):
    isbnNo = request.query_params['id']
    #print(type(isbnNo), isbnNo)
    
    


    url = f"https://openlibrary.org/isbn/{isbnNo}.json"

    req = requests.get(url)
    response = req.json()
    books_title = response['title']
    s = LibgenSearch()
    
    results = s.search_title(books_title)
    
    item_to_download = results[0]
    download_links = s.resolve_download_links(item_to_download)
    print("")
    print(results[0]['Title'])
    print("")
    print(list(download_links.values())[1])
    ans = list(download_links.values())[0]

    
    
    return JsonResponse({'isbn1':ans})