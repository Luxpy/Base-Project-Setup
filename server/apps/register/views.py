from rest_framework.generics import ListCreateAPIView

from apps.register.models import ApplicationForm
from apps.register.serializers import ApplicationFormListCreateSerializer


class ApplicationFormListCreateAPIView(ListCreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormListCreateSerializer
