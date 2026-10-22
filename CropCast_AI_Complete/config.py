
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "placement_predict_50k Dataset.csv"
)

CHART_DIR = os.path.join(BASE_DIR, "static", "images")
os.makedirs(CHART_DIR, exist_ok=True)

