import streamlit as st
from sqlalchemy import create_engine

connection_string = st.secrets["database"]["DB_CONNECTION_STRING"]

engine = create_engine(connection_string)