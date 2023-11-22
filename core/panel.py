from .settings import *

JAZZMIN_SETTINGS = {
    "site_brand": "ADMINISTRATION",
    "site_logo": "img/logo.png",
    "search_model": ["auth.User"],

    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Developer", "url": "https://ibhax.github.io", "new_window": False},
        {"model": "auth.User"},
        {"app": "index"},
    ],
    
    "usermenu_links": [
        {"name": "Developer", "url": "https://ibhax.github.io", "new_window": False},
        {"model": "auth.user"}
    ],
 # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "vertical_tabs",
   

}