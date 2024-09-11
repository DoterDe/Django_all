

def simple_middleware(get_response):

    def middleware(request):
        request.my_atribut = 'Custom_attr'
        response = get_response(request)

        return response

    return middleware



class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        request.my_atribut_class = 'Custom_attr_class'
        response = self.get_response(request)

        return response


def rubric(request):
    return {'massage':'Hello room!'}