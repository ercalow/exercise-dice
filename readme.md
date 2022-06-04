# exercise-dice
Generates randomized workouts for people who are easily bored!
Uses Django, MySQL.
Deployed here: http://ec2-54-67-95-40.us-west-1.compute.amazonaws.com:8000/

Can do now:
- User enters exercises - name, muscle group(s), difficulty, reps, and whether the workout should always include it.
- App creates a workout of 10 (max) exercises, random order, with no repeats. Works with less than 10 exercises as well.

To do:
- ~~Deploy on AWS-EC2.~~
- Add user login
- Add session management
- Be able to choose how many exercises to do.
- Be able to choose: repeats, or no repeats.
- Be able to randomize number of reps.
- Option to make it so exercises with the same muscle groups are never next to each other.
- Option to make it so easy and hard exercises are never next to each other.
- If an exercise is marked "always include," always include it.
- Make it way easier on the eyes, maybe with AngularJS
