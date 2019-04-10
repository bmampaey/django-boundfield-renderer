# django-boundfield-renderer
A rendering engine for Django forms using templatetags

## Preamble
There are already many libraries to render Django forms in templates, including the default Form methods as_p(), as_ul(), as_table(). Unfortunately, none of them (that I have encountered at least) apply strictly the concept of separation of form and function, or business logic from presentation, etc. Django has made a step into the right direction by using templates for the widgets, but the entirety of a field rendering is still partially done in python code. For example, if the developer wishes to put the label after the checkbox, he still has to write python, instead of redefining a template.

This library defines one or more registry, that associate a rendering function (called renderer) for each form field class. That rendering function is made available through the templatetag `renderer`.

## Basic steps to render a Django Form
### Create a registry and register the renderers for the field classes
For example, in the file *path/to/my_registry.py*
```python
from django import forms
from django.template.loader import get_template
from boundfield_renderer import RendererRegistry

# Create the registry
registry = RendererRegistry()

# Define a renderer function for a field class, for example the CharField
# This can be as simple as the render method of a template
template_render = get_template('mytemplates/char_field.html').render

# Register the renderer for the field class in the registry
# Either by setting it directly on the registry
registry[forms.CharField] = template_render

# Or by using the register method as a decorator on a field class definition
@registry.register(get_template('mytemplates/my_field.html').render)
class MyField(forms.Field):
	pass

```

The file *mytemplates/char_field.html* could be as simple as this:
```html
<label for="{{ id }}">{{label}}
<input type="text" id="{{ id }}" name="{{ name }}" value="{{ value }}">
</label>
<p>{{ help_text }}</p>
<ul>
{% for error in errors %}<li>{{ error }}</li>{% endfor %}
</ul>
```

### Write a template that renders the form using the `renderer` template tag
For example, in the file *mytemplates/my_form.html*
```html
{% load boundfield_renderer %}
<html>
	<body>
		<form>
			{% for boundfield in form %}
			{% renderer boundfield 'path.to.my_registry.registry' %}
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
  * __html_name__: The HTML name attribute for the field
  * __value__: The current value of the field
  * __label__: The label of the field
  * __id__: The id for the label of the field
  * __help_text__: The help_text of the field
  * __errors__: The list of Validation errors for the field
  * __disabled__: True if the field is disabled
  * __is_hidden__: True if the field is hidden
  * __required__: True if the field is required


## Resolution of renderer
To find a renderer for a field class, we follow the MRO order of the field class until we find a renderer registered for that subclass. For example:

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

In the first case, the renderer used will be the one we registered for the CharField earlier (template *mytemplates/char_field.html*). In the second, the renderer used will be the one we registered for MyOtherCharField (template *mytemplates/my_other_char_field.html*)

If no renderer is found, a ValueError is raised.

## *renderer* templatetag
The renderer templatetag takes a boundfield as the first parameter. It can also take as a second optional parameter a registry object or the full dotted path to a registry object.

If no registry is specified, it will use the default registry as defined in the settings as DEFAULT_BOUNDFIELD_RENDERER_REGISTRY.


For our example this would be:
```python
DEFAULT_BOUNDFIELD_RENDERER_REGISTRY = 'path.to.my_registry.registry'
```

Finally, the renderer tag can take optional keyword parameters that will be added to the context.

If we reuse our previous example form template *mytemplates/my_form.html*, we could change the context for a particular field "starwberry" to add a context variable "css_classes" with a value of "forever":

```html
{% load boundfield_renderer %}
<html>
	<body>
		<form>
			{% for boundfield in form %}
			{% if boundfield.name == 'strawberry' %}
			{% renderer boundfield 'path.to.my_registry.registry' css_classes='forever' %}
			{% else %}
			{% renderer boundfield 'path.to.my_registry.registry' %}
			{% endif %}
			{% endfor %}
			<input type="submit" value="Send">
		</form>
	</body>
</html>
```

## Note on renderer registration
The code that registers the renderer for a form field class must be executed by Django before the `renderer` templatetag is called.

Practically, this can be achieved by registering the renderers in the same file where the registry is defined, or in the files where the form field class are defined (for example using the *register* decorator)
