# import json
# import os
# from datetime import datetime

# import numpy as np
# import pandas as pd
# import streamlit as st
# from PIL import Image
# from tensorflow.keras.models import load_model

# # ---------------------------------
# # Page Config
# # ---------------------------------
# st.set_page_config(
#     page_title="Butterfly AI Pro",
#     page_icon="🦋",
#     layout="wide"
# )

# # ---------------------------------
# # Theme / Dark Mode
# # ---------------------------------
# dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)

# if dark_mode:
#     st.markdown("""
#     <style>
#     .stApp {
#         background-color: #0e1117;
#         color: white;
#     }
#     .custom-card {
#         background-color: #1c1f26;
#         padding: 20px;
#         border-radius: 18px;
#         box-shadow: 0 4px 18px rgba(0,0,0,0.25);
#         margin-bottom: 15px;
#     }
#     </style>
#     """, unsafe_allow_html=True)
# else:
#     st.markdown("""
#     <style>
#     .stApp {
#         background: linear-gradient(to right, #f8ffae, #43c6ac);
#     }
#     .custom-card {
#         background-color: white;
#         padding: 20px;
#         border-radius: 18px;
#         box-shadow: 0 4px 18px rgba(0,0,0,0.15);
#         margin-bottom: 15px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # ---------------------------------
# # Sidebar Navigation
# # ---------------------------------
# st.sidebar.title("🦋 Butterfly AI Pro")
# page = st.sidebar.radio(
#     "Navigate",
#     ["Home", "Predict", "History", "Model Info", "About Project"]
# )

# # ---------------------------------
# # Load Model and Class Names
# # ---------------------------------
# @st.cache_resource
# def load_ai_model():
#     return load_model("butterfly_model.keras", compile=False)

# @st.cache_data
# def load_class_names():
#     with open("class_names.json", "r") as f:
#         return json.load(f)

# model = load_ai_model()
# class_names = load_class_names()

# # ---------------------------------
# # Butterfly Information
# # ---------------------------------
# butterfly_info = {
#     "MONARCH": "A famous orange and black butterfly known for long-distance migration.",
#     "BLUE MORPHO": "A bright blue tropical butterfly known for its vivid reflective wings.",
#     "MALACHITE": "A green butterfly with striking black patterns, found in tropical regions.",
#     "VICEROY": "Looks similar to the Monarch but often has a black line across the hindwing.",
#     "PEACOCK": "A colorful butterfly with eye-like patterns on its wings.",
#     "YELLOW SWALLOW TAIL": "A large yellow and black butterfly with elegant tail-like wing extensions.",
#     "MOURNING CLOAK": "A dark butterfly with pale wing borders, often found in cooler regions.",
#     "ATLAS MOTH": "One of the largest moths in the world, famous for its huge wingspan.",
#     "COMET MOTH": "A striking moth with long tail-like hindwings, native to Madagascar.",
#     "LUNA MOTH": "A pale green moth with long tails and eye spots, usually seen at night."
# }

# # ---------------------------------
# # Session State
# # ---------------------------------
# if "history" not in st.session_state:
#     st.session_state.history = []

# # ---------------------------------
# # Prediction Function
# # ---------------------------------
# def predict_species(img: Image.Image):
#     img = img.convert("RGB")
#     img = img.resize((224, 224))

#     img_array = np.array(img, dtype=np.float32) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)

#     predictions = model.predict(img_array, verbose=0)[0]
#     top_3_idx = predictions.argsort()[-3:][::-1]

#     return [(class_names[i], float(predictions[i]) * 100) for i in top_3_idx]

# # ---------------------------------
# # HOME PAGE
# # ---------------------------------
# if page == "Home":
#     st.title("🦋 Butterfly Species Identification System")
#     st.subheader("AI-Powered Major Project using Multi-Dataset Deep Learning")

#     tab1, tab2, tab3 = st.tabs(["Overview", "Features", "Quick Stats"])

#     with tab1:
#         st.markdown("""
#         ### Welcome
#         This system identifies butterfly species from uploaded or captured images using a fine-tuned deep learning model.

#         It is built as a **major project** using:
#         - Multi-dataset merged butterfly image collection
#         - Transfer learning with MobileNetV2
#         - Fine-tuning for better accuracy
#         - Streamlit-based premium interface
#         """)

#     with tab2:
#         st.markdown("""
#         ### Features
#         - 📤 Upload image
#         - 📸 Webcam capture
#         - 🔝 Top-3 species predictions
#         - 📊 Confidence graph
#         - 🧠 Smart confidence explanation
#         - 🦋 Butterfly description
#         - 🖼 Sample reference images
#         - 🕓 Prediction history
#         - 📥 Downloadable prediction report
#         - 🌙 Dark mode
#         """)

#     with tab3:
#         st.metric("Classes", "103")
#         st.metric("Validation Accuracy", "93.94%")
#         st.metric("Project Type", "Major Project")

# # ---------------------------------
# # PREDICT PAGE
# # ---------------------------------
# elif page == "Predict":
#     st.title("🔍 Predict Butterfly Species")

#     search = st.text_input("🔎 Search Butterfly Species")
#     if search:
#         matches = [c for c in class_names if search.upper() in c.upper()]
#         if matches:
#             st.write("**Matching Species:**")
#             for m in matches[:10]:
#                 st.write(f"- {m}")
#         else:
#             st.warning("No matching species found.")

#     camera_image = st.camera_input("📸 Take a photo")
#     uploaded_file = st.file_uploader(
#         "📤 Upload Butterfly Image",
#         type=["jpg", "jpeg", "png", "webp"]
#     )

#     image = None
#     if camera_image is not None:
#         image = Image.open(camera_image)
#     elif uploaded_file is not None:
#         image = Image.open(uploaded_file)

#     if image is not None:
#         left_col, right_col = st.columns([1, 1])

#         with left_col:
#             st.markdown('<div class="custom-card">', unsafe_allow_html=True)
#             st.subheader("Input Image")
#             st.image(image, caption="Uploaded/Captured Image", use_container_width=True)
#             st.markdown('</div>', unsafe_allow_html=True)

#         with right_col:
#             st.markdown('<div class="custom-card">', unsafe_allow_html=True)

#             with st.spinner("🔍 AI is analyzing the image..."):
#                 results = predict_species(image)

#             best_species, best_conf = results[0]
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#             st.success(f"🌟 Predicted Species: **{best_species}**")
#             st.info(f"📊 Confidence: **{best_conf:.2f}%**")
#             st.write(f"🕒 Prediction Time: {timestamp}")

#             if best_conf > 90:
#                 st.success("🧠 AI is very confident about this prediction.")
#             elif best_conf > 75:
#                 st.warning("🧠 AI is moderately confident. Similar species may exist.")
#             else:
#                 st.error("🧠 Low confidence. Try a clearer image.")

#             info = butterfly_info.get(
#                 best_species.upper(),
#                 "No detailed description available for this species yet."
#             )
#             st.markdown("### 🦋 Butterfly Info")
#             st.write(info)

#             st.markdown("### 🔝 Top 3 Predictions")
#             for idx, (species, conf) in enumerate(results, start=1):
#                 st.write(f"{idx}. **{species}** — {conf:.2f}%")
#                 st.progress(min(int(conf), 100))

#             st.markdown('</div>', unsafe_allow_html=True)

#         # Confidence Graph
#         st.markdown("### 📊 Confidence Graph")
#         df = pd.DataFrame(results, columns=["Species", "Confidence"])
#         st.bar_chart(df.set_index("Species"))

#         # Sample Image
#         st.markdown("### 🖼 Sample / Reference Image")
#         sample_path_jpg = f"samples/{best_species}.jpg"
#         sample_path_png = f"samples/{best_species}.png"

#         if os.path.exists(sample_path_jpg):
#             st.image(sample_path_jpg, caption=f"Reference: {best_species}", use_container_width=True)
#         elif os.path.exists(sample_path_png):
#             st.image(sample_path_png, caption=f"Reference: {best_species}", use_container_width=True)
#         else:
#             st.write("No reference image available yet.")

#         # Save History
#         st.session_state.history.append({
#             "time": timestamp,
#             "species": best_species,
#             "confidence": best_conf
#         })

#         # Download report
#         report = f"""
# Butterfly Prediction Report
# ---------------------------
# Prediction Time: {timestamp}

# Predicted Species: {best_species}
# Confidence: {best_conf:.2f}%

# Top 3 Predictions:
# """
#         for species, conf in results:
#             report += f"\n- {species}: {conf:.2f}%"

#         report += f"\n\nDescription:\n{info}\n"

#         st.download_button(
#             label="📥 Download Prediction Report",
#             data=report,
#             file_name="butterfly_prediction_report.txt",
#             mime="text/plain"
#         )

# # ---------------------------------
# # HISTORY PAGE
# # ---------------------------------
# elif page == "History":
#     st.title("🕓 Prediction History")

#     if st.session_state.history:
#         history_df = pd.DataFrame(st.session_state.history[::-1])
#         st.dataframe(history_df, use_container_width=True)

#         if st.button("🗑 Clear History"):
#             st.session_state.history = []
#             st.rerun()
#     else:
#         st.info("No predictions yet.")

# # ---------------------------------
# # MODEL INFO PAGE
# # ---------------------------------
# elif page == "Model Info":
#     st.title("📊 Model Information")

#     tab1, tab2, tab3 = st.tabs(["Architecture", "Performance", "Technical Details"])

#     with tab1:
#         st.markdown("""
#         ### Model Architecture
#         - Base Model: **MobileNetV2**
#         - Approach: **Transfer Learning**
#         - Fine-tuning: **Last 30 layers unfrozen**
#         - Output Layer: **103 classes**
#         """)

#     with tab2:
#         st.markdown("""
#         ### Performance
#         - Stage 1 Validation Accuracy: **90.07%**
#         - Fine-tuned Validation Accuracy: **93.94%**
#         - Validation Loss: **0.1968**
#         """)

#     with tab3:
#         st.markdown("""
#         ### Technical Details
#         - Image Size: **224 x 224**
#         - Batch Size: **32**
#         - Dataset Type: **Merged multi-dataset**
#         - Data Augmentation: rotation, zoom, shifts, brightness, horizontal flip
#         """)

# # ---------------------------------
# # ABOUT PROJECT PAGE
# # ---------------------------------
# elif page == "About Project":
#     st.title("📘 About Project")

#     st.markdown("""
#     ## Butterfly Species Identification System

#     This project was developed as a **major project** to identify butterfly species using artificial intelligence.

#     ### Objectives
#     - Identify butterfly species from images
#     - Improve real-world usability using webcam and upload support
#     - Provide species descriptions and prediction confidence
#     - Build a clean and interactive frontend

#     ### Project Highlights
#     - Combined **multiple datasets**
#     - Built a **103-class classification system**
#     - Used **transfer learning + fine-tuning**
#     - Achieved around **93.94% validation accuracy**
#     - Added premium frontend features with Streamlit

#     ### Technologies Used
#     - Python
#     - TensorFlow / Keras
#     - MobileNetV2
#     - Streamlit
#     - PIL / NumPy / Pandas

#     ### Future Scope
#     - Add Grad-CAM visual explanation
#     - Add butterfly habitat map
#     - Add conservation status information
#     - Deploy as a mobile-friendly public web app
#     """)

# # ---------------------------------
# # Footer
# # ---------------------------------
# st.markdown("---")
# st.caption("Built with TensorFlow, MobileNetV2, Streamlit, and Multi-Dataset Butterfly Images")


#..........



import json
import os
import csv
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model

# ---------------------------------
# Config
# ---------------------------------
st.set_page_config(
    page_title="Butterfly AI Pro",
    page_icon="🦋",
    layout="wide"
)

HISTORY_FILE = "history.csv"
SAMPLES_DIR = "samples"

# ---------------------------------
# Theme
# ---------------------------------
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)

if dark_mode:
    st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .custom-card {
        background-color: #1c1f26;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0 4px 18px rgba(0,0,0,0.25);
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp { background: linear-gradient(to right, #f8ffae, #43c6ac); }
    .custom-card {
        background-color: white;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0 4px 18px rgba(0,0,0,0.15);
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------
# Sidebar Navigation
# ---------------------------------
st.sidebar.title("🦋 Butterfly AI Pro")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Predict", "History", "Admin", "Gallery", "About Project", "Team"]
)

# ---------------------------------
# Load model and class names
# ---------------------------------
@st.cache_resource
def load_ai_model():
    return load_model("butterfly_model.keras", compile=False)

@st.cache_data
def load_class_names():
    with open("class_names.json", "r") as f:
        return json.load(f)

model = load_ai_model()
class_names = load_class_names()

# ---------------------------------
# Butterfly Info
# ---------------------------------
butterfly_info = {
    "MONARCH": "A famous orange and black butterfly known for long-distance migration.",
    "BLUE MORPHO": "A bright blue tropical butterfly known for its vivid reflective wings.",
    "MALACHITE": "A green butterfly with striking black patterns, found in tropical regions.",
    "VICEROY": "Looks similar to the Monarch but often has a black line across the hindwing.",
    "PEACOCK": "A colorful butterfly with eye-like patterns on its wings.",
    "YELLOW SWALLOW TAIL": "A large yellow and black butterfly with elegant tail-like wing extensions.",
    "MOURNING CLOAK": "A dark butterfly with pale wing borders, often found in cooler regions.",
    "ATLAS MOTH": "One of the largest moths in the world, famous for its huge wingspan.",
    "COMET MOTH": "A striking moth with long tail-like hindwings.",
    "LUNA MOTH": "A pale green moth with long tails and eye spots."
}

# ---------------------------------
# Helpers
# ---------------------------------
def ensure_history_file():
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "species", "confidence"])

def save_history(species, confidence):
    ensure_history_file()
    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), species, f"{confidence:.2f}"])

def load_history_df():
    ensure_history_file()
    return pd.read_csv(HISTORY_FILE)

def predict_species(img: Image.Image):
    img = img.convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array, verbose=0)[0]
    top_3_idx = predictions.argsort()[-3:][::-1]

    return [(class_names[i], float(predictions[i]) * 100) for i in top_3_idx]

# ---------------------------------
# Home
# ---------------------------------
if page == "Home":
    st.title("🦋 Butterfly Species Identification System")
    st.subheader("Major Project using Multi-Dataset Deep Learning")

    st.markdown("""
    ### Welcome
    This system identifies butterfly species from uploaded or captured images using a fine-tuned deep learning model.

    ### Highlights
    - 103 classes
    - ~93.94% validation accuracy
    - Multi-dataset merged training
    - Transfer learning + fine-tuning
    - Streamlit premium interface
    """)

# ---------------------------------
# Predict
# ---------------------------------
elif page == "Predict":
    st.title("🔍 Predict Butterfly Species")

    search = st.text_input("🔎 Search Butterfly Species")
    if search:
        matches = [c for c in class_names if search.upper() in c.upper()]
        if matches:
            st.write("**Matching Species:**")
            for m in matches[:10]:
                st.write(f"- {m}")
        else:
            st.warning("No matching species found.")

    camera_image = st.camera_input("📸 Take a photo")
    uploaded_file = st.file_uploader(
        "📤 Upload Butterfly Image",
        type=["jpg", "jpeg", "png", "webp"]
    )

    image = None
    if camera_image is not None:
        image = Image.open(camera_image)
    elif uploaded_file is not None:
        image = Image.open(uploaded_file)

    if image is not None:
        left_col, right_col = st.columns([1, 1])

        with left_col:
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            st.subheader("Input Image")
            st.image(image, caption="Uploaded/Captured Image", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with right_col:
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)

            with st.spinner("🔍 AI is analyzing the image..."):
                results = predict_species(image)

            best_species, best_conf = results[0]
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            st.success(f"🌟 Predicted Species: **{best_species}**")
            st.info(f"📊 Confidence: **{best_conf:.2f}%**")
            st.write(f"🕒 Prediction Time: {timestamp}")

            if best_conf > 90:
                st.success("🧠 AI is very confident about this prediction.")
            elif best_conf > 75:
                st.warning("🧠 AI is moderately confident. Similar species may exist.")
            else:
                st.error("🧠 Low confidence. Try a clearer image.")

            info = butterfly_info.get(
                best_species.upper(),
                "No detailed description available for this species yet."
            )
            st.markdown("### 🦋 Butterfly Info")
            st.write(info)

            st.markdown("### 🔝 Top 3 Predictions")
            for idx, (species, conf) in enumerate(results, start=1):
                st.write(f"{idx}. **{species}** — {conf:.2f}%")
                st.progress(min(int(conf), 100))

            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("### 📊 Confidence Graph")
        df = pd.DataFrame(results, columns=["Species", "Confidence"])
        st.bar_chart(df.set_index("Species"))

        st.markdown("### 🖼 Sample / Reference Image")
        sample_path_jpg = os.path.join(SAMPLES_DIR, f"{best_species}.jpg")
        sample_path_png = os.path.join(SAMPLES_DIR, f"{best_species}.png")

        if os.path.exists(sample_path_jpg):
            st.image(sample_path_jpg, caption=f"Reference: {best_species}", use_container_width=True)
        elif os.path.exists(sample_path_png):
            st.image(sample_path_png, caption=f"Reference: {best_species}", use_container_width=True)
        else:
            st.write("No reference image available yet.")

        save_history(best_species, best_conf)

        report = f"""
Butterfly Prediction Report
---------------------------
Prediction Time: {timestamp}

Predicted Species: {best_species}
Confidence: {best_conf:.2f}%

Top 3 Predictions:
"""
        for species, conf in results:
            report += f"\n- {species}: {conf:.2f}%"

        report += f"\n\nDescription:\n{info}\n"

        st.download_button(
            label="📥 Download Prediction Report",
            data=report,
            file_name="butterfly_prediction_report.txt",
            mime="text/plain"
        )

# ---------------------------------
# History
# ---------------------------------
elif page == "History":
    st.title("🕓 Prediction History")
    df = load_history_df()

    if not df.empty:
        st.dataframe(df.iloc[::-1], use_container_width=True)

        csv_data = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Download History CSV",
            csv_data,
            "history.csv",
            "text/csv"
        )

        if st.button("🗑 Clear History"):
            os.remove(HISTORY_FILE)
            ensure_history_file()
            st.rerun()
    else:
        st.info("No predictions saved yet.")

# ---------------------------------
# Admin
# ---------------------------------
elif page == "Admin":
    st.title("📊 Admin Dashboard")
    df = load_history_df()

    if not df.empty:
        total_predictions = len(df)
        avg_conf = pd.to_numeric(df["confidence"], errors="coerce").mean()

        st.metric("Total Predictions", total_predictions)
        st.metric("Average Confidence", f"{avg_conf:.2f}%")

        st.markdown("### Most Predicted Species")
        top_species = df["species"].value_counts().head(10)
        st.bar_chart(top_species)

        st.markdown("### Recent Predictions")
        st.dataframe(df.tail(10).iloc[::-1], use_container_width=True)
    else:
        st.info("No history data available yet.")

# ---------------------------------
# Gallery
# ---------------------------------
elif page == "Gallery":
    st.title("🖼 Butterfly Sample Gallery")

    if os.path.exists(SAMPLES_DIR):
        sample_files = [
            f for f in os.listdir(SAMPLES_DIR)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        ]

        if sample_files:
            cols = st.columns(3)
            for idx, sample_file in enumerate(sample_files):
                img_path = os.path.join(SAMPLES_DIR, sample_file)
                species_name = os.path.splitext(sample_file)[0]

                with cols[idx % 3]:
                    st.image(img_path, caption=species_name, use_container_width=True)
        else:
            st.warning("No sample images found in samples folder.")
    else:
        st.warning("Samples folder does not exist.")

# ---------------------------------
# About Project
# ---------------------------------
elif page == "About Project":
    st.title("📘 About Project")
    st.markdown("""
    ## Butterfly Species Identification System

    This project was developed as a **major project** to identify butterfly species using artificial intelligence.

    ### Objectives
    - Identify butterfly species from images
    - Improve real-world usability using webcam and upload support
    - Provide species descriptions and prediction confidence
    - Build a clean and interactive frontend

    ### Project Highlights
    - Combined **multiple datasets**
    - Built a **103-class classification system**
    - Used **transfer learning + fine-tuning**
    - Achieved around **93.94% validation accuracy**
    - Added premium frontend features with Streamlit

    ### Technologies Used
    - Python
    - TensorFlow / Keras
    - MobileNetV2
    - Streamlit
    - PIL / NumPy / Pandas
    """)

# ---------------------------------
# Team
# ---------------------------------
elif page == "Team":
    st.title("👥 Team / Submission Page")

    st.markdown("""
    ### Project Title
    **AI-Based Butterfly Species Identification System Using Multi-Dataset Deep Learning**

    ### Student Details
    - **Name:** Soumya Subhashree
    - **Department:** Computer Science 
    - **Project Type:** Major Project

    ### Guide Details
    - **Guide Name:** Dr.Bijaylaxmi Panda

    ### College Details
    - **College Name:** Gita autonomous college 

    ### Abstract
    This project identifies butterfly species from uploaded or captured images using a deep learning model trained on a merged multi-dataset butterfly image collection. The system uses transfer learning with MobileNetV2 and fine-tuning, achieving high validation accuracy. It includes an interactive web interface with image upload, webcam capture, prediction history, species information, reference images, and downloadable reports.
    """)

# ---------------------------------
# Footer
# ---------------------------------
st.markdown("---")
st.caption("Built with TensorFlow, MobileNetV2, Streamlit, and Multi-Dataset Butterfly Images")