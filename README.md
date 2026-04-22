PDF Booklet Maker
Este código transforma un PDF común en un formato de folleto (booklet). 
Está diseñado para impresoras que imprimen por ambos lados automáticamente.

El programa reordena las páginas para que, al imprimirlas y doblarlas por la mitad, el documento mantenga el orden de lectura correcto.

¿Qué problema resuelve?
Permite crear libros o folletos caseros gratis y sin programas complicados. El archivo final te servirá de guía para que tú mismo voltees las hojas manualmente y logres una impresión profesional.

Características
Orden Automático: Reordena frentes y reversos para que coincidan al doblar.
- Relleno Automático: Agrega hojas en blanco si el total de páginas no es múltiplo de 4.
- Escalado Inteligente: Ajusta y centra las páginas en un lienzo de doble ancho.
- Compatibilidad: Genera un .pdf estándar listo para cualquier impresora.

Estructura del Proyecto
```
├── main.py           # El código principal
├── requirements.txt  # Lista de librerías necesarias
└── README.md         # Estas instrucciones
```

Requisitos
Antes de empezar, necesitas tener en tu equipo:

Python 3.12 o superior.

pip (viene incluido al instalar Python).

Instalación
Para que el programa funcione, necesitamos instalar una herramienta llamada pypdf. Abre tu terminal y escribe:

```
pip install pypdf
```
(O si prefieres usar el archivo de requisitos: ```pip install -r requirements.txt```)

Modo de Uso
Sigue estos pasos en tu terminal o consola:

Descarga el proyecto:

```git clone https://github.com/camilitaaaaaa/Booklet-printing-for-duplex-printers```
Entra a la carpeta:

```cd Booklet-printing-for-duplex-printers```
Ejecuta el programa:
Escribe python main.py seguido del nombre de tu archivo:

```python main.py {mi_archivo.pdf}```
Salida esperada:
```Booklet creado: mi_archivo-booklet.pdf```

Problemas Comunes!
Error: Index out of range: El PDF podría estar protegido con contraseña o estar vacío.

Error: ModuleNotFoundError: No se instaló pypdf. Revisa el paso de Instalación.

Dimensiones extrañas: Si tu PDF tiene páginas de distintos tamaños (ej. una carta y otra oficio), el resultado podría verse algo desalineado.

Notas finales
Ten en consideración que si ejecutas dos veces el mismo archivo .pdf, este se **sobreescribirá**, así que OJO!

Autora
Nombre: Camila Riquelme A.

GitHub: camilitaaaaaa

Licencia
Este proyecto está bajo la Licencia MIT. ¡Eres libre de usarlo y compartirlo!

Para cualquier comentario adicional, no dudes en contactarme! @luz.delitoo en Instagram. 

