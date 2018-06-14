from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from home.forms import HomeForm
from home.models import Post

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        args = {'form': form, 'posts': posts}

        data = {}
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