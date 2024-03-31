from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, FormView, ListView

from .forms import ContactForm


def index(req):
    message = EmailMessage(
        subject='this is subject',
        body='this is body',
        to=['fko2347065@stu.o-hara.ac.jp'],
    )
    message.send()
    return render(req, 'mail/index.html')


def contactFn(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        title = req.POST.get('title')
        message = req.POST.get('message')
        emailMessage = EmailMessage(
            subject='お問い合わせがありました',
            body='name: {0}\nemail: {1}\ntitle: {2}\nmessage: {3}'.format(
                name, email, title, message),
            to=['fko2347065@stu.o-hara.ac.jp'],
        )
        emailMessage.send()
        return HttpResponseRedirect('/mail/thanks/')
    return render(req, 'mail/contactFn.html')


def thanks(req):
    return HttpResponse('thank you for your message')


class ContactView(FormView):
    template_name = 'mail/contact.html'
    success_url = '/'
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        emailMessage = EmailMessage(
            subject='お問い合わせがありました',
            body='name: {0}\nemail: {1}\ntitle: {2}\nmessage: {3}'.format(
                name, email, title, message),
            to=['fko2347065@stu.o-hara.ac.jp'],
        )
        emailMessage.send()
        messages.success(self.request, 'お問い合わせありがとうございました')
        return super().form_valid(form)
