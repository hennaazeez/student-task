import django_filters
from django.forms import TextInput
from django_filters import CharFilter


from st_app.models import studentregister


class NameFilter(django_filters.FilterSet):
    username = CharFilter(field_name='name',label='',lookup_expr="icontains",widget=TextInput(attrs={'placeholder':'Search by Name'}))
    class Meta:
        model = studentregister
        fields = ('username',)