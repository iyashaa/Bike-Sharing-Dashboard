### Bike Sharing Dashboard

An interactive dashboard built with Streamlit to analyze bike rental patterns based on time, weather, and other environmental factors.

### Description

This project aims to explore bike sharing data through various visualizations, including:

* Daily bike rental trends
* Usage patterns by hour
* The impact of weather conditions on rental demand
* The relationship between temperature and rental activity

This dashboard helps uncover user behavior insights and identify key factors influencing bike rental demand.

### Environment Setup – Anaconda

```bash
conda create --name bike-ds python=3.9
conda activate bike-ds
pip install -r requirements.txt
```

### Environment Setup – Shell/Terminal

```bash
mkdir bike_sharing_dashboard
cd bike_sharing_dashboard
pipenv install
pipenv shell
pip install -r requirements.txt
```

### Running the Streamlit App

```bash
streamlit run dashboard.py
```

### Requirements

Libraries used in this project:

```txt
streamlit
pandas
plotly
numpy
matplotlib
seaborn
```

### Project Structure

```
bike-sharing-dashboard
│
├── dashboard
│   ├── dashboard.py
│   └── main_data.csv
│
├── data
│   ├── day.csv
│   └── hour.csv
│
├── requirements.txt
├── url.txt
├── notebook.ipynb
└── README.md
```


### Dashboard Features

* Daily bike rental trend visualization
* Hourly rental pattern analysis
* Comparison of rentals based on weather conditions
* Temperature impact analysis on bike usage
* KPI metrics for total users (casual & registered)


### Notes

Make sure the `main_data.csv` file is located in the same directory as `dashboard.py` to ensure the application runs properly.

## Live Demo

[View the Dashboard]((https://bike-sharing-dashboard-lcyyqlqzmjrntgsivsdvia.streamlit.app/))
