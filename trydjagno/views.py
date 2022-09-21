from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
import random


def home_view(request):
    """ 
        Home / index view 
    """
    random_id = random.randint(1, 3)

    article_obj = Article.objects.get(id=random_id)

    context = {
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id
    }

    Content_String = render_to_string('home-view.html', context=context)

    # Content_String = """ 
    # <h1> {title}  ({id})!</h1> 
    # <p> {content} </p>
    # """.format(**context)

    return HttpResponse(Content_String)

