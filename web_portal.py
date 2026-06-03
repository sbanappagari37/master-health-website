import streamlit as st

# ── 1. GLOBAL INITIALIZATION & DESIGN FLAGS ──────────────────────────────────
st.set_page_config(
    page_title="Master Health | Enterprise Revenue Cycle Management", 
    page_icon="🏦", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ── 2. UNIFIED STYLING & HORIZONTAL NAVBAR LAYER ────────────────────
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #FFFFFF !important;
    }
    
    /* Eradicate native Streamlit headers, footers, and sidebars */
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
    
    /* HORIZONTAL NAVIGATION BAR HEADER */
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
    
    /* Custom Dropdown Triggers */
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
    
    /* Popover Menu Dropdown Boxes */
    .dropdown-overlay-box {
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        background-color: #FFFFFF;
        min-width: 270px;
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
    
    /* CORPORATE HERO GRIDS */
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
    
    /* CORPORATE DEEP FOOTER */
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
        font-size: 14px;
        max-width: 280px;
    }
    
    .footer-links-column {
        flex: 1;
        min-width: 170px;
    }
    
    .footer-header {
        color: #1F7A8C;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 18px;
    }
    
    .footer-item {
        color: #93A0AD;
        font-size: 14px;
        margin-bottom: 12px;
    }
    
    .footer-bottom {
        max-width: 1200px;
        margin: 0 auto;
        padding-top: 30px;
        display: flex;
        justify-content: space-between;
        color: #637381;
        font-size: 12.5px;
    }
    </style>

    <div class="premium-navbar">
        <div class="nav-brand-wrapper">
            <a href="?view=Home" class="nav-brand-main" target="_self">Master Health</a>
            <div class="nav-brand-sub">Enterprise Revenue Operations</div>
        </div>
        <div class="nav-menu-links">
            <a href="?view=Home" class="menu-tab-link" target="_self">Home</a>
            
            <div class="menu-dropdown">
                <button class="menu-tab-link">About Us ▾</button>
                <div class="dropdown-overlay-box">
                    <a href="?view=Overview" target="_self">Overview</a>
                    <a href="?view=Founder" target="_self">Founder</a>
                </div>
            </div>
            
            <div class="menu-dropdown">
                <button class="menu-tab-link">Services ▾</button>
                <div class="dropdown-overlay-box">
                    <a href="?view=Cardiology" target="_self">Cardiology</a>
                    <a href="?view=Ophthalmology" target="_self">Ophthalmology</a>
                    <a href="?view=GI" target="_self">GI</a>
                    <a href="?view=Oncology" target="_self">Oncology</a>
                    <a href="?view=Dermatology" target="_self">Dermatology</a>
                    <a href="?view=Orthopedic" target="_self">Orthopedic</a>
                    <a href="?view=Mental_Behavioral" target="_self">Mental & Behavioral Health</a>
                </div>
            </div>
            
            <a class="menu-tab-link" href="mailto:operations@masterhealth.us?subject=Free Consultation Request">Free Consultation</a>
            <a class="menu-tab-link" href="mailto:info@masterhealth.us?subject=Corporate Inquiry">Contact</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Track active view variables directly through query tokens
current_view = st.query_params.get("view", "Home")

# ── 3. DYNAMIC CONTENT RENDERING MODULES ─────────────────────────────────────

if current_view == "Home":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-left">
            <h1 class="assembly-title">Your Trusted RCM Partner</h1>
            <p class="assembly-subtitle">Getting paid for the care you deliver shouldn’t be this hard.</p>
            <a href="mailto:operations@masterhealth.us?subject=Free Consultation Request" class="action-btn-link">Speak to an Expert</a>
        </div>
        <div class="hero-right">
            <img class="hero-img-frame" src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&w=600&q=80">
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="section-title">Institutional Protections & System Adaptability</p>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="corporate-card"><div class="card-heading">🔒 Airtight OIG & HIPAA Compliance</div><div class="card-text">Our workflows strictly follow Office of Inspector General (OIG) guidelines. We deploy ongoing chart reviews to catch structural coding errors before they flag clearinghouse audits.</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="corporate-card"><div class="corporate-card"><div class="card-heading">💻 Technology-Agnostic Framework</div><div class="card-text">We work directly inside your existing PM or EHR system. Whether your group utilizes Athenahealth, eClinicalWorks, AdvancedMD, or Epic, our teams log in via secure, encrypted pathways.</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="corporate-card"><div class="card-heading">🎓 Certified Professional Coders</div><div class="card-text">All charge routing and documentation checks are overlooked by specialists holding formal credentials (AAPC/AHIMA), ensuring accurate modifier tracking for multi-specialty practices.</div></div>', unsafe_allow_html=True)

elif current_view == "Overview":
    st.markdown('<p class="hero-title" style="margin-top:60px;">Corporate Overview</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Master Health delivers institutional-grade revenue operation infrastructures engineered specifically to shield modern medical groups from overhead bloat, structural coding errors, and clearinghouse audit friction.</p>', unsafe_allow_html=True)

elif current_view == "Founder":
    st.markdown('<p class="hero-title" style="margin-top:60px;">Executive Leadership</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Driven by advanced clinical, technical, and compliance insights, our executive framework bridges the gap between domestic clinical operations and secure high-efficiency processing systems.</p>', unsafe_allow_html=True)

else:
    # Individual Specialty Page Viewport Fallbacks
    clean_title = current_view.replace("_", " & ")
    st.markdown(f'<p class="hero-title" style="margin-top:60px;">{clean_title} Revenue Management</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="hero-subtitle">Master Health provides tailored billing guidelines, claim scrubbing sub-routines, and optimization protocols built explicitly to support institutional practices specializing in {clean_title}.</p>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="corporate-card" style="border-top: 4px solid #1F7A8C;">
        <div class="card-heading">{clean_title} Workflow Optimization Metrics</div>
        <div class="card-text" style="line-height:2;">
            • Specialized ICD-10 crosswalk monitoring ensuring error-free documentation posting.<br>
            • Proactive modifier verification (e.g., global procedural surgical timelines).<br>
            • Persistent aging follow-up loops targeted toward discipline-specific commercial insurance policies.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── 4. ENTERPRISE FOOTER MATRIX ────────────────────────────────────────────────
st.markdown("""
<div class="enterprise-footer">
    <div class="footer-content">
        <div class="footer-brand-column">
            <div class="footer-logo">Master Health</div>
            <div class="footer-tagline">Institutional Revenue Operations and Enterprise Cycle Management Solutions for Independent Practices.</div>
        </div>
        <div class="footer-links-column">
            <div class="footer-header">Solutions</div>
            <div class="footer-item">End-to-End Billing</div>
            <div class="footer-item">Denial Optimization</div>
            <div class="footer-item">Payer Fee Auditing</div>
        </div>
        <div class="footer-links-column">
            <div class="footer-header">Expertise</div>
            <div class="footer-item">Cardiology</div>
            <div class="footer-item">Ophthalmology</div>
            <div class="footer-item">GI</div>
            <div class="footer-item">Oncology</div>
            <div class="footer-item">Dermatology</div>
            <div class="footer-item">Orthopedic</div>
            <div class="footer-item">Mental & Behavioral Health</div>
        </div>
        <div class="footer-links-column">
            <div class="footer-header">Contact & Info</div>
            <div class="footer-item">info@masterhealth.us</div>
            <div class="footer-item">San Ramon, California</div>
            <div class="footer-item" style="color: #00D4B2; font-size:12px; margin-top:10px;">🔒 HIPAA Compliant Network</div>
        </div>
    </div>
    <div class="footer-bottom">
        <div>© 2026 Master Health LLC. All rights reserved.</div>
        <div>Security Framework: OIG Compliant / AAPC Certified</div>
    </div>
</div>
""", unsafe_allow_html=True)
