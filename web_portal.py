import streamlit as st

# ── 1. GLOBAL INITIALIZATION & DESIGN OVERRIDES ──────────────────────────────────
st.set_page_config(
    page_title="Master Health | Enterprise Revenue Cycle Management", 
    page_icon="🏦", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Global CSS Overrides Block
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #FFFFFF !important;
    }
    
    /* Strip native dashboard properties */
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
    
    /* ── COMPLETE PURE-WEB HORIZONTAL NAVIGATION HEADER ── */
    .premium-navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 45px 0px 20px 0px; 
        border-bottom: 1px solid #F0F2F5;
        background-color: #FFFFFF;
        position: relative;
        z-index: 999999 !important;
    }
    
    .nav-brand-wrapper {
        display: flex;
        align-items: baseline;
    }
    
    .nav-brand-main {
        color: #0A2540;
        font-size: 26px;
        font-weight: 700;
        letter-spacing: -0.5px;
        text-decoration: none !important;
    }
    
    .nav-brand-sub {
        color: #1F7A8C;
        font-weight: 500;
        font-size: 13px;
        margin-left: 12px;
        text-transform: uppercase;
        letter-spacing: 0.75px;
    }
    
    .nav-menu-links {
        display: flex;
        align-items: center;
        gap: 4px;
    }
    
    /* Dropdown Architecture */
    .menu-dropdown {
        position: relative;
        display: inline-block;
    }
    
    .menu-tab-link {
        color: #1A1A1A !important;
        background: transparent;
        border: none;
        padding: 10px 18px;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        font-size: 15px;
        text-decoration: none !important;
        cursor: pointer;
        transition: color 0.15s ease;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    
    .menu-tab-link:hover {
        color: #1F7A8C !important;
    }
    
    /* Popover Dropdown Boxes */
    .dropdown-overlay-box {
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        background-color: #FFFFFF;
        min-width: 260px;
        box-shadow: 0px 12px 30px rgba(0, 0, 0, 0.06), 0px 4px 12px rgba(0, 0, 0, 0.03);
        border: 1px solid #EFEFEF;
        border-radius: 6px;
        padding: 8px 0px;
        z-index: 9999999 !important;
        margin-top: 4px;
    }
    
    .menu-dropdown:hover .dropdown-overlay-box {
        display: block;
    }
    
    .dropdown-overlay-box a {
        display: block !important;
        padding: 11px 20px !important;
        color: #4A4A4A !important;
        text-decoration: none !important;
        font-size: 14.5px !important;
        font-weight: 400 !important;
        transition: background 0.15s ease, color 0.15s ease !important;
    }
    
    .dropdown-overlay-box a:hover {
        background-color: #F8F9FA !important;
        color: #1F7A8C !important;
    }
    
    /* ── PREMIUM CORPORATE HERO SPLIT ── */
    .hero-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 90px 0px;
        background-color: #FFFFFF;
        gap: 60px;
    }
    
    .hero-left {
        flex: 1.1;
        max-width: 560px;
    }
    
    .hero-right {
        flex: 0.9;
        display: flex;
        justify-content: flex-end;
    }
    
    .assembly-title {
        color: #111111;
        font-size: 58px;
        font-weight: 700;
        line-height: 1.1;
        letter-spacing: -1.5px;
        margin-bottom: 22px;
    }
    
    .assembly-subtitle {
        color: #333333;
        font-size: 19px;
        font-weight: 400;
        line-height: 1.55;
        margin-bottom: 35px;
    }
    
    .hero-img-frame {
        width: 100%;
        max-width: 520px;
        border-radius: 6px;
    }
    
    .action-btn-link {
        display: inline-block;
        background-color: #2D9CDB !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        padding: 15px 32px !important;
        border-radius: 6px !important;
        text-decoration: none !important;
    }
    
    .section-title {
        color: #0A2540;
        font-size: 28px;
        font-weight: 700;
        margin-top: 40px;
        margin-bottom: 25px;
        letter-spacing: -0.5px;
    }
    
    .corporate-card {
        background-color: #FFFFFF;
        padding: 35px;
        border-radius: 8px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.02);
        border: 1px solid #EFEFEF;
        height: 100%;
        margin-bottom: 20px;
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
        line-height: 1.65;
    }
    
    /* ── DEEP FOOTER STRUCTURE ── */
    .enterprise-footer {
        background-color: #0A2540;
        color: #FFFFFF;
        padding: 70px 40px 35px 40px;
        margin-top: 90px;
        margin-left: -200px;
        margin-right: -200px;
    }
    
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        padding-bottom: 45px;
    }
    
    .footer-brand-column {
        flex: 1.4;
        min-width: 260px;
    }
    
    .footer-logo {
        font-size: 23px;
        font-weight: 700;
        margin-bottom: 12px;
    }
    
    .footer-tagline {
        color: #93A0AD;
        font-size
