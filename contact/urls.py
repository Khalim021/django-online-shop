from django.urls import path

from contact.views import ContactCreateView, FaqView

app_name = 'contact'

urlpatterns = [
    path('', ContactCreateView.as_view(), name='contact'),
    path('faqs/', FaqView.as_view(), name='faq')

]









