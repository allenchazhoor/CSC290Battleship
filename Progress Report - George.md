## Progress Report - George

#### Main.py

The `main.py` is a file I created which is meant to bootstrap the application. This file initiates *PyGame*, imports `App`, and starts the game. Run this file to run the game.

Originally the `pygame` was initialized in the `App` class, see the **App** header for more.

#### The App Class

PyGame itself provides very little framework. All you really need to do is call `pygame.init()` and start drawing to the window. For this reason I created the `App` class which provides a better framework and separation of logic.

The class follows the singleton pattern (i.e. there is one instance of the class that can be accessed statically) and the instance is accessed using `App.instance`.

The class encapsulates all the objects and logic required to run the game. When `App.start()` is called, PyGame is instructed to display a window and `App` enters the game-loop by running `App.loop()`. The game loop runs while `App._running` is set to `True` and it has several discrete steps:

1. Handle PyGame events
   1. The `App.handle_events()` method loops through the current PyGame events and dispatches appropriately.
      1. If the event is `pygame.QUIT` then the `_running` flag is set to false and the game loop exits.
      2. If the event is a keyboard event, it is passed to `App.keyboard(event)`, and if it's a `MOUSEBUTTONDOWN` event, `App.click(event)`
2. Run game logic
   1. The `App.logic()` method is called, which is where all the game logic is meant to be encapsulated. If this were a live-action game then this is where the code to move physics objects would be applied.
3. Render the game: After all the events have been handled and the game logic has been run, the game needs to be drawn to the screen!
   1. The `App.render()` method is invoked, in this method:
      1. The screen is cleared using `App.fill_color`
      2. Stuff is rendered to the screen, which "stuff" will depend on the `App.render_option` flag. This is because the game has multiple states like the title screen, maybe a pause menu, and the game itself.
      3. We call `pygame.display.flip()` which applies all the rendering operations we have done to the screen

Once the loop has exited, `App.cleanup()` is called. This is where all necessary cleaning up operations like quitting PyGame, closing file handles, and maybe writing log data can be handled.

#### The Button Class

This class is my naive implementation of the classic button UI element. It's initialized with an xy position, width, height, style object, text string, and an on click (callable) handler.

##### How to use it

1. Instantiate an instance of `Button`, give it an appropriate position, width, height, etc and give it a proper `on_click` handler. The `on_click` handler can be a function or a lambda.
2. Handle clicking events. It's a button! We need to have it respond to when it's clicked. The way to do this is to call `Button.handle_click(MOUSEVENT)`. This method takes a mouse event and determines if the click happened within its own bounds and triggers the `on_click` handler if necessary. I recommend you place this in `App.click()` and pass the mouse event.
3. Ensure that the button gets rendered. Do this by inserting a `Button.render()` call inside `App.render()`. Please ensure that the button is only being rendered if you are checking mouse events and vice versa, you can do both of these optionally.