import streamlit as st


st.title("🏋️ BMI & Calorie Calculator")

st.write(
    "Calculate your BMI, daily calorie needs, and ideal weight range based on your personal details."
)

st.markdown("---")


name = st.text_input("Enter your name")

age = st.number_input(
    "Enter your age (years)",
    min_value=10,
    max_value=100,
    value=18
)

sex = st.radio(
    "Select your sex",
    ["Male", "Female"],
    horizontal=True
)

weight = st.slider(
    "Weight (kg)",
    min_value=30.0,
    max_value=150.0,
    value=60.0,
    step=0.5
)

height = st.slider(
    "Height (cm)",
    min_value=100,
    max_value=220,
    value=170,
    step=1
)

st.write(
    f"Name: {name}, Age: {age}, Sex: {sex}, Weight: {weight} kg, Height: {height} cm"
)


st.header("BMI Calculator")

height_m = height / 100
bmi = round(weight / (height_m ** 2), 1)

st.metric("BMI", bmi)

if bmi < 18.5:
    bmi_classification = "Underweight"
    health_risk = "Moderate"
    st.warning(f"Underweight - Health Risk: Moderate")

elif 18.5 <= bmi <= 24.9:
    bmi_classification = "Normal weight"
    health_risk = "Low"
    st.success(f"Normal weight - Health Risk: Low")

elif 25.0 <= bmi <= 29.9:
    bmi_classification = "Overweight"
    health_risk = "Elevated"
    st.warning(f"Overweight - Health Risk: Elevated")

else:
    bmi_classification = "Obese"
    health_risk = "High"
    st.error(f"Obese - Health Risk: High")

st.header("Daily Calorie Need")

activity_level = st.selectbox(
    "Select your activity level",
    [
        "Sedentary (desk job)",
        "Lightly active (1–3 days/wk)",
        "Moderately active (3–5 days)",
        "Very active (6–7 days)",
        "Extra active (2× training)"
    ]
)

activity_multipliers = {
    "Sedentary (desk job)": 1.2,
    "Lightly active (1–3 days/wk)": 1.375,
    "Moderately active (3–5 days)": 1.55,
    "Very active (6–7 days)": 1.725,
    "Extra active (2× training)": 1.9
}

if sex == "Male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

daily_calories = round(
    bmr * activity_multipliers[activity_level]
)

st.metric(
    "Daily Calorie Need (kcal/day)",
    daily_calories
)


st.header("Ideal Weight Range")

if sex == "Male":
    ideal_weight = 52 + 1.9 * ((height / 2.54) - 60)
else:
    ideal_weight = 49 + 1.7 * ((height / 2.54) - 60)

low_weight = round(ideal_weight * 0.9, 1)
high_weight = round(ideal_weight * 1.1, 1)

col1, col2 = st.columns(2)

with col1:
    st.metric("Lower Limit (kg)", low_weight)

with col2:
    st.metric("Upper Limit (kg)", high_weight)


st.header("Full Summary")

if st.button("Show my summary"):

    st.write(f"👤 Name: {name}")
    st.write(f"📊 BMI: {bmi} ({bmi_classification})")
    st.write(f"⚠️ Health Risk: {health_risk}")
    st.write(f"🔥 Daily Calorie Need: {daily_calories} kcal/day")
    st.write(
        f"⚖️ Ideal Weight Range: {low_weight} kg - {high_weight} kg"
    )


st.subheader("Compare Activity Levels")

selected_levels = st.multiselect(
    "Select activity levels to compare",
    [
        "Sedentary (desk job)",
        "Lightly active (1–3 days/wk)",
        "Moderately active (3–5 days)",
        "Very active (6–7 days)",
        "Extra active (2× training)"
    ]
)

if selected_levels:

    comparison_data = []

    for level in selected_levels:
        calories = round(
            bmr * activity_multipliers[level]
        )

        comparison_data.append(
            {
                "Activity Level": level,
                "Daily Calories (kcal/day)": calories
            }
        )

    st.table(comparison_data)