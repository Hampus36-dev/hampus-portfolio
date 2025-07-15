import streamlit as st
from PIL import Image
import base64
import streamlit_shadcn_ui as ui
from streamlit_timeline import timeline
from streamlit_option_menu import option_menu

# --- Config ---
st.set_page_config(page_title="Humprux – Portfolio", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #003366;
    }
    .stSidebar {
        background-color: #e6f2ff;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    col1, col2, col3 = st.columns(3)
    with col2:
        st.sidebar.image("./static/bannerkth.png", width=400)
    section = option_menu("", ["About Me", "Technoeconomic Analysis of Nuclear District Heating", 'Settings'], 
    icons=['house', 'gear'], menu_icon="cast", default_index=1)

        

# --- About Me ---
if section == "About Me":
    st.header("👨‍🔬 About the Author")

    # --- Profile Info ---
    st.subheader("📄 Profile")
    st.markdown("""
    My name is Hampus Svensson, a Master's student in Energy Systems and Sustainability at KTH Royal Institute of Technology.  
    I am passionate about sustainable infrastructure, nuclear energy, and optimization of energy systems.  

    📍 Based in Stockholm  
    📫 [LinkedIn](https://www.linkedin.com/in/hampus-svensson-a154681a4) | 📧 hamsve@kth.se
    """)

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### Experience")
            st.markdown("""
            **Quality Control Technician** – *Saab*  
            🕒 Jul 2024 – Present | Järfälla, Stockholm County, Sweden  
            🧪 Part-time position  
            - Performed quality assurance and control in production processes  
            - Collaborated with engineering teams to resolve defects and improve workflows
            """)

            st.markdown("""
            **Administrator** – *Bengt Dahlgren*  
            🕒 Nov 2022 – May 2023 | Stockholm, Sweden  
            🧾 Part-time position  
            - Supported the newly established R&D unit  
            - Created internal data libraries and document templates  
            - Carried out administrative and documentation tasks
            """)

    with col2:
        with st.container(border=True):
            st.markdown("### Education")
            st.markdown("""
            **M.Sc. in Industrial Engineering and Management** – *KTH Royal Institute of Technology*  
            🕒 2020 – 2025 | Stockholm, Sweden  
            • Focus: Energy Systems, Data Analysis, Quantitative Methods  
            • Skills: Python, Excel, Matlab, Problem Solving, Power Systems
            """)

            st.markdown("""
            **Exchange Semester in Industrial Engineering** – *INSA Lyon*  
            🕒 Aug 2023 – Feb 2024 | Lyon, France  
            • Skills: Python, Analytical Thinking, Sustainability
            """)

            st.markdown("""
            **High School Diploma** – *Ehrensvärdska Gymnasiet*  
            🕒 2017 – 2020
            """)

            st.markdown("""
            **Math Studies** – *Blekinge Tekniska Högskola*  
            🕒 Course-level | Focus: Advanced Mathematics
            """)

    with st.container(border=True):
        st.markdown("### Languages")
        st.markdown("""
        - 🇸🇪 Swedish – Native 
        - 🇬🇧 English – Full Professional Proficiency  
        - 🇫🇷 French – Limited Working Proficiency
        """)

    with st.container(border=True):
        st.markdown("### Tools and Skills")
        st.markdown("""
        - **Programming**: Python, MATLAB  
        - **Software**: Microsoft Excel, Outlook  
        - **Methods**: Data Analysis, Technical Documentation, R&D Support  
        - **Domains**: Quality Control, Energy Systems, Nuclear Engineering  
        - **Soft Skills**: Communication, Team Collaboration, Process Optimization
        """)

elif section == "Technoeconomic Analysis of Nuclear District Heating":
    st.markdown("""
        <div style='background-color: #003366; padding: 2rem; border-radius: 12px;'>
            <h1 style='color: white; margin-bottom: 0;'>Technoeconomic Analysis of Nuclear District Heating</h1>
            <h3 style='color: #cce0ff; margin-top: 0;'>A Case Study of Forsmark NPP to Stockholm & Uppsala</h3>
            <p style='color: #e6f0ff; font-size: 0.9rem; line-height: 1.6;'>
                This thesis investigates the techno-economic feasibility of implementing nuclear district heating by connecting
                the Forsmark Nuclear Power Plant (NPP) to the district heating networks of Stockholm and Uppsala.
                A detailed model was developed to optimize pipeline configuration, heat loss, pressure and cost.
            </p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    import base64
    with open("static/Hampus_Thesis.pdf", "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

        href = f'<a href="data:application/pdf;base64,{encoded}" download="Hampus_Thesis.pdf" target="_blank"><button style="padding:10px 16px; font-size:16px;">📥 Download Full Thesis</button></a>'
        st.markdown(href, unsafe_allow_html=True)
    
    st.markdown("""
    ### 🔍 Study Context & Motivation

    In recent years, Sweden has faced increasing challenges related to energy costs and emissions:

    - ⚠️ In 2023, power and district heating accounted for **9% of Sweden’s total greenhouse gas emissions**, 80% of which came from waste incineration.
    - 📈 **Biofuel prices have surged** since the 2022 energy crisis, impacting the affordability of district heating.
    - 🇸🇪 Sweden’s district heating networks are under pressure to reduce reliance on **carbon-emitting sources** and meet EU climate targets.

    This study revisits nuclear district heating as a viable solution to these issues by:
    - Leveraging **existing nuclear infrastructure** at Forsmark NPP.
    - Reducing operational costs through **waste heat reuse**.
    - Supporting long-term goals for **fossil-free heat supply** in Stockholm and Uppsala.

    Nuclear heating is not only a technically feasible alternative—it also offers **economic stability** and **sustainability gains** in the evolving European energy landscape.
    """)
    
   
    # --- Download Thesis Button ---
    st.markdown("""
    ### 🗂️ Table of Contents
    - [1. Background](#1-background)
    - [2. Techno-Economic Model](#2-techno-economic-model)
    - [3. Case Study: Forsmark to Stockholm & Uppsala](#3-case-study-forsmark-to-stockholm--uppsala)
    - [4. Results and Analysis](#4-results-and-analysis)
    - [5. Conclusions](#5-conclusions)
    - [Acknowledgements](#acknowledgements)
    """, unsafe_allow_html=True
    )

    with st.container():
        st.subheader("1. Background")
        st.markdown("""
    Sweden’s energy system features one of the most extensive **district heating networks (DHNs)** in the world, serving over **60%** of households. Traditionally fueled by **biomass and municipal waste**, these systems are now strained by rising fuel prices, emission targets, and infrastructure limitations.

    The Forsmark Nuclear Power Plant, located approximately 150 km from Stockholm, offers a unique opportunity to supply **base-load thermal energy** via **long-distance heat transport pipelines**. While nuclear plants primarily produce electricity, a significant share of thermal energy is typically lost in the condenser stage. This study evaluates the potential to harness that **low-grade waste heat** and redirect it to nearby urban heat networks.

    The background analysis covered:
    - The **thermodynamic limits** and losses in large-scale heat transfer
    - Potential **pipeline configurations and pressure drop models**
    - Urban demand profiles and **integration compatibility** with existing DHNs

    The idea builds on historical precedents in Eastern Europe and Finland, but incorporates **modern simulation techniques** and **economic assessment tools** to determine feasibility in a Swedish context.
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        ui.metric_card(title="DHN Coverage", content="60%+", description="Swedish buildings connected to DH")
    with col2:
        ui.metric_card(title="Nuclear Waste Heat", content=">60°C", description="Usable thermal energy at Forsmark outlet")
    with col3:
        ui.metric_card(title="Distance to Capital", content="~150 km", description="Forsmark → Stockholm pipeline route")

    st.subheader("Timeline – Key events shaping nuclear district heating")

    timeline_data = {
        "title": {
            "text": {
                "headline": "Energy Context in Sweden (2020–2024)",
                "text": "Major events impacting district heating and the motivation for nuclear waste heat recovery."
            }
        },
        "events": [
            {
                "start_date": {"year": "2020"},
                "text": {
                    "headline": "Biomass Prices Begin to Rise",
                    "text": "Biomass prices begin increasing steadily, peaking after 2022."
                },
                "media": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Pellets_hand.jpg/500px-Pellets_hand.jpg",
                    "caption": "Biomass fuel (wood pellets)"
                }
            },
            {
                "start_date": {"year": "2022"},
                "text": {
                    "headline": "European Energy Crisis",
                    "text": "Russia's invasion of Ukraine spikes energy prices and raises energy security concerns."
                },
                "media": {
                    "url": "https://memgraph.com/images/blog/gas-pipelines-in-europe/memgraph-european-gas-pipeline-network.png",
                    "caption": "Gas pipeline dependency"
                }
            },
            {
                "start_date": {"year": "2023"},
                "text": {
                    "headline": "9% of National GHG from Heating",
                    "text": "Heating and power account for 9% of total emissions, mostly from combustion."
                },
                "media": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/7/79/Annual_greenhouse_gas_emissions%2C_2022.png",
                    "caption": "GHG Emissions map"
                }
            },
            {
                "start_date": {"year": "2023"},
                "text": {
                    "headline": "80% of DH Emissions from Incineration",
                    "text": "Incineration remains the dominant emitter in the DH sector."
                },
                "media": {
                    "url": "https://static01.nyt.com/images/2018/09/24/world/24WASTE-INYT1/24WASTE-INYT1-superJumbo.jpg",
                    "caption": "Stockholm waste-to-energy plant"
                }
            },
            {
                "start_date": {"year": "2024"},
                "text": {
                    "headline": "Nuclear District Heating Case Study",
                    "text": "Study explores Forsmark NPP as a source of waste heat for Stockholm and Uppsala."
                },
                "media": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/1/15/Forsmark3.jpg",
                    "caption": "Forsmark Nuclear Power Plant"
                }
            }
        ]
    }

    timeline(timeline_data, height=600)
        
    
    st.markdown("""
    This background lays the foundation for the techno-economic model, which integrates **thermal loss estimation**, **cost modeling**, and **CO₂ mitigation forecasting** to assess long-term viability.
    """)

    with st.container():
        st.subheader("2. Techno-Economic Model")
        st.write("...")

    with st.container():
        st.subheader("3. Case Study: Forsmark to Stockholm & Uppsala")
        st.write("...")

    with st.container():
        st.subheader("4. Results and Analysis")
        st.write("...")

    with st.container():
        st.subheader("5. Conclusions")
        st.write("...")

    with st.container():
        st.subheader("Acknowledgements")
        st.write("...")