from django.shortcuts import render, redirect
from .forms import CreateUserForm 
from django.contrib.sites.shortcuts import get_current_site #there domain name idk when we deploy...62
from . token import user_tokenizer_generate

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode





def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            user = form.save() # we overwriting that obj

            user.is_active = False #without verification we don't activate account

            user.save()


            # Email verification setup (template)
            current_site = get_current_site(request)

            subject = 'Account verification email'

            message = render_to_string('account/registration/email-verification.html',{

                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user), 
            })

            user.email_user(subject=subject, message=message)


        return redirect('email-verification-success')#we want redirect that user to url with name...

        
    context = {'form':form}

    return render(request, 'account/registration/register.html', context=context)


def email_verification(request):

    pass


def email_verification_sent(request):

    pass


def email_verification_success(request):

    pass


def email_verification_failed(request):

    pass