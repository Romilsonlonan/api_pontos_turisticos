from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico   
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    #atribuindo a variável queryset todos os objetos da classe PontoTuristico presentes no banco de dados.
    #queryset = PontoTuristico.objects.all() # substituindo pelo método get_queryset
    
    #Um serializer é uma classe no Django Rest Framework que define como os objetos devem ser convertidos 
    # em tipos de dados Python nativos, como dicionários, listas ou JSON, e vice-versa. 
    serializer_class = PontoTuristicoSerializer 

    #A finalidade principal do método get_queryset() é fornecer uma maneira de filtrar e ordenar os objetos 
    # que serão retornados em uma resposta da API. Ele define a lógica para recuperar os objetos que serão 
    # exibidos em uma determinada view.
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
    
    #  Implementação do método list em uma classe de visualização (view) do Django. o método list recebe três 
    # parâmetros: self, request, *args e **kwargs.
    # Dentro do método list, o código retorna uma resposta HTTP contendo um dicionário serializado como JSON. 
    def list(self, request, *args, **kwargs):
        return Response({'teste':123})

