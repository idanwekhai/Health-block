from rest_framework import serializers

from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
	class Meta:

		fields = (
                'address',
                'bloodPressure',
                'temperature',
                'weight',
                'height'
			)
		model = Patient