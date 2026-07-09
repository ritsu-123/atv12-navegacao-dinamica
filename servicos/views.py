from django.shortcuts import render

servicos = [
    {
    "id":1,
    "nome_servico":"Desenvolvimento Web",
    "responsavel":"João",
    "tempo_estimado":"40 horas",
    "requisitos":"Levantamento de requisitos."
    },

    {
    "id":2,
    "nome_servico":"Consultoria",
    "responsavel":"Maria",
    "tempo_estimado":"12 horas",
    "requisitos":"Reunião inicial."
    },

    {
    "id":3,
    "nome_servico":"Infraestrutura",
    "responsavel":"Carlos",
    "tempo_estimado":"30 horas",
    "requisitos":"Mapeamento da rede."
    },

    {
    "id":4,
    "nome_servico":"Banco de Dados",
    "responsavel":"Ana",
    "tempo_estimado":"18 horas",
    "requisitos":"Modelagem."
    },

    {
    "id":5,
    "nome_servico":"Suporte",
    "responsavel":"Pedro",
    "tempo_estimado":"8 horas",
    "requisitos":"Chamado registrado."
    }

]

def listagem(request):

    return render(request, 'servicos/listagem.html', {"servicos":servicos})

def detalhe(request,id):

    servico=None

    for s in servicos:

        if s["id"] == id:
            servico = s
            break

    return render(request, 'servicos/detalhe.html', {"servico":servico})