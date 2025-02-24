import streamlit as st
def render_header():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("🏠 Descubre Madrid a través de Airbnb")
        st.markdown("""
        Bienvenido al análisis oficial de alojamientos turísticos de Madrid.
        Explora nuestra vibrante ciudad a través de los datos de Airbnb.
        
        *Una iniciativa del Departamento de Turismo de Madrid.*
        """)
    st.markdown("---")

import streamlit as st

def render_footer():
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666;'>
            <p>Desarrollado por el Departamento de Turismo de Madrid | © 2025 Ayuntamiento de Madrid</p>
            <p>¿Necesitas más información? Visita
               <a href="https://turismo.madrid.es">turismo.madrid.es</a> o
               contacta con nuestras oficinas de turismo.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    