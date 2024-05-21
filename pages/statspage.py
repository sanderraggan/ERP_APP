import streamlit as st

def stats():
    st.set_page_config(
        page_title="Stats",
        page_icon="📊",
    )
    st.header("Dine reiseregninger")
    if "reiseregninger" in st.session_state and len(st.session_state.reiseregninger)>0:
        with st.container(border=True):
            st.header("Totaloversikt")
            for k in st.session_state.reiseregninger_stats.keys():
                st.markdown(k + ": " + str(st.session_state.reiseregninger_stats[k]))
    else:
        st.write("Du har ikke registrert noen utlegg enda😊")

    if st.button("Hovedside"):
        st.switch_page("pages/landingpage.py")

if __name__ == "__main__":
    stats()

