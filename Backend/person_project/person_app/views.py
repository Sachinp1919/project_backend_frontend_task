from rest_framework.views import APIView
from .serializers import PersonSerializer
from .models import Person
from rest_framework.response import Response
import logging
from django.shortcuts import get_object_or_404



logger = logging.getLogger('mylogger')

class PersonAPI(APIView):
    def get(self, request):
        try:
            person = Person.objects.all()
            serializer = PersonSerializer(person, many=True)
            logger.info('Data fetch successfully')
            return Response(data=serializer.data, status=200)
        except:
            logger.error('Data fetching error')
            return Response(data={'details':'there is an error fetching data'}, status=400)
        
    def post(self, request):
        try:
            serializer = PersonSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('Data insert successfully')
            return Response(data=serializer.data, status=201)
        except Exception as e:
            print(e)
            logger.error('Insertion error')
            return Response(data=serializer.errors, status=400)
        
class PersonDetailsAPI(APIView):
    def get(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
            serializer = PersonSerializer(person)
            return Response(data=serializer.data, status=200)
        except:
            return Response(data={'details':'Fetching error on details API'})
        
    def put(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
            serializer = PersonSerializer(data=request.data, instance=person)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('update data')
            return Response(data=serializer.data, status=205)
        except Person.DoesNotExist as e:
            logger.error('No matching data found')
            return Response(data={'details':'Not found Data'}, status=404)
        except:
            logger.error('Error on Updating time')
            return Response(data=serializer.errors, status=400)
        
    def patch(self, request, pk):
        try:
            obj = get_object_or_404(Person, pk=pk)
            serializer = PersonSerializer(data=request.data, instance=obj, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('Field updated')
            return Response(data=serializer.data, status=205)
        except Exception as e:
            print(e)
        #     logger.error('No matching data found')
        #     return Response(data={'details':'Not found data'}, status=404)
        # except:
            logger.error('Error on field updating')
            return Response(data=serializer.errors, status=400)
        

    def delete(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
            person.delete()
            logger.info('Delete Successfully')
            return Response(data=None, status=204)
        except:
            logger.error('delete time error')
            return Response(data={'details':'Not found Data'}, status=400)
    