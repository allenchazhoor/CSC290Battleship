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

##### Must have

- GUI
  - PyGame
  - Game art
- AI for a human to play against
- A move timer

##### Good to have

- Save and load game states
- Customizable board size & number of ships

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

##### Allen

##### Bradley

##### Chris

##### Thomas