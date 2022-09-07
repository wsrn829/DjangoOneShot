# One Shot Planning

These are some markdown formatting you can use to plan. You can preview your markdown in VS Code with the command "markdown preview", commonly `Command + Shift + V` (`Ctrl + Shift + V` on Windows) while you have this file open

Edit this and make it your own. Alternatively, link your notion here:

## My Notion / weblink

https://notion...

## Steps

### Step 1

* [ ] First substep
* [ ] Second substep

### Step 2

* [ ] First substep
* [ ] Second substep

## Questions

How do I access the model instances of the reverse relationship of a many to many relationship?

## Resources

* https://ccbv.co.uk/

---

## Bonus instructions:

### Install Django Debug Toolbar

https://django-debug-toolbar.readthedocs.io/en/latest/

```bash
python -m pip install django-debug-toolbar
```

### 3. Install the App

Add `"debug_toolbar"` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    # ...
    "debug_toolbar",
    # ...
]

```

Add django-debug-toolbar’s URLs to your project’s URLconf:

```python
from django.urls import include, path

urlpatterns = [
    # ...
    path('__debug__/', include('debug_toolbar.urls')),
]

```

The Debug Toolbar is mostly implemented in a middleware. Add it to your `MIDDLEWARE` setting:

```python
MIDDLEWARE = [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]
```

The Debug Toolbar is shown only if your IP address is listed in Django’s [`INTERNAL_IPS`](https://docs.djangoproject.com/en/dev/ref/settings/#std-setting-INTERNAL_IPS "(in Django v4.2)") setting. This means that for local development, you _must_ add `"127.0.0.1"` to [`INTERNAL_IPS`](https://docs.djangoproject.com/en/dev/ref/settings/#std-setting-INTERNAL_IPS "(in Django v4.2)"). You’ll need to create this setting if it doesn’t already exist in your settings module:

```python
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

```

