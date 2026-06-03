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
        background-color: #FFFFFF !important;
    }
    
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
    
    /* ── CUSTOM REPLICATED TOP NAVBAR ── */
    .header-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 50px 0px 20px 0px; 
        margin-bottom: 0px;
        border-bottom: 1px solid #F0F2F5;
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

    /* Minimalist text button links override for Home */
    div[data-testid="stButton"] button {
        background-color: transparent !important;
        color: #1A1A1A !important;
        border: none !important;
        padding: 8px 16px !important;
        font-weight: 500 !important;
        font-size: 15px !important;
        transition: color 0.2s ease-in-out !important;
        box-shadow: none !important;
        margin-top: 24px;
    }
    div[data-testid="stButton"] button:hover {
        color: #1F7A8C !important;
        background-color: transparent !important;
    }
    div[data-testid="stButton"] button[kind="primary"] {
        color: #1F7A8C !important;
        font-weight: 700 !important;
        border-bottom: 2px solid #1F7A8C !important;
        border-radius: 0px !important;
    }
    
    /* Clean corporate style for selectbox dropdown navigation headers */
    div[data-testid="stSelectbox"] label {
        display: none !important;
    }
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {
        border: none !important;
        background-color: transparent !important;
        font-weight: 500 !important;
        font-size: 15px !important;
        color: #1A1A1A !important;
    }
    
    /* External clickable mailto links styling */
    .nav-mail-link {
        display: inline-block;
        color: #1A1A1A !important;
        text-decoration: none !important;
        font-weight: 500 !important;
        font-size: 15px !important;
        padding: 8px 16px !important;
        margin-top: 28px;
        transition: color 0.2s ease-in-out !important;
    }
    .nav-mail-link:hover {
        color: #1F7A8C !important;
    }
    
    /* ── ASYMMETRIC ASSEMBLY-STYLE HERO GRID ── */
    .hero-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 80px 0px;
        background-color: #FFFFFF;
        gap: 40px;
    }
    .hero-left {
        flex: 1.1;
        max-width: 550px;
    }
    .hero-right {
        flex: 0.9;
        display: flex;
        justify-content: flex-end;
    }
    .assembly-title {
        color: #111111;
        font-size: 56px;
        font-weight: 700;
        line-height: 1.1;
        letter-spacing: -1px;
        margin-bottom: 24px;
    }
    .assembly-subtitle {
        color: #222222;
        font-size: 18px;
        font-weight: 400;
        line-height: 1.5;
        margin-bottom: 35px;
    }
    .hero-img-frame {
        width: 100%;
        max-width: 500px;
        border-radius: 4px;
    }
    
    .action-btn-link {
        display: inline-block;
        background-color: #2D9CDB !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        padding: 14px 28px !important;
        border-radius: 6px !important;
        text-decoration: none !important;
    }
    
    .section-title {
        color: #0A2540;
        font-size: 28px;
        font-weight: 700;
        margin-top: 60px;
        margin-bottom: 25px;
        letter-spacing: -0.5px;
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
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        padding-bottom: 40px;
    }
    .footer-brand-column {
        flex: 1.5;
        min-width: 250px;
    }
    .footer-logo {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .footer-tagline {
        color: #93A0AD;
        font-size: 14px;
        max-width: 300px;
    }
    .footer-links-column {
        flex: 1;
        min-width: 180px;
    }
    .footer-header {
        color: #1F7A8C;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 15px;
    }
    .footer-item {
        color: #93A0AD;
        font-size: 14px;
        margin-bottom: 10px;
    }
    .footer-bottom {
        max-width: 1200px;
        margin: 0 auto;
        padding-top: 25px;
        display: flex;
        justify-content: space-between;
        color: #637381;
        font-size: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Brand Top Bar Layout
st.markdown("""
<div class="header-nav">
    <div class="nav-brand">Master Health<span>Enterprise Revenue Operations</span></div>
</div>
""", unsafe_allow_html=True)

# Navigation Row Layout
nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns([1.2, 2.0, 3.2, 2.2, 1.2])

with nav_col1:
    go_home = st.button("Home", key="btn_home_nav", use_container_width=True)

with nav_col2:
    about_selection = st.selectbox(
        "About Us Dropdown",
        options=["About Us", "Overview", "Founder"],
        key="drop_about"
    )

with nav_col3:
    services_selection = st.selectbox(
        "Services Dropdown",
        options=[
            "Services Offered", "Cardiology", "Ophthalmology", "GI", 
            "Oncology", "Dermatology", "Orthopedic", "Mental & Behavioral Health"
        ],
        key="drop_services"
    )

with nav_col4:
    st.markdown('<a class="nav-mail-link" href="mailto:operations@masterhealth.us?subject=Free Consultation Request">Free Consultation</a>', unsafe_allow_html=True)

with nav_col5:
    st.markdown('<a class="nav-mail-link" href="mailto:info@masterhealth.us?subject=Corporate Inquiry">Contact</a>', unsafe_allow_html=True)

st.markdown("<br><hr style='border:0; border-top:1px solid #F0F2F5; margin-top:-20px;'><br>", unsafe_allow_html=True)

# ── 3. DYNAMIC RENDERING MATRIX ───────────────────────────────────────────────

if go_home:
    st.session_state.current_view = "Home"
elif about_selection in ["Overview", "Founder"]:
    st.session_state.current_view = about_selection
elif services_selection != "Services Offered":
    st.session_state.current_view = services_selection

if "current_view" not in st.session_state:
    st.session_state.current_view = "Home"

if st.session_state.current_view == "Home":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-left">
            <h1 class="assembly-title">Your Trusted RCM Partner</h1>
            <p class="assembly-subtitle">Getting paid for the care you deliver shouldn’t be this hard.</p>
            <br>
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
        st.markdown('<div class="corporate-card"><div class="card-heading">💻 Technology-Agnostic Framework</div><div class="card-text">We work directly inside your existing PM or EHR system. Whether your group utilizes Athenahealth, eClinicalWorks, AdvancedMD, or Epic, our teams log in via secure, encrypted pathways.</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="corporate-card"><div class="card-heading">🎓 Certified Professional Coders</div><div class="card-text">All charge routing and documentation checks are overlooked by specialists holding formal credentials (AAPC/AHIMA), ensuring accurate modifier tracking for multi-specialty practices.</div></div>', unsafe_allow_html=True)

elif st.session_state.current_view == "Overview":
    st.markdown('<p class="hero-title">Corporate Overview</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Master Health delivers institutional-grade revenue operation infrastructures engineered specifically to shield modern medical groups from overhead bloat, structural coding errors, and clearinghouse audit friction.</p>', unsafe_allow_html=True)

elif st.session_state.current_view == "Founder":
    st.markdown('<p class="hero-title">Executive Leadership</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Driven by advanced clinical, technical, and compliance insights, our executive framework bridges the gap between domestic clinical operations and secure high-efficiency processing systems.</p>', unsafe_allow_html=True)

else:
    st.markdown(f'<p class="hero-title">{st.session_state.current_view} RCM Solutions</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="hero-subtitle">Dedicated revenue cycle management workflows configured specifically to handle the structural modifiers, provider schedules, and payer rules engines unique to {st.session_state.current_view} medical practices.</p>', unsafe_allow_html=True)

# ── 4. ENTERPRISE FOOTER STRUCTURE WITH UPDATED SPECIALTIES ─────────────────
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
        </div>
    </div>
    <div class="footer-bottom">
        <div>© 2026 Master Health LLC. All rights reserved.</div>
        <div>Security Framework: OIG Compliant / AAPC Certified</div>
    </div>
</div>
""", unsafe_allow_html=True)
