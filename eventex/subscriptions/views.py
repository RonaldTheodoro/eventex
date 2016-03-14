from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm

subscriptionhtml = 'subscriptions/subscription_form.html'


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, subscriptionhtml, {'form': form})

    # Send email
    _send_mail(form.cleaned_data['email'], form.cleaned_data)

    # Success feedback
    messages.success(request, 'Inscrição realizada com sucesso')

    return HttpResponseRedirect('/inscricao/')


def new(request):
    return render(request, subscriptionhtml, {'form': SubscriptionForm()})


def _send_mail(to, context):
    from_ = settings.DEFAULT_FROM_EMAIL

    body = render_to_string('subscriptions/subscription_email.txt', context)
    mail.send_mail('Confirmação de inscrição', body, from_, [from_, to])
