# -*- coding: utf-8 -*-
# Available templates to display a slideshow
SLIDESHOWS_TEMPLATES = (
    ("slideshows/slides_show/default.html", "Default template"),
    ("slideshows/slides_show/bootstrap_3.html", "Bootstrap 3 template"),
)

# Available config file to initialize your slideshow Javascript stuff
SLIDESHOWS_CONFIGS = (
    ("slideshows/slides_show/configs/default.html", "Default config"),
    ("slideshows/slides_show/configs/bootstrap_3.html", "Bootstrap 3 config"),
)

# Available templates for "random slide" mode
SLIDESHOWS_RANDOM_SLIDE_TEMPLATES = (
    ("slideshows/random_slide/default.html", "Random image default"),
)

# Default templates to use in admin forms
DEFAULT_SLIDESHOWS_TEMPLATE = SLIDESHOWS_TEMPLATES[1][0]
DEFAULT_SLIDESHOWS_CONFIG = ""
DEFAULT_SLIDESHOWS_RANDOM_SLIDE_TEMPLATE = SLIDESHOWS_RANDOM_SLIDE_TEMPLATES[1][0]
