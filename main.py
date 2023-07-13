import streamlit as st
import time

WORK_TIME_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

work_time_sec = WORK_TIME_MIN * 60
short_break_sec = SHORT_BREAK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60


def timer(moment):
    while moment:
        mins, secs = divmod(moment, 60)
        times = f'{mins:02d}:{secs:02d}'
        st.subheader(f"⏳{times}")
        time.sleep(1)
        moment -= 1


img_url = 'https://res.cloudinary.com/df7cbq3qu/image/upload/v1689234385/how-to-draw-a-tomato-featured-' \
          'image-1200_rrusfv.png'

page_config = {"page_title": 'Pomodora', "page_icon": img_url, "layout": "wide"}
st.set_page_config(**page_config)

st.title("Welcome to the Pomodora🍅 App")

st.markdown("The Pomodoro Technique is a time management method that uses a timer to break work into intervals, "
            "traditionally 25 minutes in length, separated by short breaks. "
            "This technique aims to improve focus and productivity by utilizing focused work periods and regular breaks"
            ". The timer is set for 25 minutes of work, followed by a 5-minute break. "
            "After completing four work intervals, a longer break of 20 minutes is taken. "
            "This cycle repeats to help maintain focus and avoid burnout.")

st.image("https://images.ctfassets.net/gg4ddi543f5b/36xjTs4xCqlC3Pzu0rPo83/"
         "631662e3141e4e5f8b02b6f18c3dc56e/pomodoro-1.jpg", width=1000)

col1, col2 = st.columns(2)
start_button = col1.button("Start the timer⏲️")
reset_button = col2.button("Reset⚠️")

if start_button:
    for rep in range(4):
        with st.empty():
            timer(work_time_sec)
            st.success("🔔 25 minutes is over! Time for a break😋")
            if rep == 3:
                st.info("Now we'll go on a break for 20 minutes😉.....Enjoy🍾")
                break

        with st.empty():
            timer(short_break_sec)
            st.warning("🚨5 Minutes break is over😢!!")

    with st.empty():
        timer(long_break_sec)
        st.warning("Finally we're done with the looooong break😭")

if reset_button:
    st.experimental_rerun()

with st.sidebar:
    option = st.selectbox(
        'How to do your first Pomodoro:',
        ('', 'Step 1', 'Step 2', 'Step 3', 'Step 4', 'Step 5'))
    if option == 'Step 1':
        st.write("Pick a task of your own like a project or homework")
    elif option == 'Step 2':
        st.write("Click on 'Start the Timer' and the timer will run for 25 minutes")
    elif option == 'Step 3':
        st.write("Work on the task until the time is up")
    elif option == 'Step 4':
        st.write("You will get 5 minutes of break after each pomodoro")
    elif option == 'Step 5':
        st.write("This will repeat for 4 pomodoros and finally you will have 20 minutes of long break")

    if st.checkbox("Note📝"):
        st.warning("You can click on 'Reset⚠️' to reset the timer")
