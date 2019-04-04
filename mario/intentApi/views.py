from mario.intentApi.serializers import IntentAnswerSerializer, IntentCategorySerializer, IntentSerializer, TrainingDataSerializer
from rest_framework import viewsets
from .models import Intent, IntentAnswer, IntentCategory, TrainingData
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
class IntentCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = IntentCategory.objects.all()
    serializer_class = IntentCategorySerializer


class IntentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Intent.objects.all()
    serializer_class = IntentSerializer


class IntentAnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = IntentAnswer.objects.all()
    serializer_class = IntentAnswerSerializer


class TrainingDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TrainingData.objects.all()
    serializer_class = TrainingDataSerializer


@api_view(['POST'])
def create_intentCategory(request):
    if request.method == 'POST':
        try:
            serializer = IntentCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(ex, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_allIntentCategory(request):
    return Response(IntentCategory.objects.all().values(), status=status.HTTP_200_OK)


"""
@api_view(['GET'])
def get_IntentCategory_ByName(request):
    return Response(IntentCategory.objects.get(IntentCategory.intentCategoryName).values(), status=status.HTTP_200_OK)

"""