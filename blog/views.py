from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate, logout
from django.template.context_processors import csrf
from .forms import PostForm
from django.utils import timezone



def home(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article.html', {'article':article})


def search_product(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
    else:
        search_query = ''

    # Look in Porduct title, short and full descriptions, Category title and parent Category title
    products = Article.objects.filter(Q(title__icontains=search_query))
    content = {}
    content['products'] = products

    return render(request, 'blog/search_result.html', content)


def search_r(request):
    if request.method == 'POST':
        search_query = request.POST['search']
    else:
        search_query = request.GET['search']

    contact_list = Article.objects.filter(Q(title__icontains=search_query))
    paginator = Paginator(contact_list, 3)

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'blog/search_r.html', {'products': contacts,
                                                  'search_query' : search_query
                                                  })

def login_view(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'blog/login.html', args)
    else:
        return render(request, 'blog/login.html', args)

def logout_view(request):
    logout(request)
    return redirect('/')

def new_article(request):
    form = PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/new_article.html', {'form':form})
