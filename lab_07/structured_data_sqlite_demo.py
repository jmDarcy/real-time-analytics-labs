"""Structured data scoring demo with SQLite persistence.

The example is intentionally small and self-contained. It mirrors the Lab 7
theme from the RTA2026 course: structured tabular data, numerical
representations, simple modelling, and relational storage.

Run:
    python structured_data_sqlite_demo.py
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


DB_PATH = Path(__file__).with_name("structured_predictions.db")
RANDOM_SEED = 2026


def build_dataset(n_rows: int = 300) -> pd.DataFrame:
    rng = np.random.default_rng(RANDOM_SEED)
    income = rng.normal(7_000, 2_000, n_rows).clip(1_500, 18_000)
    monthly_spend = rng.normal(2_400, 900, n_rows).clip(200, 8_000)
    account_age_months = rng.integers(1, 96, n_rows)
    support_tickets_30d = rng.poisson(1.2, n_rows)
    late_payments_12m = rng.poisson(0.7, n_rows)

    linear_risk = (
        -2.4
        + 0.00035 * monthly_spend
        - 0.00018 * income
        - 0.012 * account_age_months
        + 0.42 * support_tickets_30d
        + 0.65 * late_payments_12m
    )
    probability = 1 / (1 + np.exp(-linear_risk))
    high_risk = rng.binomial(1, probability)

    return pd.DataFrame(
        {
            "customer_id": [f"C{i:04d}" for i in range(1, n_rows + 1)],
            "income": income.round(2),
            "monthly_spend": monthly_spend.round(2),
            "account_age_months": account_age_months,
            "support_tickets_30d": support_tickets_30d,
            "late_payments_12m": late_payments_12m,
            "high_risk": high_risk,
        }
    )


def score_dataset(df: pd.DataFrame) -> pd.DataFrame:
    feature_cols = [
        "income",
        "monthly_spend",
        "account_age_months",
        "support_tickets_30d",
        "late_payments_12m",
    ]
    x_train, x_test, y_train, _ = train_test_split(
        df[feature_cols],
        df["high_risk"],
        test_size=0.25,
        random_state=RANDOM_SEED,
        stratify=df["high_risk"],
    )

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    model = LogisticRegression(max_iter=1000)
    model.fit(x_train_scaled, y_train)

    scored = df.copy()
    scored["risk_probability"] = model.predict_proba(scaler.transform(df[feature_cols]))[:, 1]
    scored["predicted_high_risk"] = (scored["risk_probability"] >= 0.5).astype(int)
    scored["scored_at_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return scored


def write_sqlite(scored: pd.DataFrame, db_path: Path = DB_PATH) -> None:
    with sqlite3.connect(db_path) as conn:
        scored.to_sql("customer_risk_scores", conn, if_exists="replace", index=False)
        summary = scored.groupby("predicted_high_risk", as_index=False).agg(
            customers=("customer_id", "count"),
            avg_probability=("risk_probability", "mean"),
            avg_monthly_spend=("monthly_spend", "mean"),
        )
        summary.to_sql("risk_score_summary", conn, if_exists="replace", index=False)


def main() -> None:
    df = build_dataset()
    scored = score_dataset(df)
    write_sqlite(scored)

    print(f"Saved scored records to {DB_PATH.resolve()}")
    print(scored[["customer_id", "risk_probability", "predicted_high_risk"]].head(10).to_string(index=False))


if __name__ == "__main__":
    main()
