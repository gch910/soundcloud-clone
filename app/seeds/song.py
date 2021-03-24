from app.models import db, Song
from datetime import date
from app.aws import upload_file_to_s3

def seed_songs():

  demo1 = Song(
    title='Your Eyez Only',
    release_date = date(2016, 12, 9),
    song_path = "https://cloudify.s3.amazonaws.com/c16a1bd8d0134eeb86210771fd6cd7e0.mp3",
    image_path = 'https://edm.com/.image/t_share/MTU5NDY5Nzk2NTUzOTI1OTA1/soundcloud.png',
    user_id = 1,
    genre_id = 1,
  )
  demo2 = Song(
    title='Leave the door open',
    release_date = date(2021, 3, 5),
    song_path = "songs/leave_the_door_open.mp3",
    image_path = 'https://edm.com/.image/t_share/MTU5NDY5Nzk2NTUzOTI1OTA1/soundcloud.png',
    user_id = 2,
    genre_id = 5,
  )
  demo3 = Song(
    title='Peaches',
    release_date = date(2021, 3, 18),
    song_path = "songs/peaches.mp3",
    image_path = 'https://edm.com/.image/t_share/MTU5NDY5Nzk2NTUzOTI1OTA1/soundcloud.png',
    user_id = 3,
    genre_id = 4,
  )
  demo4 = Song(
    title='Hold On',
    release_date = date(2012, 2, 6),
    song_path = "songs/hold_on.mp3",
    image_path = 'https://edm.com/.image/t_share/MTU5NDY5Nzk2NTUzOTI1OTA1/soundcloud.png',
    user_id = 4,
    genre_id = 2,
  )

  josh1 = Song(
    title='Never'
    release_date = date(2017, 3, 10),
    song_path = 'https://www.youtube.com/watch?v=6eFcSesrP6A&ab_channel=JIDVEVO',
    image_path = 'https://images.genius.com/a466c251e0e8fe6f511db44a3512a554.1000x1000x1.jpg', 
    user_id = 'JID',
    genre_id = 0,
  )
  josh2 = Song(
    title='Working Out'
    release_date = date(2018, 10, 3),
    song_path = 'https://www.youtube.com/watch?v=FzpJl-i7ZRg&ab_channel=COLORS',
    image_path = 'https://i1.sndcdn.com/artworks-000464716785-nkulfo-t500x500.jpg', 
    user_id = 'JID',
    genre_id = 0,
  )
  josh3 = Song(
    title='Slick Talk'
    release_date = date(2018, 12, 5),
    song_path = 'https://www.youtube.com/watch?v=XZ4vKF6ueS8&ab_channel=JID',
    image_path = 'https://images-na.ssl-images-amazon.com/images/I/81MCQY5wKwL._AC_UL600_SR600,600_.jpg', 
    user_id = 'JID',
    genre_id = 0,
  )
  josh4 = Song(
    title='Caged Bird'
    release_date = date(2015, 12, 7),
    song_path = 'https://www.youtube.com/watch?v=ukTKLdpITVU&ab_channel=J.Cole-Topic',
    image_path = 'https://upload.wikimedia.org/wikipedia/en/3/3f/DreamvilleROTD2.jpeg', 
    user_id = 'J.Cole',
    genre_id = 0,
  )
  josh5 = Song(
    title='Apparently'
    release_date = date(2014, 12, 9),
    song_path = 'https://www.youtube.com/watch?v=Hz72aS64RJE&ab_channel=J.Cole-Topic',
    image_path = 'https://images-na.ssl-images-amazon.com/images/I/71iQcMbTpWL._SL1500_.jpg', 
    user_id = 'J.Cole',
    genre_id = 0,
  )
  josh6 = Song(
    title='Crooked Smile'
    release_date = date(2013, 6, 4),
    song_path = 'https://www.youtube.com/watch?v=fzzMOMkjm8A&ab_channel=JColeVEVO',
    image_path = 'https://upload.wikimedia.org/wikipedia/en/thumb/9/95/CrookedSmileJCole.jpg/220px-CrookedSmileJCole.jpg', 
    user_id = 'J.Cole',
    genre_id = 0,
  )
  josh7 = Song(
    title='Metropolis'
    release_date = date(2014, 10, 21),
    song_path = 'https://www.youtube.com/watch?v=4bdMtenCBjc&ab_channel=VisionaryMusicGroup',
    image_path = 'https://images-na.ssl-images-amazon.com/images/I/81ch1Foa-dL._SL1500_.jpg', 
    user_id = 'Logic',
    genre_id = 0,
  )
  josh8 = Song(
    title='Fade Away'
    release_date = date(2015, 11, 5),
    song_path = 'https://www.youtube.com/watch?v=b4qyMIOIDd4&ab_channel=Logic-Topic',
    image_path = 'https://upload.wikimedia.org/wikipedia/en/e/ea/TheIncredibleTrueStory.jpg', 
    user_id = 'Logic',
    genre_id = 0,
  )
  josh9 = Song(
    title='Young Sinatra III'
    release_date = date(),
    song_path = 'https://www.youtube.com/watch?v=5rVf7jkzmxw&ab_channel=UndeniableMixtape',
    image_path = 'https://t2.genius.com/unsafe/168x0/https%3A%2F%2Fimages.genius.com%2F4cb73fd1e86a44f861bc4ba694c17126.1000x1000x1.jpg', 
    user_id = 'Logic',
    genre_id = 0,
  )

  josh10 = Song(
    title='Stuck with U(with Justin Bieber)'
    release_date = date(2020, 5, 8),
    song_path = 'https://www.youtube.com/watch?v=h2jvHynuMjI&ab_channel=JustinBieberVEVO',
    image_path = 'https://upload.wikimedia.org/wikipedia/en/d/dc/Justin_Bieber_and_Ariana_Grande_-_Stuck_with_You.png', 
    user_id = 'Ariana Grande',
    genre_id = 3,
  )
  josh11 = Song(
    title='7 Rings'
    release_date = date(2019, 1, 18),
    song_path = 'https://www.youtube.com/watch?v=InOCRXEsK3M&ab_channel=SyrebralVibes',
    image_path = 'https://upload.wikimedia.org/wikipedia/en/thumb/b/b7/Ariana_Grande_-_7_rings.png/220px-Ariana_Grande_-_7_rings.png', 
    user_id = 'Ariana Grande',
    genre_id = 3,
  )
  josh12 = Song(
    title='34+35'
    release_date = date(2020, 10, 30),
    song_path = 'https://www.youtube.com/watch?v=cnyCcF20pRo&ab_channel=ArianaGrandeVevo',
    image_path = 'https://images.genius.com/19f6cba5a8b80305ef20723150e5ac72.707x707x1.png', 
    user_id = 'Ariana Grande',
    genre_id = 3,
  )
  josh13 = Song(
    title="Don't Start Now"
    release_date = date(2019, 10, 30),
    song_path = 'https://www.youtube.com/watch?v=8CLkVWB_Lj8&ab_channel=UniqueVibes',
    image_path = 'https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Dua_Lipa_-_Don%27t_Start_Now.png/220px-Dua_Lipa_-_Don%27t_Start_Now.png', 
    user_id = 'Dua Lipa',
    genre_id = 3,
  )
  josh14 = Song(
    title='New Rules'
    release_date = date(2017, 7, 15),
    song_path = 'https://www.youtube.com/watch?v=ClhLNUPqv8Q&ab_channel=TazNetwork',
    image_path = 'https://upload.wikimedia.org/wikipedia/en/thumb/e/e5/New_Rules_%28Official_Single_Cover%29_by_Dua_Lipa.png/220px-New_Rules_%28Official_Single_Cover%29_by_Dua_Lipa.png', 
    user_id = 'Dua Lipa',
    genre_id = 3,
  )
  josh15 = Song(
    title="We're Good"
    release_date = date(2021, 2, 11),
    song_path = 'https://www.youtube.com/watch?v=VwDTp0QTyY0&ab_channel=DuaLipa',
    image_path = 'https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/Dua_Lipa_-_We%27re_Good_cover_art.png/220px-Dua_Lipa_-_We%27re_Good_cover_art.png', 
    user_id = 'Dua Lipa',
    genre_id = 3,
  )
  josh16 = Song(
    title='Blinding Lights'
    release_date = date(2019, 11, 29),
    song_path = 'https://www.youtube.com/watch?v=fHI8X4OXluQ&ab_channel=TheWeekndVEVO',
    image_path = 'https://upload.wikimedia.org/wikipedia/en/thumb/e/e6/The_Weeknd_-_Blinding_Lights.png/220px-The_Weeknd_-_Blinding_Lights.png', 
    user_id = 'The Weeknd',
    genre_id = 3,
  )
  josh17 = Song(
    title='Starboy'
    release_date = date(2016, 11, 26),
    song_path = 'https://www.youtube.com/watch?v=xizN47Box_Y&ab_channel=7clouds',
    image_path = 'https://upload.wikimedia.org/wikipedia/en/thumb/3/39/The_Weeknd_-_Starboy.png/220px-The_Weeknd_-_Starboy.png', 
    user_id = 'The Weeknd',
    genre_id = 3,
  )
  josh18 = Song(
    title='The Hills'
    release_date = date(2015, 5, 27),
    song_path = 'https://www.youtube.com/watch?v=zxdSHfZFKkY&ab_channel=7clouds',
    image_path = 'https://upload.wikimedia.org/wikipedia/en/thumb/a/af/The_Weeknd_-_The_Hills.jpg/220px-The_Weeknd_-_The_Hills.jpg', 
    user_id = 'The Weeknd',
    genre_id = 3,
  )


  db.session.add(demo1)
  db.session.add(demo2)
  db.session.add(demo3)
  db.session.add(demo4)
  db.session.commit()