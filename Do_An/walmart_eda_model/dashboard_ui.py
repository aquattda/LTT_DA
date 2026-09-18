"""Shared presentation components for the Walmart analytics workspace."""

from contextlib import contextmanager
from html import escape
from hashlib import sha256
from pathlib import Path
from base64 import b64encode

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import streamlit as st

TEAL = "#0F887B"
NAVY = "#24476B"
GOLD = "#DFA544"
COLORS = [TEAL, NAVY, GOLD, "#7C80B8", "#58A6BD"]
TYPE_COLORS = {"A": TEAL, "B": NAVY, "C": GOLD}
LABELS = {
    "Weekly_Sales": "Doanh số (USD)", "Store": "Cửa hàng", "Dept": "Bộ phận",
    "Type": "Loại cửa hàng", "Size": "Diện tích (ft²)", "Date": "Thời gian",
    "Year": "Năm", "Month": "Tháng", "Week": "Tuần", "Quarter": "Quý",
    "Temperature": "Nhiệt độ (°F)", "Fuel_Price": "Nhiên liệu (USD/gallon)",
    "CPI": "Chỉ số CPI", "Unemployment": "Thất nghiệp (%)",
}


def setup_ui():
    st.set_page_config(page_title="Walmart · Sales Intelligence", page_icon="◈", layout="wide")
    css = Path(__file__).with_name("dashboard.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    pio.templates["walmart"] = go.layout.Template(
        layout=dict(
            font=dict(family="Arial, sans-serif", size=12, color="#64748B"),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            colorway=COLORS,
            xaxis=dict(showgrid=False, zeroline=False, automargin=True),
            yaxis=dict(gridcolor="#EDF1F6", zeroline=False, automargin=True),
            hoverlabel=dict(bgcolor="#11243B", font_color="white", bordercolor="#11243B"),
        )
    )
    px.defaults.template = "walmart"
    px.defaults.color_discrete_sequence = COLORS
    px.defaults.color_discrete_map = TYPE_COLORS
    px.defaults.labels = LABELS


def money(value, compact=False):
    if value is None or not np.isfinite(value):
        return "—"
    if compact:
        for scale, unit in [(1e9, "tỷ"), (1e6, "triệu"), (1e3, "nghìn")]:
            if abs(value) >= scale:
                return f"${value / scale:,.2f} {unit}"
    return f"${value:,.0f}"


def metric(label, value, note, accent=False):
    css_class = "kpi-card kpi-accent" if accent else "kpi-card"
    st.markdown(
        f'<div class="{css_class}"><div class="kpi-label">{escape(label)}</div>'
        f'<div class="kpi-value">{escape(str(value))}</div>'
        f'<div class="kpi-note">{escape(note)}</div></div>', unsafe_allow_html=True,
    )


def metrics(items):
    for i, (col, item) in enumerate(zip(st.columns(len(items)), items)):
        with col:
            metric(*item, accent=i == 0)


def page_header(title, description, data):
    period = (f"{data.Date.min():%d.%m.%Y} — {data.Date.max():%d.%m.%Y}"
              if not data.empty else "Chưa có dữ liệu trong phạm vi")
    st.markdown(
        '<div class="page-topline"><span>WORKSPACE / SALES ANALYTICS</span>'
        '<span class="data-badge"><i></i> Dữ liệu lịch sử</span></div>'
        f'<div class="page-heading"><div><h1>{escape(title)}</h1>'
        f'<p>{escape(description)}</p></div>'
        f'<div class="period-chip">{period}</div></div>', unsafe_allow_html=True,
    )


@contextmanager
def panel(title, subtitle=None):
    with st.container(border=True, key="panel_" + sha256(title.encode()).hexdigest()[:12]):
        st.markdown(f'<h3 class="panel-title">{escape(title)}</h3>', unsafe_allow_html=True)
        if subtitle:
            st.markdown(f'<p class="panel-subtitle">{escape(subtitle)}</p>', unsafe_allow_html=True)
        yield


def chart(fig, height=310, horizontal=False):
    fig.update_layout(
        template="walmart", height=height, title=None,
        margin=dict(l=12, r=18, t=20, b=12),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0, title_text=""),
        modebar=dict(bgcolor="rgba(0,0,0,0)", color="#8795A8", activecolor=TEAL),
        bargap=0.32,
    )
    if horizontal:
        fig.update_yaxes(showgrid=False)
        fig.update_xaxes(showgrid=True, gridcolor="#EDF1F6")
    st.plotly_chart(fig, width="stretch", theme=None, config={"displaylogo": False, "scrollZoom": False})


def insight(title, body):
    st.markdown(
        '<div class="insight"><div class="insight-icon">↗</div><div>'
        f'<strong>{escape(title)}</strong><p>{escape(body)}</p></div></div>',
        unsafe_allow_html=True,
    )


def empty_state(message="Hãy chọn ít nhất một loại cửa hàng và một năm để xem phân tích."):
    st.info(message, icon="ℹ️")


@st.cache_data(show_spinner=False)
def logo_data_uri():
    logo = Path(__file__).with_name("Walmart-Logo-New.png")
    return "data:image/png;base64," + b64encode(logo.read_bytes()).decode("ascii")


def brand_logo():
    st.markdown(
        f'<div class="brand"><div class="brand-logo-frame"><img class="brand-logo" '
        f'src="{logo_data_uri()}" alt="Walmart" /></div>'
        '<div class="brand-sub">SALES INTELLIGENCE</div></div>', unsafe_allow_html=True,
    )


def scroll_to_top_on_navigation(page):
    """Run once per navigation, including A → B → A; never on filter reruns."""
    if st.session_state.get("_last_analysis_page") == page:
        return
    st.session_state["_last_analysis_page"] = page
    revision = st.session_state.get("_navigation_revision", 0) + 1
    st.session_state["_navigation_revision"] = revision
    script = Path(__file__).with_name("navigation.js").read_text(encoding="utf-8")
    script = script.replace("__NAVIGATION_REVISION__", str(revision))
    # Only local, developer-authored JavaScript; no user input is interpolated.
    st.html(f'<span class="navigation-scroll-marker" hidden></span>'
            f'<script>/* navigation {revision} */\n{script}</script>', unsafe_allow_javascript=True)
