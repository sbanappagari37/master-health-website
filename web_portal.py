import streamlit as st

# ── 1. MODERN TOP-NAVIGATION STRUCTURAL CONFIGURATION ──────────────────────────
# We use the native pages dictionary format to force a top navbar and hide the sidebar entirely
def show_home():
    # Hero Section
    st.markdown("""
    <div class="hero-box">
        <p class="hero-title">Airtight Compliance & Optimized Cash Flow For Independent Practices</p>
        <p class="hero-subtitle">Master Health delivers institutional-grade medical billing solutions. By combining rigorous compliance metrics with a specialized 24/7 delivery force, we shield your practice from revenue leakage and audit vulnerabilities.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Startup Milestones Counters
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="metric-card"><p class="metric-value">$5M+</p><p class="metric-label">Claims Managed</p></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card"><p class="metric-value">98.2%</p><p class="metric-label">Target Clean Claim Rate</p></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card"><p class="metric-value">&lt; 30</p><p class="metric-label">Avg Days in A/R Goal</p></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-card"><p class="metric-value">HIPAA</p><p class="metric-label">Compliant Data Tunnels</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    
    # Compliance Integration Layer
    st.markdown('<p class="section-header">Institutional Protections & System Adaptability</p>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("🔒 Airtight OIG & HIPAA Compliance")
        st.write("Our workflows strictly follow Office of Inspector General (OIG) guidelines. We deploy ongoing chart reviews to catch structural coding errors before they flag clearinghouse audits.")
    with c2:
        st.subheader("💻 Technology-Agnostic Framework")
        st.write("We work directly inside your existing PM or EHR system. Whether your group utilizes Athenahealth, eClinicalWorks, AdvancedMD, or Epic, our teams log in via secure, encrypted pathways—no data migrations required.")
    with c3:
        st.subheader("🎓 Certified Professional Coders")
        st.write("All charge routing and documentation checks are overlooked by specialists holding formal credentials (AAPC/AHIMA), ensuring accurate modifier tracking for multi-specialty practices.")

def show_pillars():
    st.markdown('<p class="hero-title">Our Integrated Revenue Operations Ecosystem</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">We manage your administrative footprint across every functional vector of the revenue cycle, minimizing overhead and accelerating collections.</p>', unsafe_allow_html=True)
    st.markdown('---')
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="pillar-box"><p class="pillar-title">1. Charge Posting & Specialty Coding</p><p class="pillar-body">Immediate verification and entry of clinical encounters. Our coding specialists handle complex CPT/ICD-10 crosswalks, modifiers, and global surgical packages within 24 hours of discharge.</p></div>
        <br>
        <div class="pillar-box"><p class="pillar-title">3. Payment Posting & Contractual Audit</p><p class="pillar-body">Electronic Remittance Advice (ERA) and manual EOB sheets are balanced line-by-line. Our engine flags contractual underpayments immediately if a commercial payer underpays your fee schedule.</p></div>
        <br>
        <div class="pillar-box"><p class="pillar-title">5. Targeted Denials Resolution Engine</p><p class="pillar-body">We analyze every denial as a processing feedback loop. Claims hitting rejection flags are audited, updated with missing metrics, and re-submitted or appealed within 48 hours.</p></div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="pillar-box"><p class="pillar-title">2. Proactive Claim Scrubbing</p><p class="pillar-body">Before deployment to clearinghouses, claims pass through rigorous custom front-end rules engines configured for localized commercial and government policies to stop rejections early.</p></div>
        <br>
        <div class="pillar-box"><p class="pillar-title">4. Persistent Accounts Receivable Management</p><p class="pillar-body">Dedicated aging follow-up specialists actively target and challenge unpaid metrics past the 30, 60, and 90-day marks, maintaining rigorous communication channels with payers.</p></div>
        <br>
        <div class="pillar-box"><p class="pillar-title">6. Patient Balance Care & Statements</p><p class="pillar-body">We manage patient-responsibility portions cleanly and professionally. This includes clear digital statement generation and patient communication portals to manage high-deductible collections.</p></div>
        """, unsafe_allow_html=True)

def show_model():
    st.markdown('<p class="hero-title">The Onshore Accountability Advantage</p>', unsafe_allow_html=True)
    st.write("Many providers struggle when outsourcing due to a breakdown in communication. Master Health bridges this gap completely by wrapping an elite overnight execution engine inside a domestic executive management framework.")
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.info("#### 🇺🇸 Domestic Corporate Oversight (Onshore)\n* **Strategic Leadership:** Master Health manages your onboarding, business integrations, and software setups locally.\n* **Absolute Compliance:** Domestic legal oversight ensuring airtight HIPAA data vaults and complete security compliance.\n* **Dedicated Account Managers:** Direct phone lines to your onshore strategic team to answer daily performance inquiries.")
    with col2:
        st.success("#### 🇮🇳 High-Volume Execution Force (Offshore Partnership)\n* **Overnight Processing Speed:** While your clinic is closed, our partner's execution teams scrub and submit entries so your desk is clean by morning.\n* **Functional Scaling:** Dedicated, hyper-specialized sub-teams focusing entirely on specific fields (e.g., individual payer rule matrices or complex appeals).\n* **Operational Cost Arbitrage:** Drastic reduction in local billing team overhead, office footprint needs, and human resource management.")

def show_roi():
    st.markdown('<p class="hero-title">Request a Free A/R Assessment</p>', unsafe_allow_html=True)
    st.markdown("Discover where your accounts receivable are hitting friction points. Use our dynamic estimator below, then submit your practice profile to schedule a complete billing leak analysis.")
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        monthly_charges = st.number_input("Average Monthly Practice Claims Volume ($):", value=150000, step=10000)
        leakage_rate = st.slider("Current Estimated Denial/Leakage Rate (%):", min_value=1.0, max_value=15.0, value=7.0, step=0.5)
    with c2:
        recovered = (monthly_charges * (leakage_rate / 100)) * 0.45
        annualized = recovered * 12
        st.metric(label="Estimated Monthly Revenue Recovery Potential", value=f"${recovered:,.2f}")
        st.metric(label="Projected Annualized Profit Retention Optimization", value=f"${annualized:,.2f}")
    st.markdown("---")
    st.subheader("Secure Practice Registration")
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

# ── 2. APPLICATION EXECUTION MATCHING DESIGN PATHS ───────────────────────────
pages = {
    "Home & Compliance": show_home,
    "End-to-End RCM Pillars": show_pillars,
    "The Onshore-Offshore Model": show_model,
    "ROI & Free Billing Assessment": show_roi
}

# Force Top Menu bar layout and suppress default side panels
st.set_page_config(page_title="Master Health | Enterprise RCM", page_icon="🏦", layout="wide", initial_sidebar_state="collapsed")

# Custom Styling Overrides (Hiding Native Elements + Premium Theme Injector)
st.markdown("""
    <style>
    /* Hiding native side elements & header frames completely */
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    header { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    
    /* Top Horizontal Corporate Navigation bar styling */
    .nav-container { display: flex; justify-content: space-between; align-items: center; padding: 15px 0px; margin-bottom: 25px; border-bottom: 2px solid #E9ECEF; }
    .brand-title { color: #1F3864; font-size: 26px; font-weight: bold; font-family: 'Arial'; text-decoration: none; }
    .brand-tag { color: #1F7A8C; font-size: 13px; font-style: italic; margin-top: -3px; }
    
    .main { background-color: #FFFFFF; }
    .hero-box { padding: 10px 0px 30px 0px; text-align: left; }
    .hero-title { color: #1F3864; font-family: 'Arial'; font-size: 42px; font-weight: bold; line-height: 1.15; }
    .hero-subtitle { color: #404040; font-size: 19px; font-weight: normal; margin-top: 12px; margin-bottom: 25px; max-width: 900px; line-height: 1.4; }
    .section-header { color: #1F3864; font-size: 26px; font-weight: bold; margin-top: 35px; margin-bottom: 20px; }
    
    .metric-card { background-color: #F8F9FA; padding: 25px; border-radius: 6px; text-align: center; border: 1px solid #E9ECEF; }
    .metric-value { color: #1F7A8C; font-size: 34px; font-weight: bold; margin-bottom: 2px; }
    .metric-label { color: #1F3864; font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px; }
    
    .pillar-box { background-color: #FFFFFF; padding: 22px; border-radius: 8px; border-left: 5px solid #1F7A8C; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .pillar-title { color: #1F3864; font-size: 18px; font-weight: bold; margin-bottom: 6px; }
    .pillar-body { color: #5A5A5A; font-size: 13.5px; line-height: 1.5; }
    </style>
    """, unsafe_allow_html=True)

# Generate header branding box
st.markdown("""
<div class="nav-container">
    <div>
        <a class="brand-title" href="#">Master Health</a>
        <div class="brand-tag">Enterprise Revenue Cycle Management Solutions</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Build a beautiful, horizontal page selection mechanism at the very top of the content page
current_selection = st.segmented_control(
    label="Navigate Corporate Portal Platforms:",
    options=list(pages.keys()),
    default="Home & Compliance",
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

# Render selected segment container layout
pages[current_selection]()
