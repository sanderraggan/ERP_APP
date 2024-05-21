import streamlit as st
from src.TravelExpense import TravelExpense
def reiseregning_screen():
    st.set_page_config(
        page_title="Reiseregning",
        page_icon="✈️",
    )
    #TEst
    if "authenticated" not in st.session_state:
        st.switch_page("mainpage.py")
    init_session()
    st.header("Registrer Reiseregning")
    reiseregning_form()
    #st.sidebar.header("Registrerte reiseregninger")
    #for k in st.session_state.reiseregninger_stats.keys():
    #    st.sidebar.markdown(k + ": " + str(st.session_state.reiseregninger_stats[k]))
    #if st.button("Hovedside"):
    #    st.switch_page("pages/landingpage.py")


def reiseregning_form():
    with st.form("Registrer reiseregning", clear_on_submit=True):
        navn = st.text_input("Tittel på utlegg")
        dato = st.date_input("Dato for utlegg",format="DD/MM/YYYY")
        sum_nok = st.number_input("Totalsum")
        sum_mva = st.number_input("Sum MVA")
        vedlegg = st.file_uploader("Last opp kopi av kvittering")
        if st.form_submit_button("Send til godkjenning"):
            reiseregning_temp = TravelExpense(navn,dato,sum_nok,sum_mva,vedlegg)
            st.session_state.reiseregninger.append(reiseregning_temp)
            update_stats()
            st.switch_page("pages/landingpage.py")
def update_stats():
    st.session_state.reiseregninger_stats["Antall"] = len(st.session_state.reiseregninger)
    st.session_state.reiseregninger_stats["Totalsum"] = sum(s.get_sum() for s in st.session_state.reiseregninger)

def init_session():
    if "reiseregninger" not in st.session_state:
        st.session_state.reiseregninger = []
    if "reiseregninger_stats" not in st.session_state:
        st.session_state.reiseregninger_stats = {}

if __name__ == "__main__":
    reiseregning_screen()