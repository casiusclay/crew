from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from home.forms import HomeForm, ApplyForm
from home.models import Post, Apply
from django.contrib.auth.models import User



def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, pk=0):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        args = {'form': form, 'posts': posts}

        data = {}
        if pk is not 0:
            data['success'] = True
        else:
            data['success'] = False
        filter_data = {}
        search_by = request.GET.get('search_by')
        keywords = request.GET.get('keywords')
        location = request.GET.get('location')
        # Array of Allowed field in filter process.
        allowed_filter = ['salary', 'title', 'post', 'location']

        # Build filter conditions.
        if search_by and keywords and search_by in allowed_filter:
            filter_data[search_by + "__icontains"] = keywords

        # Build initial Query.
        posts = Post.objects.filter(**filter_data)

        # Create order query.
        if location:
            filter_data['location' + "__icontains"] = location
            posts = posts.filter(**filter_data)
        posts = posts.order_by('-id')

        # Fetch data with final conditions.
        data['posts'] = posts.all()
        data['current_user'] = request.user
        applied_posts = []
        if User.objects.filter(pk=request.user.id).first() is not None:
            data['logged'] = True
            for post in posts:
               applied_apply = Apply.objects.filter(post__pk=post.pk).filter(applicant__pk=request.user.id).count()
               if applied_apply > 0:
                   print (post.title)
                   applied_posts.append(post.id)


        else:
            data['logged'] = False
        data['applied_posts'] = applied_posts


        return render(request, self.template_name, data)


    #def post(self, request):
        # form = HomeForm(request.POST)
        # if form.is_valid():
        #     post = form.save(commit=False)
        #     post.user = request.user
        #     post.save()
        #     text = form.cleaned_data['post']
        #     form = HomeForm()
        #     return redirect('home:home')
        #
        # args = {'form': form, 'text': text}
        # return render(request, self.template_name, args)

    # def search_listings(self, request):
    #     if request.method == 'GET':
    #         posts = Post.objects.all().order_by('-created')
    #         search_query = request.GET.get('search_box', None)
    #         form = HomeForm()
    #     if form.is_valid():
    #         if form.cleaned_data["text"]:
    #             posts = posts.filter(title__contains=form.cleaned_data["text"])
    #
    #     args = {'form': form, 'posts': posts}
    #     return render(request, self.template_name,
    #                   args)

def listings(request, slug):
    listing = get_object_or_404(Post, slug=slug)

    return render(request, 'accounts/listing.html', {'listings': listing,})


# def search_listings(request):
#     posts = Post.objects.all().order_by('-created')
#     form = SearchForm(request.GET)
#     if form.is_valid():
#         if form.cleaned_data["q"]:
#             countries = countries.filter(name__icontains=form.cleaned_data["q"])
#         elif form.cleaned_data["government_type"]:
#             countries = countries.filter(government=form.cleaned_data["government_type"])
#         elif form.cleaned_data["industry"]:
#             countries = countries.filter(industries=form.cleaned_data["industries"])
#     return render(request, "country/search.html",
#             {"form": form, "country_list": countries})



class ApplyCreateView(CreateView):
    template_name="apply.html"
    form_class = ApplyForm


    def form_valid(self, form):
        form.instance.applicant = self.request.user
        post = Post.objects.filter(pk=self.kwargs['pk']).first()
        form.instance.post = post

        return super(ApplyCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ApplyCreateView, self).get_context_data(**kwargs)
        context['current_user'] = self.request.user

        return context


class PostApplyListView(ListView):
    template_name = 'postapplys.html'
    model = Apply
    context_object_name = 'applys'

    def get_queryset(self):
        qs = super(PostApplyListView, self).get_queryset()
        post = Post.objects.filter(pk=self.kwargs['pk']).first()
        return qs.filter(post__pk=post.id).order_by('-id')


class UserProfileView(DetailView):
    template_name = 'accounts/profile.html'
    model = User
