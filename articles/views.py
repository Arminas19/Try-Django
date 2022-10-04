from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.http import Http404
# Create your views here.


def article_search_view(request):
    """ Search view """
    # query = query_dict.get("q")
    # try:
    #     query = query_dict.get("q")
    # except:
    #     query = None
    #     print(query)
    # article_obj = None
    query = request.GET.get('q')
    qs = Article.objects.search(query=query)
    context = {
        'object_list': qs,
    }

    return render(request, 'articles/search.html', context=context)


@login_required
def article_create_view(request):
    """ new create article """
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        return redirect("article-detail", slug=article_object.slug)
        # return redirect(article_object.get_absolute_url())
    return render(request, "articles/create.html", context=context)

# def article_create_view(request):
#     """ create article """
#     form = ArticleForm()
#     context = {
#         "form": form
#     }
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")
#             article_object = Article.objects.create(title=title, content=content)
#             context['object'] = article_object
#             context['created'] = True
#     return render(request, "articles/create.html", context=context)


def article_detail_view(request, slug=None):
    """ article detail view """
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": article_obj,
    }
    return render(request, "articles/details.html", context=context)
