# Online Shopping System

A Django e-commerce storefront: product catalogue, cart, checkout and customer accounts.

> **This is the earlier copy.** A later version with a pinned `requirements.txt` lives at [`Online-Shopping-Systems`](https://github.com/Ibrahimkhalill/Online-Shopping-Systems) (plural). Prefer that one unless you specifically need this snapshot.

## Data model

Defined in `store/models.py`:

| Model | Purpose |
|---|---|
| `Customer` | Shopper profile linked to a Django user |
| `Product` | Catalogue item |
| `Order` | Cart / placed order |
| `OrderItem` | Line item within an order |
| `ShippingAdress` | Delivery address for an order |

## Project layout

```
ecommerce/       # settings, root urls, wsgi
store/           # catalogue, cart, checkout
accounts/        # registration and login
static/          # css, js, product images
manage.py
```

Both `store.urls` and `accounts.urls` are mounted at `/`, with the Django admin at `/admin/`.

## Getting started

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install "django==3.2" django-crispy-forms pillow

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the storefront and http://127.0.0.1:8000/admin/ to add products.

## Notes

- No `requirements.txt` is checked in; the versions above match the sibling repository.
- `db.sqlite3` is committed. Delete it and re-run `migrate` for a clean database.
