"""
Knowledge base content for Aman Kag's portfolio chatbots.

Two separate knowledge bases:
- IT_SUPPORT_KB: served on the IT support / service desk portfolio site
- DATA_SCIENCE_KB: served on the data science / analytics portfolio site

Each entry is a self-contained chunk of natural-language text (not fragments)
so the embedding model has full context to work with. Keep chunks focused on
one topic each -- this is what makes retrieval accurate.
"""

CURRENT_STATUS = (
    "As of mid-2026, Aman is currently completing his Professional Year (PY) "
    "program with Performance Education, with an internship placement starting "
    "soon. Alongside this, he continues to build out hands-on data science and "
    "IT portfolio projects, including a Microsoft 365 security operations "
    "dashboard and a GenAI-powered portfolio chatbot."
)

CONTACT_INFO = (
    "Aman Kag can be contacted by phone at +61 490 786 732 or by email at "
    "info.amankag@gmail.com. He is based in Tarneit, Melbourne, Australia. "
    "He holds a 485 Graduate Visa with full working rights in Australia until "
    "July 2029. His notice period for a new role is 1 week. He is available "
    "for interviews on weekdays between 4 and 6 PM, and is mostly flexible on "
    "weekends with advance notice."
)

# ---------------------------------------------------------------------------
# IT SUPPORT / SERVICE DESK KNOWLEDGE BASE
# ---------------------------------------------------------------------------

IT_SUPPORT_KB = [
    {
        "id": "it_summary",
        "text": (
            "Aman Kag is an IT support professional specialising in Service Desk "
            "and Desktop Support work. He has hands-on experience across "
            "Microsoft 365, Azure Active Directory (Entra ID), and ServiceNow "
            "environments. He holds a Master of Data Science, which sharpens how "
            "he reads patterns in recurring issues and system data. He focuses "
            "on getting to the root cause of a problem rather than just closing "
            "a ticket, and takes pride in leaving every user better off than "
            "when they reached out. He has supported both corporate office "
            "environments and multi-site warehouse environments, and brings a "
            "calm, structured approach to troubleshooting along with a habit of "
            "documenting what he learns so future resolutions are faster."
        ),
    },
    {
        "id": "it_current_status",
        "text": CURRENT_STATUS,
    },
    {
        "id": "it_skills_service_desk",
        "text": (
            "Aman's core IT support and service desk skills include Level 1 and "
            "Level 2 troubleshooting, incident and request management, "
            "ServiceNow administration, ITIL-aligned support processes, and SLA "
            "management."
        ),
    },
    {
        "id": "it_skills_cloud_identity",
        "text": (
            "In cloud and identity management, Aman works with Microsoft 365 "
            "Administration, Azure Active Directory (Entra ID), Intune Mobile "
            "Device Management (MDM), Single Sign-On (SSO), and Multi-Factor "
            "Authentication (MFA)."
        ),
    },
    {
        "id": "it_skills_systems_networking",
        "text": (
            "Aman's systems and networking skills include Windows 10 and "
            "Windows 11 troubleshooting, hardware and device support, and "
            "networking fundamentals such as TCP/IP, DNS, DHCP, and LAN/WAN "
            "connectivity."
        ),
    },
    {
        "id": "it_skills_data",
        "text": (
            "Beyond core IT support, Aman also has data and analytics skills "
            "including Python, SQL, Power BI, and building cloud data pipelines "
            "on AWS. This combination lets him apply data-driven thinking to "
            "identifying recurring IT issues, not just resolving individual "
            "tickets."
        ),
    },
    {
        "id": "it_education",
        "text": (
            "Aman holds a Master of Data Science from Deakin University in "
            "Melbourne, Australia, completed between 2022 and 2024, covering "
            "Machine Learning, Data Wrangling, Big Data Platforms, Data "
            "Visualisation, and a Capstone Project. He also holds a Bachelor of "
            "Computer Science from IES IPS College in India, completed between "
            "2016 and 2020."
        ),
    },
    {
        "id": "it_certifications",
        "text": (
            "Aman holds two Microsoft certifications: Microsoft Azure AI "
            "Fundamentals (AI-900) and Microsoft 365 Fundamentals (MS-900)."
        ),
    },
    {
        "id": "it_experience_infinite_asset",
        "text": (
            "Aman worked as a Service Desk Analyst at Infinite Asset Solutions "
            "in Melbourne, VIC, from July 2024 to July 2025, a one-year role. "
            "He delivered Level 1 and Level 2 desktop and software support to "
            "end users across Windows 10 and 11 environments, resolving over "
            "200 service requests weekly through ServiceNow while maintaining "
            "SLA compliance. He diagnosed and resolved hardware, software, and "
            "network issues including Outlook, Teams, VPN, and connectivity "
            "problems, minimising user downtime. He deployed and configured "
            "devices using Intune and SCCM, including imaging, staging, and "
            "policy enforcement to keep endpoints secure and compliant. He set "
            "up user accounts, Microsoft 365 access, and equipment for new "
            "starters, ensuring smooth onboarding across a collaborative, "
            "fast-paced team. He also analysed ServiceNow ticket trends to "
            "identify recurring issues, contributing to knowledge base "
            "improvements and reduced repeat incidents."
        ),
    },
    {
        "id": "it_experience_mactosys",
        "text": (
            "Aman worked as a Desktop Support Engineer at Mactosys Software "
            "Technology in Indore, India, from August 2020 to August 2022, a "
            "two-year role. He provided Level 1 and Level 2 desktop and "
            "application support to over 140 corporate and warehouse users "
            "across a multi-site environment. He supported and maintained over "
            "160 devices including scanners, tablets, and printers, reducing "
            "downtime in a fast-paced logistics environment. He assisted in "
            "rolling out Exchange Online and Azure MFA, improving security "
            "posture and reducing access-related support tickets. He applied "
            "Intune MDM policies across the device fleet to ensure consistency, "
            "security compliance, and remote manageability. He also authored "
            "Business Requirements Documents (BRDs) and Functional Requirements "
            "Documents (FRDs) for process improvements, translating stakeholder "
            "requirements into specifications used by developers and QA."
        ),
    },
    {
        "id": "it_project_secops",
        "text": (
            "Aman built the KAG SecOps Dashboard, a Microsoft 365 Security "
            "Operations Platform, as a portfolio project. It's a live security "
            "dashboard consolidating Entra ID, Intune, Defender, Compliance, "
            "and Service Health into one view, built using PowerShell 7 and the "
            "Microsoft Graph SDK against a real Microsoft 365 tenant, with a "
            "FastAPI backend and React frontend. He configured three "
            "Conditional Access policies (Require MFA, Block Legacy "
            "Authentication, Require Compliant Device) in report-only mode, "
            "plus a PowerShell audit script to export policy state for "
            "compliance tracking. He also automated the joiner/leaver lifecycle "
            "end-to-end: onboarding provisions accounts, licenses, security "
            "groups, and welcome emails, while offboarding revokes sessions, "
            "disables accounts, and removes licenses, with everything fully "
            "logged for audit. The project is available on GitHub."
        ),
    },
    {
        "id": "it_projects_data_portfolio",
        "text": (
            "In addition to IT support projects, Aman has a data and analytics "
            "portfolio including a Manufacturing Quality Dashboard, an AWS "
            "medallion pipeline using S3 and Athena with Isolation Forest and "
            "K-Means models feeding a Power BI Six Sigma dashboard, live and on "
            "GitHub. He also has a set of Data Science Projects covering "
            "diabetes risk prediction, injury prediction, and SQL/Pandas "
            "analysis notebooks completed during his Master of Data Science, "
            "available on GitHub."
        ),
    },
    {
        "id": "it_strengths",
        "text": (
            "Aman's key strengths in IT support include a calm, structured "
            "approach to troubleshooting under pressure, a focus on root-cause "
            "resolution rather than quick fixes, strong documentation habits "
            "that speed up future ticket resolution, and the ability to apply "
            "data analysis to spot recurring issues in ticket trends. His "
            "combination of hands-on service desk experience with a Master of "
            "Data Science background is relatively uncommon and lets him bring "
            "analytical thinking to operational IT problems."
        ),
    },
    {
        "id": "it_contact",
        "text": CONTACT_INFO,
    },
]

# ---------------------------------------------------------------------------
# DATA SCIENCE / ANALYTICS KNOWLEDGE BASE
# ---------------------------------------------------------------------------

DATA_SCIENCE_KB = [
    {
        "id": "ds_summary",
        "text": (
            "Aman Kag is an analytical and detail-oriented Data Science "
            "graduate with a Master of Data Science from Deakin University and "
            "a Bachelor of Computer Science. He has hands-on experience "
            "designing end-to-end cloud data pipelines on AWS, building "
            "predictive machine learning models, and developing Power BI "
            "dashboards with advanced data modelling. He is seeking a graduate "
            "data science or analytics role where strong technical foundations "
            "and a natural inclination toward structured problem-solving can "
            "contribute to real, data-driven impact."
        ),
    },
    {
        "id": "ds_current_status",
        "text": CURRENT_STATUS,
    },
    {
        "id": "ds_skills_programming_ml",
        "text": (
            "Aman's programming skills include Python, Pandas, NumPy, "
            "Scikit-learn, and SQL. His machine learning skills cover "
            "classification, regression, Random Forest, Convolutional Neural "
            "Networks (CNN), and Transfer Learning."
        ),
    },
    {
        "id": "ds_skills_data_engineering",
        "text": (
            "In data engineering, Aman has experience with AWS S3, AWS Glue, "
            "Amazon Athena, ETL design, and Medallion Architecture for "
            "building layered data pipelines."
        ),
    },
    {
        "id": "ds_skills_visualisation",
        "text": (
            "Aman's data visualisation skills include Power BI, DAX, data "
            "modelling, star schema design, Matplotlib, and Seaborn. His "
            "broader toolset includes Jupyter Notebook, VS Code, Git, and "
            "Microsoft Azure."
        ),
    },
    {
        "id": "ds_education",
        "text": (
            "Aman holds a Master of Data Science from Deakin University in "
            "Melbourne, Australia, completed between 2022 and 2024, covering "
            "Machine Learning, Data Wrangling, Big Data Platforms, Data "
            "Visualisation, and a Capstone Project. He also holds a Bachelor of "
            "Computer Science from IES IPS College in India, completed between "
            "2016 and 2020."
        ),
    },
    {
        "id": "ds_certifications",
        "text": (
            "Aman holds a Microsoft Azure AI Fundamentals (AI-900) "
            "certification from Microsoft, and has completed Figma Essential "
            "Training through LinkedIn Learning."
        ),
    },
    {
        "id": "ds_project_manufacturing_dashboard",
        "text": (
            "Aman's Production Quality Analytics Dashboard was built at Deakin "
            "University in 2024. The objective was to design a cloud data "
            "pipeline and Power BI dashboard enabling a manufacturing company "
            "to understand production quality trends across product types and "
            "time periods. Working individually, Aman designed a three-layer "
            "medallion architecture on AWS S3, with a Bronze layer for raw "
            "ingestion, a Silver layer for Python-cleaned data, and a Gold "
            "layer for analytics-ready output. AWS Glue handled ETL automation "
            "and Amazon Athena enabled serverless SQL querying before final "
            "import into Power BI. He built a multi-page dashboard with star "
            "schema relationships, DAX measures, and year-on-year slicers "
            "visualising defect rates, scrap percentages, downtime hours, and "
            "production volumes across five product categories. The result was "
            "a fully functional analytics dashboard simulating a real "
            "enterprise data workflow, developing practical skills across cloud "
            "data engineering, ETL pipeline design, dimensional modelling, and "
            "BI reporting."
        ),
    },
    {
        "id": "ds_project_heart_diabetes",
        "text": (
            "Aman built Heart Disease and Diabetes Prediction Models at Deakin "
            "University in 2023. The objective was to build binary "
            "classification models predicting the likelihood of heart disease "
            "and diabetes in patients using real-world clinical health "
            "datasets. Working individually, he sourced and preprocessed two "
            "clinical datasets, handling missing values, encoding categorical "
            "variables, and scaling features. He trained and compared three "
            "machine learning algorithms, Logistic Regression, Decision Tree, "
            "and Random Forest, across both datasets, evaluating performance "
            "using accuracy, precision, recall, F1-score, and ROC-AUC, with "
            "results visualised through confusion matrices and feature "
            "importance charts. Random Forest outperformed the other models on "
            "both datasets, and the project built a strong practical "
            "understanding of the end-to-end machine learning workflow, "
            "evaluation metrics, and algorithm trade-off analysis."
        ),
    },
    {
        "id": "ds_project_recycling_cnn",
        "text": (
            "Aman built a Recyclable vs Non-Recyclable Item Classifier at "
            "Deakin University in 2023, a computer vision project. The "
            "objective was to develop a model that accurately classifies waste "
            "items as recyclable or non-recyclable from images, supporting "
            "sustainability outcomes. Working individually, he built and "
            "trained a Convolutional Neural Network (CNN) model on a labelled "
            "image dataset using TensorFlow and Keras. Image preprocessing "
            "included resizing, normalisation, and data augmentation to improve "
            "generalisation, and transfer learning was applied to boost "
            "classification accuracy. The model achieved strong classification "
            "accuracy on unseen test images, building practical understanding "
            "of deep learning architecture, transfer learning techniques, and "
            "image preprocessing for real-world applications."
        ),
    },
    {
        "id": "ds_experience_overview",
        "text": (
            "Work experience overview: Aman has two professional roles on his "
            "record. He worked as a Service Desk Analyst at Infinite Asset "
            "Solutions in Melbourne, Australia (July 2024 - July 2025), resolving "
            "Level 1 incidents across Microsoft 365, Azure AD, Intune, and "
            "Windows via ServiceNow. Before that, he worked at Mactosys Software "
            "Technology in India (August 2020 - August 2022) in a role covering "
            "desktop support and business analysis, authoring BRDs/FRDs and "
            "analysing production data across 140+ users. Together this gives "
            "him both hands-on operational IT experience and business-analysis "
            "experience, alongside his data science education."
        ),
    },
    {
        "id": "ds_experience_mactosys",
        "text": (
            "Work experience: Mactosys Software Technology. Aman worked at Mactosys Software Technology in India from August "
            "2020 to August 2022, in a role covering desktop support and "
            "business analysis. He authored Business Requirements Documents "
            "(BRDs) and Functional Requirements Documents (FRDs) for internal "
            "manufacturing process improvements, translating stakeholder "
            "requirements into structured functional specifications used by "
            "developers and QA. He methodically analysed production and "
            "inventory data in Excel and SQL to identify bottlenecks, "
            "supporting decisions on workflow changes across 140+ users and "
            "160+ devices. He facilitated requirement-gathering workshops with "
            "operations, warehouse, and IT teams to map current-state and "
            "future-state processes and define acceptance criteria, and "
            "collaborated with developers on User Acceptance Testing (UAT) and "
            "change requests."
        ),
    },
    {
        "id": "ds_experience_service_desk",
        "text": (
            "Work experience: Infinite Asset Solutions. Aman worked as a Service Desk Analyst at Infinite Asset Solutions "
            "in Melbourne, Australia, from July 2024 to July 2025. He resolved "
            "Level 1 incidents across Microsoft 365, Azure AD, Intune, and "
            "Windows for end users via ServiceNow, consistently meeting SLA "
            "targets. He investigated recurring issues using ticket trend "
            "data, contributing to knowledge base articles that reduced repeat "
            "tickets, and supported device provisioning, account lifecycle, and "
            "access management following ITIL-aligned incident and change "
            "practices. This service desk experience gives Aman a practical, "
            "operational view of how data and systems are actually used day to "
            "day, which complements his analytical data science background."
        ),
    },
    {
        "id": "ds_personal_attributes",
        "text": (
            "Aman is an analytical and methodical problem-solver, as "
            "demonstrated through independently designing and delivering three "
            "end-to-end data science projects spanning cloud engineering, "
            "machine learning, and computer vision during his Master of Data "
            "Science. He is an adaptable and self-directed learner, having "
            "acquired practical AWS and Power BI skills beyond formal "
            "coursework to complete a production-quality analytics pipeline "
            "and dashboard. He is detail-oriented with a strong focus on data "
            "quality, consistently applying data validation and integrity "
            "principles throughout pipeline and modelling work. He is also a "
            "clear and structured communicator, translating complex data "
            "outcomes into accessible visual dashboards and presenting project "
            "findings to academic audiences."
        ),
    },
    {
        "id": "ds_contact",
        "text": CONTACT_INFO,
    },
]

KNOWLEDGE_BASES = {
    "it": IT_SUPPORT_KB,
    "ds": DATA_SCIENCE_KB,
}
