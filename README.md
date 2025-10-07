

This project has been deployed on Render. This is the link!



To run this project on DevEdu, 

    source myenv/bin/activate
    python manage.py runserver 0.0.0.0:3000
    Then click on the button that pops up or the APP button

For this assignment, I used a lot of help from the internet as well as ChatGPT.
I had never used Django before, so I mainly used AI to understand how the basics worked.
Below are some of the main topics I asked ChatGPT about and what I learned from each part:

Understanding the Django structure (models.py, views.py, urls.py)
At first, I didn’t really understand how anything connected together.
ChatGPT explained that:
    models.py defines the database structure (for me, that meant Movies, Seats, and Bookings).
    views.py handles what gets displayed or sent back to the user.
    urls.py connects everything by linking URLs to views.

From there, I learned how to use path() and include() correctly and how to make sure the app was registered in settings.py.
There were a lot of moments where I had to keep going back and forth fixing small issues, but that helped me actually understand how Django links everything.

Fixing my models, serializers, and API endpoints
This part was definitely the hardest.
I kept getting random errors like “ImportError” 
ChatGPT helped me debug each one step-by-step until I started understanding what happened

The API endpoints I got a lot of help with because I kept getting "unauthorized". So we slowly debugged and I now better understand how Django passes data between frontend and backend and how to trace back to each part that was breaking. That took me a while.

ChatGPT showed me how to:
Use ModelViewSet and connect it correctly in urls.py
Reminded me to test my API endpoints with curl commands
Create proper relationships between Movies, Seats, and Bookings 

I also learned about POST requests and why I was getting “unauthorized” errors at first.
By the end, I understood how to check if my routes were working and if data was actually being saved to the database.

Writing tests and checking if everything worked
    I wrote several tests to make sure everything was working 
    Create movies successfully
    Create seats and connect them to movies
    Create bookings from those seats and movies

ChatGPT helped me understand Django’s TestCase class and how to structure my unit tets
When I got test errors like when Django didn’t accept time() values, chatGPt told me to fix them with timedelta

Learning how to use HTML templates and Bootstrap
ChatGPT helped me style everything using Bootstrap like buttons and such

We also fixed an issue with the “Book Seats” button.
At first, it broke when I moved the project to Render because it still used /proxy/3000/, which only works in DevEdu.
After changing it to a dynamic {% url 'seat_booking' movie.id %}, it worked well

Deploying to Render

This part took a lot of trial and error, and ChatGPT helped me fix it
Here’s what I learned during deployment:
What a Procfile is and how to use Gunicorn to run the Django app
How to configure static files with STATIC_ROOT and Whitenoise
How to fix broken dependencies in requirements.txt like removing gyp since Render does not support

This is a long list, but I truly feel like I now understand a lot more. ChatGPT helped me fix a lot of code that I had a hard time understanding and seeing in the first place. I am also pretty impressed about how much ChatGPT knows. I doubted it but it was truly able to answer all of my questions and guide me correctly.







