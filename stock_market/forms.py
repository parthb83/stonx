from django import forms
from .models import Stock
from django.contrib.auth.models import User

class StockForm(forms.ModelForm):
	def __init__(self, **kwargs):
		self.user = kwargs.pop('user', None)
		super(StockForm, self).__init__(**kwargs)

	def save(self, commit=True):
		obj = super(StockForm, self).save(commit=False)
		obj.user = self.user
		if commit:
			obj.save()
		return obj

	class Meta:
		model = Stock
		fields = ["ticker"]