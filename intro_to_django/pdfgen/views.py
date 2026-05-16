from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Report
from .tasks import generate_pdf_report

# Create your views here.
class ReportCreateView(CreateView):
    model = Report
    fields = ["title"]
    template_name = "create_report.html"
    success_url = reverse_lazy("report_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        generate_pdf_report.delay(self.object.id)
        return response

class ReportListView(ListView):
    model = Report
    template_name = "pdflist.html"
    context_object_name = "reports"