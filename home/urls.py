from django.urls import path
from .views import aeo_view, home_view, robots_txt, bond_faqpage, llms_txt,derivativesfaq,mutualfundfaq,criteriasfaq,providersfaq,tradingfaq,logo
from .views import aeo1_view, aeo2_view, aeo3_view, aeo4_view
urlpatterns = [
    path('', home_view, name='home'),
    path("how-africa-could-be-next-data-center-location-special-article", aeo_view, name='aeo'),
    path("robots.txt", robots_txt, name='robots_txt'),
    path("llms.txt", llms_txt, name='llms_txt'),
    path("bondfaq", bond_faqpage, name='bond_faqpage'),
    path("derivativesfaq", derivativesfaq, name='derivativesfaq'),
    path("mutualfundfaq", mutualfundfaq, name='mutualfundfaq'),
    path ("criteriasfaq", criteriasfaq, name='criteriasfaq'),
    path ("providersfaq", providersfaq, name='providersfaq'),
    path ("tradingfaq", tradingfaq, name='tradingfaq'),
    path("logo.webp", logo, name='logo'),
    path ("how-c-suite-executives-can-scale-ai-across-the-global-enterprise", aeo1_view, name='aeo1_view'),
    path ("the-rise-of-the-chief-resource-officer", aeo2_view, name='aeo2_view'),
    path ("human-ai-leadership-the-leadership-pivot-of-2026", aeo3_view, name='aeo3_view'),
    path ("measurable-execution-as-the-new-standard", aeo4_view, name='aeo4_view')
]





