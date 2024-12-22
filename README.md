# 🌍 SNIA Backend

**SNIA Backend** es el backend del Sistema Nacional de Información Ambiental (SNIA) para el Ministerio de Medio ambiente y Agua, desarrollado con **Django REST Framework** para proporcionar una API robusta que facilite la gestión y consulta de datos ambientales.

---

## 🚀 Características principales

- ✅ **API RESTful** con Django REST Framework.
- 🔐 **Autenticación segura** y control de acceso basado en roles.
- 🗂️ Modular y escalable para fácil mantenimiento.
- 📊 **Endpoints optimizados** para la gestión de información ambiental.

---

## 📋 Requisitos previos

Antes de comenzar, asegúrate de tener instalados:

- **Python 3.8 o superior**
- **Django 5.x**
- **PostgreSQL** 
- **pip** para manejar paquetes

---

## ⚙️ Instalación y configuración

### 1️⃣ Clonar el repositorio
```bash
git clone https://gitlab.mmaya.gob.bo/g-snia/snia-backend.git
cd snia-backend
```

### 2️⃣ Crear un entorno virtual y activarlo
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar las variables de entorno
- Copia el archivo `.env.example` como `.env`:
```bash
cp .env.example .env
```
- Edita el archivo `.env` y configura los valores necesarios.

### 5️⃣ Ejecutar el servidor

```bash
python manage.py runserver
```
- La API estará disponible en: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---
### 6️⃣ Si tienes error de No module named 'pkg_resources'
```bash
pip uninstall setuptools
pip install setuptools

python3 -m pip install --upgrade setuptools
sudo apt update
sudo apt install python3-setuptools 
```
### Ejecuta el servidor
```bash
python manage.py runserver
```

## 🛠️ Uso de la API

### 📄 Documentación interactiva
- Visita **[http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)** para explorar la API si tienes Swagger instalado.

---

## 🧪 Pruebas

Ejecuta las pruebas con:
```bash
python manage.py test
```

---

## 🤝 Contribuciones

¡Contribuciones! Sigue estos pasos:

1. Realiza un fork del repositorio.
2. Crea una nueva rama con tus cambios:
   ```bash
   git checkout -b mi-rama
   ```
3. Haz un commit:
   ```bash
   git commit -m "Descripción del cambio"
   ```
4. Haz push a tu rama:
   ```bash
   git push origin mi-rama
   ```
5. Abre un **Merge Request** en GitLab.

---

## 📝 Licencia

Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT).

---

## 📧 Contacto

Si tienes dudas o necesitas más información, contacta al equipo del proyecto liz.lemus@mmaya.gob.bo