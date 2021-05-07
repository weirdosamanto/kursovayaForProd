from django.shortcuts import render
from .models import Articles, ArticleNew
from .forms import ArticlesForm


# Create your views here.
def index(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма не верна'
        pass

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about-us.html')


def News(request):
    news = ArticleNew.objects.order_by('-pub_date')[:5]
    return render(request, 'main/News.html',{'news': news})

