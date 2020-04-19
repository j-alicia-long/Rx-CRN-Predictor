from django.urls import path
from . import views

app_name = 'rx_core'

urlpatterns = [
	path('', views.index, name='index'),
	path('welcome/', views.index, name='welcome'),
	path('patients/', views.patient_portal, name='patient_portal'),
	path('patients/new/', views.PatientIntake.as_view(), name='patient_intake'),
	path('patients/thanks/', views.patient_confirmation, name='patient_confirmation'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('waiting-room/', views.WaitingRoomView.as_view(), name='waiting_room'),
	path('waiting-room/patient/<int:pk>', views.PatientDetailView.as_view(), name='patient_detail'),
	path('checked-patients/', views.CompletedRoomView.as_view(), name='checked_patients'),
]
