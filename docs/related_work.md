# Related Work

## Overview

Fall detection using smartphones and wearable sensors has been widely researched in recent years. Most approaches use inertial measurement unit (IMU) data, especially accelerometer and gyroscope signals, to distinguish between normal activities of daily living and fall events. The main challenge is that fall events are short, sudden, and rare, while normal daily movements can sometimes look similar in the sensor data.

This project is based on existing research about smartphone-based fall detection, public fall datasets, sensor-based activity recognition, and machine learning methods for time-series classification.

## Smartphone-Based Fall Detection

Casilari et al. (2015) provide a broad overview of Android-device-based fall detection systems. Their work shows that smartphones are suitable for fall detection because they already contain motion sensors such as accelerometers and gyroscopes. This makes smartphone-based fall detection a low-cost alternative to special wearable devices. However, the authors also highlight important challenges, including sensor placement, differences between devices, and the difficulty of evaluating fall detection systems under realistic conditions.

For this project, the smartphone-based approach is especially relevant because the data is collected with the Sensor Logger app on regular smartphones. This allows the team to build a prototype without additional hardware.

## Public Fall Datasets

Several public datasets are commonly used in fall detection research. The SisFall dataset by Sucerquia et al. (2017) is one of the most important examples. It contains multiple types of falls and activities of daily living. The dataset also provides a structured data collection protocol, including safety considerations and the use of mats during simulated falls. This is relevant for our project because our own data collection also needs a safe and clearly documented protocol.

The MobiFall dataset by Vavoulas et al. (2014) is particularly relevant because it focuses on smartphone-based fall detection. It includes different fall types and daily activities recorded with a smartphone. The dataset uses fall categories such as forward, backward, and sideways falls. These categories are similar to the fall taxonomy used in our project.

UMAFall is another relevant dataset because it combines smartphone data with additional wearable sensors. It includes forward, backward, and lateral falls as well as activities of daily living. While our project only uses smartphone IMU data, UMAFall supports the decision to use a small number of clearly defined fall classes.

## Machine Learning for Fall Detection

Zurbuchen et al. (2021) show that classical machine learning models such as Random Forest and Gradient Boosting can achieve strong results for fall detection based on wearable sensor data. Their work is important for this project because it supports the use of classical machine learning instead of complex deep learning models. For a small student dataset, models such as Random Forest are more realistic and easier to interpret.

The study also discusses the influence of sensor sampling rates. This is relevant because our project records smartphone sensor data with Sensor Logger and then resamples the data to a consistent frequency. A consistent sampling rate is important to make the recordings comparable across devices.

## Feature Extraction

Fall detection systems often rely on features extracted from short time windows. Common features include mean, standard deviation, minimum, maximum, signal magnitude, acceleration peaks, and jerk. Frequency-domain features can also be used to describe movement patterns.

For this project, the planned pipeline uses time-domain and frequency-domain features extracted from accelerometer and gyroscope signals. The tsfresh library is a suitable tool for automatic feature extraction from time-series data. It can generate a large number of statistical features and supports feature selection, which makes it useful for a machine learning pipeline based on sensor windows.

## Sensor Logger and Data Format

The Sensor Logger app is used to collect smartphone IMU data. It can export recordings as Zipped CSV files, which contain separate CSV files for sensors such as the accelerometer and gyroscope. This format is practical because it can be processed with Python using libraries such as pandas and zipfile.

For this project, the ZIP upload format is also important for the Streamlit prototype. The app should allow users to upload a Sensor Logger ZIP file, extract the files, process the sensor data, and display a prediction result.

## Relevance for This Project

The reviewed literature supports the main design decisions of this project. First, smartphone IMU data is a suitable basis for fall detection. Second, fall classes such as forward, backward, sideways, and trip-stumble are consistent with common fall detection datasets. Third, classical machine learning models are realistic for a small student project and can be combined with interpretable feature extraction. Finally, a clearly documented data collection protocol is necessary to ensure safety and reproducibility.

Based on this related work, the project focuses on a practical pipeline: collecting Sensor Logger data, preprocessing the IMU signals, extracting features, training classical machine learning models, and demonstrating the results in a Streamlit web application.

## References

Casilari, E., Luque, R., & Morón, M. J. (2015). Analysis of Android Device-Based Solutions for Fall Detection. Sensors, 15(8), 17827–17894. https://doi.org/10.3390/s150817827

Sucerquia, A., López, J. D., & Vargas-Bonilla, J. F. (2017). SisFall: A Fall and Movement Dataset. Sensors, 17(1), 198. https://doi.org/10.3390/s17010198

Vavoulas, G., Pediaditis, M., Chatzaki, C., Spanakis, E. G., & Tsiknakis, M. (2014). The MobiFall Dataset: Fall Detection and Classification with a Smartphone. International Journal of Monitoring and Surveillance Technologies Research, 2(1), 44–56. https://doi.org/10.4018/ijmstr.2014010103

Zurbuchen, N., Wilde, A., & Bruegger, P. (2021). A Machine Learning Multi-Class Approach for Fall Detection Systems Based on Wearable Sensors with a Study on Sampling Rates Selection. Sensors, 21(3), 938. https://doi.org/10.3390/s21030938

Christ, M., Braun, N., Neuffer, J., & Kempa-Liehr, A. W. (2018). Time Series Feature Extraction on Basis of Scalable Hypothesis Tests. Neurocomputing, 307, 72–77. https://doi.org/10.1016/j.neucom.2018.03.067