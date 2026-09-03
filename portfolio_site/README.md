# Onah Samuel Iyojeni — Portfolio Site

A Django-backed personal site: home, a projects index ("Work"), a blog ("Journal"),
an about page, and a working contact form. Content — including images — is managed
through Django's built-in admin, no code changes needed.

Design: colorful, image-forward editorial — a masthead nav, project/post listings as
photo cards with hover motion, drop caps on long-form text, and a colorful generated
placeholder (gradient + initials) for anything that doesn't have a photo yet. Set in
Fraunces (display), Source Serif 4 (body), and Inter (UI/meta).

## If you already have this project running (upgrading)

You added images and a Profile section on top of an earlier version. To upgrade
your existing local copy without losing your data:

1. Replace all your project files with the ones in this download (keep your own
   `db.sqlite3` and `venv/` folders where they are — don't overwrite those).
2. With your venv activated: `pip install -r requirements.txt` (adds Pillow, needed
   for image uploads).
3. `python manage.py migrate` — this adds the new image fields and the Profile
   table on top of your existing data. Your existing projects and posts are kept.
4. `python manage.py seed_demo` — safe to re-run; it fills in your bio in the new
   Profile section if it's empty, and won't duplicate your projects/posts.
5. `python manage.py runserver` as usual.

## 1. Set up (fresh install)

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. First-time database setup

```bash
python manage.py migrate
python manage.py createsuperuser   # you'll use this to log into /admin/
```

Optional — load placeholder projects/posts so the site isn't empty while you build:

```bash
python manage.py seed_demo
```

(You can delete or edit any of the seeded content from the admin afterward.)

## 3. Run it

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** for the site and **http://127.0.0.1:8000/admin/**
to manage content.

## 4. Adding your photos and info

Everything personal — your name, tagline, bio, portrait, and an optional hero
background photo — lives in one place: log into `/admin/` and open **Profile**
(there's only one row; the admin takes you straight to it). Fields:

- **portrait** — shown on the About page
- **hero_image** — optional; if set, shows behind the home page headline
- **bio** — plain text, one paragraph per line
- **email / github_url / linkedin_url** — power the footer links

**Projects and blog posts** — add/edit these under `/admin/` too. Each `Project`
and `Post` has a **cover_image** field — upload a photo and it appears as the card
image on the index pages and at the top of the detail page. Leave it blank and the
card shows a colorful auto-generated placeholder instead, so the site still looks
finished before you've uploaded anything.

Image tips:
- Landscape/wide photos (roughly 4:3 or 16:9) work best for project and post covers.
- Portrait photos work best as a tall rectangle (roughly 4:5) for the About page.
- Uploaded images are saved to a `media/` folder that's created automatically —
  it's excluded from git via `.gitignore`, so remember to include it (or re-upload
  through the admin) when you move to a new machine or deploy.

## 5. Colors and type

All design tokens live at the top of `static/css/style.css` under `:root` —
`--coral`, `--teal`, `--gold`, `--plum` are the accent colors used throughout
(tags, placeholder gradients, buttons). Change them there to retheme the whole site.

## 6. Contact form

Messages currently save to the database and appear under `ContactMessage` in the
admin. If you'd rather get them by email, swap the `EMAIL_BACKEND` in
`portfolio/settings.py` for an SMTP backend and add a `send_mail(...)` call in
`core/views.py::contact`.

## 7. Deploying

Before deploying anywhere public:
- Set `DEBUG = False` in `portfolio/settings.py`
- Set a real `SECRET_KEY` via an environment variable, not the committed default
- Set `ALLOWED_HOSTS` to your real domain
- Switch `DATABASES` from SQLite to Postgres if your host recommends it
- Run `python manage.py collectstatic` and serve `/static/` via your host or whitenoise
- Uploaded images (`MEDIA_ROOT`) need real storage in production — most hosts
  recommend something like Amazon S3 or Cloudinary rather than the local disk

Any host that runs Django works: Railway, Render, Fly.io, PythonAnywhere, a VPS, etc.
