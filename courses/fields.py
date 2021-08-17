from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):
	def __init__(self, for_fields=None, *arg, **kwargs):
		self.for_fields = for_fields
		super().__init__(*args, **kwargs)

	def pre_save(self, model_instance, add):
		if getattr(model_instance, self.attname) is None:
			# no current value
			try:
				qs = self.model.objects.all()
				if self.for_fields:
					# filter by objects with the same field values
					# for the fields in "for_fields" 