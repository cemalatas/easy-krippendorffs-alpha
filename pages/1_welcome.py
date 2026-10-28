"""Step 1: Welcome."""

import streamlit as st

st.set_page_config(page_title="Welcome - K's Alpha Calculator", layout="wide")

st.title("Welcome to the Intercoder Reliability Calculator")

st.markdown("""
This educational platform helps you calculate and understand **Krippendorff's Alpha**
and other intercoder reliability statistics for content analysis research.

## What is Intercoder Reliability?

Intercoder reliability (also called interrater reliability) measures how consistently
multiple coders classify the same content. It's essential for:

- Validating your coding scheme
- Ensuring your findings are reproducible
- Meeting publication standards

## What is Krippendorff's Alpha?

Krippendorff's Alpha (α) is a reliability coefficient developed for content analysis. It:

- **Accounts for chance agreement** (unlike simple percent agreement)
- **Works with any number of coders** (2 or more)
- **Handles missing data** gracefully
- **Supports different measurement levels**: nominal, ordinal, interval, and ratio
""")

with st.expander("Learn More: Interpreting Alpha Values"):
    st.markdown("""
    | Alpha Value | Interpretation | Recommendation |
    |-------------|----------------|----------------|
    | α ≥ 0.80 | **Acceptable** reliability | Proceed with analysis |
    | 0.67 ≤ α < 0.80 | **Tentative** reliability | Report with caution |
    | α < 0.67 | **Insufficient** reliability | Revise codebook or retrain coders |

    *Thresholds based on Krippendorff (2019). Content Analysis: An Introduction to Its Methodology.*
    """)

st.markdown("---")

if st.button("Get Started", type="primary"):
    st.session_state.app_state['current_step'] = 2
    st.info("Navigate to **2. Data Upload** in the sidebar to continue.")

# Show current status
st.markdown("---")
st.subheader("Current Status")

if st.session_state.app_state.get('coder_data'):
    st.success(f"✅ Data loaded: {st.session_state.app_state['coder_data'].n_coders} coders, {st.session_state.app_state['coder_data'].n_units} units")
else:
    st.info("⬜ No data loaded yet")

if st.session_state.app_state.get('analysis_complete'):
    st.success("✅ Analysis complete")
else:
    st.info("⬜ Analysis not yet run")
