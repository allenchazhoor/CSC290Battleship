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

##### Out of scope

- Mobile version
- Online

#### Work Breakdown Structure

---

**Design Presentation**:

- 

**Programming**:

- Game tester
  - -
- AI
  - Allen
- GUI
  - -
  - Game art
    - -
- Game Logic
  - Board class
  - Ship class
  - etc
- 

**Final Presentation**:

- 

#### Tools & Software

---

Programming language: Python :snake:

GUI Library: PyGame

Version control: Github

Communication software: Discord:tm:

Documenting: Markdown

Presentation: Powerpoint

#### Deliverables & Milestones

---

1. Project Plan
2. Class design and program structure
   - How all the classes are going to interact
3. Project timeline
   - When we expect things to be completed
4. Game backend
   - Core logic of the game
5. GUI plan
   - Drawings, concept art
6. GUI Complete
7. Project Complete

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

##### Allen: Came up with title of game, contributed to Tools and Software, Milestones, Deadlines. Offered to code AI aspect of game

##### Bradley

##### Chris
For the creation of the project plan my contributions were discussing with the group about the scope of the projects. These topics ranged from the must-haves, good to have, and the out of scope ideas for the game we have selected. In addition, I also contributed towards this group work by discussing some of the class’s objects, methods, and other variance attributes that the game should have in order for it to work. Additionally, I also helped my group with organizing specific deadlines and milestones that should be set, such as when should the game be completed, by what time should the must haves for the game be completed, etc.   

##### Thomas
