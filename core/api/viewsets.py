from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico   
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    #atribuindo a variável queryset todos os objetos da classe PontoTuristico presentes no banco de dados.
    queryset = PontoTuristico.objects.all()
    
    #Um serializer é uma classe no Django Rest Framework que define como os objetos devem ser convertidos 
    # em tipos de dados Python nativos, como dicionários, listas ou JSON, e vice-versa. 
    serializer_class = PontoTuristicoSerializer 

