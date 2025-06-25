import streamlit as st
from agent_utils import getSearchResults

st.set_page_config(page_title="Erklären", page_icon='📜')

st.title("Welcome to Erklären")
st.markdown('~ Your AI Explainer')
st.badge('Based on llama-3.1')
query = st.text_input("Enter your query:",placeholder="e.g. What is the story behind Bermuda Triangle?")
st.caption("Instead of just typing a few keywords, enter a full sentence describing exactly what you're looking for")

if st.button("Search"):
    if query.strip():
        with st.spinner("Searching"):
            response = getSearchResults(query)
        st.success("☑️ HERE WE GO:")
        st.write(response)
    else :
        st.warning("👎Please enter a query before searching")

st.markdown(
    """
    <footer style="color: #181818">
       <p>© 2025 SIDDHESHUMESHSARANG</p>
    </footer>
    """,
    unsafe_allow_html=True
)