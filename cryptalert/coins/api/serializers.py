from rest_framework import serializers
from ..models import Coin

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Coin
    	fields = ['id', 'coin_id', 'name', 'symbol']
    
    # TODO: Add a validation function
    '''
    def validate(self, data):
    	content = data.get('content', None)
    	if content == '':
    		content = None
    	image = data.get('image', None)
    	if content is None and image is None:
    		raise serializers.ValidationError("Content or image is required")
    	return data

    def validate_content(self, value):
    	if len(value) > 1000:
    		raise serializers.ValidationError("Content is too long")
    	return value 
    '''