from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth import logout
from FruityDelightApp.models import Order, Complaint

# Create your views here.
class Landpage(View):

    def get(self, request):
        return render(request, 'landpage.html', {
            'title':'Fruity Delight',
        })

class GetFruity(View):
    def get(self, request, order="item"):
        if order == "item":
            return render(request, 'getFruity.html', {
            'title':'Order'
        })
        else:
            return render(request, 'order.html', {
                'title':order
            })

class Ordered(View):
    def post(self, request):
        name = request.POST.get('name')
        item = request.POST.get('item')

        new_order = Order(
            name=name,
            item=item,
            completed=False
        )
        id = new_order.save()

        return redirect('waiting', new_order.id)

class Waiting(View):
    def get(self, request, id):
        return render(request, 'waiting.html', {
            'title':f'Order Id ({id})',
            'item':Order.objects.get(pk=id)
        })

class SeeOrders(View):
    def get(self, request):
        return render(request, 'seeOrders.html', {
            'title':'Orders',
            'items':Order.objects.all().order_by('-order_date_time')
        })
    def post(self, request):
        completed = request.POST.get('updatecheck')

        if completed == 'on':
            id = request.POST.get('id')
            instance = Order.objects.get(pk=id)
            instance.completed = True
            instance.save()
        
        return redirect('seeorders')

class AboutUs(View):
    def get(self, request):
        return render(request, 'aboutus.html', {
            'title':'About Us'
        })

class AboutTeam(View):
    def get(self, request):
        return render(request, 'aboutteam.html', {
            'title':"About Team"
        })

class ComplaintView(View):
    def get(self, request):
        return render(request, 'complaint.html', {
            'title':'Complaint',
        })
    
    def post(self, request):
        print(request.POST)
        name=request.POST.get('name')
        complaint=request.POST.get('complaint')
        print(name, complaint)
        complaint = Complaint(
            name=request.POST.get('name'),
            complaint=request.POST.get('complaint')
        )
        complaint.save()
        return render(request, 'complaint.html', {
            'title':'Complaint Submitted Succussfully',
            'successcomplaint':True
        })

def logout_user(request):
    logout(request)
    return redirect('landpage')