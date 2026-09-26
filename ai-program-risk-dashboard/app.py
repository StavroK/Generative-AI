from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

BASE = Path(__file__).parent
portfolio = pd.read_csv(BASE / "data" / "portfolio.csv")
metrics = pd.read_csv(BASE / "data" / "ai_metrics.csv")
risks = pd.read_csv(BASE / "data" / "risks.csv")

st.set_page_config(page_title="Northstar AI Portfolio", layout="wide")
st.title("Northstar Enterprise AI Portfolio")
st.caption("Executive delivery, risk and AI-quality view — fictional demonstration data")

approved = portfolio["approved_budget_k"].sum()
forecast = portfolio["forecast_budget_k"].sum()
yellow = (portfolio["health"] == "Yellow").sum()
exec_items = (portfolio["exec_attention"] == "Yes").sum()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Active initiatives", len(portfolio))
c2.metric("Yellow initiatives", int(yellow))
c3.metric("Forecast vs approved", f"${forecast/1000:.3f}M", f"${(forecast-approved):.0f}K")
c4.metric("Executive decisions / attention", int(exec_items))

st.subheader("Portfolio health")
health_counts = portfolio.groupby("health", as_index=False).size()
st.plotly_chart(px.bar(health_counts, x="health", y="size", text="size", labels={"size":"Projects"}), use_container_width=True)

st.subheader("Budget forecast")
budget = portfolio[["initiative", "approved_budget_k", "forecast_budget_k"]].melt(
    id_vars="initiative", var_name="budget_type", value_name="budget_k"
)
st.plotly_chart(px.bar(budget, x="initiative", y="budget_k", color="budget_type", barmode="group", labels={"budget_k":"$K"}), use_container_width=True)

st.subheader("Schedule variance")
st.plotly_chart(px.bar(portfolio, x="initiative", y="schedule_variance_days", text="schedule_variance_days"), use_container_width=True)

st.subheader("GenAI operational metrics")
st.dataframe(metrics, use_container_width=True, hide_index=True)

st.subheader("Portfolio risks")
exposure_filter = st.multiselect("Exposure", sorted(risks["exposure"].unique()), default=sorted(risks["exposure"].unique()))
st.dataframe(risks[risks["exposure"].isin(exposure_filter)], use_container_width=True, hide_index=True)

st.info("This prototype demonstrates portfolio reporting patterns. Production dashboards should source governed systems of record and enforce enterprise access controls.")
