import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="You Are the Neural Network",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# Title & Introduction
# -----------------------------
st.title("🧠 You Are the Neural Network")
st.info(
    "You will act as a **neural network** and decide whether the image contains a **cat** 🐱.\n\n"
    "⚠️ The system may sometimes be wrong — this is intentional and realistic."
)

# -----------------------------
# Input Image
# -----------------------------
st.header("🖼️ Step 1: Look at the Image")

image_choice = st.radio(
    "Which image do you want to analyse?",
    ["CAT", "NOT A CAT"],
    horizontal=True,
    key="image_choice"
)

if image_choice == "CAT":
    st.image("images/cat.jpeg", caption="Input Image: Cat 🐱", use_column_width=True)
else:
    st.image("images/not_cat.jpeg", caption="Input Image: Not a Cat 🦁", use_column_width=True)

st.caption(
    "💡 The neural network does not understand images like humans.\n"
    "It only works with features."
)

# -----------------------------
# Step 2: Features
# -----------------------------
st.header("🕹️ Step 2: Select Observed Features")

with st.expander("🔍 Click to select features you observe", expanded=True):
    ears = st.checkbox("🐱 Pointed ears detected", key="ears")
    eyes = st.checkbox("👀 Cat-like eyes detected", key="eyes")
    tail = st.checkbox("🐾 Long tail detected", key="tail")

# -----------------------------
# Step 3: Weights
# -----------------------------
st.header("🎚️ Step 3: Adjust Importance")

with st.expander("⚖️ Adjust how important each feature is", expanded=True):
    w_ears = st.slider("Importance of ears", 0.0, 1.0, 0.4, key="w_ears")
    w_eyes = st.slider("Importance of eyes", 0.0, 1.0, 0.4, key="w_eyes")
    w_tail = st.slider("Importance of tail", 0.0, 1.0, 0.2, key="w_tail")

    st.caption("⬆️ Higher value = more influence on decision")

# -----------------------------
# Step 4: Decision
# -----------------------------
st.header("🤖 Step 4: Neural Network Decision")

i_ears = int(ears)
i_eyes = int(eyes)
i_tail = int(tail)

score_ears = i_ears * w_ears
score_eyes = i_eyes * w_eyes
score_tail = i_tail * w_tail
total_score = score_ears + score_eyes + score_tail

st.metric("🔢 Combined Score", f"{total_score:.2f}")

threshold = 0.6

if total_score >= threshold:
    st.success("✅ Prediction: **It is a cat!** 🐱")
else:
    st.error("❌ Prediction: **It is NOT a cat**")

# -----------------------------
# Learning Feedback
# -----------------------------
if image_choice == "NOT A CAT" and total_score >= threshold:
    st.warning(
        "⚠️ The system predicted **cat** even though the image is not a cat.\n\n"
        "This shows how AI can be **confident but wrong** when features overlap."
    )

# -----------------------------
# Explanation (Collapsed)
# -----------------------------
with st.expander("🧠 What is happening here? (Click to understand)"):
    st.markdown(
        """
        - The image is **input data**
        - Selected features are **inputs**
        - Importance values are **weights**
        - The score is a **combination of inputs**
        - The threshold acts like an **activation**
        - Learning happens by adjusting weights
        """
    )

    st.info(
        "💡 This is a **simulation** to help you understand neural networks.\n"
        "It is not a real image recognition system."
    )

st.markdown("---")
st.markdown("### 🔄 Controls")

if st.button("Reset Game 🔁"):
    for key in [
        "image_choice",
        "ears", "eyes", "tail",
        "w_ears", "w_eyes", "w_tail"
    ]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

# ---------------------------------
# Footer
# ---------------------------------
st.markdown(
    """
    <div style="text-align:center; font-size:13px; margin-top:40px;">
        <b>Neural Network Simulation</b><br>
        Fundamentals of AI – Rule Based</br>
        Developed by Ts. Ainie Hayati Noruzman © 2026
    </div>
    """,
    unsafe_allow_html=True
)
