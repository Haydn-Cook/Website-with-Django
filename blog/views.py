from datetime import datetime
from django.shortcuts import render,redirect
from .models import Blog_Post
from django.contrib.auth.models import User

def blog(request):
    """
    Display all blog posts.

    This view retrieves all the blog posts from the database using
    `Blog_Post.objects.all()` and renders them on the 'blog/blog.html' template.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML page displaying all blog posts.
    :rtype: HttpResponse
    """
    blog_posts = Blog_Post.objects.all()
    return render(request, 'blog/blog.html', {'blog_posts': blog_posts})


def add_blog(request):
    """
    Add a new blog post.

    This view handles the creation of new blog posts based on user input. When the
    HTTP request method is POST, it extracts the user ID, blog title, and body
    from the request's POST data. It then attempts to find the user with the given
    ID using `User.objects.get(id=user_id)` and creates a new `Blog_Post` object
    with the provided information. After saving the new blog post, it redirects
    the user to the main blog page.

    If the user with the provided ID does not exist, it does not create a new blog
    post and simply continues rendering the 'blog/add_blog.html' template.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A redirect to the main blog page or a rendered HTML page for adding a blog post.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        user_id = request.POST.get('user')
        title = request.POST.get('blog_title')
        body = request.POST.get('body')
        try:
            user = User.objects.get(id=user_id)

            new_blog = Blog_Post(user=user, blog_title=title, body=body, date=datetime.now())
            new_blog.save()

            return redirect('blog')
        except User.DoesNotExist:
            # Handle the case where the user with the provided ID does not exist
            pass

    return render(request, 'blog/add_blog.html')
