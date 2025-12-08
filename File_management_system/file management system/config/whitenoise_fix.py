"""
WSGI config for config project.
"""

import os
import mimetypes

from django.core.wsgi import get_wsgi_application

# Add MIME types before getting WSGI application
mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("application/javascript", ".js", True)
mimetypes.add_type("image/png", ".png", True)
mimetypes.add_type("image/jpeg", ".jpg", True)
mimetypes.add_type("image/jpeg", ".jpeg", True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()