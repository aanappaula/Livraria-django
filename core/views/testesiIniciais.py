from django.http import HttpResponse, JsonResponse

def teste (request):
    return HttpResponse("Olá mundo de Django.")

def teste2 (request):
     data = {
        "data": {
            "1": "Carrinho",
            "2": "Realizado",
            "3": "Finalizado"
        }
    }
    return JsonResponse(data)