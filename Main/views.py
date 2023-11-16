from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.urls import reverse
from . models import *
from . forms import *
from multi_form_view import MultiModelFormView
from django.core.mail import send_mail
from django.conf import settings


def home_page(request):
    return render(request, 'index.html')


class dronepermit(MultiModelFormView):
    form_classes = {
        'owner_form': OwnerForm,
        'drone_form': DroneForm,
        'area_form': AreaForm,
        'dronepermit_form': DronePermitForm,
    }
    template_name = 'registrationform.html'
    def get_success_url(self):
        return reverse("Main:home")
    def forms_valid(self, forms):
        owner = forms['owner_form'].save(commit=False)
        drone = forms['drone_form'].save(commit=False)
        area = forms['area_form'].save(commit=False)
        drone_permit = forms['dronepermit_form'].save(commit=False)
        return super(dronepermit,self).forms_valid(forms)

def userprofile(request, owner_id):
    owner = get_object_or_404(Owner, pk = owner_id)
    drones = owner.drones.all()

    context = {
        'owner': owner,
        'drones': drones,
    }
    return render(request, 'profile.html', context)

def permits(request):
    if request.user.is_officer:
        permit_list = DronePermit.objects.exclude(status='approved')
        return render(request, 'permits.html', {'permit_list': permit_list})

def update_status(request):
    if request.method == 'POST':
        permit_id = request.POST.get('permit_id')
        new_status = request.POST.get('status')
        try:
            permit = DronePermit.objects.get(id=permit_id)
            if new_status == 'approved':
                permit.status = 'approved'
                permit.save()

                owner = permit.owner
                drone = permit.drone
                subject = 'Drone Permit Approved'
                message = f"Dear {owner.fname} {owner.lname},\n\nYour drone permit for {drone.manufacturer} {drone.modelno} has been approved. You can proceed with your planned flight.\n\nThank you."
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = [owner.email]
                send_mail(subject, message, from_email, to_email)
            else:
                permit.status = new_status
                permit.save()
        except DronePermit.DoesNotExist:
            pass
    return redirect('Main:permits')