from rest_framework import permissions,  serializers, viewsets, response, mixins, generics
from rest_framework.utils.serializer_helpers import ReturnDict
from django.shortcuts import get_object_or_404
from .models import Efemeride
from datetime import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.cache import cache_page


class EfemeridesError(object):
    VALUE_ERROR = "Date filter has wrong format. Use one of these formats instead: YYYY-MM-DD."


class EfemerideReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Efemeride
        fields = ["hoy", "mes"]


#class EfemerideViewSet(viewsets.ReadOnlyModelViewSet):
class EfemerideViewSet(generics.ListAPIView, viewsets.GenericViewSet):
    """
    query params:
    **day**

    """
    queryset = Efemeride.objects.all()
    serializer_class = EfemerideReadSerializer
    http_method_names = ['get',]

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        day = request.GET.get('day', None)
        if day:
            try:
                day = datetime.strptime(day, "%Y-%m-%d")
            except ValueError:
                return response.Response({"day": [EfemeridesError.VALUE_ERROR]}, 400)
        else:
            day = datetime.now()

        #efemerides = Efemeride.objects.filter(dia__day=day.day, dia__month=day.month, dia__year=day.year)
        efemerides = Efemeride.objects.filter(dia__day=day.day, dia__month=day.month)
        if efemerides.count():
            dia = [i.cita for i in efemerides]
            mes = efemerides.first().mes

        else:
            efemerides = Efemeride(dia=day)
            dia = efemerides.cita
            mes = efemerides.mes

        return response.Response({"dia": dia, "mes": mes})
