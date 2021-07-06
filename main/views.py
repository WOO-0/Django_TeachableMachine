from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SigninView(TemplateView):
    template_name = 'signin.html'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class HomeView(TemplateView):
    template_name = 'home.html'


class TestView(TemplateView):
    template_name = 'test.html'

# def events(request):
#     all_events = Events.objects.all()
#     get_event_types = Events.objects.only('event_type')
#     calendars = Calendar.objects.all()

#     if request.GET:
#         event_arr = []
#         if request.GET.get('event_type') == "all":
#             all_events = Events.objects.all()
#         else:
#             all_events = Events.objects.filter(event_type__icontains=request.GET.get('event_type'))

#         for i in all_events:
#             event_sub_arr = {}
#             event_sub_arr['id'] = i.event_id
#             event_sub_arr['calendar'] = i.calendar
#             event_sub_arr['calendar_id'] = i.calendar.id
#             event_sub_arr['title'] = i.event_name
#             start_date = datetime.strptime(str(i.start_date.date()), "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
#             end_date = datetime.strptime(str(i.end_date.date()), "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
#             event_sub_arr['start'] = start_date
#             event_sub_arr['end'] = end_date
#             event_arr.append(event_sub_arr)
#         return HttpResponse(json.dumps(event_arr))

#     context = {
#         "calendars": calendars,
#         "events": all_events,
#         "get_event_types": get_event_types,

#     }
#     return render(request, 'main/selectable.html', context)


# def add_event(request, pk):
#     opp = get_object_or_404(OpportunityList, pk=pk) # This is the lead which will be schaduled for. Nothing to do with this question.
#     events = Events.objects.all() # All the events scheduled so far.

#     user = User.objects.get(username=request.user)
#     opp_locked = get_object_or_404(Locked, pk=pk) # Locked lead. Just ignore it.
#     form = ZakaziForma() # Scheduling form(simple form with the model fields)

#     if request.method == 'POST':
#         form = ZakaziForma(request.POST or None)

#         if form.is_valid():
#             event = Events.objects.create(
#                 start_date=form.cleaned_data['start_date'],
#                 end_date=form.cleaned_data['end_date'],
#                 event_name=form.cleaned_data['event_name'],
#                 added_by=user,
#                 event_comment=form.cleaned_data['event_comment'],
#                 status=form.cleaned_data['status'],
#                 zakazan=True,
#                 opp_eluid=int(opp_locked.locked_eluid.eluid),
#                 calendar=form.cleaned_data['calendar'],
#             )
#             opp_locked.is_locked = False
#             opp_locked.zakazan = True
#             opp_locked.save()
#             event.save()
#             messages.success(request, 'Uspešno ste zakazali termin za ' + opp_locked.locked_comment)
#             return redirect('opportunity:optika')
#     context = {
#         'form': form,
#         'opp': opp,
#         'events': events
#     }
#     return render(request, 'opportunity/detalji/zakazi.html', context)
