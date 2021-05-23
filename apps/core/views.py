from django.views.generic import TemplateView


class App1View(TemplateView):
    template_name = "core/app1.html"


class App2View(TemplateView):
    template_name = "core/app2.html"

