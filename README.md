# 🗃️ Django Job Board

Job Board is a dynamic and responsive web-based job portal application developed using Django for the backend and HTML, CSS, JavaScript, and Bootstrap for the frontend. The platform enables employers to post job openings while allowing job seekers to browse and search available opportunities. It features complete CRUD operations for job listings, user-friendly navigation, and an admin dashboard for managing job posts. Additional functionalities include form validations, search and filter options, pagination for organized job displays, and a contact inquiry form.


---

## 🚀 Features

- View available job postings
- Job detail pages with full description
- Submit applications with name, email, message, and CV upload (PDF)
- Admin panel to manage jobs and applications
- TailwindCSS for a clean and responsive UI
- File upload system using Django `FileField`

---

## 🛠️ Tech Stack

- Python 3
- Django 4+
- Tailwind CSS (via CDN)
- SQLite (default)
- Crispy Forms + Tailwind template pack

---

## 📦 Setup Instructions

1. **Clone this repo:**
   ```bash
   git clone https://github.com/your-username/django-job-board.git
   cd django-job-board
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run server:**
   ```bash
   python manage.py runserver
   ```

6. **Visit app:**
   Open browser and go to [http://localhost:8000](http://localhost:8000)

---

## 📁 File Uploads (Resume)

Uploaded resumes are stored in the `media/resumes/` folder. Be sure to create that folder and configure Django settings:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

In `urls.py`:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## ✅ To-Do / Ideas

- ✅ Apply form with file upload (CV)
- 🔜 Add search/filter by company or salary
- 🔜 Admin download links for resumes
- 🔜 Pagination and SEO meta tags
- 🔜 Deploy on Render / Railway / Vercel

---

## 👨‍💻 Author
Built with ☕, 🧠, and a lot of Tailwind by Long 😎🚀.

---

## 📄 License
MIT License. Do whatever you want, but credit is always appreciated 🙌

