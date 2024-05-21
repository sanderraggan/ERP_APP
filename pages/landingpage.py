import streamlit as st

def landingpage():
    st.set_page_config(
            page_title="Hjem",
            page_icon="🙌",
        )
    st.header("POWERKJØP PORTAL")
    if st.button("Registrer utlegg"):
        st.switch_page("pages/expencepage.py")
    if st.button("Se utlegg"):
        st.switch_page("pages/statspage.py")

if __name__ == "__main__":
    landingpage()