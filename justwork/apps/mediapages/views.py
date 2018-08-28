from rest_framework import (generics, mixins, status)
from rest_framework.response import Response
from .models import (Page)
from .serializers import (PageSerializer, )
from rest_framework.pagination import PageNumberPagination
from justwork.apps.mediapages.tasks import upd_counter

def upd_count(pk):
    upd_counter.delay(pk)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
    def get_paginated_response(self, data):
        return Response({'count': self.page.paginator.count,
                         'next': self.get_next_link(),
                         'previous': self.get_previous_link(),
                         'pages': data})

class PageListView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        courses = Page.objects.order_by('order_number').all()
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(courses, request)
        serializer = PageSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

class PageView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """
    Retreive Page by ID
    """
    queryset = Page.objects.all()
    lookup_url_kwarg = 'pk'
    serializer_class = PageSerializer

    def get(self, request, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        upd_count(kwargs['pk'])

        return response
