import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

def clear_registration_form():
    st.session_state.register_username = ""
    st.session_state.register_email = ""
    st.session_state.register_password = ""
    st.session_state.register_role = "User"

def register_user(
    username: str,
    email: str,
    password: str,
    role: str,
) -> dict:
    response = requests.post(
        f"{API_BASE_URL}/register",
        json={
            "username": username,
            "email": email,
            "password": password,
            "role": role,
        },
    )

    response.raise_for_status()

    return response.json()


def login_user(
    username: str,
    password: str,
) -> dict:
    response = requests.post(
        f"{API_BASE_URL}/login",
        json={
            "username": username,
            "password": password,
        },
    )

    response.raise_for_status()

    return response.json()


def test_protected_endpoint(token: str) -> dict:
    response = requests.get(
        f"{API_BASE_URL}/protected",
        params={
            "token": token,
        },
    )

    response.raise_for_status()

    return response.json()


def test_admin_endpoint(token: str) -> dict:
    response = requests.get(
        f"{API_BASE_URL}/admin",
        params={
            "token": token,
        },
    )

    response.raise_for_status()

    return response.json()


st.set_page_config(
    page_title="Enterprise Access Management Portal",
    page_icon="🔐",
    layout="wide",
)

if "access_token" not in st.session_state:
    st.session_state.access_token = None

if "current_user" not in st.session_state:
    st.session_state.current_user = None

if "current_role" not in st.session_state:
    st.session_state.current_role = None

if "register_username" not in st.session_state:
    st.session_state.register_username = ""

if "register_email" not in st.session_state:
    st.session_state.register_email = ""

if "register_password" not in st.session_state:
    st.session_state.register_password = ""

if "login_username" not in st.session_state:
    st.session_state.login_username = ""

if "login_password" not in st.session_state:
    st.session_state.login_password = ""

if "register_role" not in st.session_state:
    st.session_state.register_role = "User"

st.title("🔐 Enterprise Access Management Portal")

st.markdown(
    """
    Authentication, Authorization, and Role-Based Access Control Dashboard
    """
)

col1, col2, col3 = st.columns(3)

with col1:

    authentication_status = (
        "Authenticated"
        if st.session_state.access_token
        else "Not Logged In"
    )

    st.metric(
        "Authentication",
        authentication_status,
    )

with col2:

    token_status = (
        "Active"
        if st.session_state.access_token
        else "No Token"
    )

    st.metric(
        "JWT Status",
        token_status,
    )

with col3:

    role_status = (
        st.session_state.current_role
        if st.session_state.current_role
        else "Unknown"
    )

    st.metric(
        "Current Role",
        role_status,
    )

st.divider()

tab1, tab2, tab3 = st.tabs(
    [
        "Register User",
        "Login",
        "Access Testing",
    ]
)

with tab1:

    st.subheader("User Registration")

    username = st.text_input(
        "Username",
        key="register_username",
    )

    email = st.text_input(
        "Email",
        key="register_email",
    )

    password = st.text_input(
        "Password",
        type="password",
        key="register_password",
    )

    role = st.selectbox(
        "Role",
        [
            "User",
            "Manager",
            "Admin",
        ],
        key="register_role",
    )

    if st.button("Register User"):
        try:
            result = register_user(
                username=username,
                email=email,
                password=password,
                role=role,
            )

            st.success("User registered successfully.")
            st.json(result)

        except requests.exceptions.HTTPError as error:

            error_detail = error.response.json().get(
                "detail",
                "Registration failed.",
            )

            st.error(error_detail)

        except Exception as error:
            st.error(f"Registration failed: {error}")

    st.button(
        "Clear Registration Form",
        on_click=clear_registration_form,
    )

with tab2:

    st.subheader("User Login")

    login_username = st.text_input(
        "Username",
        key="login_username",
    )

    login_password = st.text_input(
        "Password",
        type="password",
        key="login_password",
    )

    if st.button("Login"):
        try:
            result = login_user(
                username=login_username,
                password=login_password,
            )

            st.session_state.access_token = result["access_token"]

            protected_result = test_protected_endpoint(
                result["access_token"]
            )

            st.session_state.current_user = protected_result["user"]
            st.session_state.current_role = protected_result["role"]

            st.success("Login successful.")
            st.json(result)

            st.rerun()

        except Exception as error:
            st.error(f"Login failed: {error}")
with tab3:

    st.subheader("Access Testing")

    if st.session_state.access_token:
        st.success("Authenticated session active.")

        if st.session_state.current_user:
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Current User",
                    st.session_state.current_user,
                )

            with col2:
                st.metric(
                    "Current Role",
                    st.session_state.current_role,
                )

        st.text_area(
            "JWT Access Token",
            value=st.session_state.access_token,
            height=120,
        )

        if st.button("Test Protected Endpoint"):
            try:
                result = test_protected_endpoint(
                    st.session_state.access_token
                )

                st.session_state.current_user = result["user"]
                st.session_state.current_role = result["role"]

                st.success("Protected access granted.")
                st.json(result)

            except Exception as error:
                st.error(f"Protected access failed: {error}")

        if st.button("Test Admin Endpoint"):
            try:
                result = test_admin_endpoint(
                    st.session_state.access_token
                )

                st.success("Admin access granted.")
                st.json(result)

            except Exception as error:
                st.error(f"Admin access failed: {error}")

        if st.button("Logout / Clear Session"):
            st.session_state.access_token = None
            st.session_state.current_user = None
            st.session_state.current_role = None
            st.rerun()

    else:
        st.warning("Please log in before testing protected access.")