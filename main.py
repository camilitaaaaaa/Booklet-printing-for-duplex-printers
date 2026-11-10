"""
    Este código transforma un PDF común en un formato de folleto (booklet).
    Está diseñado para impresoras que imprimen por ambos lados automáticamente.
    A.K.A Las impresors crisol de la u <3

    Al imprimir: doble cara, horizontal, voltear por el BORDE CORTO.
    Uso:  python booklet.py documento.pdf
"""

import sys
from pypdf import PdfReader, PdfWriter, Transformation
import os 

GIRAR_REVERSO = False

def hacer_booklet_pro(input_pdf): # función que hará TODO lol
    reader = PdfReader(input_pdf) # módulo para leer 
    writer = PdfWriter() # módulo para escribir

    paginas = list(reader.pages) # acceder a las páginas del documento

    # si la cantidad de hojas no es múltiplo de 4, 
    # se insertan páginas en blanco al final del documento.
    while len(paginas) % 4 != 0:
        paginas.append(None)

    # total = cantidad de páginas 
    total = len(paginas)

    # devuelve: ("documento", ".pdf")
    base, _ = os.path.splitext(input_pdf)
    output_pdf = f"{base}-booklet-duplex.pdf"

    # (forma pares de páginas para imprimir un documento como un booklet)
    for i in range(0, total // 2, 2):
        pares = [
            (paginas[total - 1 - i], paginas[i]),         # frente
            (paginas[i + 1], paginas[total - 2 - i])      # reverso
        ]

        for idx, (izq, der) in enumerate(pares):

            ref = izq or der or paginas[0]
            w = float(ref.mediabox.width)
            h = float(ref.mediabox.height)

            # Auto paper size (doble ancho)
            nueva = writer.add_blank_page(width=w * 2, height=h)

            def colocar(pagina, offset_x, rotar=False):
                if pagina is None:
                    return

                pw = float(pagina.mediabox.width)
                ph = float(pagina.mediabox.height)

                escala = min(w / pw, h / ph)

                tx = offset_x + (w - pw * escala) / 2
                ty = (h - ph * escala) / 2

                t = Transformation()

                if rotar:
                    # (solo si GIRAR_REVERSO = True) gira la página 180°
                    t = t.rotate(180)
                    tx = offset_x + w - (w - pw * escala) / 2
                    ty = h - (h - ph * escala) / 2

                t = t.scale(escala).translate(tx, ty)

                nueva.merge_transformed_page(pagina, t)

            # ANTES: es_reverso = (idx == 1)  -> giraba SIEMPRE los reversos y salían al revés
            es_reverso = GIRAR_REVERSO and (idx == 1)

            colocar(izq, 0, rotar=es_reverso)
            colocar(der, w, rotar=es_reverso)

    # esto escribe un nuevo pdf en el formato booklet
    with open(output_pdf, "wb") as f:
        writer.write(f)

    # imprime un mensaje en la consola sobre que el booklet está listo
    print(f" Booklet creado: {output_pdf}")


if __name__ == "__main__":
    # si olvidas escribir el nombre del PDF, avisa en vez de dar error
    if len(sys.argv) < 2:
        print("Uso: python booklet.py documento.pdf")
        sys.exit(1)
    hacer_booklet_pro(sys.argv[1])
