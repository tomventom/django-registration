from .forms import UserAdminCreationForm
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "accounts/home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

class AboutView(TemplateView):
    template_name = "accounts/about.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        return context

class BlogView(TemplateView):
    template_name = "accounts/blog.html"
    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        return context

class RegisterView(CreateView):
    template_name = "accounts/reg_form.html"
    form_class = UserAdminCreationForm
    success_url = '/account/login/'
