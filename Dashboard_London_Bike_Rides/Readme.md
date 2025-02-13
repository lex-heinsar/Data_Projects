# 🚴 London Bike Sharing Dataset Analysis

## 📌 Project Overview  
This project explores historical bike-sharing data in **London**, using **Python** for data manipulation and **Tableau** for visualization. The dataset is sourced from **TfL Open Data** (Transport for London).  

🔗 **Data Source:** [Kaggle - London Bike Sharing Dataset](https://www.kaggle.com/datasets/hmavrodiev/london-bike-sharing-dataset/data)  

The project is inspired by an online tutorial by **Mo Chen**:  
🎥 [Watch the tutorial](https://youtu.be/nl9eZl1IOKI?si=e5rKSHWQKvgNBekr)  

However, instead of just following along, I aimed to **deepen my understanding** by:
- Immersing myself in the dataset.
- Discovering additional insights.
- Experimenting with alternative visualizations.

🔗 **Created Visuals:** [Open the Visuals in Tableau Public](https://public.tableau.com/views/LondonBikeRides-MovingAverageandHeatmap_17393885362540/Dashboard1?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## 🚀 Project Steps  
This project follows three key steps:

1️⃣ **Programmatically gather data**  
2️⃣ **Explore, assess, and manipulate data** using `pandas` in Python  
3️⃣ **Create impactful visualizations** in Tableau  

---

## 📊 Dataset Structure  
This dataset contains **hourly bike-sharing records** from **January 4, 2015, to January 3, 2017**.  
It includes **weather conditions**, **timestamps**, and **the number of new bike shares per hour**.

### 🗃 Metadata  
| Column | Description |
|--------|-------------|
| `timestamp` | Date & time of the record |
| `cnt` | Number of new bike shares per hour |
| `t1` | Actual temperature (°C) |
| `t2` | "Feels like" temperature (°C) |
| `hum` | Humidity (%) |
| `wind_speed` | Wind speed (km/h) |
| `weather_code` | Weather category (see below) |
| `is_holiday` | 1 = Holiday, 0 = Non-holiday |
| `is_weekend` | 1 = Weekend, 0 = Weekday |
| `season` | Meteorological season (0 = Spring, 1 = Summer, 2 = Fall, 3 = Winter) |

### 🌦 Weather Code Breakdown  
| Code | Description |
|------|------------|
| 1  | Clear / Mostly clear (haze, fog, patches of fog) |
| 2  | Scattered clouds / Few clouds |
| 3  | Broken clouds |
| 4  | Cloudy |
| 7  | Rain / Light rain shower |
| 10 | Rain with thunderstorm |
| 26 | Snowfall |
| 94 | Freezing fog |

---

## 🔧 Technologies Used  
- **Python** (`pandas` library)  
- **Tableau** (for visualizations)  
