from django.shortcuts import render

# Create your views here.

produtos = [

    {
        "id":1,
        "nome":"Notebook Dell",
        "categoria":"Informática",
        "preco":5200.00,
        "descricao":"Notebook para desenvolvimento."
    },

    {
        "id":2,
        "nome":"Mouse Gamer",
        "categoria":"Periférico",
        "preco":250.00,
        "descricao":"Mouse RGB."
    },

    {
        "id":3,
        "nome":"Monitor LG",
        "categoria":"Monitor",
        "preco":1400.00,
        "descricao":"Monitor Full HD."
    },

    {
        "id":4,
        "nome":"Teclado Mecânico",
        "categoria":"Periférico",
        "preco":450.00,
        "descricao":"Teclado ABNT2."
    },

    {
        "id":5,
        "nome":"SSD 1TB",
        "categoria":"Armazenamento",
        "preco":600.00,
        "descricao":"SSD NVMe."
    }

]

def listar_tabela(request):

    return render(request, 'produtos/listagem.html', {"produtos": produtos})

def detalhes_elementos(request, id):
    
    produto = None
    
    for p in produto:
        if p["id"]==id:
            produto = p
            break

    return render(request, 'produtos/detalhe.html', {"produto":produto})

