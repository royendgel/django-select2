# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.views.generic import FormView


class TemplateFormView(FormView):
    template_name = 'form.html'


def heavy_data_1(request):
    numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five']
    results = [{'id': index, 'text': value} for (index, value) in enumerate(numbers)]
    return HttpResponse(json.dumps({'err': 'nil', 'results': results}), content_type='application/json')


def heavy_data_2(request):
    numbers = ['Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Fortytwo']
    results = [{'id': index, 'text': value} for (index, value) in enumerate(numbers)]
    return HttpResponse(json.dumps({'err': 'nil', 'results': results}), content_type='application/json')
