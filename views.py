from numpy import iinfo
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view 
from datetime import date, datetime

# Create your views here.

@api_view(['GET'])
def personDetail(request, id):
    person = Person.objects.get(iin=id)
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def personCreate(request):
    serializer = PersonSerializer(data=request.data)
    
    if serializer.is_valid():
      def iin_converter(iin):
         def calculate_age(born):
             today = date.today()
             return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        
         if iin[6]=='3' or iin[6]=='4':
            born = f"19{iin[0:2]}-{iin[2:4]}-{iin[4:6]}"
            return calculate_age(born)
         born = f"20{iin[0:2]}-{iin[2:4]}-{iin[4:6]}"
         return calculate_age(born)
      
      iin = serializer.cleaned_data["iin"]
      age = iin_converter(iin)
      serializer = PersonSerializer(iin=iin,age=age)
      serializer.save()
    return Response(serializer.data)
