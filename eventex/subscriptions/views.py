from django.conf import settings
from django.core import mail
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


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

    subscription = Subscription.objects.create(**form.cleaned_data)

    # Send email
    _send_mail(form.cleaned_data['email'], {'subscription': subscription})

    return HttpResponseRedirect('/inscricao/{}/'.format(subscription.pk))


def new(request):
    return render(request, subscriptionhtml, {'form': SubscriptionForm()})


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404

    return render(
            request,
            'subscriptions/subscription_detail.html',
            {'subscription': subscription}
    )


def _send_mail(to, context):
    from_ = settings.DEFAULT_FROM_EMAIL

    body = render_to_string('subscriptions/subscription_email.txt', context)
    mail.send_mail('Confirmação de inscrição', body, from_, [from_, to])
