# Modelos

**user:**
- username. PK
- gmail
- password

**profile:**
- id_profile. PK
- photo
- biography
- username. FK
- id_followers. FK
- id_posts. FK

**posts:**
- id_posts. PK
- numberPosts
- photo
- descripition
- postDate
- publicOrPrivate
- id_coments. FK
- username. FK
- like 

**followers:**
 - id_followers
 - myfollows
 - myfollowers
 - username. FK
 
**coments:**
- id_coments. PK
- dateOfComent
- coment_text
- username. FK
- number_likes

**chat:**
- id_chat. PK
- date_text
- chat_text
- username. FK

**histories:**
- id_history. PK
- date_of_history
- history (photo)
- username. FK


