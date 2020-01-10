# brc-python

This folder contains the backend for the BRC class web page.

## API

### Students
get all students
    GET  /api/students
get students by name
    GET  /api/students?last_name=<last_name>,first_name=<first_name>
get student by id
    GET  /api/students?id=<id_>

post create student(?)
    POST /api/students
post modify student
    PUT /api/students?id=<id_>


### Instructors
get all instructors
    GET  /api/instructors
get instructors by name
    GET  /api/instructors?last_name=<last_name>,first_name=<first_name>
get instructor by id
    GET  /api/instructors?id=<id_>

post create instructor
    POST /api/instructors
post modify instructor
    PUT /api/instructors?id=<id_>


### Reviews
get all submitted reviews for student by id
    GET  /api/reviews/student?id=<id_>
get all reviews for instructor id
    GET  /api/reviews/instructor?id=<id_>
get all in-progress student reviews by instructor id
    GET  /api/reviews/student?instructor=<instructor_id>,submitted="false"
get unread student reviews
    GET  /api/reviews/student?unread

post create student review
    POST /api/reviews/student
post modify student review
    PUT /api/reviews/student?id=<id_>
post create instructor review
    POST /api/reviews/instructor


### Homework
get all homework
    GET /api/homework
get homework by week
    GET /api/homework?week=<week_>


### Lectures
get all lectures
    GET /api/lectures
get lectures by week
    GET /api/lectures?week=<week_>


### Outings
get all outings
    GET  /api/outings
get outings by week
    GET  /api/outings?week=<week_>


### Gear
get all gear
    GET  /api/gear


### Posts
get all posts
    GET  /api/posts
get requested number of recent posts
    GET  /api/posts?count=<count_>
get posts from the past 7 days
    GET  /api/posts?past_week
get post by id
    GET  /api/posts?id=<id_>









