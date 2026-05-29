# 5-Slide Presentation Outline

## Slide 1 — Problem and Motivation

**Title:** Smartphone-Based Fall Detection

**Key message:** Falls can be dangerous, especially in workplace safety, elderly care, and situations where people work alone.

**Content:**
- Falls can lead to serious health consequences if no help arrives quickly.
- Smartphones already contain motion sensors such as accelerometers and gyroscopes.
- This project explores whether smartphone IMU data can be used to detect falls.
- The prototype is relevant for sensor-based safety analytics and health monitoring.

---

## Slide 2 — Data Collection

**Title:** Sensor Logger Data Collection

**Key message:** The project uses smartphone IMU data collected with the Sensor Logger app.

**Content:**
- Data format: Sensor Logger ZIP files with CSV sensor data.
- Sensors: accelerometer and gyroscope.
- Planned fall classes:
  - forward
  - backward
  - sideways
  - trip-stumble
- Planned non-fall activities:
  - walking
  - sitting
  - stairs
  - jumping
- Data collection follows a safety protocol using a mattress and supervised trials.

---

## Slide 3 — Method and Pipeline

**Title:** From Sensor Data to Prediction

**Key message:** The system processes raw sensor files and converts them into machine learning predictions.

**Content:**
1. Upload Sensor Logger ZIP file.
2. Extract accelerometer and gyroscope data.
3. Preprocess and resample the sensor signals.
4. Split signals into time windows.
5. Extract statistical and time-series features.
6. Use a machine learning model to predict fall/no fall and fall type.

**Planned models:**
- Random Forest Classifier
- Gradient Boosting
- Impact-intensity regression for peak acceleration

---

## Slide 4 — Streamlit Demo

**Title:** Interactive Web Prototype

**Key message:** The prototype is demonstrated through a Streamlit web app.

**Content:**
- User uploads a Sensor Logger ZIP file.
- The app extracts the recording.
- The prediction function returns:
  - fall detected: yes/no
  - fall type
  - confidence
  - peak acceleration
  - severity
- Results are shown with metric cards and a JSON output.
- Later integration will replace the mock prediction with the real model from the ML pipeline.

---

## Slide 5 — Future Work

**Title:** Future Extensions: Context-Aware Fall Risk

**Key message:** Future versions could combine fall detection with environmental risk factors.

**Content:**
- Weather data could improve risk estimation, e.g. icy or rainy conditions.
- GPS location could help distinguish indoor and outdoor contexts.
- A future risk score could combine:
  - movement data
  - weather conditions
  - location context
  - user risk profile
- This is planned only as a future-work concept, not as part of the current implementation.

**Example future output:**
```json
{
  "fall_detected": true,
  "fall_type": "sideways",
  "peak_g": 4.1,
  "weather_risk": "high",
  "recommendation": "Send alert"
}
