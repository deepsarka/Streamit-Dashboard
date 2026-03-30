# 🎛️ Streamlit EDA Dashboard

An interactive multi-page EDA dashboard — upload any CSV and explore your data visually in seconds.

## Features
- Upload any `.csv` file and auto-detect numeric & categorical columns
- Optional missing value removal
- 4 analysis pages: Univariate, Bivariate, Multivariate, and Insights
- All charts are dynamic and respond to column selection

## Pages
| Page | Charts |
|---|---|
| Univariate | Histogram, Count Plot, Box Plot, Pie Chart |
| Bivariate | Line Chart, Scatter Plot, Bar Chart, Box Plot |
| Multivariate | Pair Plot (sampled to 300 rows), Correlation Heatmap |
| Insights | Mean, Median, Max, Min, Std Dev / Top value counts |

## Tech Stack
`Python` · `Streamlit` · `Pandas` · `Matplotlib` · `Seaborn`

## How to Run
```bash
git clone <your-repo-url>
cd streamlit-eda-dashboard
pip install streamlit pandas matplotlib seaborn
streamlit run app.py
```
App opens at `http://localhost:8501`

## Deploy to Streamlit Cloud
1. Push to a public GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Select `app.py` as the entry point → **Deploy**

## Project Structure
```
├── app.py
└── README.md
```
