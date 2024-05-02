from django.urls import path
from download.views import show_main, show_xml, show_xml_by_id, show_json, show_json_by_id
from download.views import add_downloaded_show, delete_downloaded_show

app_name = 'download'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'), 
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('add/<int:id>', add_downloaded_show, name='add_downloaded_show'),
    path('delete/<int:id>', delete_downloaded_show, name='delete_downloaded_show'),
]