'''
def my_middleware(get_response):
    print("One time initialization")
    def middleware(request):
        print("Before view")
        response = get_response(request)
        print("After view")
        return response
    return middleware
'''
from django.http import HttpResponse


class my_middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time initialization")
    
    def __call__(self, request):
        #print("Before view")
        response = self.get_response(request)
        #print("After view")
        return response
    def process_view(request,*args, **kwargs):
        print("process view")
        return None
    #to handle exceptions
    def process_exception(self,request,exception):
        print(exception)
        msg=exception
        print("process exception")
        return HttpResponse(msg)

