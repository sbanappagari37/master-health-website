import streamlit as st

# ── 1. PAGE SETUP & STRUCTURAL CANCEL FLAGS ──────────────────────────────────
st.set_page_config(
    page_title="Master Health | Enterprise Revenue Cycle Management", 
    page_icon="🏦", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Global CSS Injector to strip Streamlit styling and apply enterprise design tokens
st.markdown("""
    <style>
    /* Import Premium Corporate Typography */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #FAFAFA !important;
    }
    
    /* Completely eliminate all native Streamlit headers, footers, and sidebars */
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    header { visibility: hidden !important; height: 0px !important; }
    footer { visibility: hidden !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* Block Wrapper Resets */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        max-width: 1200px !important;
    }
    
    /* ── CUSTOM CORPORATE TOP NAVBAR ── */
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

    /* ── MINIMALIST CORPORATE NAVBAR LINKS ── */
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
    
    /* ── PREMIUM ENTERPRISE TEXT STYLING ── */
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
    
    /* ── ASSEMBLY-STYLE CARDS ── */
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
    
    /* ── METRIC BLOCK STYLING ── */
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
    
    /* ── HIGH-END CORPORATE FOOTER ── */
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
        margin-bottom: 20px;
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
        line-height: 1.5;
    }
    .footer-links-column {
        flex: 1;
        min-width: 180px;
        margin-bottom: 20px;
    }
    .footer-header {
        color: #1F7A8C;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
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
    
    div[data-testid="stForm"] {
        border: none !important;
        background-color: #FFFFFF !important;
        padding: 0px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ── 2. SESSION STATE NAVIGATION TRACKER ──────────────────────────────────────
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home & Compliance"

def set_page(page_name):
    st.session_state.current_page = page_name

# Render Fixed Enterprise Top Bar Layout
st.markdown("""
<div class="header-nav">
    <div class="nav-brand">Master Health<span>Enterprise Revenue Operations</span></div>
</div>
""", unsafe_allow_html=True)

# Navigation Grid with Contact Tab Added
nav1, nav2, nav3, nav4, nav5 = st.columns([1.5, 1.8, 1.8, 2.2, 1.5])
with nav1:
    if st.button("Home & Compliance", key="btn_home", use_container_width=True, type="secondary" if st.session_state.current_page != "Home & Compliance" else "primary"):
        set_page("Home & Compliance")
with nav2:
    if st.button("End-to-End RCM Pillars", key="btn_pillars", use_container_width=True, type="secondary" if st.session_state.current_page != "End-to-End RCM Pillars" else "primary"):
        set_page("End-to-End RCM Pillars")
with nav3:
    if st.button("The Onshore Advantage", key="btn_model", use_container_width=True, type="secondary" if st.session_state.current_page != "The Onshore Advantage" else "primary"):
        set_page("The Onshore Advantage")
with nav4:
    if st.button("ROI & Free Billing Assessment", key="btn_roi", use_container_width=True, type="secondary" if st.session_state.current_page != "ROI & Free Billing Assessment" else "primary"):
        set_page("ROI & Free Billing Assessment")
with nav5:
    if st.button("Contact Us", key="btn_contact", use_container_width=True, type="secondary" if st.session_state.current_page != "Contact Us" else "primary"):
        set_page("Contact Us")

st.markdown("<br>", unsafe_allow_html=True)

# ── 3. INTERACTIVE PAGE CONTAINERS ───────────────────────────────────────────

if st.session_state.current_page == "Home & Compliance":
    st.markdown('<p class="hero-title">Airtight Compliance & Optimized Cash Flow For Independent Practices</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Master Health delivers institutional-grade medical billing solutions. By combining rigorous compliance metrics with a specialized 24/7 delivery force, we shield your practice from revenue leakage and audit vulnerabilities.</p>', unsafe_allow_html=True)
    
    # Hero Image for Home Tab
    st.image("https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=1200&q=80", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Premium Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="metric-wrapper"><p class="metric-num">$5M+</p><p class="metric-lbl">Claims Managed</p></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-wrapper"><p class="metric-num">98.2%</p><p class="metric-lbl">Target Clean Claim Rate</p></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-wrapper"><p class="metric-num">&lt; 30</p><p class="metric-lbl">Avg Days in A/R Goal</p></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-wrapper"><p class="metric-num">HIPAA</p><p class="metric-lbl">Compliant Data Tunnels</p></div>', unsafe_allow_html=True)
        
    st.markdown('<p class="section-title">Institutional Protections & System Adaptability</p>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="corporate-card">
            <div class="card-icon">🔒</div>
            <div class="card-heading">Airtight OIG & HIPAA Compliance</div>
            <div class="card-text">Our workflows strictly follow Office of Inspector General (OIG) guidelines. We deploy ongoing chart reviews to catch structural coding errors before they flag clearinghouse audits.</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="corporate-card">
            <div class="card-icon">💻</div>
            <div class="card-heading">Technology-Agnostic Framework</div>
            <div class="card-text">We work directly inside your existing PM or EHR system. Whether your group utilizes Athenahealth, eClinicalWorks, AdvancedMD, or Epic, our teams log in via secure, encrypted pathways.</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="corporate-card">
            <div class="card-icon">🎓</div>
            <div class="card-heading">Certified Professional Coders</div>
            <div class="card-text">All charge routing and documentation checks are overlooked by specialists holding formal credentials (AAPC/AHIMA), ensuring accurate modifier tracking for multi-specialty practices.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<p class="section-title">Specialty-Specific Revenue Expertise</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">We deploy custom rules engines mapped directly to the billing nuances of individual medical specialties.</p>', unsafe_allow_html=True)
    
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown("""
        <div class="corporate-card">
            <div class="card-heading">OB-GYN Practices</div>
            <div class="card-text">Flawless execution of global OB packages, antepartum visit structures, and specialized ultrasound modifier management to completely halt payer delays.</div>
        </div>
        """, unsafe_allow_html=True)
    with s2:
        st.markdown("""
        <div class="corporate-card">
            <div class="card-heading">Otolaryngology (ENT)</div>
            <div class="card-text">Deep mastery of multi-procedural surgical modifiers, audiology code bundling, and complex in-office surgical coding tracking.</div>
        </div>
        """, unsafe_allow_html=True)
    with s3:
        st.markdown("""
        <div class="corporate-card">
            <div class="card-heading">Multi-Specialty Clinics</div>
            <div class="card-text">Centralized dashboard management built to route claims across conflicting commercial contracts without cross-contaminating practice tax IDs.</div>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.current_page == "End-to-End RCM Pillars":
    st.markdown('<p class="hero-title">Our Integrated Revenue Operations Ecosystem</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">We manage your administrative footprint across every functional vector of the revenue cycle, minimizing overhead and accelerating collections.</p>', unsafe_allow_html=True)
    
    # Hero Image for Pillars Tab
    st.image("https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?auto=format&fit=crop&w=1200&q=80", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="corporate-card">
            <div class="card-heading">1. Charge Posting & Specialty Coding</div>
            <div class="card-text">Immediate verification and entry of clinical encounters. Our coding specialists handle complex CPT/ICD-10 crosswalks, modifiers, and global surgical packages within 24 hours of discharge.</div>
        </div><br>
        <div class="corporate-card">
            <div class="card-heading">3. Payment Posting & Contractual Audit</div>
            <div class="card-text">Electronic Remittance Advice (ERA) and manual EOB sheets are balanced line-by-line. Our engine flags contractual underpayments immediately if a commercial payer underpays your fee schedule.</div>
        </div><br>
        <div class="corporate-card">
            <div class="card-heading">5. Targeted Denials Resolution Engine</div>
            <div class="card-text">We analyze every denial as a processing feedback loop. Claims hitting rejection flags are audited, updated with missing metrics, and re-submitted or appealed within 48 hours.</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="corporate-card">
            <div class="card-heading">2. Proactive Claim Scrubbing</div>
            <div class="card-text">Before deployment to clearinghouses, claims pass through rigorous custom front-end rules engines configured for localized commercial and government policies to stop rejections early.</div>
        </div><br>
        <div class="corporate-card">
            <div class="card-heading">4. Persistent Accounts Receivable Management</div>
            <div class="card-text">Dedicated aging follow-up specialists actively target and challenge unpaid metrics past the 30, 60, and 90-day marks, maintaining rigorous communication channels with payers.</div>
        </div><br>
        <div class="corporate-card">
            <div class="card-heading">6. Patient Balance Care & Statements</div>
            <div class="card-text">We manage patient-responsibility portions cleanly and professionally. This includes clear digital statement generation and patient communication portals to manage high-deductible collections.</div>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.current_page == "The Onshore Advantage":
    st.markdown('<p class="hero-title">The Onshore Accountability Advantage</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Many providers struggle when outsourcing due to a breakdown in communication. Master Health bridges this gap completely by wrapping an elite overnight execution engine inside a domestic executive management framework.</p>', unsafe_allow_html=True)
    
    # Hero Image for Advantage Tab
    st.image("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1200&q=80", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="corporate-card" style="border-top: 4px solid #1F7A8C;">
            <div class="card-heading" style="font-size:20px;">🇺🇸 Domestic Corporate Oversight (Onshore)</div><br>
            <div class="card-text" style="font-size:15px; line-height:2;">
                • <b>Strategic Leadership:</b> Master Health manages your onboarding, business integrations, and software setups locally.<br>
                • <b>Absolute Compliance:</b> Domestic legal oversight ensuring airtight HIPAA data vaults and complete security compliance.<br>
                • <b>Dedicated Account Managers:</b> Direct phone lines to your onshore strategic team to answer daily performance inquiries.
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="corporate-card" style="border-top: 4px solid #0A2540;">
            <div class="card-heading" style="font-size:20px;">🇮🇳 High-Volume Execution Force (Offshore Partnership)</div><br>
            <div class="card-text" style="font-size:15px; line-height:2;">
                • <b>Overnight Processing Speed:</b> While your clinic is closed, our partner's execution teams scrub and submit entries so your desk is clean by morning.<br>
                • <b>Functional Scaling:</b> Dedicated, hyper-specialized sub-teams focusing entirely on specific fields (e.g., individual payer rule matrices).<br>
                • <b>Operational Cost Arbitrage:</b> Drastic reduction in local billing team overhead, office footprint needs, and human resource management.
            </div>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.current_page == "ROI & Free Billing Assessment":
    st.markdown('<p class="hero-title">Interactive Operational Financial Estimator</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Review the real economic impact of leakage stabilization based on your standard monthly volumes.</p>', unsafe_allow_html=True)
    
    # Hero Image for Calculator Tab
    st.image("https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=1200&q=80", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Calculator Segment in clean Card Wrapper
    st.markdown('<div class="corporate-card">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        monthly_charges = st.number_input("Average Monthly Practice Claims Volume ($):", value=150000, step=10000)
        leakage_rate = st.slider("Current Estimated Denial/Leakage Rate (%):", min_value=1.0, max_value=15.0, value=7.0, step=0.5)
    with c2:
        recovered = (monthly_charges * (leakage_rate / 100)) * 0.45
        annualized = recovered * 12
        st.metric(label="Estimated Monthly Revenue Recovery Potential", value=f"${recovered:,.2f}")
        st.metric(label="Projected Annualized Profit Retention Optimization", value=f"${annualized:,.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == "Contact Us":
    st.markdown('<p class="hero-title">Connect with Our Corporate Team</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Speak directly with an expert to review your practice footprint, EHR integration logistics, or compliance guidelines.</p>', unsafe_allow_html=True)
    
    # Hero Image for Contact Tab
    st.image("https://images.unsplash.com/photo-1423662055902-359430b051b7?auto=format&fit=crop&w=1200&q=80", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)

    con_col1, con_col2 = st.columns(2)
    with con_col1:
        st.markdown("""
        <div class="corporate-card" style="height: 100%;">
            <div class="card-heading" style="font-size: 22px; color: #0A2540;">Corporate Communication Desk</div><br>
            <p class="card-text" style="font-size: 16px;">
                For general corporate inquiries, scheduling onboarding meetings, or executing vendor agreements, reach our operations channel directly at:
            </p>
            <h3 style="color: #1F7A8C; font-size: 24px; margin-top: 20px;">✉️ info@masterhealth.us</h3>
            <br>
            <p class="card-text" style="color: #637381; font-size: 14px;">
                📍 <b>Headquarters:</b> San Ramon, California, United States
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with con_col2:
        st.markdown("""
        <div class="corporate-card" style="height: 100%;">
            <div class="card-heading" style="font-size: 22px; color: #0A2540;">Security & Encrypted Intake</div><br>
            <p class="card-text" style="font-size: 15px; line-height: 1.8;">
                • <b>Data Tunnels:</b> All communications passing through our infrastructure utilize full TLS encryption protocols.<br>
                • <b>HIPAA Alignment:</b> Operational execution environments are strictly audited for data isolation rules.<br>
                • <b>AAPC Rules:</b> Internal data governance oversight complies fully with domestic healthcare security structures.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ── 4. BRAND NEW ENTERPRISE FOOTER STRUCTURE ────────────────────────────────
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
            <div class="footer-item">OB-GYN Operations</div>
            <div class="footer-item">Otolaryngology (ENT)</div>
            <div class="footer-item">Multi-Specialty Rules</div>
        </div>
        <div class="footer-links-column">
            <div class="footer-header">Contact & Info</div>
            <div class="footer-item">info@masterhealth.us</div>
            <div class="footer-item">San Ramon, California</div>
            <div class="footer-item" style="color: #00D4B2;">🔒 HIPAA Secure Endpoints</div>
        </div>
    </div>
    <div class="footer-bottom">
        <div>© 2026 Master Health LLC. All rights reserved.</div>
        <div>Security Framework: OIG Compliant / AAPC Certified</div>
    </div>
</div>
""", unsafe_allow_html=True)
