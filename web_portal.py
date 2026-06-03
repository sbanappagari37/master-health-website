import streamlit as st

# ── 1. GLOBAL INITIALIZATION & REGULATORY DESIGN TOKENS ─────────────────────
st.set_page_config(
    page_title="Master Health | Enterprise Revenue Cycle Management", 
    page_icon="🏦", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ── 2. UNIFIED STYLING & HORIZONTAL NAVBAR MARKDOWN LAYER ────────────────────
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #FFFFFF !important;
        color: #1A1A2E;
        line-height: 1.6;
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
    
    /* HORIZONTAL NAVIGATION BAR HEADER */
    .premium-navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 45px 0px 20px 0px; 
        border-bottom: 1px solid #E2E8F0;
        background-color: #FFFFFF;
        position: relative;
        z-index: 999999 !important;
    }
    
    .logo-mark {
        width: 40px; height: 40px;
        background: #0A7E6E;
        border-radius: 8px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        vertical-align: middle;
        margin-right: 10px;
    }
    
    .logo-text {
        font-size: 1.25rem;
        font-weight: 800;
        color: #0D1B3E;
        display: inline-block;
        vertical-align: middle;
        text-decoration: none !important;
    }
    .logo-text span { color: #0A7E6E; }
    
    .nav-menu-links {
        display: flex;
        align-items: center;
        gap: 4px;
    }
    
    /* Dropdown Hover Framework */
    .menu-dropdown {
        position: relative;
        display: inline-block;
    }
    
    .menu-tab-link {
        color: #0D1B3E !important;
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
        color: #0A7E6E !important;
    }
    
    /* Popover Dropdown Styling Overlay */
    .dropdown-overlay-box {
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        background-color: #FFFFFF;
        min-width: 270px;
        box-shadow: 0px 12px 30px rgba(0, 0, 0, 0.06), 0px 4px 12px rgba(0, 0, 0, 0.03);
        border: 1px solid #E2E8F0;
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
        color: #4A5568 !important;
        text-decoration: none !important;
        font-size: 14.5px !important;
        font-weight: 400 !important;
        transition: background 0.15s ease, color 0.15s ease !important;
    }
    
    .dropdown-overlay-box a:hover {
        background-color: #E8F5F2 !important;
        color: #0A7E6E !important;
    }
    
    /* ── REPLICATED CLAUDE STRIP DESIGN METRICS ── */
    .hero-strip {
        background: linear-gradient(135deg, #0D1B3E 0%, #1A3460 55%, #0D4D40 100%);
        padding: 100px 40px;
        margin-left: -200px;
        margin-right: -200px;
        color: #FFFFFF;
        text-align: left;
    }
    .hero-content {
        max-width: 1200px;
        margin: 0 auto;
    }
    .hero-tag {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255,255,255,.1);
        border: 1px solid rgba(255,255,255,.2);
        border-radius: 30px;
        padding: 6px 16px;
        font-size: .8rem;
        font-weight: 600;
        color: rgba(255,255,255,.9);
        text-transform: uppercase;
        letter-spacing: .06em;
        margin-bottom: 28px;
    }
    .hero-tag::before {
        content: '';
        width: 8px; height: 8px;
        background: #4ADE80;
        border-radius: 50%;
    }
    .hero-title-text {
        font-size: 3.5rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 24px;
        color: #FFFFFF;
    }
    .hero-title-text em {
        font-style: normal;
        color: #4DD9C4;
    }
    .hero-subtitle-text {
        font-size: 1.15rem;
        color: rgba(255,255,255,.8);
        max-width: 540px;
        margin-bottom: 40px;
        line-height: 1.7;
    }
    
    .btn-action-primary {
        display: inline-block;
        background: #0A7E6E;
        color: #FFFFFF !important;
        padding: 14px 32px;
        border-radius: 6px;
        font-weight: 600;
        font-size: .95rem;
        text-decoration: none !important;
        margin-right: 14px;
    }
    .btn-action-outline {
        display: inline-block;
        border: 2px solid #FFFFFF;
        color: #FFFFFF !important;
        padding: 12px 28px;
        border-radius: 6px;
        font-weight: 600;
        font-size: .95rem;
        text-decoration: none !important;
    }

    /* Stats Banner strip */
    .stats-strip {
        background: #0D1B3E;
        padding: 32px 40px;
        margin-left: -200px;
        margin-right: -200px;
        border-bottom: 1px solid rgba(255,255,255,.08);
    }
    
    /* Grid Matrices Layouts */
    .web-grid-3 {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
        width: 100%;
        margin-top: 40px;
    }
    .web-grid-4 {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0px;
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
    }
    .stat-item {
        text-align: center;
        padding: 12px 20px;
        border-right: 1px solid rgba(255,255,255,.1);
    }
    .stat-item:last-child { border-right: none; }
    .stat-number {
        font-size: 2.2rem;
        font-weight: 800;
        color: #4DD9C4;
        margin-bottom: 6px;
    }
    .stat-label {
        font-size: .8rem;
        color: rgba(255,255,255,.65);
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: .06em;
    }

    .section-label {
        font-size: .75rem;
        font-weight: 700;
        letter-spacing: .12em;
        text-transform: uppercase;
        color: #0A7E6E;
        margin-top: 80px;
        margin-bottom: 12px;
    }
    .section-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #0D1B3E;
        line-height: 1.2;
        margin-bottom: 16px;
        letter-spacing: -0.5px;
    }
    .section-body {
        font-size: 1.05rem;
        color: #4A5568;
        max-width: 640px;
        line-height: 1.75;
        margin-bottom: 40px;
    }

    .section-block-grey {
        background-color: #F7FAFC;
        padding: 96px 40px;
        margin-left: -200px;
        margin-right: -200px;
        border-top: 1px solid #E2E8F0;
        border-bottom: 1px solid #E2E8F0;
    }
    
    .corporate-card {
        background-color: #FFFFFF;
        padding: 32px 28px;
        border-radius: 14px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.02);
        border: 1px solid #E2E8F0;
        height: 100%;
        position: relative;
    }
    
    .card-heading {
        color: #0D1B3E;
        font-size: 1.15rem;
        font-weight: 800;
        margin-bottom: 12px;
    }
    .card-text {
        color: #4A5568;
        font-size: .92rem;
        line-height: 1.7;
    }
    
    .service-tag {
        position: absolute;
        top: 20px; right: 20px;
        background: #E8F5F2;
        color: #0A7E6E;
        font-size: .72rem;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 20px;
        text-transform: uppercase;
    }

    /* DEEP FOOTER CONTAINER */
    .enterprise-footer {
        background-color: #0D1B3E;
        color: #FFFFFF;
        padding: 64px 40px 32px 40px;
        margin-top: 90px;
        margin-left: -200px;
        margin-right: -200px;
    }
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 48px;
        border-bottom: 1px solid rgba(255,255,255,.08);
        padding-bottom: 56px;
    }
    .footer-brand p {
        font-size: .88rem;
        color: rgba(255,255,255,.55);
        line-height: 1.7;
        max-width: 280px;
        margin-top: 16px;
    }
    .footer-col h4 {
        font-size: .85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .1em;
        color: rgba(255,255,255,.5);
        margin-bottom: 16px;
    }
    .footer-col a {
        display: block;
        font-size: .88rem;
        color: rgba(255,255,255,.7);
        padding: 6px 0;
        text-decoration: none !important;
    }
    .footer-bottom {
        max-width: 1200px;
        margin: 0 auto;
        padding-top: 28px;
        display: flex;
        justify-content: space-between;
        color: rgba(255,255,255,.4);
        font-size: .82rem;
    }
    .footer-bottom a { color: rgba(255,255,255,.5); text-decoration: none !important; }
    </style>

    <div class="premium-navbar">
        <div class="nav-brand-wrapper">
            <div class="logo-mark">
                <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
            </div>
            <a href="?view=Home" class="logo-text" target="_self">Master<span>Health</span></a>
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
                    <a href="?view=GI" target="_self">Gastroenterology (GI)</a>
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

# Capture current view parameters cleanly from dynamic query indexes
current_view = st.query_params.get("view", "Home")

# ── 3. DYNAMIC CONTENT REGIONS ──────────────────────────────────────────────

if current_view == "Home":
    # Hero Full-Width Strips Component
    st.markdown("""
    <div class="hero-strip">
        <div class="hero-content">
            <div class="hero-tag">Trusted RCM Partner</div>
            <h1 class="hero-title-text">Your Trusted RCM &<br><em>Medical Billing Partner</em></h1>
            <p class="hero-subtitle-text">Getting paid for the care you deliver shouldn't be this hard. Master Health streamlines your revenue cycle so you can focus on what matters most — your patients.</p>
            <div>
                <a class="btn-action-primary" href="mailto:operations@masterhealth.us?subject=Free Consultation Request">Contact Master Health</a>
                <a class="btn-action-outline" href="?view=Overview" target="_self">Learn More</a>
            </div>
        </div>
    </div>
    
    <div class="stats-strip">
        <div class="web-grid-4">
            <div class="stat-item">
                <div class="stat-number">95%+</div>
                <div class="stat-label">Clean Claim Rate</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">&lt;40</div>
                <div class="stat-label">Net Days in A/R</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">7+</div>
                <div class="stat-label">Specialties Served</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">100%</div>
                <div class="stat-label">HIPAA Compliant</div>
            </div>
        </div>
    </div>
    
    <p class="section-label">Why Master Health</p>
    <h2 class="section-title">Expert-Driven Revenue Cycle Management</h2>
    <p class="section-body">Master Health steps in as your hands-on partner — so your team can spend less time wrestling claims and more time focused on care. We become an extension of your practice.</p>
    
    <div class="web-grid-3">
        <div class="corporate-card">
            <div class="card-heading">🔒 Airtight HIPAA Vaults</div>
            <div class="card-text">Our workflows strictly follow Office of Inspector General (OIG) guidelines. We deploy ongoing chart reviews to catch structural coding errors before they flag clearinghouse audits.</div>
        </div>
        <div class="corporate-card">
            <div class="card-heading">💻 Technology-Agnostic</div>
            <div class="card-text">We work directly inside your existing PM or EHR system. Whether your group utilizes Athenahealth, eClinicalWorks, AdvancedMD, or Epic, our teams log in via secure, encrypted pathways.</div>
        </div>
        <div class="corporate-card">
            <div class="card-heading">🎓 AAPC Certified Experts</div>
            <div class="card-text">All charge routing and documentation checks are overlooked by specialists holding formal credentials (AAPC/AHIMA), ensuring accurate modifier tracking for multi-specialty practices.</div>
        </div>
    </div>
    <br><br>
    """, unsafe_allow_html=True)

elif current_view == "Overview":
    st.markdown("""
    <div class="section-block-grey" style="margin-top:40px;">
        <div class="inner-content-wrapper">
            <p class="section-label">About Master Health</p>
            <h1 class="section-title">Transforming Revenue Cycles Across America</h1>
            <p class="section-body">At Master Health, we believe healthcare providers should spend their energy on patients — not paperwork. We are a full-service Revenue Cycle Management (RCM) and medical billing partner serving physician practices across the United States.</p>
            <p class="section-body" style="margin-top:-20px;">Our team brings deep specialty expertise, modern technology, and a commitment to transparency that ensures you're collecting every dollar you're contractually owed.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# SECTION: Reconfigured Leadership Viewport (Reduced to 1 Profile: Founder Dr. Sashi)
elif current_view == "Founder":
    st.markdown("""
    <div class="section-block-grey" style="margin-top:40px;">
        <div class="inner-content-wrapper">
            <p class="section-label">Leadership Profile</p>
            <h1 class="section-title">Meet Our Founder</h1>
            <p class="section-body">The corporate compliance vision and strategic RCM framework behind Master Health operations.</p>
            
            <div class="corporate-card" style="margin-top:30px; border-top: 4px solid #0A7E6E;">
                <div class="card-heading" style="font-size:24px; margin-bottom:4px;">Dr. Sashi</div>
                <div class="card-text" style="color:#0A7E6E; font-weight:600; font-size:14px; margin-bottom:20px; text-transform:uppercase;">Founder & Chief Executive</div>
                <div class="card-text" style="font-size:15.5px; line-height:1.8; color:#1A1A2E;">
                    Dr. Sashi establishes the overarching vision, corporate strategy, and compliance frameworks for Master Health. 
                    With a career built on specialized scientific pathways, operational scaling models, and institutional data governance, 
                    Dr. Sashi designs data infrastructures to handle high-volume billing operations while keeping data pipelines perfectly 
                    isolated under strict HIPAA and OIG parameters.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

else:
    # Individual Clinical Specialties Subpages Canvas Viewports (Assembly Model)
    clean_title = current_view.replace("_", " & ")
    
    specialty_copy_matrix = {
        "Cardiology": "Comprehensive billing for the full spectrum of cardiac services — from routine office visits and diagnostic testing (ECG, echocardiography, stress tests) to complex interventional procedures and electrophysiology. We navigate the nuanced cardiology coding landscape to maximize your reimbursements while maintaining strict compliance.",
        "Ophthalmology": "Specialized billing expertise for comprehensive eye exams, refractions, surgical procedures (cataract, LASIK, glaucoma), and retinal treatments. We understand the ophthalmology billing landscape — including the critical distinction between medical and routine vision benefits — to ensure accurate claim submission and superior collection rates.",
        "GI": "Expert GI billing for endoscopic procedures, colonoscopies, upper GI studies, liver biopsies, and motility testing. We handle the complex bundling rules, modifier requirements, and facility vs. professional fee distinctions that make GI billing challenging, ensuring you receive proper reimbursement for every procedure performed.",
        "Oncology": "Meticulous billing for medical oncology, including infusion and injection administration, chemotherapy services, and supportive care drugs. We also cover radiation oncology treatment planning and delivery. Our team manages the complex prior authorization requirements, payer-specific drug policies, and compendia reviews that are central to oncology revenue capture.",
        "Dermatology": "Full-service billing for medical and cosmetic dermatology, including lesion removals, biopsies, MOHS surgery, phototherapy, and cosmetic procedures. We accurately apply the right procedure codes and modifiers, and manage the medical-vs-cosmetic distinction that is pivotal to claim approval and optimal reimbursement.",
        "Orthopedic": "Specialized RCM for orthopedic surgery, sports medicine, and musculoskeletal care — including joint replacements, fracture care, spine procedures, and physical therapy coordination. We handle global period tracking, implant billing, and the complex authorization workflows that orthopedic practices face daily.",
        "Mental_Behavioral": "Dedicated billing support for psychiatry, psychology, counseling, substance use disorder treatment, and telehealth mental health services. We navigate the unique parity requirements, prior authorization processes, and time-based coding rules of behavioral health billing to maximize legitimate reimbursements for your practice."
    }
    
    active_copy = specialty_copy_matrix.get(current_view, "Dedicated revenue cycle management workflows configured specifically to handle provider modifier rules templates, insurance verification steps, and contract aging directories.")
    
    st.markdown(f"""
    <div class="section-block-grey" style="margin-top:40px;">
        <div class="inner-content-wrapper">
            <p class="section-label">Specialty Solutions</p>
            <h1 class="section-title">{clean_title} Revenue Management</h1>
            
            <div class="corporate-card" style="margin-top:30px; border-top: 4px solid #0A7E6E;">
                <span class="service-tag">Active Specialty</span>
                <div class="card-heading">{clean_title} Operational Paradigm</div>
                <div class="card-text" style="font-size:15px; line-height:1.75; margin-bottom:20px;">
                    {active_copy}
                </div>
                <div class="card-text" style="line-height:2; font-weight:500; border-top:1px solid #E2E8F0; padding-top:20px;">
                    • Specialized ICD-10 crosswalk monitoring ensuring error-free documentation posting.<br>
                    • Proactive modifier verification matching localized commercial and public policy rules engines.<br>
                    • Persistent aging follow-up loops targeted toward discipline-specific commercial insurance policies.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── 4. ENTERPRISE FOOTER MATRIX ────────────────────────────────────────────────
st.markdown("""
<div class="enterprise-footer">
    <div class="footer-content">
        <div class="footer-brand">
            <div class="logo-text" style="color:#FFFFFF;">Master<span>Health</span></div>
            <p>Your trusted RCM and medical billing partner. We help healthcare providers across the United States maximize revenue and reduce administrative burden.</p>
        </div>
        <div class="footer-col">
            <h4>Company</h4>
            <a href="?view=Overview" target="_self">About Us</a>
            <a href="?view=Founder" target="_self">Founder</a>
            <a href="?view=Home" target="_self">Solutions Hub</a>
        </div>
        <div class="footer-col">
            <h4>Specialties</h4>
            <a href="?view=Cardiology" target="_self">Cardiology</a>
            <a href="?view=Ophthalmology" target="_self">Ophthalmology</a>
            <a href="?view=GI" target="_self">Gastroenterology</a>
            <a href="?view=Oncology" target="_self">Oncology</a>
            <a href="?view=Dermatology" target="_self">Dermatology</a>
        </div>
        <div class="footer-col">
            <h4>Contact</h4>
            <a href="mailto:info@masterhealth.us">info@masterhealth.us</a>
            <a href="mailto:operations@masterhealth.us">operations@masterhealth.us</a>
            <a href="mailto:operations@masterhealth.us?subject=Free Consultation Request" style="margin-top:12px; color:#4DD9C4; font-weight:600;">Free Consultation →</a>
        </div>
    </div>
    <div class="footer-bottom">
        <div>© 2026 Master Health LLC. All rights reserved. HIPAA Compliant Network.</div>
        <div>Security Framework: OIG Guidelines Mapped / AAPC Certified</div>
    </div>
</div>
""", unsafe_allow_html=True)
