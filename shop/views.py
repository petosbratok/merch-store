from django.shortcuts import render

# Create your views here.
class Home(ListView):
    model = Goods
    template_name = 'blog/home.html'
    context_object_name = 'good'
    ordering = ['-date_added']
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        # posts = Post.objects.all()
        # liked_ids = []
        # for post in posts:
        #     if post.likes.filter(id=self.request.user.id).exists():
        #         liked_ids.append(post.id)
        # context['liked_ids'] = liked_ids
        return context
