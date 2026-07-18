from controllers.db import get_connection


def obtener_productos():
    conn = get_connection()
    productos = conn.execute("SELECT * FROM productos").fetchall()
    conn.close()
    return [dict(p) for p in productos]


def obtener_producto(producto_id):
    conn = get_connection()
    producto = conn.execute(
        "SELECT * FROM productos WHERE id = ?", (producto_id,)
    ).fetchone()
    conn.close()
    return dict(producto) if producto else None


def crear_producto(nombre, precio, stock):
    conn = get_connection()
    conn.execute(
        "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
        (nombre, precio, stock),
    )
    conn.commit()
    conn.close()


def eliminar_producto(producto_id):
    conn = get_connection()
    conn.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
    conn.commit()
    conn.close()
