import streamlit as st

# ── 1. GLOBAL INITIALIZATION & REGULATORY DESIGN TOKENS ─────────────────────
st.set_page_config(
    page_title="Master Health | Enterprise Revenue Cycle Management", 
    page_icon="🏦", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Global CSS Master Layer
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #FFFFFF !important;
    }
    
    /* Strict eradication of app infrastructure watermarks and padding rails */
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    header { visibility: hidden !important; height: 0px !important; }
    footer { visibility: hidden !important; height: 0px !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        max-width: 1200px !important;
    }
    
    /* ── REPLICATED TRUE-WEB NAVIGATION BAR ── */
    .premium-navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 45px 0px 20px 0px; 
        border-bottom: 1px solid #F0F2F5;
        background-color: #FFFFFF;
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
    
    /* Popover Menu Block Styles */
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
        z-index: 999999 !important;
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
        box-shadow: 0px 20px 40px rgba(0,0,0,0.02);
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
        box-shadow: 0px 4px 10px rgba(45, 156, 219, 0.2);
        transition: transform 0.15s ease, background-color 0.15s ease !important;
    }
