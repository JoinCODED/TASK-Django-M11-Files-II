Time to purchase some islands!

## Setup

1. Fork and clone [this repository](https://github.com/malthunayan/TASK-Django-M11-Files-II).
2. Install the `requirements` using `pip install -r requirements.txt`.
3. Run the `migrations`.

## Task

### Static & Media Files

1. Add the setup for the static files in `settings.py`:

   ```python
   STATIC_URL = "static/"
   STATIC_ROOT = BASE_DIR / "static"
   ```

2. Add the setup for the static files in `urls.py`:

   ```python
   ...

   from django.conf import settings
   from django.conf.urls.static import static

   urlpatterns = [
       ...
   ]

   if settings.DEBUG:
       urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   ```

3. Add the setup for the media files in `settings.py`:

   ```python
   MEDIA_URL = "media/"
   MEDIA_ROOT = BASE_DIR / "media"
   ```

4. Add the setup for the media files in `urls.py`:

   ```python
   ...

   urlpatterns = [
       ...
   ]

   if settings.DEBUG:
       ...
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

5. Go to the admin site and create some islands (if you do this step before setting up media files, the images will be in the root directory of the project).
6. Go to `http://localhost:8000/islands/` and see your beautiful islands!
7. Fix the image by adding a `src` (look [here](https://docs.djangoproject.com/en/4.1/topics/files/#using-files-in-models) for help).
8. Load your static file here and add a `static` folder inside of `islands`.
9. Add a stylesheet to your island list template and link it to the template.
10. Add some CSS and prettify your list of islands!
11. Commit and push your code.

### Media Files w/ Forms

1. Add `forms.py` inside of `islands`.
2. Add a model form for `Island` called `IslandForm`, and include the `name` field.
3. Add a `photos` attribute above `class Meta` that will be a `FileField` with multiple uploads allowed ([look here](https://docs.djangoproject.com/en/4.0/topics/http/file-uploads/#uploading-multiple-files) for more info).
4. Add `photos` to the list of fields inside of `IslandForm`.
5. Add a `create_island` view and create a url for it in our `urls.py`.
   - The view should render the form in a template called `create_island.html`.
6. Add the `create_island.html` template inside of `islands/templates`.
7. Make sure to wrap it with a `form` tag as follows:

   ```html
   <form
     action="{% url 'create-island' %}"
     method="POST"
     enctype="multipart/form-data"
   >
     ...
   </form>
   ```

   - Again, `enctype` is what will allow us to deal with user-uploaded files.

8. Update our view in order to handle the file upload:

   ```python
   def create_island(request: HttpRequest) -> HttpResponse:
       form = IslandForm()
       if request.method == "POST":
           form = IslandForm(request.POST, request.FILES)
           if form.is_valid():
               form.save()
               return redirect("island-list")
       context = {
           "form": form,
       }
       return render(request, "create_island.html", context)
   ```

9. The code above will not work, because the island model does not have `photos` as an attribute (in fact, a lot of it will need to change).
10. You will need to create the island separately first.
11. Then iterate over the `request.FILES` and create `IslandPhoto`s.
12. Test out the form and commit your changes.
13. Push your code.

#### Media Files w/ Forms Bonus

Instead of creating an `IslandPhoto` on each iteration, accumulate all the `IslandPhoto`s that will be created and bulk create them. [This link](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#bulk-create) should help you out.
