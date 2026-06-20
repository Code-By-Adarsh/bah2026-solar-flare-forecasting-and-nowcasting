import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Solar Flare Intelligence System",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS ARCHITECTURE FOR EXACT MATCH ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght=400;500;600;700&display=swap');

/* Global Reset */
html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    font-family: 'Inter', sans-serif !important;
}

/* Sidebar Styling */
.sidebar-title-container {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 28px;
    margin-top: -10px;
}
.sidebar-main-title {
    font-weight: 700;
    font-size: 15px;
    letter-spacing: 0.5px;
    line-height: 1.2;
}
.sidebar-sub-title {
    color: #64748B;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.5px;
}

.nav-item {
    display: flex;
    align-items: center;
    padding: 10px 14px;
    border-radius: 8px;
    margin-bottom: 4px;
    font-size: 13.5px;
    font-weight: 500;
    color: #94A3B8;
}
.nav-icon {
    margin-right: 12px;
    font-size: 15px;
}

/* --- ALERT BOX --- */
.alert-card {
    background: linear-gradient(135deg, #250A0A 0%, #140505 100%) !important;
    border: 1px solid #EF4444 !important;
    box-shadow: 0px 0px 15px rgba(239, 68, 68, 0.25) !important;
    padding: 16px;
    border-radius: 12px;
    height: 130px;
    display: flex;
    align-items: center;
    gap: 14px;
}
.alert-icon-box {
    background: #4C0519 !important;
    border: 1px solid #EF4444 !important;
    box-shadow: 0px 0px 8px rgba(239, 68, 68, 0.4) !important;
    border-radius: 50%;
    width: 52px;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
}
.alert-content h4 {
    color: #EF4444 !important;
    margin: 0;
    font-size: 14.5px;
    font-weight: 700;
    letter-spacing: 0.5px;
}
.alert-content p {
    color: #94A3B8;
    margin: 3px 0 10px 0;
    font-size: 11.5px;
}
.badge-wrapper {
    display: flex;
    gap: 8px;
}
.custom-badge {
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(239, 68, 68, 0.3);
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 10.5px;
    line-height: 1.3;
}
.custom-badge span { color: #64748B; display: block; font-size: 9px; font-weight: 500; }

/* Dynamic Theme Cards */
.stat-card {
    background-color: var(--secondary-background-color);
    border: 1px solid rgba(148, 163, 184, 0.1);
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
    padding: 16px;
    border-radius: 12px;
    height: 130px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.title-yellow { color: #F59E0B !important; font-size: 14px; font-weight: 600; }
.title-green { color: #10B981 !important; font-size: 14px; font-weight: 600; }
.title-normal { color: #94A3B8; font-size: 13px; font-weight: 500; }
.large-icon { font-size: 18px; margin-right: 5px; }

.stat-value-white {
    color: #FFFFFF !important;
    font-size: 30px;
    font-weight: 700;
    margin-top: 5px;
    margin-bottom: auto;
}
.stat-sub { color: #64748B; font-size: 11.5px; }

/* --- EXACT SENSOR CONFIRMATION SECTION (WHITE-DARK SS LOOK) --- */
.sensor-section-header {
    color: #94A3B8;
    font-size: 11.5px;
    font-weight: 700;
    margin-bottom: 10px;
    letter-spacing: 0.5px;
}
.sensor-card-panel {
    background-color: var(--secondary-background-color);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 10px;
    padding: 12px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 64px;
}
.sensor-left-group {
    display: flex;
    align-items: center;
    gap: 12px;
}
.sensor-checkbox-mock {
    width: 18px;
    height: 18px;
    border: 1.5px solid #64748B;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: transparent;
    font-size: 11px;
    font-weight: bold;
}
.sensor-checked {
    border-color: #10B981 !important;
    background-color: #10B981 !important;
    color: #FFFFFF !important;
}
.sensor-details h5 {
    margin: 0;
    font-size: 13.5px;
    font-weight: 600;
    color: #F1F5F9;
}
.sensor-details h5 span {
    color: #64748B;
    font-size: 11.5px;
    font-weight: 400;
    margin-left: 4px;
}
.sensor-status-text {
    font-size: 12px;
    font-weight: 500;
    margin-top: 1px;
}
.status-text-active { color: #10B981; }
.status-text-idle { color: #64748B; }

/* Combined Result Specifics */
.combined-panel {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.combined-panel span {
    color: #64748B;
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.combined-panel b {
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.3px;
    margin-top: 2px;
}
.combined-active { color: #10B981; }
.combined-idle { color: #64748B; }

/* Lower Panels */
.widget-panel {
    background-color: var(--secondary-background-color);
    border: 1px solid rgba(148, 163, 184, 0.1);
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    border-radius: 12px;
    padding: 18px;
    height: 275px;
    box-sizing: border-box;
}
.widget-header {
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 16px;
    letter-spacing: 0.5px;
}
.reason-row {
    color: #94A3B8;
    font-size: 12px;
    margin-bottom: 11px;
    display: flex;
    align-items: flex-start;
    gap: 8px;
}
.reason-tick { color: #10B981; font-weight: 700; }

.tech-item {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid rgba(148, 163, 184, 0.1);
    font-size: 12px;
}
.tech-lbl { color: #94A3B8; }

.bottom-notice {
    background-color: var(--secondary-background-color);
    border: 1px solid rgba(129, 140, 248, 0.2);
    color: #818CF8;
    padding: 11px 14px;
    border-radius: 8px;
    font-size: 11.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 20px;
}

.event-table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
    font-size: 12px;
}
.event-table th {
    color: #64748B;
    font-weight: 500;
    padding: 10px 6px;
    border-bottom: 1px solid rgba(148, 163, 184, 0.1);
}
.event-table td { padding: 14px 6px; }
.status-pill {
    background: #064E3B;
    color: #34D399;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 10.5px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "triggered" not in st.session_state:
    st.session_state.triggered = False

# --- SIDEBAR UI ---
with st.sidebar:
    st.markdown("""
    <div class="sidebar-title-container">
        <span style='font-size: 24px; color: #F59E0B;'>☀️</span>
        <div>
            <div class="sidebar-main-title">SOLAR FLARE</div>
            <div class="sidebar-sub-title">INTELLIGENCE SYSTEM</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    navigation_map = [
        ("Dashboard", "🏠"), ("Nowcasting", "👁️‍🗨️"), ("Forecasting", "📈"),
        ("Events Catalog", "📋"), ("Data Explorer", "🧭"), ("Reports", "📄"),
        ("Settings", "⚙️"), ("About", "ℹ️")
    ]
    
    for label, icon in navigation_map:
        st.markdown(f" <div class='nav-item'><span class='nav-icon'>{icon}</span>{label}</div>", unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color: rgba(148, 163, 184, 0.15); margin: 5px 0;'/><br>", unsafe_allow_html=True)
    st.file_uploader("Upload SoLEXS (.lc)", type=["lc", "csv"], key="solexs_live")
    st.file_uploader("Upload HEL1OS (.lc)", type=["lc", "csv"], key="hel1os_live")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Analyze Data 🚀", use_container_width=True, type="primary"):
        st.session_state.triggered = True

# --- HEADER TITLES ---
left_panel, right_panel = st.columns([3, 1])
with left_panel:
    st.markdown("<h2 style='margin:0; font-weight:700; font-size:26px;'>Nowcasting</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748B; font-size:13.5px; margin: 4px 0 20px 0;'>Real-time detection and analysis of solar flares using SoLEXS and HEL1OS data</p>", unsafe_allow_html=True)
with right_panel:
    st.markdown("""
    <div style='background: var(--secondary-background-color); border: 1px solid rgba(148, 163, 184, 0.1); padding: 10px 14px; border-radius: 8px; text-align: right; margin-top: 5px;'>
        <div style='color: #64748B; font-size: 10px; font-weight:500;'>📅 Analysis Time (UTC)</div>
        <div style='font-weight: 600; font-size: 13px; margin-top:2px;'>14 Jun 2026, 09:15:30</div>
    </div>
    """, unsafe_allow_html=True)

# --- DATA GENERATION ---
t_axis = pd.date_range(start="2026-06-14 07:30", end="2026-06-14 10:15", freq="1min")
solexs_wave = np.random.normal(10, 0.7, len(t_axis))
hel1os_wave = np.random.normal(12, 0.5, len(t_axis))

if st.session_state.triggered:
    v_peak, v_time, v_dur, v_tot, v_conf = "59", "08:56", "14", "1", "91%"
    t_mean, t_std, t_dyn, t_hi, t_tot = 5.04, 4.57, 18.74, 2015, 86400
    flare_envelope = [idx for idx, timestamp in enumerate(t_axis) if timestamp.hour == 8 and 45 <= timestamp.minute <= 59]
    solexs_wave[flare_envelope] += np.exp(-((np.arange(len(flare_envelope)) - 11) ** 2) / 10) * 54
    hel1os_wave[flare_envelope] += np.exp(-((np.arange(len(flare_envelope)) - 11) ** 2) / 8) * 27
else:
    v_peak, v_time, v_dur, v_tot, v_conf = "0", "--:--", "0", "0", "0%"
    t_mean, t_std, t_dyn, t_hi, t_tot = 0.00, 0.00, 0.00, 0, 0

# --- STRIP METRIC CARDS ---
c1, c2, c3, c4, c5 = st.columns([1.4, 1, 1, 1, 1])

with c1:
    if st.session_state.triggered:
        st.markdown(f"""
        <div class="alert-card">
            <div class="alert-icon-box">☀️</div>
            <div class="alert-content">
                <h4>SOLAR FLARE DETECTED</h4>
                <p>Active event found in the uploaded data</p>
                <div class="badge-wrapper">
                    <div class="custom-badge"><span>Event ID</span><b style="color:#E2E8F0;">FLR-001</b></div>
                    <div class="custom-badge"><span>Confidence</span><b style="color:#F59E0B;">{v_conf}</b></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="alert-card" style="background: var(--secondary-background-color); border:1px solid rgba(148, 163, 184, 0.1); box-shadow:none !important;">
            <div class="alert-icon-box" style="background:rgba(148, 163, 184, 0.1); border-color:transparent; box-shadow:none !important;">💤</div>
            <div class="alert-content">
                <h4 style="color:#94A3B8;">SYSTEM STANDBY</h4>
                <p style="color:#64748B;">Upload telemetry files to begin analysis</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

with c2: 
    st.markdown(f'<div class="stat-card"><div class="title-yellow"><span class="large-icon">🔥</span>Peak Count</div><div class="stat-value-white">{v_peak}</div><div class="stat-sub">counts</div></div>', unsafe_allow_html=True)
with c3: 
    st.markdown(f'<div class="stat-card"><div class="title-green"><span class="large-icon">⏱️</span>Peak Time</div><div class="stat-value-white" style="font-size:22px; margin-top:14px;">{v_time} <span style="font-size:12px; color:#64748B; font-weight:normal;">UTC</span></div><div class="stat-sub">14 Jun 2026</div></div>', unsafe_allow_html=True)
with c4: 
    st.markdown(f'<div class="stat-card"><div class="title-normal"><span class="large-icon">⏳</span>Duration</div><div class="stat-value-white">{v_dur}</div><div class="stat-sub">minutes</div></div>', unsafe_allow_html=True)
with c5: 
    st.markdown(f'<div class="stat-card"><div class="title-normal">🔲 Total Events</div><div class="stat-value-white">{v_tot}</div><div class="stat-sub">detected</div></div>', unsafe_allow_html=True)

st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

# --- SENSOR CONFIRMATION SECTION (AS IT IS SS LOOK) ---
st.markdown('<div class="sensor-section-header">SENSOR CONFIRMATION</div>', unsafe_allow_html=True)
s1, s2, s3 = st.columns(3)

if st.session_state.triggered:
    with s1:
        st.markdown("""
        <div class="sensor-card-panel">
            <div class="sensor-left-group">
                <div class="sensor-checkbox-mock sensor-checked">✓</div>
                <div class="sensor-details">
                    <h5>SoLEXS<span>(Soft X-ray)</span></h5>
                    <div class="sensor-status-text status-text-active">Flare Detected</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with s2:
        st.markdown("""
        <div class="sensor-card-panel">
            <div class="sensor-left-group">
                <div class="sensor-checkbox-mock sensor-checked">✓</div>
                <div class="sensor-details">
                    <h5>HEL1OS<span>(Hard X-ray)</span></h5>
                    <div class="sensor-status-text status-text-active">Flare Detected</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with s3:
        st.markdown("""
        <div class="sensor-card-panel">
            <div class="combined-panel">
                <span>Combined Result</span>
                <b class="combined-active">CONFIRMED EVENT</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
else:
    with s1:
        st.markdown("""
        <div class="sensor-card-panel">
            <div class="sensor-left-group">
                <div class="sensor-checkbox-mock">-</div>
                <div class="sensor-details" style="opacity: 0.5;">
                    <h5>SoLEXS<span>(Soft X-ray)</span></h5>
                    <div class="sensor-status-text status-text-idle">Offline</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with s2:
        st.markdown("""
        <div class="sensor-card-panel">
            <div class="sensor-left-group">
                <div class="sensor-checkbox-mock">-</div>
                <div class="sensor-details" style="opacity: 0.5;">
                    <h5>HEL1OS<span>(Hard X-ray)</span></h5>
                    <div class="sensor-status-text status-text-idle">Offline</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with s3:
        st.markdown("""
        <div class="sensor-card-panel">
            <div class="combined-panel">
                <span>Combined Result</span>
                <b class="combined-idle">IDLE</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)

# --- CHART GRAPHS LINE PLOTS ---
g1, g2 = st.columns(2)

with g1:
    f1 = go.Figure()
    f1.add_trace(go.Scatter(x=t_axis, y=solexs_wave, mode='lines', line=dict(color='#A855F7', width=2)))
    if st.session_state.triggered:
        f1.add_vrect(x0="2026-06-14 08:35", x1="2026-06-14 09:15", fillcolor="#A855F7", opacity=0.12, line_width=1, line_dash="dash", line_color="#A855F7")
    f1.update_layout(
        title="SoLEXS Light Curve (Soft X-ray)", title_font=dict(size=13, family="Inter", weight="bold"),
        template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=40, r=20, t=45, b=30), height=270,
        xaxis=dict(gridcolor="rgba(148, 163, 184, 0.1)", tickformat="%H:%M"), yaxis=dict(gridcolor="rgba(148, 163, 184, 0.1)", title="Counts")
    )
    st.plotly_chart(f1, use_container_width=True)

with g2:
    f2 = go.Figure()
    f2.add_trace(go.Scatter(x=t_axis, y=hel1os_wave, mode='lines', line=dict(color='#38BDF8', width=2)))
    if st.session_state.triggered:
        f2.add_vrect(x0="2026-06-14 08:35", x1="2026-06-14 09:15", fillcolor="#38BDF8", opacity=0.1, line_width=1, line_dash="dash", line_color="#38BDF8")
    f2.update_layout(
        title="HEL1OS Light Curve (Hard X-ray)", title_font=dict(size=13, family="Inter", weight="bold"),
        template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=40, r=20, t=45, b=30), height=270,
        xaxis=dict(gridcolor="rgba(148, 163, 184, 0.1)", tickformat="%H:%M"), yaxis=dict(gridcolor="rgba(148, 163, 184, 0.1)")
    )
    st.plotly_chart(f2, use_container_width=True)

# --- LOWER INTEL BLOCKS MATRIX ---
b1, b2, b3 = st.columns([1.3, 2, 1.2])

with b1:
    if st.session_state.triggered:
        st.markdown("""
        <div class="widget-panel">
            <div class="widget-header">🧠 DETECTION REASON</div>
            <div class="reason-row"><span class="reason-tick">✓</span> Count exceeded the dynamic threshold</div>
            <div class="reason-row"><span class="reason-tick">✓</span> Sustained elevated activity detected</div>
            <div class="reason-row"><span class="reason-tick">✓</span> Peak Count reached 59</div>
            <div class="reason-row"><span class="reason-tick">✓</span> Confirmed by SoLEXS (Soft X-ray)</div>
            <div class="reason-row"><span class="reason-tick">✓</span> Confirmed by HEL1OS (Hard X-ray)</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="widget-panel">
            <div class="widget-header">🧠 DETECTION REASON</div>
            <p style='color:#64748B; font-size:12px;'>Waiting for data analysis pipeline...</p>
        </div>
        """, unsafe_allow_html=True)

with b2:
    if st.session_state.triggered:
        st.markdown("""
        <div class="widget-panel" style="padding-bottom:10px;">
            <div class="widget-header">📋 DETECTED EVENTS</div>
            <table class="event-table">
              <tr>
                <th>Event ID</th>
                <th>Start Time (UTC)</th>
                <th style="color:#EF4444;">Peak Time (UTC)</th>
                <th>End Time (UTC)</th>
                <th>Peak Count</th>
                <th>Confidence</th>
                <th>Status</th>
              </tr>
              <tr>
                <td>FLR-001</td>
                <td>08:49</td>
                <td style="color: #EF4444; font-weight:700;">08:56</td>
                <td>09:03</td>
                <td>59</td>
                <td style="color: #EF4444; font-weight:600;">91%</td>
                <td><span class="status-pill">Active</span></td>
              </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="widget-panel">
            <div class="widget-header">📋 DETECTED EVENTS</div>
            <p style='color:#64748B; font-size:12px;'>No anomaly events present in memory buffer.</p>
        </div>
        """, unsafe_allow_html=True)

with b3:
    st.markdown(f"""
    <div class="widget-panel">
        <div class="widget-header">⚙️ TECHNICAL DETAILS</div>
        <div class="tech-item"><span class="tech-lbl">Mean Count</span><span class="tech-val"><b>{t_mean:.2f}</b></span></div>
        <div class="tech-item"><span class="tech-lbl">Standard Deviation</span><span class="tech-val"><b>{t_std:.2f}</b></span></div>
        <div class="tech-item"><span class="tech-lbl">Dynamic Threshold</span><span class="tech-val"><b>{t_dyn:.2f}</b></span></div>
        <div class="tech-item"><span class="tech-lbl">High Activity Points</span><span class="tech-val"><b>{t_hi}</b></span></div>
        <div class="tech-item" style="border-bottom:none;"><span class="tech-lbl">Total Data Points</span><span class="tech-val"><b>{t_tot:,}</b></span></div>
    </div>
    """, unsafe_allow_html=True)

# --- SYSTEM NOTICE BAR ---
st.markdown("""
<div class="bottom-notice">
    <span style="font-size:13px; font-weight:bold;">ℹ️</span> Nowcasting analysis is performed on the uploaded data. Results represent the period covered by the dataset.
</div>
""", unsafe_allow_html=True)