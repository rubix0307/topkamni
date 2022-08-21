from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Category, Post
# Create your views here.

def index(request):

    context = {
        'title': 'TopKamni.ru: сайт о драгоценных камнях',
    }
    return render(request, 'main/index.html', context)



class NewsFromCategory(ListView):
    model = Post
    template_name = 'main/posts_from_category.html'
    context_object_name = 'posts'
    paginate_by = 5



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs['slug']
        name_of_category = Category.objects.get(slug=slug)
        context['title'] = f'Записи категории "{name_of_category}"'
        
        updated_posts = []
        for post in context['posts']:
            post.content = post.content.replace('<h2>','<h4>').replace('</h2>','</h4>')
            updated_posts.append(post)
        context['posts'] = updated_posts


        return context