from django.shortcuts import render
from django.views import generic
from blog.models import Article, categories

# Create your views here.


class Home(generic.ListView):
    model = Article
    paginate_by = 30
    template_name = 'index/home.html'

    def get_context_data(self, **kwargs):
        context = {
            'must_read': Article.objects.filter(must_read=True)[:5],
            'articles': Article.objects.all(),
            'categories': get_category
        }

        return context


def get_category():  # return a list of blog categories
    raw = []
    readable = []

    for i in categories:
        raw.append(i[0])  # gets the first item of the list of tuples
        readable.append(i[1])  # gets the second item of the list of tuples

    output = zip(raw, readable)

    return output
