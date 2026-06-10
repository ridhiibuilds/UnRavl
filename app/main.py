#jun 4


import streamlit as st
import sys
sys.path.append(".")
from data.suggestions import get_suggestions, get_suggestions_by_vibe, get_easy_suggestions
#new imports for ai brain yeeehooo
from transformers import pipeline
from PIL import Image


#class labels-----------------------------------------------------------------------------------------------------------

class_names = ["Blazer",
"Blouse",
"Cardigan",
"Dress",
"Hoodie",
"Jacket",
"Jeans",
"Nightgown",
"Outerwear",
"Pajamas","Rain jacket",
"Rain trousers",
"Robe",
"Shirt",
"Shorts",
"Skirt",
"Sweater",
"T-shirt",
"Tank top",
"Tights",
"Top",
"Training top",
"Trousers",
"Tunic",
"Vest",
"Winter jacket","Winter trousers"]

@st.cache_resource
def load_classifier():
    return pipeline("image-classification", model="wargoninnovation/wargon-clothing-classifier", framework="pt")

classifier = load_classifier()

# PAGE CONFIG-----------------------------------------------------------------------------------------------------------


st.set_page_config(
    page_title="UnRavl",
    page_icon="🧵",
    layout="centered"
)


# HEADER-----------------------------------------------------------------------------------------------------------


st.title("🧵⚡ UnRavl")
st.subheader("Transform clothes you're bored of into something you actually want to wear.")
st.divider()


# STEP 1 — UPLOAD PHOTO-----------------------------------------------------------------------------------------------------------

default_index = 0 

st.markdown("### Step 1 — Upload your garment")
uploaded_file = st.file_uploader(
    "Take a clear photo of the garment",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Your garment", width=500)

    image = Image.open(uploaded_file)          # turn upload into an image the model can read
    with st.spinner("Analyzing your garment..."):
        results = classifier(image)
        
   

    top = results[0]
    number = int(top['label'].replace("LABEL_", ""))
    garment = class_names[number]
    
    default_index = class_names.index(garment)

    st.success(f"Detected: {garment} ({top['score']:.0%})")         
    st.divider()

    # STEP 2 — GARMENT DETAILS
    

    st.markdown("### Step 2 — Tell us about it")

    garment_type = st.selectbox(
        "What type of garment is this?",class_names,index=default_index
    )

    garment_color = st.text_input(
        "What color is it?",
        placeholder="e.g. black, white, blue"
    ).strip().lower()

    st.divider()

    # STEP 3 — CONDITION QUESTIONS

    st.markdown("### Step 3 — What's the situation?")

    is_bored = st.checkbox("I'm bored of it")
    doesnt_fit = st.checkbox("It doesn't fit anymore")
    is_damaged = st.checkbox("It's damaged or stained")

    st.divider()

    # STEP 4 — VIBE SELECTOR

    st.markdown("### Step 4 — What vibe are you going for?")

    vibe = st.selectbox(
        "Pick your aesthetic",
        ["any", "casual", "edgy", "Y2K", "minimal", 
         "feminine", "streetwear", "grunge", "vintage", "bohemian"]
    )

    st.divider()

    # STEP 5 — GET SUGGESTIONS

    if st.button("✨ UnRavl It"):

        with st.spinner("Analysing your garment... 🧵"):
            import time
            time.sleep(2)

        st.markdown("### Here's what we found")
        st.markdown(f"**Garment:** {garment_type}")
        st.markdown(f"**Color:** {garment_color}")

        if is_damaged:
            st.warning("⚠️ Looks damaged — here are repair and upcycle ideas")
        if doesnt_fit:
            st.info("📐 Doesn't fit — here are resize and reconstruction ideas")
        if is_bored:
            st.success("✨ Bored of it — perfect for a transformation!")

        st.divider()
        st.markdown("### Your Upcycle Suggestions")

        if vibe == "any":
            suggestions = get_suggestions(garment_type)
        else:
            suggestions = get_suggestions_by_vibe(garment_type, vibe)

        if is_damaged:
            suggestions = get_easy_suggestions(garment_type)

        if len(suggestions) == 0:
            st.warning("No suggestions found for this combination. Try a different vibe!")
        else:
            for suggestion in suggestions:
                with st.expander(f"✂️ {suggestion['name']} — {suggestion['difficulty']}"):
                    st.write(f"**What to do:** {suggestion['description']}")
                    st.write(f"**Tools needed:** {', '.join(suggestion['tools'])}")
                    st.write(f"**Vibes:** {', '.join(suggestion['vibe'])}")

else:
    st.info("👆 Upload a photo of your garment to get started.") 
