from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from app.models import publisher
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
    
    
def createpost(request):
        if request.method == 'POST':
            if request.POST.get('note'):
                userid = request.user.id
                post=publisher()
                post.note= request.POST.get('note')
                post.uid = userid
                post.save()
                
                return render(request, 'createpost.html')  

        else:
            return render(request, 'createpost.html')
			
			
def display(request):
    userid = request.user.id
    allnotes = publisher.objects.all().filter(uid=userid)
    context = {'allnotes':allnotes}
    return render(request,'display.html',context)
	
	
class DeleteView(SuccessMessageMixin, DeleteView):
	model = publisher
	success_url = '/'
	success_message = "deleted..."

def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    name = self.object.name
    request.session['name'] = name  # name will be change according to your need
    message = request.session['name'] + ' deleted successfully'
    messages.success(self.request, message)
    return super(DeleteView, self).delete(request, *args, **kwargs)