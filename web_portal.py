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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
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
        padding-bottom: 3rem !important;
        max-width: 1200px !important;
    }
    
    /* ── CUSTOM CORPORATE TOP NAVBAR ── */
    .header-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 45px 0px 20px 0px; /* Increased top padding to clear the floating tag */
        margin-bottom: 40px;
        border-bottom: 1px solid #EAEAEA;
    }
    .nav-brand {
        color: #0A2540;
        font-size: 24px;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    .nav-brand span {
        color: #1F7A8C;
        font-weight: 400;
        font-size: 14px;
        margin-left: 8px;
    }
    
    /* ── PREMIUM ENTERPRISE TEXT STYLING ── */
    .hero-title {
        color: #0A2540;
        font-size: 44px;
        font-weight: 700;
        line-height: 1.2;
        letter-spacing: -1px;
        margin-bottom: 16px;
    }
    .hero-subtitle {
        color: #637381;
        font-size: 19px;
        font-weight: 400;
        line-height: 1.5;
        max-width: 850px;
        margin-bottom: 35px;
    }
    .section-title {
        color: #0A2540;
        font-size: 26px;
        font-weight: 700;
        margin-top: 40px;
        margin-bottom: 24px;
        letter-spacing: -0.5px;
    }
    
    /* ── ASSEMBLY-STYLE CARDS & GRIDS ── */
    .corporate-card {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);
        border: 1px solid #EFEFEF;
        height: 100%;
    }
    .card-icon {
        font-size: 24px;
        margin-bottom: 12px;
    }
    .card-heading {
        color: #0A2540;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .card-text {
        color: #637381;
        font-size: 14px;
        line-height: 1.6;
    }
    
    /* ── METRIC BLOCK STYLING ── */
    .metric-wrapper {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 6px;
        border: 1px solid #EFEFEF;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .metric-num {
        color: #1F7A8C;
        font-size: 32px;
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
    
    /* Clean up native Streamlit form box outline lines */
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
    <div class="nav-brand">Master Health<span>Enterprise Revenue Cycle Management</span></div>
</div>
""", unsafe_allow_html=True)

# Generate a professional seamless navigation header rows using clear columns
nav1, nav2, nav3, nav4, nav5 = st.columns([1.5, 1.8, 1.8, 2.2, 3])

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

st.markdown("<br><br>", unsafe_allow_html=True)

# ── 3. INTERACTIVE PAGE CONTAINERS ───────────────────────────────────────────

if st.session_state.current_page == "Home & Compliance":
    st.markdown('<p class="hero-title">Airtight Compliance & Optimized Cash Flow For Independent Practices</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Master Health delivers institutional-grade medical billing solutions. By combining rigorous compliance metrics with a specialized 24/7 delivery force, we shield your practice from revenue leakage and audit vulnerabilities.</p>', unsafe_allow_html=True)
    
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

elif st.session_state.current_page == "End-to-End RCM Pillars":
    st.markdown('<p class="hero-title">Our Integrated Revenue Operations Ecosystem</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">We manage your administrative footprint across every functional vector of the revenue cycle, minimizing overhead and accelerating collections.</p>', unsafe_allow_html=True)
    
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
    st.markdown('<p class="hero-title">Request a Free A/R Assessment</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Discover where your accounts receivable are hitting friction points. Use our dynamic estimator below, then submit your practice profile to schedule a complete billing leak analysis.</p>', unsafe_allow_html=True)
    
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
    
    st.markdown('<p class="section-title">Secure Practice Registration</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="corporate-card">', unsafe_allow_html=True)
    with st.form("assessment_form"):
        f1, f2 = st.columns(2)
        with f1:
            p_name = st.text_input("Practice / Group Organization Name:")
            c_name = st.text_input("Contact Full Name & Title:")
        with f2:
            ehr_system = st.text_input("Active EHR/Billing Platform (e.g., Athena, eCW):")
            p_count = st.number_input("Number of Billing Providers:", min_value=1, value=2)
        notes = st.text_area("Primary Operational Pain Points (e.g., backlogged collections, slow posting):")
        
        btn = st.form_submit_button("Submit Assessment Request")
        if btn:
            st.success("Thank you. Master Health's corporate executive team will review your practice scale and EHR framework, coordinate with our operations center, and contact you within 1 business day.")
    st.markdown('</div>', unsafe_allow_html=True)
