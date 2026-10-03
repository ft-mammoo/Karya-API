from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # User can specify the page size using this query parameter
    max_page_size = 50