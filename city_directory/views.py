import json
from django.views import View
from django.http.response import JsonResponse

from .models import Catalog

class CatalogsView(View):
    
    def get(self, request):

        all_catalogs = Catalog.objects.all()
        catalogs = []
        for catalog in all_catalogs:
            catalogs.append(
               {
                   "name": bytes(catalog.name, "utf-8").decode("unicode_escape"),
                   "address": catalog.address,
                   "city": catalog.city,
               } 
            )
        data = {"catalogs":catalogs}
        return JsonResponse(data=data)
    
    def single(self, catalog_id):
        catalog = Catalog.objects.get(pk = catalog_id)
        if catalog:
            catalog = {
                    "name": bytes(catalog.name, "utf-8").decode("unicode_escape"),
                    "address": catalog.address,
                    "city": catalog.city,
                }
            return JsonResponse(data=catalog)
        else:
            return JsonResponse(data={"error":"catalog not found"})
    
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        city = data.get('city')
        address = data.get('address')
        
        new_catalog = Catalog.objects.create(
            name = name,
            description = description,
            city = city,
            address = address,            
        )
        return JsonResponse(data={"status":"Success", "id": new_catalog.id})