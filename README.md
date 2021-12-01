# Python Tkinter_Calculator
#### Video Demo:  https://youtu.be/uEJ0HvVzZyY
#### Description:
Bryan Adams
Naples, Fl
USA

The assignment I decided to build after much consideration was a 4-function calculator.
However, while designing it in Python I realized that it would not be as grand enough as I would like it to be.
From there, I found a python module known as "tkinter" which would provide all the necessary components to build a 
calculator similar to the one windows has to offer.

The 4-function calculator features Addition(+), Subtraction(-), Multiplication(*), and Division(/)
as its operators. It also contains numbers 1-9 and can even provide decimals as an output.

At first, I planned to make an Indeed Web Scraper to sort all of jobs relevant to the fields the user
inserted, but quickly learned that could conflict with Indeed's terms of service, and I fell back to my calculator idea.

To break down the code, I defined functions for the equals sign (solving the equation), clicking the buttons, and 
clearing the screen. From there, I used a pretty standard sizing of area to display the calculator on and then created a
bunch of buttons.

On my calculator I decided that I needed to use the "/" for division because the typical division symbol we see in math does not
exist on a keyboard, and I think most people would understand that the "/" meant division.

Another noteable feature of the calculator was the color. I decided to make it gray as I felt that color would best display a simplistic yet retro feel
to the calculators overall design. If I wanted to get really creative with it I could have changed the font color of the numbers and operators. 
However, I felt that black was pretty standard and chose that as my color of choice.

Putting all this information together was made possible by the Tkinter. After reading the module's documentation I was able to figure out the 
required steps using Python to make such an interface possible.
This is because Tkinter allows for the creation of Graphical User Interfaces (GUI)

While creating this calculator I had to keep in mind what an actual calculator looked like because no one wants to use the wierd off brand calculator 
that does not follow the traditional layout of most calculators. That being said, I listed the first first row [7, 8, 9] and the second row would be [4, 5, 6] 
and so on. In my particular case I simply looked at the TI-83 I had nearby to stylize the numbering off of.

...and that's my CS50 Final Project!