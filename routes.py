from flask import Blueprint, render_template, request, redirect, url_for
from controllers import obtener_productos, crear_producto, eliminar_producto

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    productos = obtener_productos()
    return render_template("index.html", productos=productos)


@bp.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    precio = float(request.form["precio"])
    stock = int(request.form["stock"])
    crear_producto(nombre, precio, stock)
    return redirect(url_for("main.index"))


@bp.route("/eliminar/<int:id>")
def eliminar(id):
    eliminar_producto(id)
    return redirect(url_for("main.index"))
