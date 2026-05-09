from django.urls import path
from .views import home_view, robots_txt, bond_faqpage, llms_txt,derivativesfaq,mutualfundfaq,criteriasfaq,providersfaq,tradingfaq,logo

urlpatterns = [
    path('', home_view, name='home'),
    path("robots.txt", robots_txt, name='robots_txt'),
    path("llms.txt", llms_txt, name='llms_txt'),
    path("bondfaq", bond_faqpage, name='bond_faqpage'),
    path("derivativesfaq", derivativesfaq, name='derivativesfaq'),
    path("mutualfundfaq", mutualfundfaq, name='mutualfundfaq'),
    path ("criteriasfaq", criteriasfaq, name='criteriasfaq'),
    path ("providersfaq", providersfaq, name='providersfaq'),
    path ("tradingfaq", tradingfaq, name='tradingfaq'),
    path("logo.webp", logo, name='logo'),
]
