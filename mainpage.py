import streamlit as st

def mainpage():
    st.set_page_config(
        page_title="Login",
        page_icon="🚦",
    )
    st.title("POWERKJØP PORTALEN v.1")
    init_session()
    if not st.session_state.authenticated:
        with st.container(border=True):
            st.session_state.navn = st.text_input("Navn", disabled=st.session_state.authenticated)
            st.text_input("Passord", type="password", disabled=st.session_state.authenticated)
            if st.button("Logg inn", disabled=st.session_state.authenticated):
                st.session_state.authenticated = True
                st.write("Hei " +str(st.session_state.navn)+"! Du er nå logget inn 😊")
                st.switch_page("pages/landingpage.py")

    #st.sidebar.success("Velg sider")

def init_session():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

if __name__ == "__main__":
    mainpage()
