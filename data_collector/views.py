from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from data_collector.models import DataPoint,Alert
from django.core.urlresolvers import reverse


# Create your views here.

class StatusView(TemplateView):
    template_name = 'status.html'
    def get_context_data(self, **kwargs):
        ctx = super(StatusView,self).get_context_data(**kwargs)
        alerts = Alert.objects.filter(is_active=True)
        # only fetch these two fields
        nodes_and_data_types=DataPoint.objects.all().values('node_name','data_type').distinct()
        status_data_dict =dict()
        for nodes_and_data_type_pair in nodes_and_data_types:
            node_name=nodes_and_data_type_pair['node_name']
            data_type=nodes_and_data_type_pair['data_type']

            ###add here. has_alert

            latest_data_point = DataPoint.objects.filter(node_name=node_name,data_type=data_type).latest('datetime')
            latest_data_point.has_alert = self.does_alert(latest_data_point,alerts)

            data_point_map = status_data_dict.setdefault(node_name,dict())
            data_point_map[data_type]=latest_data_point
        ctx['status_data_dict']=status_data_dict
        return ctx
        """
        status_data_dict will generate records like this
        {u'a': {u'1': <DataPoint: DataPoint for a. 1 = 0.95>},
 u'b':
 u'c': {u'2': <DataPoint: DataPoint for c. 2 = 0.85>,
            u'1': <DataPoint: DataPoint for c. 1 = 9.0>}}
                """
    def does_alert(self,data_point,alerts):
        for alert in alerts:
            if alert.node_name and data_point.node_name !=alert.node_name:
                continue
            if alert.data_type != data_point.data_type:
                continue
            if alert.min_value is not None and data_point.data_value < alert.min_value:
                return True
            if alert.max_value is not None and data_point.data_value > alert.max_value:
                return True
        return False


class AlertListView(ListView):
    template_name = 'alert_list.html'
    model = Alert

class NewAlertView(CreateView):
    template_name = 'create_or_update_alert.html'
    model = Alert
    fields =  ['data_type','min_value','max_value','node_name','is_active']
    def get_success_url(self):
        return reverse('alerts_list')

class EditAlertView(UpdateView):
    template_name = 'create_or_update_alert.html'
    model = Alert
    fields =  ['data_type','min_value','max_value','node_name','is_active']
    def get_success_url(self):
        return reverse('alerts_list')

class DeleteAlertView(DeleteView):
    template_name = 'delete_alert.html'
    model=Alert
    def get_success_url(self):
        return reverse('alerts_list')