from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm, VehicleRegistrationForm
from .models import UserProfile, Vehicle, Product, QualityCheck
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            is_security_department = form.cleaned_data.get('is_security_department', False)
            UserProfile.objects.create(user=user, is_security_department=is_security_department)
            return redirect('vmsapp:login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                try:
                    userprofile = UserProfile.objects.get(user=user)
                    print(userprofile)
                    if userprofile.is_security_department:
                        return redirect('vmsapp:sd_dashboard')  
                    else:
                        return redirect('vmsapp:user_dashboard')
                except UserProfile.DoesNotExist:
                    print("failed")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url=reverse_lazy("vmsapp:login"))
def user_dashboard(request):
    # Logic for regular user dashboard
    return render(request, 'user_dashboard.html')

@login_required(login_url=reverse_lazy("vmsapp:login"))
def security_department_dashboard(request):
    # Logic for security department dashboard
    return render(request, 'security_department_dashboard.html')

@csrf_exempt
@login_required(login_url=reverse_lazy("vmsapp:login"))
def vehicle_registration(request):
    form = VehicleRegistrationForm()
    if request.method == "POST":
        form = VehicleRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            # Retrieve the UserProfile instance associated with the current user
            user_profile = request.user.userprofile
            vehicle.user = user_profile
            vehicle.save()
            return redirect('vmsapp:vehicle_listing')
    return render(request, 'vehicle_registration.html', {'form': form})


@login_required(login_url=reverse_lazy("vmsapp:login"))
def vehicle_listing(request):
    # Retrieve the UserProfile instance associated with the current user
    user_profile = request.user.userprofile
    # Filter vehicles based on the user_profile
    vehicles = Vehicle.objects.filter(user=user_profile)
    return render(request, 'vehicle_listing.html', {'vehicles': vehicles})

#security department vehicle list based PO number
@csrf_exempt
@login_required(login_url=reverse_lazy("vmsapp:login"))
def vehicle_list(request):
    po_numbers = Vehicle.objects.values_list('purchase_order_number', flat=True).distinct()
    
    if request.method == 'POST':
        po_number = request.POST.get('po_number')
        if po_number:
            # Retrieve vehicles associated with the specified P.O. number
            vehicles = Vehicle.objects.filter(purchase_order_number=po_number)
            if vehicles.exists():
                # Redirect to the first vehicle details page for the selected P.O. number
                return redirect('vmsapp:vehicle_details', vehicle_id=vehicles.first().id)
            else:
                # Handle the case where no vehicles are found for the selected P.O. number
                return render(request, 'no_vehicle_found.html')  # Create a template for this
                
    else:
        # If the request method is not POST, render the form initially
        return render(request, 'vehicle_list.html', {'po_numbers': po_numbers})
    
@login_required(login_url=reverse_lazy("vmsapp:login")) 
def vehicle_details(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    return render(request, 'vehicle_details.html', {'vehicle': vehicle})

@csrf_exempt 
@login_required(login_url=reverse_lazy("vmsapp:login"))  
def quality_check(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['Processing', 'Pass', 'Fail']:
            # Check if a QualityCheck instance exists for the vehicle
            quality_check_instance, created = QualityCheck.objects.get_or_create(vehicle=vehicle)
            
            # Update the status of the QualityCheck instance
            quality_check_instance.status = status
            quality_check_instance.save()
            
            return redirect('vmsapp:vehicle_details', vehicle_id=vehicle_id)
    
    return render(request, 'quality_check.html',{'vehicle':vehicle})

@csrf_exempt
@login_required(login_url=reverse_lazy("vmsapp:login"))
def vehicle_checkout(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    vendor = None
    if vehicle.product:
        vendor = vehicle.product.vendor
    
    
    quality_check_status = vehicle.quality_check.status if vehicle.quality_check else None
    
    if request.method == 'POST':
        vehicle.checked_out = True
        vehicle.save()
        
        return redirect('vmsapp:vehicle_details', vehicle_id=vehicle_id)
    
    return render(request, 'vehicle_checkout.html', {'vehicle': vehicle, 'vendor': vendor, 'quality_check_status':quality_check_status})

def user_logout(request):
    logout(request)
    return redirect('vmsapp:login')