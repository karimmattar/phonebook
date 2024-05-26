from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.forms import inlineformset_factory

from .models import Contact, ContactNumber
from .forms import ContactNumberForm


class ContactListView(ListView):
    model = Contact
    template_name = 'contact/contact_list.html'
    paginate_by = 10


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact/contact_view.html'


class ContactAddView(CreateView):
    model = Contact
    fields = ['first_name', 'last_name']
    template_name = 'contact/contact_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra = int(self.request.GET.get('extra', 1))  # Get the value of 'extra' from the query string
        ContactFormSet = inlineformset_factory(Contact, ContactNumber, form=ContactNumberForm, extra=extra,
                                               can_delete=True)
        context['number_formset'] = ContactFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        self.object = form.save()
        number_formset = self.get_context_data()['number_formset']
        if number_formset.is_valid():
            number_formset.instance = self.object
            number_formset.save()
        return super().form_valid(form)
