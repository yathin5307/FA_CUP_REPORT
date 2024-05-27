import streamlit as st

# Page title
st.title('FA Cup Final: Manchester City vs Manchester United')

# Match details
st.subheader('Match Details')
st.write("""
- **Date:** May 25, 2024
- Time: 🕞 "Fashionably late" aka 15:30 (UTC). POV: UK guys don't let us sleep
- **Venue:** Wembley Stadium, London
""")

# Match preview
st.subheader('Match Preview')
st.write("""
The FA Cup final between Manchester City and Manchester United promises to be an exciting encounter. Both teams have a rich history and a fierce rivalry. Manchester City, under the management of Pep Guardiola, have been dominant in recent days, but Manchester United, led by Erik Ten Hag, have shown significant improvement this season, which was not enough till this day.

The match is expected to be closely contested, with both teams boasting talented squads.
""")

# Match prediction
st.subheader('Match Score')
# You can add your prediction model or simply write your prediction here
st.write("Manchester City 1 - 2 Manchester United")

# Inserting a PNG image
st.subheader('Match Poster')
image = "img1.png"  # Replace "path_to_your_image.png" with the path to your PNG image
st.image(image, caption='FA Cup Final Poster', use_column_width=True)


# Placeholder for memes for each goal
st.subheader('Goals')
# Page title
st.title('30’ GOOAL! MCI 0-1 MUN! GARNACHO SCORES!')

# Description
st.write("""
🤦‍♂️ Oops, Manchester City just pulled a classic "I got it! No, you get it!" move. It's like watching a sitcom gone wrong on the football field! Gvardiol forgets which manchester he's playing for!!!

🏰 Ortega rushes out like a knight in shining armor to save the day, but wait! Gvardiol's header goes full Matrix dodge mode, leaving poor Ortega looking like he's auditioning for a comedy of errors.

🤷‍♂️ Garnacho? Oh, he's just casually strolling into the scene, picking up the ball like it's his lost pet, and gently nudging it into the net.

🤣 And there you have it, A comedy of errors so epic... Manchester City's defense is a sitcom we never knew we needed!
""")

st.link_button("Click for the goal", "https://x.com/UTDFat/status/1794810159929389204")

st.title('39’ GOALL! MCI 0-2 MUN! MAINOO DOUBLES LEAD!')

# Description
st.write("""
🤦‍♂️ Aiyyo! What's happening, yaar? Man City's defense is more leaky than a tea strainer! United's just strolling in like, "Chalo bhai, let's score some goals!"

🏃‍♂️ So, Garnacho gets this long pass, and he's like, "Bhai, let's go for a run!" And Fernandes goes, "Haan yaar, I see you!" and passes the ball to Mainoo. It's like a game of pass-the-ball, but with a little extra masala!

🤣 Seriously, it's like watching a comedy show, but instead of laughs, we're getting goals! Man City's defense is going in circles out there! Gumir will be jumping of joyyy...
""")

st.link_button("Click here", "https://x.com/Kick_Clips_/status/1794745314261471268")

# Page title
st.title('87’ GOALL! MCI 1-2 MUN! DOKU PULLS ONE BACK!')

# Description
st.write("""
🤦‍♂️ Oh, bhai, what is Man City doing? It's like they're playing with the goals, but they're the only ones losing!

🏃‍♂️ So, Doku gets the ball and he's like, "Chalo yaar, let's give it a go!" And he shoots, aiming for Onana's near post. But wait, what's this? Onana's be, "Oops, my bad!" and accidentally helps the ball sneak in! It's like trying to hold a cup of chai without spilling, but ending up with a chai-stained shirt anyway!

👀 And there's City, suddenly thinking they've got a chance. But let's be honest, it's like finding a rupee coin on the street when you're expecting a jackpot!
""")

st.image(
            "https://i.pinimg.com/736x/53/0a/cd/530acd076c2afa90a95600734c96ff68.jpg",
            width=400, # Manually Adjust the width of the image as per requirement
        )

st.write("Finally!!!!! Man united fans breathe some air after 6 months into the year. Man United fans(Gumir) emerge, with a trophy and with a sigh of relief.")

st.image(
            "https://i.pinimg.com/736x/f5/5f/7d/f55f7d5e210b9431a3a1c41479b16209.jpg",
            width=400, # Manually Adjust the width of the image as per requirement
        )

# Footer
st.text("© 2024 signingoff.com. All rights reserved.")
