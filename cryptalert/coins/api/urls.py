from django.conf.urls import url
from .views import CoinList, CoinDetail

urlpatterns = [
    url(r'^$', CoinList.as_view()),
    url(r'^(?P<coin_id>\d+)/$', CoinDetail.as_view())
]