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

---

![](D:\Projects\CSC290Battleship\WBS.svg)

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

I hosted video calls and typed up what people were saying (this document). I was involved in the brainstorming and discussion and directly committed to the git respository. I took part in writing:

- The class structure
- The general stuff at the top
- Tools & software
- must and good to haves
- etc

I will be responsible for submitting on MarkUs and I am part of the GUI team, although we can fluctuate between areas of focus to help. I also took part in determining our groups internal and external deadlines for deliverables and our milestones.

##### Allen
My first contribution was the idea for the game's title. I was involved in all our group's brainstorming and discussion sessions and I set up the git repository that we have been using and will continue to use for our project. I contributed to and helped write most of the subsections of the project plan such as the Tools and Software, Milestones, and Deadlines. I assisted in conceptualizing the code design and division (classes and attributes) and proposed some of the key deadlines. I will code AI aspect of the game.

##### Bradley

##### Chris
For the creation of the project plan my contributions were discussing with the group about the scope of the projects. These topics ranged from the must-haves, good to have, and the out of scope ideas for the game we have selected. In addition, I also contributed towards this group work by discussing some of the class’s objects, methods, and other variance attributes that the game should have in order for it to work. Additionally, I also helped my group with organizing specific deadlines and milestones that should be set, such as when should the game be completed, by what time should the must haves for the game be completed, etc.   

##### Thomas
We all worked on the different topics together, since the project plan was not very long. First we discussed the scopes of the project where all came up with ideas and put the best ones in. For the rest of the project plan, we did it mostly together where everyone put ideas in and discussed them. I mostly contributed to the goals and motivations part as well as the risks and how to solve them. I also contributed some other ideas: like having different types of strategies for the computer among other things in the class part.
