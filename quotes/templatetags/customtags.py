from django import template

register = template.Library()

@register.filter(name='percentFormat')
def percentFormat(value, decimal_places):
	'''Multiplies a raw number by 100 and formats with passed number of decimal places.'''
	return round(value * 100, decimal_places)

@register.filter(name='multiply')
def multiply(value, multiplier):
	'''Multiplies a raw number by 100 and formats with passed number of decimal places.'''
	return value * multiplier