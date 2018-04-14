# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse


from django.views.generic import TemplateView

class AnasayfaSayfaGorunumu(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'anasayfa.html',context=None)

class BelgelerSayfaGorunumu(TemplateView):
    template_name="belgeler.html"

class Detayyenibilgim1SayfaGorunumu(TemplateView):
    template_name="detayyenibilgim1.html"

class Detayyenibilgim2SayfaGorunumu(TemplateView):
    template_name="detayyenibilgim2.html"

class GuzelsozlerSayfaGorunumu(TemplateView):
    template_name="guzelsozler.html"

class KisabilgilerSayfaGorunumu(TemplateView):
    template_name="kisabilgiler.html"

class MakalelerSayfaGorunumu(TemplateView):
    template_name="makaleler.html"

class ResimlerSayfaGorunumu(TemplateView):
    template_name="resimler.html"
