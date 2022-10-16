'''
The logout_view() function is straightforward: we just import Django's
logout() function, call it, and then redirect back to the home page.
Because module [django.core.urlresolvers import reverse] is deprocated
we use module  [django.urls import reverse]
Here we import the render() function. Then import the login() and
authenticate() functions to log in the user if their registration information
is correct. We also import the default UserCreationForm. In the register() 
function, we check whether or not we're responding to a POST request.
'''
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

#===================================================================
# Log the user out.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
#===================================================================
# Register a new user. 
def register(request):
    # Check whether or not we're responding to a POST request
    # If not, make an instance of UserCreationForm with no initial data
    if request.method != 'POST':
        form = UserCreationForm() # Display blank registration form.
    else: # Process completed form.
        # Make an instance of UserCreationForm based on the submitted data
        form = UserCreationForm(data=request.POST)
        # Check that the data is valid. If YES, i.e. username/passwords match, 
        # call the form’s save() method to save the username and the hash of 
        # the password to the database. 
        if form.is_valid():
            # The save() method returns the newly created user object, 
            # which we store in new_user.
            new_user = form.save()
            # Log the user in and then redirect to home page.
            # When the user’s information is saved, we log them in, 
            # which is a 2-step process: we call authenticate() with 
            # the arguments new_user.username and their password
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            # When user registers, he is asked to enter two matching passwords, 
            # and because the form is valid, we know the passwords match so we 
            # can use either one. Here we get the value associated with the
            # 'password1' key in the form’s POST data. If the username and 
            # password are correct, the method returns an authenticated user 
            # object, which we store in authenticated_user. We then call the 
            # login() function with the request and authenticated_user objects
            # which creates a valid session for the new user
            login(request, authenticated_user)
            # Finally, redirect the user to the home page, where a personalized
            # greeting in the header tells them their registration was successful.
            return HttpResponseRedirect(reverse('learning_logs:index'))
    # Send context to the template = 'register.html'         
    context = {'form': form}
    return render(request, 'users/register.html', context)
#===================================================================
#===================================================================
#===================================================================

