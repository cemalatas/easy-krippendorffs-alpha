"""
Krippendorff's Alpha Educational Calculator
A Streamlit app for calculating intercoder reliability.
"""

import streamlit as st

st.set_page_config(
    page_title="Krippendorff's Alpha Calculator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'app_state' not in st.session_state:
    st.session_state.app_state = {
        # Data
        'raw_dataframes': {},
        'coder_data': None,
        'column_mapping': {},
        'measurement_levels': {},
        'variable_levels': [],

        # Results
        'overall_alpha': None,
        'per_variable_results': None,
        'pairwise_results': None,
        'pairwise_overall': None,
        'coder_impact': None,
        'additional_stats': {},
        'disagreements': [],

        # Report
        'generated_report': None,

        # Navigation
        'current_step': 1,
        'analysis_complete': False,
    }


def render_progress_indicator():
    """Render the step progress indicator in sidebar."""
    st.sidebar.markdown("## Progress")

    steps = [
        ("1. Welcome", 1),
        ("2. Data Upload", 2),
        ("3. Configure Variables", 3),
        ("4. Run Analysis", 4),
        ("5. Disagreements", 5),
        ("6. Results", 6),
        ("7. Report", 7),
    ]

    current = st.session_state.app_state['current_step']

    for name, step_num in steps:
        if step_num < current:
            st.sidebar.markdown(f"✅ {name}")
        elif step_num == current:
            st.sidebar.markdown(f"**➡️ {name}**")
        else:
            st.sidebar.markdown(f"⬜ {name}")


# Main page content
st.title("📊 Krippendorff's Alpha Calculator")
st.markdown("""
Welcome to the **Intercoder Reliability Educational Platform**!

This tool helps you:
- **Calculate** Krippendorff's Alpha and other reliability statistics
- **Understand** what your results mean with interpretation guidelines
- **Explore** disagreements between coders in detail
- **Generate** comprehensive reports grounded in methodology

### Getting Started

Use the **sidebar navigation** to move through the steps:

1. **Welcome** - Learn about intercoder reliability
2. **Data Upload** - Upload your coded data files
3. **Configure Variables** - Set up your variables and measurement levels
4. **Run Analysis** - Compute all reliability statistics
5. **Disagreements** - Explore per-row disagreements
6. **Results** - View comprehensive dashboard
7. **Report** - Generate educational report

---
*Navigate using the pages in the sidebar →*
""")

# Render sidebar components
render_progress_indicator()
