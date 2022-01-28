import imp
from rest_framework import serializers

from digital_buddy.onepoint.models import NewJoinerDetails

class NewJoinerSerializer(serializers.Serializer):
    class Meta:
        model = NewJoinerDetails
        fields = [
            'PSID', 'first_name', 'last_name', 'email', 'city', 'country', 'other_phone', 'grade', 'dept_id', 'email_address', 'date_of_joining', 'work_location'
        ]
