from django.shortcuts import render


# Pagina principal da calculadora de frete
def calculadora_app(request):
    try:
        if request.method == "POST":
            cep_destino = request.POST.get("cep")
            peso_destino = request.POST.get("peso")
            altura_destino = request.POST.get("altura")
            largura_destino = request.POST.get("largura")
            comprimento_destino = request.POST.get("comprimento")
            dados = {
                "cep_destino": cep_destino,
                "peso_destino": peso_destino,
                "altura_destino": altura_destino,
                "largura_destino": largura_destino,
                "comprimento_destino": comprimento_destino,
            }
            return validar_dados(request, dados)
    except Exception as e:
        # Registre a exceção ou trate-a adequadamente
        
        print(f"Error: {e}")
    return render(request, template_name="calculadora_app/home.html")


def validar_dados(request, dados):
    print(dados.get("comprimento_destino"))
    return render(request, template_name="calculadora_app/home.html")
