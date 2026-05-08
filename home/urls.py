from django.urls import path
from .views import home_view, robots_txt, bond_faqpage, llms_txt,derivativesfaq

urlpatterns = [
    path('', home_view, name='home'),
    path("robots.txt", robots_txt, name='robots_txt'),
    path("bondfaq", bond_faqpage, name='bond_faqpage'),
    path("derivativesfaq", derivativesfaq, name='derivativesfaq'),
    path("llms.txt", llms_txt, name='llms_txt')
]
