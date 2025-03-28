Basically a top-down zombie shooter
currently have working movement, shift to sprint, crosshair and primitive line between player and crosshair, can use pygame.mouse.set_cursor() to set right onto mouse
Plan to anchor world around player, moving mouse moves camera slightly but never so that the player is out of frame.

TODO :
walls / obstacles:
    Add randomly generated walls or block which the player cant walk through or into and which stops bullets
zombies:
    Spawn variously coloured zombies around the map and give them an fov (dk abt range yet), if player enters fov or if makes sound in range (dk if possible) start following player
zombie behaviour:
    walk around randomly, if see player start moving towards player, zombie speed is faster than base player movement speed, if wall or obstacle is in the way go around (dk if possible)
shooting:
    if left click is clicked and there is ammo and not reloading shoot a bullet along line (current line from player to crosshair) and check if anything is in the line and continue depending on that
gun:
    give player ability to choose from presets of real guns (glock, desert eagle, revolver, fuck it even a glock with a switch (basically cheat code), and use different stats based on chosen guns, like magazine size, dmg, firing speed
shop:
    add some sort of shop where player can buy items or upgrades and ammo. make shop split up into different windows scattered around the screen with each window having details about different thins, for example one window has current gun stats and visualisations (attachments), other window has shop loot and such
detection with walls and zombies:
    collision triggers with walls and zombies. cant walk into walls and if walk into zombies deal damage (temporary slow = trauma ?), also collision for zombies and walls and pathing around (dk if possible)
zombie loot:
    zombies drop coins or crafting materials (dk yet), different zombies drop different loot, some could drop bullets, bandages, maybe one type of zombie could drop a live grenade general
optimization using classes and functions:
    optimize code using classes and functions to make it easier to understand and fix in the future
data saving / loading:
    save data into txt file based on name given at start, ability to share txt files and a load menu which loads given name, crash game if wrong name given too many times (3)
    can use pygame.key.start_text_input() for text related stuffs
