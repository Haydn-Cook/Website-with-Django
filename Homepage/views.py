from django.shortcuts import render

# Create your views here.

def Homepage(request):
    """
    Render the homepage.

    This view renders the 'Homepage/Homepage.html' template, which represents the
    homepage of the website.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML page for the homepage.
    :rtype: HttpResponse
    """
    return render(request, 'Homepage/Homepage.html')

