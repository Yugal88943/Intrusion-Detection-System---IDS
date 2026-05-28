import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# Load Saved Files
# -----------------------------

lr_model = joblib.load("lr_model.pkl")
ann_model = joblib.load("ann_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# -----------------------------
# Title
# -----------------------------

st.title("Intrusion Detection System")

st.write("Predict whether network traffic is Normal or an Attack")

# -----------------------------
# User Inputs
# -----------------------------

protocol_type = st.selectbox(
    "Protocol Type",
    ["tcp", "udp", "icmp"]
)

service = st.selectbox(
    "Service",
    ["http", "ftp_data", "private", "smtp", "domain_u", "other"]
)

flag = st.selectbox(
    "Flag",
    ["SF", "S0", "REJ"]
)

src_bytes = st.number_input("Source Bytes", min_value=0)

dst_bytes = st.number_input("Destination Bytes", min_value=0)

count = st.number_input("Count", min_value=0)

srv_count = st.number_input("Service Count", min_value=0)

# -----------------------------
# Model Selection
# -----------------------------

model_choice = st.radio(
    "Choose Model",
    ["Logistic Regression", "ANN"]
)

# -----------------------------
# Predict Button
# -----------------------------

if st.button("Predict"):

    # Create input dictionary
    input_data = {
        'duration': 0,
        'src_bytes': src_bytes,
        'dst_bytes': dst_bytes,
        'land': 0,
        'wrong_fragment': 0,
        'urgent': 0,
        'hot': 0,
        'num_failed_logins': 0,
        'logged_in': 1,
        'num_compromised': 0,
        'root_shell': 0,
        'su_attempted': 0,
        'num_root': 0,
        'num_file_creations': 0,
        'num_shells': 0,
        'num_access_files': 0,
        'num_outbound_cmds': 0,
        'is_host_login': 0,
        'is_guest_login': 0,
        'count': count,
        'srv_count': srv_count,
        'serror_rate': 0,
        'srv_serror_rate': 0,
        'rerror_rate': 0,
        'srv_rerror_rate': 0,
        'same_srv_rate': 0,
        'diff_srv_rate': 0,
        'srv_diff_host_rate': 0,
        'dst_host_count': 0,
        'dst_host_srv_count': 0,
        'dst_host_same_srv_rate': 0,
        'dst_host_diff_srv_rate': 0,
        'dst_host_same_src_port_rate': 0,
        'dst_host_srv_diff_host_rate': 0,
        'dst_host_serror_rate': 0,
        'dst_host_srv_serror_rate': 0,
        'dst_host_rerror_rate': 0,
        'dst_host_srv_rerror_rate': 0,
        'protocol_type': protocol_type,
        'service': service,
        'flag': flag
    }

    # Convert to dataframe
    input_df = pd.DataFrame([input_data])

    # Apply one-hot encoding
    input_df = pd.get_dummies(
        input_df,
        columns=['protocol_type', 'service', 'flag']
    )

    # Match training columns
    input_df = input_df.reindex(
        columns=columns,
        fill_value=0
    )

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Select model
    if model_choice == "Logistic Regression":
        prediction = lr_model.predict(input_scaled)

    else:
        prediction = ann_model.predict(input_scaled)

    # Show result
    if prediction[0] == 1:
        st.error("Attack Detected")
    else:
        st.success("Normal Traffic")