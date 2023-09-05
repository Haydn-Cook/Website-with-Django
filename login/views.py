from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def login_create(request):
    """
    Render the login or create account page.

    This view renders the 'login/login_or_create.html' template, which provides
    users with the option to log in or create a new account.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML page for the login or create account page.
    :rtype: HttpResponse
    """
    return render(request, 'login/login_or_create.html')


def login(request):
    """
    Render the login page.

    This view renders the 'login/login.html' template, which provides the user
    with a login form to enter their credentials and authenticate.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML page for the login form.
    :rtype: HttpResponse
    """
    return render(request, 'login/login.html')


def create_user(request):
    """
    Create a new user account.

    This view handles the creation of a new user account based on user input.
    When the HTTP request method is POST, it extracts the provided username
    and password from the request's POST data. It checks for empty fields and
    whether the username already exists in the database. If the username is
    unique and not empty, a new user account is created using
    `User.objects.create_user`. Success and error messages are displayed to
    the user, and upon successful user creation, the user is redirected to
    the homepage.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML page or a redirection to the homepage.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Please provide a username and password')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username already exists. Please use another.')
            else:
                user = User.objects.create_user(username=username, password=password)
                messages.success(request, 'User account created successfully')
                return redirect('homepage:Homepage')  # Redirect to the login page after successful user creation

    return render(request, 'login/login.html')



