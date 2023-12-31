from rest_framework.decorators import action 
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
    
    # Em resumo, o método create em um ViewSet no Django tem a finalidade de receber os dados enviados pelo 
    # cliente em uma solicitação POST e criar um novo objeto com base nesses dados no modelo associado à API. 
    # Ele é responsável por validar e persistir os dados enviados pelo cliente no banco de dados.
    def create(self, request, *args, **kwargs):
        return Response({'Hello':request.data['nome']})
    
    # O método destroy em um ViewSet no Django tem a finalidade de lidar com a solicitação DELETE para excluir 
    # um objeto existente. A ação destroy é responsável por excluir um objeto específico do modelo associado ao 
    # ViewSet A finalidade do método destroy é encontrar e excluir um objeto existente no banco de dados com 
    # base em um identificador único (geralmente o ID do objeto). Quando uma solicitação DELETE é feita para a 
    # URL correspondente a esse ViewSet, o método destroy será chamado internamente.
    def destroy(self, request, *args, **kwargs):
        pass
    
    # A finalidade do método retrieve é buscar um objeto específico no banco de dados com base em um identificador 
    # único (geralmente o ID do objeto). Quando uma solicitação GET é feita para a URL correspondente a esse 
    # ViewSet, o método retrieve será chamado internamente.    
    def retrieve(self, request, *args, **kwargs):
        pass

    # O método update em um ViewSet no Django tem a finalidade de lidar com a solicitação PUT ou PATCH para atualizar 
    # um objeto existente com base nos dados fornecidos pelo cliente.    
    def update(self, request, *args, **kwargs):
        pass       

    # Action personalizada para teste    
    @action(methods=['post', 'get'], detail=True)    
    def denunciar(self, request, pk=None):
        pass    

    # Action personalizada para teste     
    @action(methods=['get'], detail=False)    
    def teste(self, request):
        pass   