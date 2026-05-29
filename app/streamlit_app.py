import streamlit as st
import tempfile
import zipfile
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.inference import predict


st.set_page_config(
    page_title="Smartphone Fall Detection",
    page_icon="📱",
    layout="wide"
)

st.title("Smartphone-Based Fall Detection")
st.write(
    "Upload a Sensor Logger ZIP file to detect whether a fall occurred "
    "and estimate the fall type and impact intensity."
)

uploaded_file = st.file_uploader(
    "Upload Sensor Logger ZIP",
    type=["zip"]
)

if uploaded_file is not None:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        zip_path = tmp_path / uploaded_file.name
        zip_path.write_bytes(uploaded_file.getbuffer())

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(tmp_path)

        st.success("File uploaded and extracted successfully.")

        result = predict(tmp_path)

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Fall detected?", "YES" if result["fall"] else "NO")
        col2.metric("Fall type", result["type"])
        col3.metric("Confidence", f"{result['confidence']:.0%}")
        col4.metric("Peak acceleration", f"{result['peak_g']} g")

        st.subheader("Prediction result")
        st.json(result)

        with st.expander("Extracted files"):
            files = [
                str(p.relative_to(tmp_path))
                for p in tmp_path.rglob("*")
                if p.is_file()
            ]
            st.write(files)
else:
    st.info("Please upload a Sensor Logger ZIP file to start.")
