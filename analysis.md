## App Structure
### accounts
### courses


## Model Structure

### Profile
- **User**
- name
- email
- image
- favorites (ManyToMany)
- purchased_courses (ManyToMany)


### Course :
- **Instructor**
- title
- subtitle
- image
- price
- preview_video
- description
- **Category**
- language
- what_you_learn
- requirements
- *rate*
- *sections*
- *lectures*
- date_added
- date_modified


### Section
- **Course**
- name

### Lecture
- **Course**
- **Lecture**
- title
- subtitle
- video

### Category
- name

### Review
- **Course**
- **User**
- rating
- content
- date_added

### Insructor :
- Name
- title
- image
- description
