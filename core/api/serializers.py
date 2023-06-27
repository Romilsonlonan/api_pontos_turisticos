from rest_framework.serializers import ModelSerializer 
from core.models import PontoTuristico

# serializer será responsável por serializar objetos da classe PontoTuristico e incluirá apenas os campos 
# 'id', 'nome' e 'descricao' na serialização. Isso significa que, ao serializar um objeto PontoTuristico, apenas esses campos serão incluídos na resposta HTTP.

# definindo classe chamada PontoTuristicoSerializer que herda da classe ModelSerializer
class PontoTuristicoSerializer(ModelSerializer):
    # Dentro da classe PontoTuristicoSerializer, há uma classe interna chamada Meta que 
    # define metadados para o serializer.
    class Meta:

        # O atributo model dentro da classe Meta especifica o modelo associado ao serializer, ou seja, 
        # a classe PontoTuristico é o modelo que será serializado por esse serializer
        model = PontoTuristico

        # O atributo fields dentro da classe Meta especifica os campos do modelo que serão incluídos na 
        # serialização. Nesse caso, apenas os campos 'id', 'nome' e 'descricao' serão incluídos.
        fields = ('id', 'nome', 'descricao')