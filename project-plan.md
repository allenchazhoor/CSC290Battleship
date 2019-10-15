## Project Plan

##### Members:

- George
- Allen
- Bradley
- Chris
- Thomas

**Creation Date**: 8 October 2019

**Game**: Battleship

**Project Title**: <span style="background:black;color:white;padding:3px;border-radius:3px;">**DreadNought**:tm:</span>

**MarkUs Submitter**: George

**Meetings**: Friday afternoons in person or on Discord:tm:

 what the goals and motivations are of your project, and what success looks like how work will be divided, and how to ensure that the division is fair how team members will work together, including tools that you will use and meetings that you will hold how your team members can contribute ideas and work who will be responsible for submitting the deliverables on Markus who will be responsible for checking if team members need help what the protocols are if a team member is having difficulties what your deliverables will be, including "internal" deliverables that are *not* graded what your milestones will be, and when you expect to hit those milestones what your risks are and how to mitigate them (e.g. if a group member drops the course, if a group member does not show up to a presentation) 

---
##### Overall scope: have a functional game of battleship, be able to play against another human or the computer.

##### Goals/Motivations

Develop communication skills in a group environment. Good preparation for group projects in the industry. Get a high grade in the course. Build a game/app from scratch, the end product could be very rewarding. Put it on resume.

##### Risks and how to solve them
- Drop course: tell instructors, then divide the work of the person equally among the remaining people in the group.
- Person not responding: reach out to the person first (in lecture/tutorial/at school). If still doesn’t answer: tell instructor.
- Falling behind on schedule: arrange more group meetings/ remove additional features of the game that are not entirely necessary.
- Not shows up to presentation: already have a backup plan: divide the work among the group/ someone takes up his lines.

##### Must have

- GUI
  - PyGame
  - Game art
- AI for a human to play against
- A move timer
- Human vs Human

##### Good to have

- Save and load game states
- Customizable board size & number of ships
- Different strategies for computer player, so that it doesn’t play randomly.
- sounds and special effects 

##### Out of scope

- Mobile version
- Online

**Design Presentation**:

- Introduction
  - Explain battleship
    - Rules, etc
  - Chris
- Class structure & semantics
  - UML Diagram?
  - How everything fits together
  - Thomas & George
- Potential challenges and how we plan to overcome them
  - Allen & Bradley
- Questions
  - Everyone

**Programming**:

- AI
  - Allen
- GUI
  - Bradley & George
- Game Logic
  - Chris & Thomas

**Final Presentation**:

- TBD

#### Tools & Software

---

Programming language: Python 3.7.x :snake:

GUI Library: PyGame

Version control: Github

Communication software: Discord:tm:

- Communicate with TA using email & in-person

Documenting: Markdown

Presentation: Google Slides (exported as a ppt)

#### Deliverables & Milestones

---

1. Project Plan

   - Due 14 Oct 2019

2. Class design and program structure

   - By Friday 18 October 2019

   - How all the classes are going to interact

3. Design Presentation

   - Due 21 October 2019 @ 11pm

4. Game backend

   - By week 8 (9 November..?)

   - Core logic of the game

5. GUI plan

   - By 25 Oct

   - Drawings, concept art

6. GUI Complete

   - By week 8

7. Project Complete

   - By week 9

8. Final Presentation

   - Week 10 & 11

#### Deadlines

---

- Monday October 14 @ 9pm: Project plan
- Week 6 & 7 tutorials: Design Review Presentation
- October 27 @ 9pm: Individual Code Commit
- November 10 @ 9pm: Individual documentation
- TBD: Project repository
- Week 10 & 11: Final Presentation

#### Classes

---

- DreadNoughtController
  - game: DreadNought
- DreadNought
  - Player: enum
    - one
    - two
  - p1board: Board
  - p2board: Board
  - **Methods**
    - start(): void
    - move():
    - get_winner(): Player
- Board
  - tile: Enum
    - empty
    - hit
    - ship
    - ship_hit
  - board: tile\[][]
  - ships: list\<Ship>
- Ship
  - parts: list<(int, int)>
  - type: string
  - **Methods**
    - Size(): int
    - health(): int
      - `[0, size()]`
      - if `0`, ship is sunk
    - sunk(): boolean
    - is_hit(): boolean

#### Addendum

---

##### George

- Typing

##### Allen
My first contribution was the idea for the game's title. I was involved in all our group's brainstorming and discussion sessions and setup the git repository that we have been using and will continue to use for our project. I contributed to and helped write the Tools and Software, Milestones, and Deadlines subsections of the project plan. I will code AI aspect of game.

##### Bradley

##### Chris
For the creation of the project plan my contributions were discussing with the group about the scope of the projects. These topics ranged from the must-haves, good to have, and the out of scope ideas for the game we have selected. In addition, I also contributed towards this group work by discussing some of the class’s objects, methods, and other variance attributes that the game should have in order for it to work. Additionally, I also helped my group with organizing specific deadlines and milestones that should be set, such as when should the game be completed, by what time should the must haves for the game be completed, etc.   

##### Thomas
