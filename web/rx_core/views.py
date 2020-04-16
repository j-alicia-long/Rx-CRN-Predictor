from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy

from django.utils import timezone

from .models import Patient
# from .forms import PatientIntakeForm

def index(request):
	return render(request, 'rx_core/index.html')

def patient_portal(request):
	return render(request, 'rx_core/patient_portal.html')

# class PatientIntakeView(FormView):
#     template_name = 'rx_core/patient_portal.html'
#     form_class = PatientIntakeForm
#     success_url = 'patients/thanks/'

class PatientIntake(CreateView):
	model = Patient
	fields = '__all__'
	success_url = reverse_lazy('rx_core:patient_confirmation')

def patient_confirmation(request):
	return render(request, 'rx_core/patient_confirmation.html')


# @login_required
def dashboard(request):
	return render(request, 'rx_core/dashboard.html')

# @login_required
class WaitingRoomView(ListView):
    template_name = 'rx_core/waiting_room.html'
    context_object_name = 'patient_list'

    def get_queryset(self):
        return Patient.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PatientDetailView(DetailView):
    model = Patient
