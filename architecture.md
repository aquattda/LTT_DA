# Architecture Memory

## Project Overview
- Academic Walmart weekly sales analysis project at `C:/Users/luong/OneDrive/LTT_DA`.
- Stack: Python, pandas, NumPy, scikit-learn, Streamlit, Plotly, Matplotlib, Seaborn.

## Components and Data Flow
- `Do_An/dataset/`: `train.csv`, `test.csv`, `stores.csv`, `features.csv`.
- `Do_An/walmart_eda_model/3122410447_LTT.ipynb`: EDA, preprocessing, four regression models, evaluation including WMAE, and joblib model export. CSV paths are relative to the notebook directory (`../dataset/`).
- `Do_An/walmart_eda_model/streamlit_dashboard.py`: seven dashboard pages; `load_data()` resolves dataset paths from `__file__`, merges stores and features, and creates time features.
- Dashboard `train_model()` fits GradientBoostingRegressor on an 80/20 random split when the prediction page is opened; caches the model with Streamlit. It does not load a pretrained model file.
- `train.csv` includes `Weekly_Sales`; `test.csv` does not. Local validation is split from training data.
- `.gitignore` excludes `myvenv/` and `*.pkl`. `Do_An/readme.md` contains the existing model download link.

## Run Commands
- Install: `python -m pip install -r Do_An/walmart_eda_model/requirements.txt`.
- Dashboard from repository root: `python -m streamlit run Do_An/walmart_eda_model/streamlit_dashboard.py`.
- Notebook requires a Jupyter environment in addition to the listed requirements; run with the notebook directory as working directory.

## Documentation
- Root `README.md`: Vietnamese overview, dataset inventory, directory tree, setup instructions, stored result images, course attribution.
- PNG result figures are stored under `Do_An/walmart_eda_model/`; they represent saved results, not a newly verified training run.

_Last updated: 2026-09-17_
