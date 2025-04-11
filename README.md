# 🔥 Fire Image & Sensor Dataset

This repository contains a multimodal dataset designed for **AI-based fire detection**, combining both **image data** and **time-series sensor readings** from fire scenarios.

---

## 📦 Dataset Contents

### 🔗 [Download Full Dataset (.rar ~325 MB)](https://github.com/palashngl/Fire-Images-Dataset/blob/main/Fire_Image_Sensor_Data.rar?raw=true)

After extraction, the `.rar` archive includes:

```
Fire_Image_Sensor_Data/
├── images/
│   ├── fire/  no_fire/        
├── sensors/
│   └── Raw_data.xlsx            # Full sensor log (timestamped)
```

---

## 🔬 Sensor Data Description

From `Raw_data.xlsx`:

| Column                    | Description                                 |
|---------------------------|---------------------------------------------|
| `Timestamp`               | Date and time of reading                    |
| `Gas Concentration (ppm)`| Gas levels in ppm (air quality indicator)   |
| `Flame Detection`         | Binary: 1 = flame detected, 0 = no flame    |
| `IR Reading`              | Infrared sensor value                       |
| `Temperature (°C)`        | Temperature in degrees Celsius              |
| `Humidity (%)`            | Ambient relative humidity in %              |

---

## 🧠 Use Cases

This dataset can be used to develop and evaluate:
- Fire detection systems (image-based, sensor-based, or fused)
- Real-time alert systems in smart buildings or forests
- Multimodal models (CNN + LSTM, Transformers, etc.)
- AI for safety robotics or edge devices

---

## 📈 Suggested Tasks

- 🔥 Binary fire classification (yes/no)
- 🧪 Sensor anomaly detection
- 🧠 Multimodal sensor-vision fusion
- 📊 Time-series prediction of fire risk

---

## 📝 License

This dataset is released under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.  
Feel free to use, modify, and cite it with attribution.

---

## 🤝 Cite This Dataset (If Used)

```bibtex
@misc{ingle2025fireimages,
  title={Fire Image & Sensor Dataset},
  author={Palash Ingle, Joshua Tito},
  year={2025},
  url={https://github.com/palashngl/Fire-Images-Dataset}
}
```
