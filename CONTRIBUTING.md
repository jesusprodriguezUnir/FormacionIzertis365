# Contribuir a FormacionIzertis365

¡Gracias por tu interés en contribuir! Este proyecto es parte de la formación de Izertis en herramientas Microsoft 365.

## Cómo contribuir

### Reportar errores

Si encuentras un error, por favor:
1. Ve a [Issues](../../issues)
2. Haz clic en "New Issue"
3. Describe el error con claridad incluyendo:
   - Pasos para reproducir
   - Comportamiento esperado
   - Comportamiento actual
   - Versión de Python y Django

### Sugerir mejoras

Para sugerencias de nuevas características:
1. Abre un Issue con la etiqueta `enhancement`
2. Describe la funcionalidad deseada
3. Explica el valor que aporta

### Enviar cambios

1. Fork el repositorio
2. Crea una rama para tu feature: `git checkout -b feature/AmazingFeature`
3. Commit tus cambios: `git commit -m 'Add some AmazingFeature'`
4. Push a la rama: `git push origin feature/AmazingFeature`
5. Abre un Pull Request

## Estándares de código

- Sigue [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Comentarios claros en español e inglés
- Pruebas unitarias para nuevas funcionalidades
- Actualiza la documentación

## Configuración del entorno para desarrollo

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/FormacionIzertis365.git
cd FormacionIzertis365

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Cargar datos iniciales
python manage.py load_initial_data

# Ejecutar servidor
python manage.py runserver
```

## Estructura de commits

Usa prefijos en tus commits:
- `feat:` Nueva funcionalidad
- `fix:` Corrección de error
- `docs:` Cambios en documentación
- `style:` Cambios de estilo (sin afectar código)
- `refactor:` Refactorización de código
- `test:` Adición de tests

Ejemplo:
```
feat: Agregar sistema de autenticación de usuarios
fix: Corregir búsqueda en recursos
docs: Actualizar README con instrucciones de instalación
```

## Licencia

Al contribuir, aceptas que tus contribuciones se licencien bajo los términos de licencia del proyecto.

---

Para preguntas, contacta a la formación de Izertis.
