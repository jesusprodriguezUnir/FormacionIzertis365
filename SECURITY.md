# Seguridad de GitHub

## Reportar vulnerabilidades de seguridad

Por favor, **NO** abras un issue público para reportar vulnerabilidades de seguridad.

En su lugar, envía un email a:
- **jesus.productioncontrol@gmail.com**

Por favor, incluye:
- Descripción de la vulnerabilidad
- Pasos para reproducirla
- Posible impacto
- Sugerencia de solución (si la tienes)

Nos comprometeremos a:
- Reconocer tu reporte dentro de 24 horas
- Mantener confidencialidad hasta que se publique el fix
- Darte crédito por el descubrimiento (si lo deseas)

## Políticas de Seguridad

### Dependencias
- Mantenemos las dependencias actualizadas
- Ejecutamos Dependabot para alertas de seguridad
- Realizamos auditorías regulares con `pip audit`

### Prácticas
- No guardamos datos sensibles en el repositorio
- Variables de entorno en `.env` (no en git)
- Validación y sanitización de entrada
- Protección CSRF habilitada

---

Gracias por ayudar a mantener seguro el Portal Educativo.
