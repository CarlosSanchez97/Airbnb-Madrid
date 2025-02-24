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