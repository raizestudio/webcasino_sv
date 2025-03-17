from django.contrib import admin

from financial.models import Currency, Exchange, FinancialApiProvider, Ticker

admin.site.register(Currency)
admin.site.register(Exchange)
admin.site.register(Ticker)
admin.site.register(FinancialApiProvider)
