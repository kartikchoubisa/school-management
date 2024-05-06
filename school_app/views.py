from django.views.generic import TemplateView
from django.utils import timezone
from django.db.models import Sum, Count
from apps.finance.models import Receipt

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = timezone.localdate()
        today_receipts = Receipt.objects.filter(date_paid=today)

        current_month_start = today.replace(day=1)
        next_month_start = (current_month_start + timezone.timedelta(days=32)).replace(day=1)
        current_month_end = next_month_start - timezone.timedelta(days=1)

        today_aggregates = Receipt.objects.filter(date_paid=today).aggregate(
            sum_paid_today=Sum('amount_paid'),
            count_today=Count('id')
        )

        context.update({
            'today_receipts': today_receipts,
            'sum_paid_today': today_aggregates['sum_paid_today'],
            'count_today': today_aggregates['count_today'],
        })

        return context
