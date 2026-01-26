# 📚 Guía de Publicación en GitHub - FormacionIzertis365

## 🚀 Pasos para Publicar tu Aplicación

### PASO 1: Crear el Repositorio en GitHub

1. Ve a https://github.com/new
2. Rellena los siguientes datos:
   ```
   Repository name: FormacionIzertis365
   Description: Portal Educativo para formación en Microsoft Copilot y Microsoft 365
   Public: ✓ (Selecciona Public)
   ```
3. **NO marques** "Add .gitignore", "Add README" ni "Add license" (ya existen)
4. Haz clic en **"Create repository"**

### PASO 2: Conectar tu Repositorio Local a GitHub

Abre PowerShell y ejecuta estos comandos:

```powershell
cd d:\Personal\Izertis\Formacion\aplicacion_web

# Reemplaza YOUR_USERNAME con tu usuario de GitHub
git remote add origin https://github.com/YOUR_USERNAME/FormacionIzertis365.git

# Renombra la rama a main
git branch -M main

# Haz push al repositorio
git push -u origin main
```

**Nota:** GitHub te pedirá autenticación. Ve al siguiente paso.

### PASO 3: Autenticación - Opción Recomendada (Token)

1. Ve a https://github.com/settings/tokens
2. Haz clic en **"Generate new token"** → **"Generate new token (classic)"**
3. Completa:
   ```
   Token name: FormacionIzertis365
   Expiration: 90 days (o tu preferencia)
   Select scopes: ✓ repo (acceso completo)
   ```
4. Haz clic en **"Generate token"**
5. **COPIA el token** (aparece solo una vez)

### PASO 4: Primer Push a GitHub

Cuando ejecutes `git push -u origin main`:

- **Username:** Tu usuario de GitHub
- **Password:** Pega el token que copiaste en PASO 3

¡Listo! Tu repositorio estará publicado.

### PASO 5: Verificar la Publicación

Abre https://github.com/YOUR_USERNAME/FormacionIzertis365

Deberías ver:
- ✅ Todos tus archivos
- ✅ El README con instrucciones
- ✅ Archivo LICENSE.md
- ✅ Archivo CONTRIBUTING.md

## 📝 Información del Repositorio

**URL:** `https://github.com/YOUR_USERNAME/FormacionIzertis365`

### Archivos principales:
- `README.md` - Instrucciones de instalación
- `requirements.txt` - Dependencias Python
- `manage.py` - Utilidad Django
- `portal_educativo/` - Configuración Django
- `core/` - Aplicación principal
- `LICENSE.md` - Términos de uso
- `CONTRIBUTING.md` - Guía para contribuidores

### Ramas:
- `main` - Rama principal (producción)

### Features:
- 🎨 Interfaz moderna con Bootstrap
- 📚 Gestión de secciones y recursos
- 🔍 Búsqueda avanzada
- 👨‍💼 Panel de administración
- 📱 Diseño responsive

## 🔐 Seguridad

**IMPORTANTE:** Nunca comites:
- Archivos `.env` con credenciales reales
- Bases de datos `db.sqlite3`
- Archivos `__pycache__`
- Carpeta `venv` o `node_modules`

Estos archivos ya están en `.gitignore` ✓

## 📊 Próximas Acciones Recomendadas

Después de publicar, considera:

1. **Crear Issues** para funcionalidades futuras
2. **Agregar Badges** al README (build, coverage, etc.)
3. **Configurar CI/CD** con GitHub Actions
4. **Abrir Discussions** para comunidad
5. **Crear Releases** para versiones estables

## 🆘 Solución de Problemas

### Error: "fatal: remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/FormacionIzertis365.git
```

### Error: "Authentication failed"
- Verifica que usaste un token válido
- El token debe tener permiso `repo`
- El token puede haber expirado

### Error: "403 Forbidden"
- Asegúrate de que el usuario tiene permisos
- Crea un nuevo token si es necesario

## 📧 Contacto

Para soporte con GitHub:
- Documentación: https://docs.github.com
- Issues del proyecto: Abre un Issue en tu repositorio

---

**Versión:** 1.0
**Fecha:** Enero 2026
**Proyecto:** FormacionIzertis365
