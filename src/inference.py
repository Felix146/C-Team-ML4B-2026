from pathlib import Path


def predict(folder_path: Path) -> dict:
    """
    Temporary mock prediction function.

    This function will later be replaced by the real ML inference pipeline.
    The Streamlit app can already use this interface.
    """
    return {
        "fall": True,
        "type": "forward",
        "confidence": 0.78,
        "peak_g": 4.3,
        "severity": "moderate"
    }
