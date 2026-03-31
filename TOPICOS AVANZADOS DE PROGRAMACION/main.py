import flet as ft

# ----- Datos de productos -----
productos = [
    {
        "id": 1,
        "nombre": "Laptop",
        "descripcion": "Laptop para trabajo y estudio",
        "precio": 15000,
        "ruta_imagen": "assets/laptop.png"
    },
    {
        "id": 2,
        "nombre": "Mouse",
        "descripcion": "Mouse inalámbrico",
        "precio": 300,
        "ruta_imagen": "assets/mouse.png"
    },
    {
        "id": 3,
        "nombre": "Teclado",
        "descripcion": "Teclado mecánico",
        "precio": 800,
        "ruta_imagen": "assets/teclado.png"
    },
    {
        "id": 4,
        "nombre": "Audífonos",
        "descripcion": "Audífonos bluetooth",
        "precio": 1200,
        "ruta_imagen": "assets/audifonos.png"
    },
    {
        "id": 5,
        "nombre": "Monitor",
        "descripcion": "Monitor Full HD",
        "precio": 4000,
        "ruta_imagen": "assets/monitor.png"
    }
]


# ----- Componente reutilizable -----
class ProductCard(ft.Container):

    def __init__(self, nombre, descripcion, precio, imagen):

        super().__init__()

        self.width = 250
        self.padding = 10
        self.border_radius = 10
        self.bgcolor = "white"
        self.shadow = ft.BoxShadow(blur_radius=10, color="black26")

        self.content = ft.Column(
            [
                # Imagen corregida
                ft.Image(src=imagen, height=150, fit="contain"),

                ft.Text(nombre, size=18, weight="bold"),

                ft.Text(descripcion, size=12),

                ft.Text(f"${precio}", size=16, color="green"),

                ft.Row(
                    [
                        ft.IconButton(icon=ft.Icons.FAVORITE_BORDER),
                        ft.ElevatedButton("Agregar al carrito")
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ]
        )


# ----- Interfaz principal -----
def main(page: ft.Page):

    page.title = "Tienda Tecnológica"
    page.bgcolor = "#f5f5f5"
    page.scroll = "auto"

    tarjetas = []

    for producto in productos:
        tarjeta = ProductCard(
            producto["nombre"],
            producto["descripcion"],
            producto["precio"],
            producto["ruta_imagen"]
        )
        tarjetas.append(tarjeta)

    page.add(
        ft.Column(
            [
                ft.Text(
                    "CATÁLOGO DE PRODUCTOS TECNOLÓGICOS",
                    size=30,
                    weight="bold"
                ),

                ft.Row(
                    tarjetas,
                    wrap=True,
                    spacing=20
                )
            ]
        )
    )


ft.app(target=main)