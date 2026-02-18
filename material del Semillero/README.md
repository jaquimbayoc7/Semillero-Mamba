# Guía de Configuración - Página Web Semillero Mamba

## 📋 Instrucciones para Configurar el Formulario de Inscripción

La página web incluye un formulario de inscripción que necesita ser configurado para que las inscripciones lleguen al correo de los coordinadores.

### Pasos para Configurar Formspree:

1. **Accede a Formspree**
   - Ve a: https://formspree.io
   - Crea una cuenta o inicia sesión

2. **Crea un Nuevo Formulario**
   - Haz clic en "New Form"
   - Ingresa el correo destino: `julian.quimbayo@corhuila.edu.co`
   - Recibirás un ID único (ej: `mbjqovon`)

3. **Actualiza el HTML**
   - Abre el archivo `material del Semillero/index.html`
   - Busca la línea: `<form action="https://formspree.io/f/xyzpwqvr" method="POST">`
   - Reemplaza `xyzpwqvr` con tu ID único de Formspree
   - Guarda los cambios

4. **Prueba el Formulario**
   - Abre la página en tu navegador
   - Completa el formulario de inscripción
   - Verifica que el correo llegue a la bandeja de entrada

## 📱 Características de la Página Web

✅ **Diseño Minimalista y Responsivo**
- Colores institucionales de CORHUILA (verde y rojo)
- Compatible con dispositivos móviles y desktop

✅ **Secciones Principales**
- Header con navegación
- Sección de bienvenida (Hero)
- Objetivo general
- Objetivos específicos (6 cards)
- Líneas de investigación
- Misión y Visión
- Información de coordinadores
- Formulario de inscripción
- Footer

✅ **Formulario de Inscripción**
Campos incluidos:
- Nombre completo (requerido)
- Correo electrónico (requerido)
- Teléfono
- Programa académico (requerido)
- Semestre (requerido)
- Línea de investigación (requerido)
- Experiencia/Habilidades (opcional)
- Aceptación de términos (requerido)

## 🎨 Colores Utilizados

```css
--primary-green: #1a7c5e    /* Verde principal CORHUILA */
--secondary-green: #2a9d7e  /* Verde secundario */
--accent-red: #d32f2f       /* Rojo de acentos */
--light-bg: #f8f9fa         /* Fondo claro */
```

## 📍 Ubicación de Archivos

```
Semillero-Mamba/
└── material del Semillero/
    ├── index.html          (Página principal)
    └── README.md           (Este archivo)
```

## 🚀 Próximos Pasos

1. Configura Formspree con el correo de inscripciones
2. Despliega la página en un servidor web
3. Comparte el link con los estudiantes
4. Monitorea las inscripciones

## 📧 Coordinadores

- **Ing. Julián Andrés Quimbayo** - julian.quimbayo@corhuila.edu.co
- **Ing. José Miguel Llanos Mosquera** - jose.llanos@corhuila.edu.co

## 🏫 Información Institucional

**Corporación Universitaria del Huila - CORHUILA**
- Sitio web: http://www.corhuila.edu.co
- Programa: Ingeniería de Sistemas
- Semillero: Mamba (Desde 2017)

---

*Documento de apoyo para la gestión del Semillero Mamba - CORHUILA*
