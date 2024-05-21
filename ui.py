import time
import streamlit as st



st.markdown("<h1 style='text-align: center;font-size: 3.5rem;'>Discover Movies based on your mood</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;font-size: 1.5rem;'>How are you feeling now?</h1>", unsafe_allow_html=True)

moods = [
    "😄 Happy", "😃 Excited", "💪 Motivated", "🙏 Grateful", "🤢 Sick",
    "😢 Sad", "😔 Lonely", "😞 Disappointed", "💔 Heartbroken", "🤫 Smart",
    "😡 Angry", "😤 Frustrated", "😠 Annoyed", "😣 Irritated", "😡 Enraged",
    "😫 Stressed", "😰 Overwhelmed", "😨 Anxious", "😱 Panicked", "😨 Nervous",
    "😌 Chill", "🤓 Nerdy", "🤗 Hugging", "🤡 Clownish", "🤑 Rich"
]
st.markdown("""<style>.stButton>button {width: 130px; height: 50px; margin: 1px;}</style>""", unsafe_allow_html=True)
cols = st.columns(5)
mood_selected = None
for i, m in enumerate(moods):
    if cols[i % 5].button(m):
        mood_selected = m

if mood_selected is not None:
    st.write(f"You're feeling {mood_selected}!")
    st.write("Here are some movie recommendations for you:")
    
    with st.status("Loading recommendation system...",expanded=True) as status:
        time.sleep(2)
        st.write("Processing user mood...")
        time.sleep(1)
        st.write("Fetching movie data...")
        time.sleep(1)
        st.write("Generating recommendations...")
        
    
    
        from g4f.client import Client
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Please provide recommendations for five movies If a person is feeling {mood_selected}. For each movie, include the following details:(Name of the movie; Details about the movie, This should include a brief description of the story, ratings, tags, year of release, and duration;YouTube link to the trailer;)Ensure each recommendation follows this structure."}], 
        )
        status.update(label="Recommendation Generation complete!", state="complete", expanded=False)
    st.write(response.choices[0].message.content)

st.markdown("<h5 style='text-align: center;margin-top: 20px;font-size: 1rem;'>Made with 🎓 by JAMRI</h5>", unsafe_allow_html=True)
#
#🎓 (Graduation Cap) - Represents education and learning.
#💡 (Light Bulb) - Represents ideas and innovation.
#🚀 (Rocket) - Represents progress and advancement.
#📚 (Books) - Represents knowledge and study.
#🖥️ (Desktop Computer) - Represents technology and computing.
#'''