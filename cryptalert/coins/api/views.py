from .serializers import CoinSerializer
from coins.models import Coin


from rest_framework import generics


class CoinList(generics.ListAPIView):
	permission_classes 		= []
	authentication_classes 	= []
	serializer_class 		= CoinSerializer
	queryset 				= Coin.objects.all()

class CoinDetail(generics.RetrieveAPIView):
	permission_classes 		= []
	authentication_classes 	= []
	serializer_class 		= CoinSerializer
	queryset				= Coin.objects.all()
	lookup_field 			= 'coin_id'

	def get_object(self, *args, **kwargs):
		coin_id = self.request.GET.get('coin_id', None)
		return Coin.objects.get(coin_id=coin_id)

