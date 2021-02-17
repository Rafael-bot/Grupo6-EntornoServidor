# Modelos

**user:**
- username. PK
- gmail
- password

**profile:**
- id_profile. PK
- photo
- number
- biography
- username. FK
- followers. FK
- id_posts. FK

**posts:**
- id_posts. PK
- numberPosts
- photo
- descripition
- postDate
- publicOrPrivate
- id_coments. FK
- like 

**followers:**
 - myfollows
 - myfollowers
 - username. FK
 
**coments:**
- id_coments. PK
- dateOfComent
- coment_text
- username. FK

**chat:**
- id_chat. PK
- chat_text
- username. FK

**historias:**
- id_history. PK
- history (photo)
- username. FK


