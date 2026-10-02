import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_loader import load_data
from utils.ai_matcher import calculate_job_match, analyze_skill_gap

# Page Configuration
st.set_page_config(
    page_title="TechPulse360 - AI Job & Career Analytics",
    page_icon="🚀",
    layout="wide"
)

# Header Section
st.title("🚀 TechPulse360 — AI-Powered Job & Career Analytics")
st.markdown("Real-time Job Market Insights, Skill Gap Analysis & Salary Projections")
st.divider()

# Load Data
df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Market Filters")
selected_location = st.sidebar.multiselect("Select Location", options=df['location'].unique(), default=df['location'].unique())
selected_job_type = st.sidebar.multiselect("Select Job Type", options=df['job_type'].unique(), default=df['job_type'].unique())

# Filter Dataframe
filtered_df = df[
    (df['location'].isin(selected_location)) & 
    (df['job_type'].isin(selected_job_type))
]

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Market Analytics Dashboard", 
    "🤖 AI Job Matcher", 
    "💡 Skill Gap Analysis", 
    "📈 Salary Predictor & Growth"
])

# TAB 1: DASHBOARD
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Jobs Listed", len(filtered_df))
    col2.metric("Avg Salary (LPA)", f"₹{filtered_df['salary_lpa'].mean():.1f} L" if not filtered_df.empty else "N/A")
    col3.metric("Max Salary Offered", f"₹{filtered_df['salary_lpa'].max():.1f} L" if not filtered_df.empty else "N/A")
    col4.metric("Avg Experience Required", f"{filtered_df['experience_yrs'].mean():.1f} Yrs" if not filtered_df.empty else "N/A")
    
    st.markdown("---")
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.subheader("💰 Salary Distribution by Job Title")
        if not filtered_df.empty:
            fig1 = px.bar(
                filtered_df.sort_values(by="salary_lpa", ascending=False), 
                x="title", y="salary_lpa", color="company", text_auto=True
            )
            st.plotly_chart(fig1, use_container_width=True)

    with chart_col2:
        st.subheader("📍 Job Openings by Location")
        if not filtered_df.empty:
            fig2 = px.pie(filtered_df, names="location", title="Location Wise Spread", hole=0.4)
            st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📋 Explore Job Data")
    st.dataframe(filtered_df, use_container_width=True)

# TAB 2: AI MATCHER
with tab2:
    st.subheader("🤖 Smart Skill & Job Matching Engine")
    user_skills_input = st.text_input("Apni skills enter karein (e.g., Python, SQL, Machine Learning):", "Python, Machine Learning, SQL")
    
    if st.button("🔍 Find Matching Jobs", type="primary"):
        matched_df = calculate_job_match(user_skills_input, filtered_df)
        st.success("Matching Complete!")
        
        for idx, row in matched_df.head(5).iterrows():
            with st.container():
                st.markdown(f"### **{row['title']}** at **{row['company']}**")
                col_a, col_b, col_c = st.columns(3)
                col_a.write(f"📍 **Location:** {row['location']}")
                col_b.write(f"💼 **Salary:** ₹{row['salary_lpa']} LPA")
                col_c.write(f"🎯 **Match Score:** `{row['match_percentage']}%`")
                st.caption(f"**Required Skills:** {row['skills']}")
                st.divider()

# TAB 3: SKILL GAP ANALYSIS
with tab3:
    st.subheader("💡 Identify Missing Skills For Your Dream Job")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        current_skills = st.text_area("Your Current Skills:", "Python, SQL, Pandas")
    with col_s2:
        target_role = st.selectbox("Select Target Dream Role:", options=df['title'].unique())
        
    if st.button("⚡ Analyze Skill Gap", type="primary"):
        matched_s, missing_s = analyze_skill_gap(current_skills, target_role, df)
        
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.success(f"✅ **Skills You Already Have ({len(matched_s)}):**")
            for ms in matched_s:
                st.write(f"• {ms}")
                
        with col_res2:
            st.error(f"❌ **Skills You Need to Learn ({len(missing_s)}):**")
            for mis in missing_s:
                st.write(f"• **{mis}**")

# TAB 4: SALARY & GROWTH PREDICTOR
with tab4:
    st.subheader("📈 Experience vs Salary Growth Analysis")
    
    if not filtered_df.empty:
        fig_growth = px.scatter(
            filtered_df, 
            x="experience_yrs", 
            y="salary_lpa", 
            color="title",
            size="salary_lpa",
            hover_data=["company", "skills"],
            labels={"experience_yrs": "Experience (Years)", "salary_lpa": "Salary (LPA)"},
            title="How Experience Impacts Salary (Industry Trend)"
        )
        st.plotly_chart(fig_growth, use_container_width=True)