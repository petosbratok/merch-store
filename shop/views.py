from django.shortcuts import render
from django.views.generic import ListView
from .models import Good, Type

class Home(ListView):
    model = Good
    template_name = 'shop/home.html'
    context_object_name = 'goods'
    ordering = ['-date_added']
    # paginate_by = 8

    # def get_context_data(self, **kwargs):
        # context = super(PostListView, self).get_context_data(**kwargs)
        # posts = Post.objects.all()
        # liked_ids = []
        # for post in posts:
        #     if post.likes.filter(id=self.request.user.id).exists():
        #         liked_ids.append(post.id)
        # context['liked_ids'] = liked_ids
        # return context
