import streamlit as st
from nave import Nave
from naveDB import NaveDB
from planetas import Planeta
from planetasDB import PlanetaDB
from astronauta import Astronauta, Rango
from astronautaDB import AstronautaDB

nave_db = NaveDB()
planeta_db = PlanetaDB()
astro_db = AstronautaDB()

def naves_a_objetos(filas):
    lista = []
    for fila in filas:
        nave = Nave(fila[1], fila[2], fila[3])
        nave.id = fila[0]
        lista.append(nave)
    return lista


def opciones_naves():
    naves = nave_db.query_read_all_naves() or []
    return {fila[0]: fila[1] for fila in naves}


def texto_o_default(valor, default="—"):
    return valor if valor not in (None, "") else default

def hangar_naves():
    st.header("Hangar de Naves")

    naves = naves_a_objetos(nave_db.query_read_all_naves() or [])

    modelos = sorted({n.modelo for n in naves if n.modelo})
    filtro = st.selectbox("Filtrar por modelo", ["Todos"] + modelos)
    if filtro != "Todos":
        naves = [n for n in naves if n.modelo == filtro]

    if not naves:
        st.info("No hay naves cargadas.")
    for n in naves:
        with st.expander(f"#{n.id} · {n.nombre_nave}"):
            st.write(n.obtener_informacion())
            es_pesada = n.capacidad_pasajeros >= 10
            st.write("Carga pesada" if es_pesada else "Carga estándar")
            if st.button("Eliminar nave", key=f"del_nave_{n.id}"):
                nave_db.query_delete_nave((n.id,))
                st.rerun()

    st.divider()

    st.subheader("Registrar nueva nave")
    with st.form("form_nave", clear_on_submit=True):
        nombre = st.text_input("Nombre de la nave")
        modelo = st.text_input("Modelo")
        capacidad = st.number_input("Capacidad de pasajeros", min_value=0, step=1)
        enviar = st.form_submit_button("Guardar nave")

        if enviar:
            if not nombre.strip():
                st.error("El nombre de la nave es obligatorio.")
            elif capacidad < 0:
                st.error("La capacidad no puede ser negativa.")
            else:
                nueva = Nave(nombre.strip(), modelo.strip(), int(capacidad))
                nave_db.query_create_nave(nueva)
                st.success(f"Nave '{nombre}' registrada correctamente.")
                st.rerun()


def panel_astronautas():
    st.header("Panel de Control de Astronautas")

    filas = astro_db.query_read_astronautas_con_nave() or []
    rangos = [r.name for r in Rango]
    filtro = st.selectbox("Filtrar por rango", ["Todos"] + rangos)
    if filtro != "Todos":
        filas = [f for f in filas if f[3] == filtro]

    if not filas:
        st.info("No hay astronautas cargados.")
    for f in filas:
        with st.expander(f"#{f[0]} · {f[1]} {f[2]} ({f[3]})"):
            st.write(f"Horas de vuelo: {f[4]}")
            st.write(f"Nave asignada: {texto_o_default(f[5])}")
            veterano = (f[4] or 0) >= Astronauta.VET_HORAS_DE_VUELO
            st.write("Estado: 🎖️ Veterano" if veterano else "Estado: Novato")
            if st.button("Eliminar astronauta", key=f"del_astro_{f[0]}"):
                astro_db.query_delete_astronauta((f[0],))
                st.rerun()

    st.divider()

    st.subheader("Registrar nuevo astronauta")
    naves = opciones_naves()
    with st.form("form_astro", clear_on_submit=True):
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        rango_sel = st.selectbox("Rango", [r.name for r in Rango])
        horas = st.number_input("Horas de vuelo", min_value=0, step=1)
        nave_id = None
        if naves:
            nave_id = st.selectbox(
                "Asignar a nave",
                options=list(naves.keys()),
                format_func=lambda i: naves[i],
            )
        else:
            st.caption("No hay naves para asignar todavía.")
        enviar = st.form_submit_button("Guardar astronauta")

        if enviar:
            if not nombre.strip() or not apellido.strip():
                st.error("Nombre y apellido son obligatorios.")
            elif horas < 0:
                st.error("Las horas de vuelo no pueden ser negativas.")
            else:
                nuevo = Astronauta(
                    nombre.strip(), apellido.strip(),
                    Rango[rango_sel], int(horas), nave_id
                )
                astro_db.query_create_astronauta(nuevo)
                st.success(f"Astronauta '{nombre} {apellido}' registrado.")
                st.rerun()

def mapa_estelar():
    st.header("Mapa Estelar (Planetas)")

    filas = planeta_db.query_read_all_planetas() or []
    atmosferas = sorted({f[3] for f in filas if f[3]})
    filtro = st.selectbox("Filtrar por atmósfera", ["Todas"] + atmosferas)
    if filtro != "Todas":
        filas = [f for f in filas if f[3] == filtro]

    if not filas:
        st.info("No hay planetas cargados.")
    for f in filas:
        with st.expander(f"#{f[0]} · {f[1]}"):
            st.write(f"Distancia al Sol: {f[2]} UA")
            st.write(f"Atmósfera: {texto_o_default(f[3])}")
            if st.button("Eliminar planeta", key=f"del_plan_{f[0]}"):
                planeta_db.query_delete_planeta((f[0],))
                st.rerun()

    st.divider()

    st.subheader("Registrar nuevo planeta")
    naves = opciones_naves()
    with st.form("form_planeta", clear_on_submit=True):
        nombre = st.text_input("Nombre del planeta")
        distancia = st.number_input("Distancia al Sol (UA)", min_value=0.0, step=0.1)
        atmosfera = st.text_input("Tipo de atmósfera")
        nave_id = None
        if naves:
            nave_id = st.selectbox(
                "Nave asignada",
                options=list(naves.keys()),
                format_func=lambda i: naves[i],
            )
        enviar = st.form_submit_button("Guardar planeta")

        if enviar:
            if not nombre.strip():
                st.error("El nombre del planeta es obligatorio.")
            elif distancia <= 0:
                st.error("La distancia al Sol debe ser mayor a cero.")
            else:
                nuevo = Planeta(nombre.strip(), float(distancia),
                                atmosfera.strip(), nave_id)
                planeta_db.query_create_planeta(nuevo)
                st.success(f"Planeta '{nombre}' registrado.")
                st.rerun()

def main():
    st.set_page_config(page_title="Galactic Pioneer Command", page_icon="🛰️")
    st.title("Galactic Pioneer Command")
    st.caption("ORT Space Agency — Sistema de gestión de la flota")

    seccion = st.sidebar.radio(
        "Navegación",
        ["Astronautas", "Naves", "Planetas"],
    )

    if seccion == "Astronautas":
        panel_astronautas()
    elif seccion == "Naves":
        hangar_naves()
    else:
        mapa_estelar()


if __name__ == "__main__":
    main()
