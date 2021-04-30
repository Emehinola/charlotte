from django.shortcuts import render, redirect
from django.views import generic
from . models import Comment, Article
from . forms import CommentForm
from index.views import get_category

# category dictionary
categories_dict = {
    "accomodation": "Accomodation",
    "advice": "Advice",
    "books":  "Books and Novels",
    "beaty": "Beauty",
    "business": "Business",
    "computerscience": "Computer Science",
    "cooking": "Cooking",
    "comedy": "Comedy",
    "corruption": "Corruption",
    "crime": "Crime",
    "counselling": "Counselling",
    "challenge": "Challenge",
    "crypto": "Crypto",
    "drama": "Drama",
    "economy": "Economy",
    "education": "Education",
    "entertainment": "Entertainment",
    "engineering": "Engineering",
    "employment": "Employment",
    "fitness": "Fitness",
    "fashion": " Fashion and Beauty",
    "food":  "Foods and Nutrition",
    "fuel_subsidy": "Fuel Subsidy",
    "food": "Foods",
    "forsale": "For Sale",
    "graphics": "Grpahics design",
    "gossip":  "Gossip",
    "giveaway": "Giveaway",
    "hair-style": "Hair style",
    "health": "Health",
    "insecurity": "Insecurity",
    "jokes": "Jokes",
    "love": "Love",
    "marriage": "Marriage",
    "maintenance": "Maintenance",
    "movie": "Movie",
    "media": "Media",
    "music": "Music",
    "nutrition": "Nutrition",
    "telecom": "Telecom",
    "medical": "Medical",
    "psychology": "Psychology",
    "politics":  "Politics",
    "protest": "Protest",
    "Quotes": "Quotes",
    "Relationship": "Relationship",
    "religion": "Religion",
    "riddles": "Riddles",
    "sex-education": "Sex Education",
    "sports": "Sports",
    "strike": "Strike",
    "scarcity": "Scarcity",
    "security": "Security",
    "skin-care": "Skin Care",
    "story": "Story",
    "tricks_and_hacks":  "Tricks and Hacks",
    "technology": "Technology",
    "transport": "Transport",
    "violence": "Violence",
    "wealth": "Wealth",
    "others": "Others"
}


# def articles(request):
#     return render(request, 'index/home.html')
class ArticleList(generic.ListView):
    model = Article
    template_name = 'index/home.html'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = {
            'must_read': Article.objects.filter(must_read=True)[:5],
            'articles': Article.objects.all(),
            'categories': get_category
        }

        return context


class ArticleCategory(generic.ListView):
    paginate_by = 30
    template_name = 'blog/category.html'
    context_object_name = 'articles'


def single_blog(request, link_title):
    error = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_id = Article.objects.get(link_title=link_title).id
            instance.save()
            return redirect(f'/articles/{link_title}')
        else:
            error = 'please fill all entries'

    article = Article.objects.get(link_title=link_title)
    title = article.title
    comments = Comment.objects.filter(
        article_id=article.id)  # comments to this post
    related_article = Article.objects.filter(
        category=article.category).exclude(id=article.id)[:4]
    context = {'title': title, 'article': article,
               'error': error, 'comments': comments, 'comments_count': comments.count(), 'categories': get_category, 'related_articles': related_article}
    return render(request, 'blog/single-blog.html', context)


def category(request):
    category = request.GET.get('q')
    articles = Article.objects.filter(category=category)
    must_read = Article.objects.filter(must_read=True)[:10]

    context = {'articles': articles,
               'category': categories_dict[category], 'must_read': must_read, 'count': must_read.count(), 'categories': get_category, 'articles_count': articles.count()}
    return render(request, 'blog/category.html', context)


def create_article(request):
    return render(request, 'blog/create-article.html')
