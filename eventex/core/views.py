from django.views.generic import ListView, DetailView
from eventex.core.models import Speaker, Talk


# Main page
home = ListView.as_view(template_name='index.html', model=Speaker)
# Speakers info
speaker_detail = DetailView.as_view(model=Speaker)
# Talk info
talk_list = ListView.as_view(model=Talk)
