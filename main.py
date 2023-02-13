import streamlit as st
from PIL import Image

# Add a dropdown menu to select the anniversary gift
gift_options = ['Read why I love you','Read Poems', 'Read a Letter', 'Look at our Photos', 'Listen to our old Songs','Valentine 2023']
activity_type = st.sidebar.selectbox('What would you like to do today?', gift_options)


if activity_type == "Read why I love you":
    st.title('Hi Neelu,')
    st.header('Happy Birthday and Happy Anniversary!!')
    st.subheader("Welcome to our website.")
    st.write('The two days I am very thankful for is the day you were born, and the day you said yes. It has been an amazing journey and I am so grateful to have you in my life. Every thing that we have ever been through has led you to this moment.')
    st.header("Here are some things I love about you:")
    st.markdown("- You are kind and caring.")
    st.markdown("- You are beautiful and smart.")
    st.markdown("- You are strong, I am proud of the woman you turned out to be.")
    st.markdown("- You always try to bring the best out of me, make me want to be a better person.")
    st.markdown("- The way you try to raise one eyebrow and fail.")
    st.markdown("- You think you have great sense of humor, it's mediocre at best.")
    st.markdown("- Just how lucky you make me feel to have you.")

    st.text("Now got to the options on the top left corner and enjoy the rest of your gift")
    
elif activity_type == "Read Poems":
    st.header("Happy valentines day my love <3")
    
    

elif activity_type == "Read Poems":
    st.header("Here are some words i have written for you over the years:")
    poemlist=['How many more times do you want me to say this?','Sapphire sky', 'Poet', 'Atheist','Magic', 'Home', 'Poem', 'Where it all started']
    p=st.selectbox("Select a poem:",poemlist )
    if p=='How many more times do you want me to say this?':
        st.subheader("I love you!! I thank every god that there ever was, is or will be that you came into my life.")
    if p=='Sapphire sky':
        poem='''
        When everything is clouded, \n
        And I bite the dust, \n
        When I can't move, \n
        Like I'm paralysed by rust,\n
        I look for you, my sunshine, \n
        You feel like the spring in july, \n
        You're warm, bright and peaceful,\n
        Like walking under the sapphire sky. 
        '''
        st.text(poem)

    if p=='Poet':
        poem='''
        I'm a poet sweetheart,  \n
        I will describe you in a way, \n
        The universe itself will fall for you. \n
        (and you, for me).
        '''
        st.text(poem)
        st.caption("PSSSTT. It worked!! yay!!")
    if p=='Atheist':
        poem='''
        When i looked at her,\n 
        I prayed to god, with all my heart,\n
        let our destinies entwine, \n
        let our paths align, \n
        And let her be mine.\n
        And I'm an atheist. 
        '''
        st.text(poem)
        st.caption("well agnostic now, but you get the crux")
    if p=='Magic':
        poem='''
        She's like ice cream in the summer heat, \n
        Like my favourite song on repeat, \n
        Like winning money on a every bet, \n
        Like calmness of a sunset, \n
        Like icing on a stunning cake,\n 
        Beautiful as a snowflake, \n
        The one for which I'm homesick, \n 
        For she is pure magic. 
        '''
        st.text(poem)
    if p=='Home':
        poem='''
        Rolling down the Unfamiliar roads,\n
        don't care where we're from,\n
        Because whenever I'm with you, \n
        It feels like I'm home. 
        '''
        st.text(poem)
    if p=='Where it all started':
        image = Image.open('pictures/poem.jpg')
        image=image.rotate(270)
        st.image(image)
        st.caption("My first ever poem I wrote for you. You should have known right here I was head over heels in love with you.")
        st.write("-----------------------------------------------------------------------------------------")




elif activity_type == "Read a Letter":
    st.header("Open when letters!!")
    st.subheader('Rules:')
    st.write("1. Open only one letter at a time.")
    st.write("2. Let me know when you open a letter(feel free to give a reply as well).")
    st.write("3. Open these letters only when you are alone, you can however choose to show it to others later.")
    st.write("4. when none of these letters cover what you need, ask me which one you can open.")

    st.subheader("Open this letter when - ")
    # letter=["You just want to open a letter",'You miss me:',"You need to see my face",'When you feel like giving up',"I don't have words","you miss me(physically)","You can't feel my love"]
    # st.selectbox("Select a Letter:", letter)
    st.markdown(
        """
        <style>
        .streamlit-expanderHeader {
        font-size: x-large;
        font-weight: bold;
        border: 2px solid black;
        }
        
        </style>
        """, unsafe_allow_html=True
    )

    with st.expander("You miss me"):
      st.write('''
      Dear Neelu,

I know that being apart from you can be hard, and there are times when I miss you so much it feels like a physical ache. But I want you to know that no matter how far apart we are, my love for you is always strong and constant.

Remember all the little moments we've shared together? Like our first date, or the way you curl up into to me on the bed when we're watching a movie and i put my arm around you. Our first kiss, boy was that funny and so sweet. We have made so many memories over the last decade, i wish there was a way to get into our brains and extract it as a video. 
Those are the moments that make me realize just how much you mean to me.

I know that distance can be tough, but I want you to know that I'm always here for you and thinking of you. I am counting down the days until we can be together again. 
I hate everything about this time, but my love for you is bigger than this. Every moment we're apart just makes me appreciate and cherish the time we have together even more. You are my rock, my sunshine, and the love of my life. I can't wait until we're reunited again and can hold each other close.

Love,

Idiot

      ''')
    with st.expander("You need to see my face"):
        image = Image.open('pictures/mypic.jpg')
        st.write("Hi Sweetestheart,")
        st.image(image)
        st.write('''
        love,\n
        idiot
        ''')

    with st.expander("When you feel like giving up"):
      st.write('''
      Hi Neelu, 


Please know that you are not alone and that there are people who care about you and want to help you. If there's no one else, I'm here, always. 


It can be difficult to face the challenges that life throws our way, and it can feel like the weight of the world is on our shoulders at times. But I know that you are strong and capable of overcoming anything that comes your way.


I am proud of the woman you've been for the past few months. And i know, even though a lot of bad things have happened recently, you can still find your way. 

Rest, take some time off, I'll be your strength for a while, but don't stop putting in the inches. One inch at a time kiddo. You got this. 


Love, 

Idiot 

      ''')
    with st.expander("My words were not enough"):
      st.write('''
      Dear Neelu,

There are moments when I am at a loss for words, That's why I wanted to write this letter to you – to let you know that even when I don't have the words, my love for you is always strong.

Since i don't have words, I will write about the memories where we didn't need words to express our feelings.

That rainy day in the auto, me keeping that big plastic sheet for your portfolio. All our Holi celebrations together and our signature pose. Me randomly putting my arms around you on your terrace, and holding your hands.
The time we watched some shows together, And how in the middle we'd start kissing out of nowhere. When you used to kiss me while closing my eyes with your hand. How we used to just lie down hugging for some time.
all those forehead kisses. You showing me your favourite things, from arshi to BTS. You not liking sarabhai vs sarabhai. our mirror selfies. The way you blush at times, hide your face and then outright deny blushing.
The one time we went out and i didn't feel right and drank all your coldrink. You still haven't paid me back for your back exam fees even after making 2 lacs a month(chindi). 

The moment i came from kochi to surprise you and you cried. And you couldn't figure out why and from where times of our lives is being played. The way we hug and bobble. The times we have kissed against that wall. the times i'd slap and say "sexy ass".
the times alien was watching shows with us and we kissed quietly. The time you put all the photos in my bedroom for my birthday. and how i kept that birthday hat on for so long.
I still sometimes see confetti coming out of my laptop from that birthday. 
Our first date, I was thinking if i can hold your hand in public and you did it first. We drove around in my car for long while your hand was over mine. 

I wish we could just live those days again, this time knowing how special those moments are going to be for us. I guess we just have to make some more like that. 
Please know even though i don't have words right now, I still have all my love to give to you. 

Be Mine.

Love,

idiot

      ''')

#     with st.expander("You miss me(physically)"):
#       st.write('''
#       Hi Neelu,
#
#
# Please know that you are not alone and that there are people who care about you and want to help you. If there's no one else, I'm here, always.
#
#
# It can be difficult to face the challenges that life throws our way, and it can feel like the weight of the world is on our shoulders at times. But I know that you are strong and capable of overcoming anything that comes your way.
#
#
# I am proud of the woman you've been for the past few months. And i know, even though a lot of bad things have happened recently, you can still find your way.
#
# Rest, take some time off, I'll be your strength for a while, but don't stop putting in the inches. One inch at a time kiddo. You got this.
#
#
# Love,
#
# Idiot
#
#       ''')

    with st.expander("You can't feel my love"):
      st.write('''
      Hi sweetestheart, 


I know that you may be going through a difficult time right now and feeling like you are all alone, but there's no chance in hell I'm leaving your side. 


I also know it's been a while since you've been able to feel the love i have for you, so i just wanted to remind you that you are the love of my life, everything i have, and everything i am, will one day be yours, forever.


I can't wait to be with you, to tease you, to call you pappu again on the road, to talk to you while i hold your hands, and my arms are around you. Can't wait to watch things with you, listen to songs you like, hear you complain about Punjabi. 
I can't wait to kiss your lips, lick your boobs, run my hands all over your body, go on our next date, drive with your hand over mine. Give all of my love to you. God i have so much and you deserve all of it. 


You may not be able to reciprocate that love right now, you might not even be able to see things clearly to know that it's there, but i assure you, it is. 


You are hot and smart, almost as much as me, which makes you the luckiest woman on planet, but also i get to spend my life with someone who can match me, so I'm even luckier than you. 


Just remember, doesn't matter where you are and what you're doing, you'll always have a home in me. 


Until next time, our wall awaits. 


Love, 

Idiot 

      ''')

    with st.expander("You are having a hard time coping"):
      st.write('''
      Hi Neelu, 


You are struggling and are not able to cope with life right now. I want you to know that I am here for you and that you are not alone.


I know things are difficult and you don't seem to be able to function properly right now. Today was hard, maybe tomorrow will be harder, but whatever goes up, must come down. So will that hard part. It will get easier over time, things will happen. I have complete faith in you. 


It's okay if you couldn't do anything today, it'll be fine if you're not able to tomorrow as well. Take your time, there's no rush. I know once you get into that zone, no one will be able to catch you again. And i also know its just a matter of time now. 


Draw strength from me today if you're empty (you've been using my brain anyway  ). 
I can't wait to look back at this day and say I told you so. 


Fighting!!


Love, 

Idiot 

      ''')


elif activity_type == "Look at our Photos":
    st.header("Some memories that we made along the way!!")

    st.write("Funny how farewell are generally where things end, and it wasn't even the start for us")
    image = Image.open('pictures/farewell.jpg')
    st.image(image)
    st.caption("The one at the farewell")

    st.write("-----------------------------------------------------------------------------------------")

    image = Image.open('pictures/mall.jpg')
    st.image(image)
    st.caption("The one at the mall")
    st.write("-----------------------------------------------------------------------------------------")

    image = Image.open('pictures/photoframe.jpg')
    st.image(image)
    st.caption("The one with the photoframe")
    st.write("-----------------------------------------------------------------------------------------")

    image = Image.open('pictures/diwalilight.jpg')
    st.image(image)
    st.caption("The one with the Diwali lights")
    st.write("-----------------------------------------------------------------------------------------")

    image = Image.open('pictures/holi1.jpg')
    st.image(image)
    st.caption("The one on the Holi")
    st.write("-----------------------------------------------------------------------------------------")

    image = Image.open('pictures/holi2.jpg')
    st.image(image)
    st.caption("The one on the Holi after 'YES' ")
    st.write("-----------------------------------------------------------------------------------------")

    st.write('The photo that started all the teasing throughout my extended family')
    image = Image.open('pictures/originalpose.jpg')
    st.image(image)
    st.caption("The one with the original pose")
    st.write("-----------------------------------------------------------------------------------------")

    image = Image.open('pictures/recreate.jpg')
    rotated_img = image.rotate(90)
    st.image(rotated_img)
    st.caption("The one where we tried to recreate the pose")
    st.write("-----------------------------------------------------------------------------------------")

    image = Image.open('pictures/ilike.jpg')
    st.image(image)
    st.caption("The one where we look good together")
    st.write("-----------------------------------------------------------------------------------------")




else:
    st.header("Some songs that we used to listen to!!")
    st.write("-----------------------------------------------------------------------------------------")
    audio_file = open('song/Bruno Mars - Count on me [Official Video].mp3','rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    st.caption("who can you always count on?")

    st.write("-----------------------------------------------------------------------------------------")
    audio_file = open('song/Bruno Mars - Just The Way You Are (Official Music Video).mp3','rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    st.caption("Look yourself through my eyes")

    st.write("-----------------------------------------------------------------------------------------")
    audio_file = open('song/Jamie Scott -  Unbreakable Lyrics.mp3','rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    st.caption("What do you become when I put my arms around you?")

    st.write("-----------------------------------------------------------------------------------------")
    audio_file = open('song/Lawson - Where My Love Goes.mp3','rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    st.caption("Where do my love go?")

    st.write("-----------------------------------------------------------------------------------------")
    audio_file = open('song/Loser Of The Year (Acoustic Version).mp3','rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    st.caption("What am I without you?")

    st.write("-----------------------------------------------------------------------------------------")
    audio_file = open('song/NSYNC - This I Promise You (Official Music Video).mp3','rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    st.caption("Our wedding wows maybe?")

    st.write("-----------------------------------------------------------------------------------------")
    audio_file = open('song/Thank You_ - Official Music Video (Jason Chen Original) ft. ChaChi.mp3','rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    st.caption("What do I say for this amazing decade you have been with me?")

    st.write("-----------------------------------------------------------------------------------------")
    audio_file = open('song/The Script - Science & Faith (Official Video).mp3','rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    st.caption("How do someone explain a love like ours?")

    st.write("-----------------------------------------------------------------------------------------")
    audio_file = open('song/Train - If its love.mp3','rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    st.caption("You are the Greatest thing about me!!")

    st.write("-----------------------------------------------------------------------------------------")
    audio_file = open('song/Tyrone Wells - Time of our lives lyrics.mp3','rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    st.caption("The song with one of the best memories of my life. I hope this gift trumps that one")


