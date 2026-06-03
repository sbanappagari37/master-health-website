import streamlit as st

# ── 1. GLOBAL INITIALIZATION & DESIGN OVERRIDES ──────────────────────────────────
st.set_page_config(
    page_title="Master Health | Enterprise Revenue Cycle Management", 
    page_icon="🏦", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #FAFAFA !important;
    }
    
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    header { visibility: hidden !important; height: 0px !important; }
    footer { visibility: hidden !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        max-width: 1200px !important;
    }
    
    .header-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 65px 0px 20px 0px; 
        margin-bottom: 20px;
        border-bottom: 1px solid #EAEAEA;
    }
    .nav-brand {
        color: #0A2540;
        font-size: 26px;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    .nav-brand span {
        color: #1F7A8C;
        font-weight: 400;
        font-size: 13px;
        margin-left: 10px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    div[data-testid="stButton"] button {
        background-color: transparent !important;
        color: #637381 !important;
        border: none !important;
        padding: 8px 16px !important;
        font-weight: 500 !important;
        font-size: 15px !important;
        transition: color 0.2s ease-in-out !important;
        box-shadow: none !important;
    }
    div[data-testid="stButton"] button:hover {
        color: #1F7A8C !important;
        background-color: transparent !important;
    }
    div[data-testid="stButton"] button[kind="primary"] {
        color: #0A2540 !important;
        font-weight: 700 !important;
        border-bottom: 2px solid #1F7A8C !important;
        border-radius: 0px !important;
    }
    
    .hero-title {
        color: #0A2540;
        font-size: 46px;
        font-weight: 700;
        line-height: 1.15;
        letter-spacing: -1px;
        margin-bottom: 18px;
    }
    .hero-subtitle {
        color: #637381;
        font-size: 19px;
        font-weight: 400;
        line-height: 1.5;
        max-width: 900px;
        margin-bottom: 40px;
    }
    .section-title {
        color: #0A2540;
        font-size: 28px;
        font-weight: 700;
        margin-top: 50px;
        margin-bottom: 25px;
        letter-spacing: -0.5px;
    }
    .section-subtitle {
        color: #637381;
        font-size: 16px;
        margin-top: -20px;
        margin-bottom: 30px;
    }
    
    .corporate-card {
        background-color: #FFFFFF;
        padding: 32px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        border: 1px solid #EFEFEF;
        height: 100%;
        margin-bottom: 20px;
    }
    .card-icon {
        font-size: 26px;
        margin-bottom: 14px;
    }
    .card-heading {
        color: #0A2540;
        font-size: 19px;
        font-weight: 600;
        margin-bottom: 12px;
    }
    .card-text {
        color: #637381;
        font-size: 14.5px;
        line-height: 1.6;
    }
    
    .metric-wrapper {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 8px;
        border: 1px solid #EFEFEF;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.01);
    }
    .metric-num {
        color: #1F7A8C;
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .metric-lbl {
        color: #0A2540;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .enterprise-footer {
        background-color: #0A2540;
        color: #FFFFFF;
        padding: 60px 40px 30px 40px;
        margin-top: 80px;
        margin-left: -200px;
        margin-right: -200px;
    }
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        display: flex
