from django.http import HttpResponse


def home_view(request):
    """ 
        Home / index view 
    """
    Home_String = '<h1> Hello Home </h1>'

    return HttpResponse(Home_String)

