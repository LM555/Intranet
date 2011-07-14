
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from pipa.addressbook.models import PipaProfile
from pipa.addressbook.forms import ProfileForm, NewMemberForm


def alumni(request):
    profiles = PipaProfile.objects.\
                        filter(show_profile=True).order_by('user__first_name')
    return render_to_response(
                              "alumni/alumni.html",
                              RequestContext(request, locals()))


@login_required
def addressbook(request):
    profile = request.user.get_profile()

    initial_dict = {
                    'email': request.user.email,
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name
                    }

    default_profile_form = ProfileForm(
                                       instance=profile,
                                       initial=initial_dict
                                       )
    profile_form = None
    newmemberform = None
    newmemberform_show = False

    if request.method == 'POST':

        if 'usersubmit' in request.POST:
            submit_name = 'usersubmit'

        elif 'profilesubmit' in request.POST:
            submit_name = 'profilesubmit'

        else:
            submit_name = None

        profile_form = ProfileForm(
                                   request.POST,
                                   request.FILES,
                                   instance=profile)

        if profile_form.is_valid() and submit_name == 'profilesubmit':
            # this should probably be better integrated with LDAP
            request.user.email = profile_form.cleaned_data['email']
            request.user.first_name = profile_form.cleaned_data['first_name']
            request.user.last_name = profile_form.cleaned_data['last_name']
            request.user.save()
            profile_form.save()
            return HttpResponseRedirect(request.path)

        newmemberform = NewMemberForm(request.POST)

        if newmemberform.is_valid() and submit_name == 'usersubmit':
            # TODO: add user to the system

            # on successful add of new member
            newmemberform_show = True
            kwargs = {
                      'newmember_username': newmemberform.\
                                                    cleaned_data['username'],
                      'profile_form': default_profile_form,
                      'newmemberform': NewMemberForm(),
                      'newmemberform_show': newmemberform_show
                      }
            return render_to_response(
                                      "org/addressbook.html",
                                      kwargs,
                                      context_instance=RequestContext(request)
                                      )

        if submit_name == 'usersubmit':
            profile_form = default_profile_form
            newmemberform_show = True

        elif submit_name == 'profilesubmit':
            newmemberform = NewMemberForm()

    else:
        profile_form = default_profile_form
        newmemberform = NewMemberForm()

    context = {'profile_form': profile_form,
        'object_list': PipaProfile.objects.all(),
        'user_list': User.objects.all().order_by('username'),
        'newmemberform': newmemberform,
        'newmemberform_show': newmemberform_show
        }

    return render_to_response(
                              "org/addressbook.html",
                              RequestContext(request, context)
                              )
