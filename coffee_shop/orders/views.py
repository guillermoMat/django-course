from django.views.generic import DetailView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Order
from .forms import OrderProductForm

# Create your views here.

class MyOrderView(DetailView,LoginRequiredMixin):
    model=Order
    template_name="orders/myOrder.html"
    context_object_name = "orders"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_activate=True,user=self.request.user).first()


class CreateOrderProductView(CreateView,LoginRequiredMixin):
    form_class=OrderProductForm
    template_name="orders/create_order_product.html"
    success_url=reverse_lazy("misOrdenes")

    def form_valid(self, form):
        order,_=Order.objects.get_or_create(
            is_activate=True,
            user=self.request.user,
        )
        form_instance_order=order
        form_instance_quantity=1
        form.save()
        return super().form_valid(form)

