import os
import urllib.request

# Crear la carpeta "img" si no existe
os.makedirs("img", exist_ok=True)

# Diccionario con los nombres de archivo y las URLs originales
imagenes = {
    "logo.png": "https://http2.mlstatic.com/frontend-assets/ml-web-navigation/ui-navigation/6.6.92/mercadolibre/logo__large_plus.png",
    "meli-plus.webp": "https://http2.mlstatic.com/D_NQ_921810-MLA75591965416_042024-OO.webp",
    "banner-hero.webp": "https://http2.mlstatic.com/D_NQ_782069-MLA75591965420_042024-F.webp",
    "producto-1.webp": "https://http2.mlstatic.com/D_NQ_NP_2X_704044-MLA74805790425_022024-F.webp",
    "producto-2.webp": "https://http2.mlstatic.com/D_NQ_NP_2X_910793-MLA74681650630_022024-F.webp"
}

# Configurar un User-Agent (Disfrazar el script como Google Chrome) para evitar el Error 403
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')]
urllib.request.install_opener(opener)

print("Descargando imágenes...")

for nombre_archivo, url in imagenes.items():
    ruta_destino = os.path.join("img", nombre_archivo)
    try:
        urllib.request.urlretrieve(url, ruta_destino)
        print(f"✅ {nombre_archivo} descargado con éxito.")
    except Exception as e:
        print(f"❌ Error al descargar {nombre_archivo}: {e}")

print("\n¡Listo! Abre tu archivo mercadolibre.html y ya deberías ver las imágenes.")