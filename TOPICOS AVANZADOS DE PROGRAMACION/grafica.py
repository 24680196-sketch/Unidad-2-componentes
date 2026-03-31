import matplotlib.pyplot as plt
import flet as ft
import random
import io
import base64


# Convertir figura a base64
def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    img = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)
    return img


# -------- GRAFICA DE BARRAS --------
def generar_grafica_barras():
    productos = ["A", "B", "C", "D"]
    ventas = [15, 25, 35, 10]

    fig, ax = plt.subplots(figsize=(4,3))
    ax.bar(productos, ventas)
    ax.set_title("Ventas por Producto")

    return fig_to_base64(fig)


# -------- GRAFICA DE LINEAS --------
def generar_grafica_lineas():
    meses = ["Ene","Feb","Mar","Abr","May"]
    rendimiento = [10,20,15,18,25]

    fig, ax = plt.subplots(figsize=(4,3))
    ax.plot(meses, rendimiento, marker="o")
    ax.set_title("Tendencia de Rendimiento")

    return fig_to_base64(fig)


# -------- GRAFICA DE PUNTOS --------
def generar_grafica_puntos():
    x = [1,2,3,4,5,6,7]
    y = [5,7,3,8,4,9,6]

    fig, ax = plt.subplots(figsize=(4,3))
    ax.plot(x, y, 'ro')
    ax.set_title("Gráfica de Puntos")

    return fig_to_base64(fig)


# -------- GRAFICA DE PASTEL --------
def generar_grafica_pastel():
    categorias = ["Tecnología", "Ropa", "Alimentos", "Otros"]
    valores = [40, 25, 20, 15]

    fig, ax = plt.subplots(figsize=(4,3))
    ax.pie(valores, labels=categorias, autopct='%1.1f%%')
    ax.set_title("Distribución de Ventas")

    return fig_to_base64(fig)


# -------- INTERFAZ --------
def main(page: ft.Page):

    page.title = "Dashboard TAP - Gráficas"
    page.scroll = "auto"

    header = ft.Text(
        "Dashboard de Visualización",
        size=25,
        weight="bold"
    )

    grid = ft.GridView(
        expand=True,
        runs_count=2,
        spacing=20,
        run_spacing=20
    )

    graficas = [
        generar_grafica_barras(),
        generar_grafica_lineas(),
        generar_grafica_puntos(),
        generar_grafica_pastel()
    ]

    for g in graficas:
        grid.controls.append(ft.Image(src=f"data:image/png;base64,{g}"))

    page.add(header, grid)


ft.app(target=main)