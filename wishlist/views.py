from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.views.generic import ListView
from django.apps import apps
from wishlist.models import UserActivity


class WishListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist.html'

    def get_queryset(self):
        return self.request.user.likes.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['content_type'] = UserActivity.objects.order_by('-pk')

        return context


@login_required
def add_wishlist(request, pk, klass):
    app, klass = klass.split('.')[0], klass.split('.')[-1]
    model = apps.get_model(app_label=app, model_name=klass)
    ct = ContentType.objects.get_for_model(model)
    user = request.user

    if UserActivity.objects.filter(liked_by=user, object_id=pk, content_type=ct).exists():
        UserActivity.objects.filter(liked_by=user, object_id=pk, content_type=ct).delete()
    else:
        UserActivity.objects.create(liked_by=user, object_id=pk, content_type=ct)

    return redirect(request.GET.get('next', '/'))

