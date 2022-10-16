'''
The logout_view() function is straightforward: we just import Django's
logout() function, call it, and then redirect back to the home page.
Because module [django.core.urlresolvers import reverse] is deprocated
we use module  [django.urls import reverse]
'''
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse
from django.contrib.auth import logout
#===================================================================
# Log the user out.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
#===================================================================