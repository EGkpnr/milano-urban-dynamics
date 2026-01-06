<div align="center">
  <img src="assets/dashboard_hero_banner.png" alt="Milano Urban Dynamics Banner" width="100%">
  <br>
  <h1>🏙️ Milano Urban Dynamics:<br>AI-Driven Telecom Analysis & Strategic Tariff Optimization</h1>

  <p>
    <b>From Big Data to Business Strategy:</b> Decoding the digital pulse of Milan using 300 Million+ telecom records to forecast urban traffic, uncover hidden socioeconomic patterns, and engineer a data-driven product strategy.
  </p>

  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://cloud.google.com/bigquery"><img src="https://img.shields.io/badge/Google_Cloud-BigQuery-4285F4?style=flat-square&logo=google-cloud&logoColor=white" alt="BigQuery"></a>
  <a href="https://lookerstudio.google.com/"><img src="https://img.shields.io/badge/BI-Looker_Studio-F9AB00?style=flat-square&logo=google-analytics&logoColor=white" alt="Looker Studio"></a>
  <img src="https://img.shields.io/badge/ML-XGBoost%20%7C%20K--Means-FF6F00?style=flat-square" alt="ML">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=flat-square" alt="Status">

  <br><br>
  <a href="[DASHBOARD_LINKINIZ]"><strong>🖥️ View Live Dashboard</strong></a> |
  <a href="docs/Milano_Technical_Report.pdf"><strong>📄 Download Technical Report (PDF)</strong></a> |
  <a href="#-repository-structure"><strong>🛠️ Explore Code</strong></a>
</div>

---

## 📋 Table of Contents

- [📍 Executive Summary](#-executive-summary)
- [💼 Business Context & Problem Statement](#-business-context--problem-statement)
- [🏗️ Solution Architecture](#%EF%B8%8F-solution-architecture)
- [🧠 Technical Methodology](#-technical-methodology)
  - [1. Urban Structure Decoding (Unsupervised Learning)](#1-urban-structure-decoding-unsupervised-learning)
  - [2. Predictive Modelling (Forecasting)](#2-predictive-modelling-forecasting)
  - [3. Deep Insights: Gentrification & Retail](#3-deep-insights-gentrification--retail)
- [💡 Strategic Outcome: Milano Smart Flex](#-strategic-outcome-milano-smart-flex)
- [📊 Dashboard Gallery](#-dashboard-gallery)
- [🛠️ Technology Stack](#%EF%B8%8F-technology-stack)
- [📂 Repository Structure](#-repository-structure)

---

## 📍 Executive Summary

**Milano Urban Dynamics** is an end-to-end data science project that leverages **Big Data Analytics** and **Machine Learning** to bridge the gap between static urban planning and dynamic human behavior.

By processing **300 Million+** Call Detail Records (CDR) from 2013, this project reveals the "invisible city"—mapping real-time population shifts, predicting network stress, and identifying socioeconomic disparities.

**Key Achievements:**
* **Data Processing:** Handled petabyte-scale data using Google BigQuery.
* **Model Accuracy:** Achieved **$R^2 = 0.996$** in hourly traffic forecasting using XGBoost.
* **Business Impact:** Identified a critical market gap (Supply: 2GB vs. Demand: 5.77GB) and formulated the **"Milano Smart Flex"** strategy to reduce churn and optimize network load.

---

## 💼 Business Context & Problem Statement

**The Problem:** In 2013, telecom operators and city planners were operating in "blind flight." Static census data failed to capture the pulse of the city, leading to inefficient infrastructure investments and rigid tariff plans that did not meet user needs.

**The Goal:** transform the "Silent Witness" (CDR Data) into actionable intelligence to:
1.  **Map** the functional use of city zones (Business vs. Residential) without labeled data.
2.  **Forecast** network traffic to prevent outages and optimize bandwidth.
3.  **Design** a dynamic, profitable product strategy based on actual consumption behavior.

---

## 🏗️ Solution Architecture

The project follows a modern, scalable ETL and ML pipeline architecture.

```mermaid
graph LR
    A[Raw CDR Data\n(300M+ Rows)] --> B(Google BigQuery\nData Warehouse);
    B --> C{Data Cleaning &\nWinsorization};
    C --> D[Aggregation &\nFeature Engineering];
    D --> E(Python ML Engine\nScikit-learn / XGBoost);
    E --> F[Predictive Models &\nClustering Results];
    F --> G(Looker Studio\nInteractive BI Dashboard);
    D --> G;
    G --> H[Strategic Business\nInsights];
    style B fill:#4285F4,stroke:#fff,color:#fff
    style E fill:#3776AB,stroke:#fff,color:#fff
    style G fill:#F9AB00,stroke:#fff,color:#fff
🧠 Technical Methodology1. Urban Structure Decoding (Unsupervised Learning)Using K-Means Clustering on temporal signal patterns, we classified the city into functional zones without any labeled data.Cluster 1 (Business Districts): Sharp activity rise at 09:00, drop at 18:00. Identified "Hidden Office Hubs" in officially residential areas.Cluster 0 (Residential): Dual peaks (Morning/Evening).Cluster 2 (Leisure/Mixed): Sustained activity late into the night.2. Predictive Modelling (Forecasting)To optimize network resource allocation, we predicted future traffic load.Algorithm: XGBoost Regressor (with Prophet for trend decomposition).Features: Temporal (Hour, Day, Month), Spatial (Grid ID, Cluster Type), and Lag Features.Result: The model captured complex urban rhythms with 99.6% Accuracy ($R^2$), enabling proactive network management.3. Deep Insights: Gentrification & RetailGoing beyond standard analysis to extract socioeconomic value:Digital Gentrification Index: Calculated the ratio of Data Usage vs. SMS Usage. Areas with high Data/SMS ratios were identified as "High-End/Modern" zones, correlating with higher purchasing power.Retail Opportunity Heatmap: Tracked post-event crowd dispersion (e.g., after a San Siro match), revealing that 60% of the crowd flows towards specific nightlife districts (Navigli), pinpointing prime locations for targeted advertising.💡 Strategic Outcome: Milano Smart FlexThe core output of this analysis is a strategic product proposal designed to solve the 2013 market inefficiency. Analysis showed users consumed 3x more data than the market standard allowed.The Solution: A hybrid tariff model using "Dead Zones" (Business districts at night) as leverage.FeatureMarket Standard (2013)Milano Smart Flex (Our Proposal)Business ValuePrice€15.00 / Mo€12.00 / MoCompetitive EdgeData Cap2 GB (Hard Limit)4 GB + Smart UnlimitedChurn ReductionInnovationNoneZone-Zero & Night-OwlNetwork Load BalancingImpactHigh Overage RiskCustomer LoyaltySustainable RevenueZone-Zero: Unlimited data in Business Clusters during office hours, utilizing idle capacity.📊 Dashboard GalleryThe insights are visualized in a "Duomo Notte" themed interactive dashboard.Urban Structure & AnomaliesStrategy & Model Performance<img src="assets/dashboard_screenshot_urban.png" width="450" alt="Urban Structure"><img src="assets/dashboard_screenshot_strategy.png" width="450" alt="Strategy">K-Means clustering and Anomaly detection.XGBoost predictions and Tariff Strategy.(Click the "View Live Dashboard" link at the top to explore interactively)🛠️ Technology StackDomainTechnologyUse CaseData WarehouseGoogle BigQueryStorage & Processing of 300M+ rows.LanguagePython 3.9+Data Science & ML Pipeline.ML LibrariesScikit-learn, XGBoostClustering & Regression.Data ManipulationPandas, NumPyCleaning & Feature Engineering.GeospatialGeoPandas, BigQuery GISSpatial Analysis (WKT Polygons -> Points).VisualizationLooker StudioBusiness Intelligence Dashboard.📂 Repository StructureBashmilano-urban-dynamics/
├── README.md               # Project Documentation
├── LICENSE                 # MIT License
├── requirements.txt        # Python Dependencies
│
├── notebooks/              # Jupyter Notebooks (Run in order)
│   ├── 01_Data_Cleaning_and_Prep.ipynb
│   ├── 02_Urban_Structure_Clustering.ipynb
│   ├── 03_Mobility_Network_Analysis.ipynb
│   ├── 04_Traffic_Forecasting_XGBoost.ipynb
│   └── 05_Deep_Insights_and_Strategy.ipynb
│
├── docs/                   # Reports & Presentations
│   ├── Milano_Technical_Report.pdf
│   └── Project_Presentation_Slides.pdf
│
└── assets/                 # Images for README
    ├── dashboard_hero_banner.png
    ├── dashboard_screenshot_urban.png
    └── dashboard_screenshot_strategy.png
<div align="center"><p>Developed with ❤️ and lots of coffee by <strong>[ADINIZ SOYADINIZ]</strong></p><a href="[LINKEDIN_LINKINIZ]"><img src="https://www.google.com/search?q=https://img.shields.io/badge/LinkedIn-Connect-0077B5%3Fstyle%3Dfor-the-badge%26logo%3Dlinkedin%26logoColor%3Dwhite" alt="LinkedIn"></a><a href="mailto:[EMAIL_ADRESINIZ]"><img src="https://www.google.com/search?q=https://img.shields.io/badge/Email-Contact%2520Me-D14836%3Fstyle%3Dfor-the-badge%26logo%3Dgmail%26logoColor%3Dwhite" alt="Email"></a></div>