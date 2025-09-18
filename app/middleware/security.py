import re
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class PortfolioSecurityMiddleware:
    """
    Middleware para portafolio personal:
    - Protege rutas de administración
    - Permite acceso público al portafolio
    """

    # ---------- CONFIGURACIÓN ----------
    PUBLIC_PATHS = [
        r'^/$',                      # Página principal
        r'^/portfolio/',             # Vista pública del portafolio
        r'^/projects/',              # Detalles de proyectos públicos
        r'^/login/$',
        r'^/register/$',
        r'^/static/',
        r'^/media/',
        r'^/api/',                   # Si tienes API pública
    ]

    PROTECTED_PATTERNS = [
        r'^/admin/',                # Panel de administración
        r'^/dashboard/',            # Panel de control del usuario
        r'^/manage/projects/',      # Gestión de proyectos
        r'^/account/',              # Configuración de cuenta
        r'^/experience/',
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        # ---------- RUTAS PÚBLICAS ----------
        if any(re.match(pattern, path) for pattern in self.PUBLIC_PATHS):
            return self.get_response(request)

        # ---------- PROTECCIÓN DE RUTAS ----------
        if any(re.match(pattern, path) for pattern in self.PROTECTED_PATTERNS):
            if not request.user.is_authenticated:
                return redirect(f'{settings.LOGIN_URL}?next={path}')

        # ---------- SEGURIDAD ADICIONAL ----------
        response = self.get_response(request)
        
        # Headers de seguridad
        security_headers = {
            'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
            'Pragma': 'no-cache',
            'Expires': '0',
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'DENY',
            'X-XSS-Protection': '1; mode=block',
        }
        
        for header, value in security_headers.items():
            response[header] = value

        return response