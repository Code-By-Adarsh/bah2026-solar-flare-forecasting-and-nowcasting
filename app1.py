import streamlit as st
import pandas as pd
import traceback
import plotly.graph_objects as go
from datetime import datetime

from Backend.file_reader import (
    read_solexs,
    read_hel1os_cdte1
)

from Backend.flare_detector import (
    detect_solexs_flare,
    detect_hel1os_flare
)

from Backend.catalog_builder import (
    build_master_catalog
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Solar Flare Intelligence System",
    page_icon="☀️",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background-color: #0B1220;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg,#111827,#1F2937);
    border: 1px solid #374151;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

h1 {
    color: #F59E0B;
}

.stAlert {
    border-radius: 12px;
}

div[data-testid="stDataFrame"] {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown("""
<h1 style='font-size:48px'>
☀️ Solar Flare Intelligence System
</h1>

<p style='font-size:18px;color:#94A3B8'>
Real-Time Solar Flare Detection, Analysis and Nowcasting
using Aditya-L1 SoLEXS & HEL1OS Data
</p>
""", unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("Control Panel")

    st.info(
        """
        Current Version

        ✅ SoLEXS Analysis

        ✅ HEL1OS Analysis

        ✅ Unified Master Catalog

        🚧 Forecasting (Upcoming)
        """
    )

    run_analysis = st.button(
        "Analyze Data 🚀",
        use_container_width=True
    )

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

if run_analysis:

    try:

        # -----------------------
        # READ DATA
        # -----------------------

        solexs_data = read_solexs(
            "Data/sample_data/SOLEXS/AL1_SOLEXS_20260615_SDD2_L1.lc"
        )

        hel1os_data = read_hel1os_cdte1(
            "Data/sample_data/HEL1OS/lightcurve_cdte1.fits",
            "Data/sample_data/HEL1OS/lightcurve_cdte1_2.fits"
        )

        # -----------------------
        # DETECT FLARES
        # -----------------------

        solexs_result = detect_solexs_flare(
            solexs_data
        )

        hel1os_result = detect_hel1os_flare(
            hel1os_data
        )

        # -----------------------
        # BUILD CATALOG
        # -----------------------

        catalog = build_master_catalog(
            solexs_result,
            hel1os_result
        )

        st.success(
            "Analysis Completed Successfully"
        )

        # ==================================================
        # SUMMARY CARDS
        # ==================================================

        st.subheader("Detection Summary")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "☀️ SoLEXS Peak",
            solexs_result["peak_value"]
        )

        c2.metric(
            "⚡ HEL1OS Peak",
            hel1os_result["peak_value"]
        )

        c3.metric(
            "📈 SoLEXS Threshold",
            solexs_result["threshold"]
        )

        c4.metric(
            "🎯 HEL1OS Threshold",
            hel1os_result["threshold"]
        )

        st.divider()

        # ==================================================
        # SOLEXS STATS
        # ==================================================

        st.subheader("SoLEXS Statistics")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Mean",
            solexs_result["mean"]
        )

        c2.metric(
            "Std",
            solexs_result["std"]
        )

        c3.metric(
            "Flare Points",
            solexs_result["flares"]
        )

        peak_time_solexs = datetime.utcfromtimestamp(
            solexs_result["peak_time"]
        )

        c4.metric(
            "Peak Time UTC",
            peak_time_solexs.strftime("%H:%M:%S")
        )

        # ==================================================
        # HEL1OS STATS
        # ==================================================

        st.subheader("HEL1OS Statistics")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Mean",
            hel1os_result["mean"]
        )

        c2.metric(
            "Std",
            hel1os_result["std"]
        )

        c3.metric(
            "Flare Points",
            hel1os_result["flares"]
        )

        peak_time_hel1os = datetime.utcfromtimestamp(
            hel1os_result["peak_time"]
        )

        c4.metric(
            "Peak Time UTC",
            peak_time_hel1os.strftime("%H:%M:%S")
        )

        st.divider()

        # ==================================================
        # SOLEXS GRAPH
        # ==================================================

        st.subheader("SoLEXS Light Curve")

        fig1 = go.Figure()

        fig1.add_trace(
            go.Scatter(
                x=solexs_data["time"],
                y=solexs_data["counts"],
                mode="lines",
                name="Counts"
            )
        )

        fig1.update_layout(
            height=450,
            xaxis_title="Unix Time",
            yaxis_title="Counts"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

        # ==================================================
        # HEL1OS GRAPH
        # ==================================================

        st.subheader("HEL1OS Light Curve")

        fig2 = go.Figure()

        fig2.add_trace(
            go.Scatter(
                x=hel1os_data["unix_time"],
                y=hel1os_data["ctr"],
                mode="lines",
                name="CTR"
            )
        )

        fig2.update_layout(
            height=450,
            xaxis_title="Unix Time",
            yaxis_title="CTR"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        st.divider()

        # ==================================================
        # CATALOG
        # ==================================================

        st.subheader("Unified Master Flare Catalog")

        st.dataframe(
            catalog,
            use_container_width=True
        )

        st.divider()

        # ==================================================
        # EVENT REPORT
        # ==================================================

        st.subheader("Event Report")

        st.info(
            f"""
            SoLEXS Peak Value : {solexs_result['peak_value']}

            HEL1OS Peak Value : {hel1os_result['peak_value']}

            Unified Master Catalog Generated Successfully.
            """
        )

    except Exception as e:
        st.error(str(e))
        st.code(traceback.format_exc())

else:

    st.warning(
        "Click 'Analyze Data 🚀' to start analysis."
    )
