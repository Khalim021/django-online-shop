from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView

from contact.forms import ContactModelForm
from contact.models import FaqModel


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('contact:contact')


class FaqView(ListView):
    template_name = 'faq.html'

    def get_queryset(self):
        qs = FaqModel.objects.all()

        return qs
