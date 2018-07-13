from rest_framework import serializers, viewsets, generics, permissions
from .models import Food, Report
from django.contrib.auth.models import User


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ('brand', 'item', 'description')

class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('delayed_reaction', 'buildup_reaction', 'immediate_reaction', 'details', 'company_response')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        owner = self.context['request'].user
        report = Report.objects.create(owner=owner, **validated_data)
        return report

class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.none()

    def get_queryset(self):
        owner = self.request.user

        if owner.is_anonymous:
            return Report.objects.none()

        else:
            return Report.objects.filter(owner=owner)
