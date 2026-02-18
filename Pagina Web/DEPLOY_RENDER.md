# 🚀 Guía de Despliegue en Render

## Pasos para Desplegar en Render.com

### 1. Crear una Cuenta
- Ve a [render.com](https://render.com)
- Crea una cuenta con GitHub (recomendado)
- Conecta tu repositorio

### 2. Crear un Nuevo Servicio
- Click en "New +"
- Selecciona "Static Site"
- Conecta tu repositorio `Semillero-Mamba`
- Selecciona la rama `master`

### 3. Configurar el Servicio
**Build Command:** (dejar vacío)
**Publish Directory:** `Pagina Web`

### 4. Deploy
- Render detectará automáticamente los cambios en GitHub
- El sitio estará disponible en: `https://semillero-mamba-xxxx.onrender.com`

---

## 📋 Checklist de Optimización

### ✅ Performance
- [ ] Imágenes optimizadas (< 100KB cada una)
- [ ] CSS minificado
- [ ] Lazy loading habilitado
- [ ] Cache headers configurados

### ✅ SEO
- [ ] Meta tags descriptivos ✓
- [ ] Títulos únicos por página ✓
- [ ] Descriptions útiles ✓
- [ ] Crear sitemap.xml
- [ ] Crear robots.txt

### ✅ Seguridad
- [ ] HTTPS habilitado (Render lo hace automático)
- [ ] No grabar credenciales en código
- [ ] Validar formularios server-side (si aplica)

### ✅ Responsive Design
- [ ] Mobile first ✓
- [ ] Tablet compatible ✓
- [ ] Desktop optimizado ✓
- [ ] Probar en navegadores principales

---

## 🎨 Mejoras Sugeridas para el Sitio

### 1. **Optimizar Imágenes**
```bash
# Comprimir fotos de coordinadores
# Usar TinyPNG o ImageOptim
# Meta: < 50KB por foto
```

### 2. **Agregar sitemap.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://semillero-mamba.onrender.com/</loc>
    <lastmod>2026-02-18</lastmod>
    <changefreq>weekly</changefreq>
  </url>
  <url>
    <loc>https://semillero-mamba.onrender.com/blog-como-comenzamos.html</loc>
    <lastmod>2026-02-18</lastmod>
    <changefreq>monthly</changefreq>
  </url>
</urlset>
```

### 3. **Agregar robots.txt**
```text
User-agent: *
Allow: /
Sitemap: https://semillero-mamba.onrender.com/sitemap.xml
```

### 4. **Analytics**
```html
<!-- Agregar Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### 5. **Open Graph Meta Tags**
```html
<meta property="og:title" content="Semillero Mamba - CORHUILA"/>
<meta property="og:description" content="Espacio de investigación en desarrollo de software, calidad, análisis de datos y arquitectura"/>
<meta property="og:image" content="https://tudominio.com/Logo/Logo.png"/>
<meta property="og:url" content="https://tudominio.com"/>
```

---

## 🔧 Comandos Útiles

### Crear sitemap.xml
```bash
# Instalar generador
npm install -g sitemap-generator-cli

# Generar después del deploy
sitemap -u https://tu-sitio.onrender.com -m /path/to/public
```

### Comprimir imágenes
```bash
# Usando ImageMagick
convert coordinador.jpg -quality 85 coordinador-optimized.jpg
```

---

## 📊 Métricas a Monitorear

- **Lighthouse Score**: Meta 90+
- **Core Web Vitals**: Good
- **Page Load Time**: < 3 segundos
- **Mobile Usability**: Sin errores

---

## 🌐 Dominio Personalizado

1. En Render Dashboard → Settings
2. "Custom Domain"
3. Apunta tu DNS al servidor Render
4. SSL se configura automáticamente

---

## 💡 Tips Finales

✅ Mantén el sitio simple y rápido
✅ Actualiza contenido regularmente (Blog)
✅ Monitorea analytics
✅ Responde comentarios en WhatsApp
✅ Haz backups del repositorio

---

**Fecha de Creación:** 18 Feb 2026
**Versión:** 1.0
**Último Update:** Configuración inicial
