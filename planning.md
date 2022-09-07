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

---

## Bonus instructions:

### Install Django Debug Toolbar

https://django-debug-toolbar.readthedocs.io/en/latest/

### Pip Install

```bash
python -m pip install django-debug-toolbar
```

### Install the App

Add `"debug_toolbar"` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    # ...
    "debug_toolbar",
    # ...
]
```

### Add to urls

Add django-debug-toolbar’s URLs to your project’s URLconf `urls.py`:

```python
from django.urls import include, path

urlpatterns = [
    # ...
    path('__debug__/', include('debug_toolbar.urls')),
]
```

### Add to middleware

Add it to your `MIDDLEWARE` setting in `settings.py`:

```python
MIDDLEWARE = [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]
```

### Add to INTERNAL IPs

Add the following to `settings.py`:

```python
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
```

