from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy

from django.utils import timezone

from .models import Patient
from .forms import PatientIntakeForm

def index(request):
    return render(request, 'rx_core/index.html')

def patient_portal(request):
    return render(request, 'rx_core/patient_portal.html')

class PatientIntake(CreateView):
    template_name = 'rx_core/patient_form.html'
    form_class = PatientIntakeForm
    success_url = reverse_lazy('rx_core:patient_confirmation')

    def get_initial(self, *args, **kwargs):
        initial = super(PatientIntake, self).get_initial(**kwargs)
        # initial['name'] = 'My Goal'
        return initial


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
        return Patient.objects.filter(checked=False)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

class CompletedRoomView(ListView):
    template_name = 'rx_core/completed_room.html'
    context_object_name = 'patient_list'

    def get_queryset(self):
        return Patient.objects.filter(checked=True)

class PatientDetailView(DetailView):
    model = Patient
