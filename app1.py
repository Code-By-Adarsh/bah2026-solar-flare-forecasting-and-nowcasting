import streamlit as st
import pandas as pd
import traceback
import tempfile
import plotly.graph_objects as go
from datetime import datetime
from Backend.file_reader import (read_solexs,read_hel1os_cdte1)
from Backend.flare_detector import (detect_solexs_flare,detect_hel1os_flare)
from Backend.catalog_builder import (build_master_catalog)

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
<h1 style='font-size:48px;color:#FDB813'>
☀️ Solar Flare Intelligence System
</h1>

<p style='font-size:20px;color:#E2E8F0;font-weight:800'>
🚀 Bharatiya Antariksh Hackathon 2026
</p>

<p style='font-size:20px;color:#E2E8F0;font-weight:600'>
🎯 Problem Statement [15] : Forecasting and/or Nowcasting of Solar Flares using combined Soft and Hard X-ray data from Aditya-L1
</p>

<p style='font-size:20px;color:#E2E8F0;font-weight:600'>
⚡ Team Anant
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

    st.subheader("📂 Upload Files")

    solexs_file = st.file_uploader(
        "Upload SoLEXS File",
        type=["lc"]
    )

    if solexs_file:
        st.success("✅ SoLEXS File Uploaded")

    hel1os_file_1 = st.file_uploader(
        "Upload HEL1OS CDTE1 Part-1",
        type=["fits"]
    )

    if hel1os_file_1:
        st.success("✅ HEL1OS CDTE1 Part-1 Uploaded")

    hel1os_file_2 = st.file_uploader(
        "Upload HEL1OS CDTE1 Part-2",
        type=["fits"]
    )

    if hel1os_file_2:
        st.success("✅ HEL1OS CDTE1 Part-2 Uploaded")

    st.divider()

    use_sample_data = st.checkbox(
        "🧪 Use Built-in Sample Dataset (15 June 2026)"
    )

    st.caption(
        "Having trouble uploading files? "
        "Use the built-in sample dataset."
    )

    files_ready = (
        use_sample_data
        or
        (
        solexs_file and
        hel1os_file_1 and
        hel1os_file_2
        )
    )

    run_analysis = st.button(
        "Analyze Data 🚀",
        use_container_width=True,
        disabled=not files_ready
    )

    if run_analysis:
        st.success("✅ Analysis Completed Successfully")
    
# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

if run_analysis:

    try:

        # -----------------------
        # READ DATA
        # -----------------------
        if not use_sample_data:
            if not solexs_file:
                st.error("Upload SoLEXS file")
                st.stop()

            if not hel1os_file_1:
                st.error("Upload HEL1OS CDTE1 Part-1")
                st.stop()

            if not hel1os_file_2:
                st.error("Upload HEL1OS CDTE1 Part-2")
                st.stop()


        if use_sample_data:
            solexs_data = read_solexs(
                "Data/sample_data/SOLEXS/AL1_SOLEXS_20260615_SDD2_L1.lc"
            )

            hel1os_data = read_hel1os_cdte1(
                "Data/sample_data/HEL1OS/lightcurve_cdte1.fits",
                "Data/sample_data/HEL1OS/lightcurve_cdte1_2.fits"
            )

        else:
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".lc"
            ) as tmp_solexs:

                tmp_solexs.write(
                    solexs_file.getbuffer()
                )

                solexs_path = tmp_solexs.name

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".fits"
            ) as tmp_hel1os_1:

                tmp_hel1os_1.write(
                    hel1os_file_1.getbuffer()
                )

                hel1os_path_1 = tmp_hel1os_1.name

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".fits"
            ) as tmp_hel1os_2:

                tmp_hel1os_2.write(
                    hel1os_file_2.getbuffer()
                )

                hel1os_path_2 = tmp_hel1os_2.name

            solexs_data = read_solexs(
                solexs_path
            )

            hel1os_data = read_hel1os_cdte1(
                hel1os_path_1,
                hel1os_path_2
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
            "✅ Analysis Completed Successfully"
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

        c1, c2, c3, c4, c5 = st.columns(5)

        c1.metric(
            "Mean Count",
            solexs_result["mean"]
        )

        c2.metric(
            "Standard Deviation",
            solexs_result["std"]
        )

        c3.metric(
            "Threshold",
            solexs_result["threshold"]
        )

        c4.metric(
            "Threshold Crossings",
            solexs_result["flares"]
        )

        peak_time_solexs = datetime.utcfromtimestamp(
            solexs_result["peak_time"]
        )

        c5.metric(
            "Peak Time (UTC)",
            peak_time_solexs.strftime("%H:%M:%S")
        )

        # ==================================================
        # HEL1OS STATS
        # ==================================================

        st.subheader("HEL1OS Statistics")

        c1, c2, c3, c4, c5= st.columns(5)

        c1.metric(
            "Mean Count",
            hel1os_result["mean"]
        )

        c2.metric(
            "Standard Deviation",
            hel1os_result["std"]
        )

        c3.metric(
            "Threshold",
            hel1os_result["threshold"]
        )

        c4.metric(
            "Threshold Crossings",
            hel1os_result["flares"]
        )

        peak_time_hel1os = datetime.utcfromtimestamp(
            hel1os_result["peak_time"]
        )

        c5.metric(
            "Peak Time (UTC)",
            peak_time_hel1os.strftime("%H:%M:%S")
        )

        st.divider()

        # ==================================================
        # SOLEXS GRAPH
        # ==================================================

        #st.subheader("SoLEXS Light Curve")
        col1,col2 = st.columns(2)


        fig1 = go.Figure()

        fig1.add_hline(
            y=solexs_result["threshold"],
            line_dash="dash",
            line_color="white",
            line_width=3,
            annotation_text=f"Threshold = {solexs_result['threshold']}",
            annotation_position="top right"
        )

        fig1.add_trace(
            go.Scatter(
                x=[solexs_result["peak_time"]],
                y=[solexs_result["peak_value"]],
                mode="markers+text",
                text=[f"Peak = {solexs_result['peak_value']}"],
                marker=dict(size=16),
                name="Peak",
                textposition="top center"
            )
        )

        fig1.update_layout(
            template="ggplot2",
            height=500,
            showlegend=False
        )

        fig1.add_trace(
            go.Scatter(
                x=solexs_data["time"],
                y=solexs_data["counts"],
                mode="lines",
                name="Counts"
            )
        )

        fig1.update_layout(
            height=600,
            xaxis_title="Unix Time",
            yaxis_title="Counts"
        )

        #st.plotly_chart(fig1,use_container_width=True)
        with col1:
            st.subheader("☀️ SoLEXS Light Curve")
            st.plotly_chart(fig1,use_container_width=True)


        # ==================================================
        # HEL1OS GRAPH
        # ==================================================

        #st.subheader("HEL1OS Light Curve")

        fig2 = go.Figure()

        fig2.add_hline(
            y=hel1os_result["threshold"],
            line_dash="dash",
            line_color="white",
            line_width=3,
            annotation_text=f"Threshold = {hel1os_result['threshold']}",
            annotation_position="top right"
        )

        fig2.add_trace(
            go.Scatter(
                x=[hel1os_result["peak_time"]],
                y=[hel1os_result["peak_value"]],
                mode="markers+text",
                text=[f"Peak = {hel1os_result['peak_value']}"],
                marker=dict(size=16),
                name="Peak",
                textposition="top center"
            )
        )

        fig2.update_layout(
            template="ggplot2",
            height=500,
            showlegend=False
        )

        fig2.add_trace(
            go.Scatter(
                x=hel1os_data["unix_time"],
                y=hel1os_data["ctr"],
                mode="lines",
                name="CTR"
            )
        )

        fig2.update_layout(
            height=600,
            xaxis_title="Unix Time",
            yaxis_title="CTR"
        )

        #st.plotly_chart(fig2,use_container_width=True)
        with col2:
            st.subheader("⚡ HEL1OS Light Curve")
            st.plotly_chart(fig2,use_container_width=True)

        st.divider()

        # ==================================================
        # CATALOG
        # ==================================================

        st.subheader("📋 Unified Master Flare Catalog")

        current_time = datetime.now().strftime("%Y-%M-%D_%H-%M-%S")

        csv = catalog.to_csv(
            index=False
        )

        st.download_button(
            label="📥 Download Catalog",
            data=csv,
            file_name=f"SolarFlareCatalog_{current_time}.csv",
            mime="text/csv"
        )

        st.dataframe(
            catalog,
            use_container_width=True,
            hide_index = True
        )

        st.divider()

        # ==================================================
        # EVENT REPORT
        # ==================================================

        st.subheader("🚀 Analysis Report")

        st.success(
        f"""Solar flare activity successfully detected.\n
• SoLEXS Peak Count : {solexs_result['peak_value']}

• HEL1OS Peak Count : {hel1os_result['peak_value']}

• SoLEXS Threshold : {solexs_result['threshold']}

• HEL1OS Threshold : {hel1os_result['threshold']}

• Unified Master Catalog Generated Successfully

Status: READY FOR NOWCASTING
"""
)

    except Exception as e:
        st.error(str(e))
        st.code(traceback.format_exc())

else:

    st.info(
        """
☀️ Solar Flare Intelligence System Ready

    Upload:
    • SoLEXS (.lc)
    • HEL1OS CDTE1 Part-1 (.fits)
    • HEL1OS CDTE1 Part-2 (.fits)

    Then click 🚀 Analyze Data to begin solar flare nowcasting.
    """
        )

    st.divider()

st.markdown("""
### 👨‍🚀 Team Anant

- Adarsh Jayprakash Mishra
- Deepanshi Rathee
- Hindavi Rajendra Kudu
- Disha Vartak

**Bharatiya Antariksh Hackathon 2026**
""")
