import requests
import pandas as pd
import os
from datetime import datetime

url = "https://intradayscreener.com/api/indices/indexcontributors/NIFTY%2050"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()["data"]

    all_contributors = data.get("indexContributionList", [])
    positive = data.get("positiveIndexContributionList", [])
    negative = data.get("negativeIndexContributionList", [])

    df_all = pd.DataFrame(all_contributors)
    df_positive = pd.DataFrame(positive)
    df_negative = pd.DataFrame(negative)

    today = datetime.today().strftime("%Y-%m-%d")
    save_dir = os.path.join("data", today)
    os.makedirs(save_dir, exist_ok=True)

    df_all.to_csv(os.path.join(save_dir, "all_contributors.csv"), index=False)
    df_positive.to_csv(os.path.join(save_dir, "positive_contributors.csv"), index=False)
    df_negative.to_csv(os.path.join(save_dir, "negative_contributors.csv"), index=False)

    print(f"CSV files saved in: {save_dir}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
