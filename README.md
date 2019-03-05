# django-form-renderer
A rendering engine for Django forms using templatetags

## Preamble
There are already many libraries to render Django form in templates, including the default Form methods as_p(), as_ul(), as_table(). Unfortunately, none of them (that I have encountered at least) apply strictly the concept of separation of form and function, or business logic from presentation, etc. Django has made a step into the right direction by using template for the widgets, but the entirety of a field rendering is still partially done in python code. For example, if the developer wishes to put the label after the checkbox, he still has to write python, instead of redefining a template.

This library defines one or more registry, that associate a rendering function (called renderer) for each Form Field class. That rendering function is made available through the templatetag renderfield.

## Basic steps to render a Django Form

### Create a registry
For example, in the file *path/to/my_registry.py*
```python
from django import forms
from formrenderer import FormRendererRegistry

registry = FormRendererRegistry()
```

### Register a renderer for a formfield
```python
from django.template.loader import get_template
from

# This can be done by calling directly the register method of the registry
registry.register(forms.CharField, get_template('mytemplates/char_field.html').render)

# Or using the decorator on a class definition
@registry.register(get_template('mytemplates/my_field.html').render)
class MyField(forms.Field):
	pass

```

The file *mytemplates/char_field.html* could be as simple as this:
```html
<label for={{ id }}>{{label}}
<input type="text" id={{ id }} name={{ name }} value={{ value }}>
</label>
<p>{{help_text}}</p>
<ul>
{% for error in errors %}<li>{{ error }}</li>{% endfor %}
</ul>
```

### Write a template that renders the form
```html
{% load formrenderer %}
<html>
	<body>
		<form>
			{% for field in form %}
			{{ field|renderfield:'path.to.my_registry.registry' }}
			{% endfor %}
			<input type="submit" value="Send">
		</form>
	</body>
</html>
```

## Renderer function
A renderer function does not have to be a template render method, it can be any method that returns a string. (Must it be marked safe?) It is passed a single parameter that is a dict (called context) with the following key/values:

  * __form__: The form the field belongs to
  * __boundfield__: The bound field itself
  * __widget__: The widget instance of the field
  * __name__: The name HTML attribute for the field
  * __value__: The current value of the field
  * __label__: The label of the field
  * __id__: The id for the label of the field
  * __errors__: The list of Validation errors for the field
  * __help_text__: The help_text of the field
  * __disabled__: True if the field is disabled
  * __is_hidden__: True if the field is hidden
  * __required__: True if the field is required

## Context modifier function

When registering a renderer for a Form Field, it is possible to specify a context modifier function. This function will receive the context as the only parameter, and is suppose to return it modified. For example:

```python
# Let's add a some class to the widget attrs

def add_class(context):
	context['widget'].attrs.class = 'bowtie'
	return context

@registry.register(get_template('mytemplates/my_field.html').render, add_class)
class MySuperField(MyField):
	pass
```

## Resolution of renderer
To find a renderer for a Form Field, we follow the MRO order of the Form Field until a we find a renderer registered for that Form Field. For example:
```python
from django.core.exceptions import ValidationError

# Override CharField to add some extra clean, BUT DO NOT register a new renderer
class MyCharField(forms.CharField):
	def clean(self, value):
		if value == 'Spanish Inquisition':
			raise ValidationError('I was not expecting the Spanish Inquisition!')
		else:
			return super().clean(value)

# Override MyCharField AND register a new renderer
@registry.register(get_template('mytemplates/my_other_char_field.html').render)
class MyOtherCharField(MyCharField):
	pass

```

In the first case, the renderer used will be the one we registered for the CharField earlier (template 'mytemplates/char_field.html'). In the second, the renderer used will be the one we registered for MyOtherCharField (template 'mytemplates/my_other_char_field.html')

If no renderer is found, a NotImplementedError is raised.

## *renderfield* templatetag
The renderfield templatetag can take a single parameter, that is a registry object or the full dotted path to a registry object.

If no parameter is given, it will use the default registry as defined in the settings. For our example this would be:
```python
FORM_RENDERER_DEFAULT_REGISTRY = 'path.to.my_registry.registry'
```
