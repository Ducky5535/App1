This app is the Mr Scany and its main goal is to look out for people where you can not see so if its out side your door or in your front door it will scan them and send you a text so you will be aware of them.



This piece of code takes machine learning and apply it to security camera so it only sends the code if there is a human if not then it waits untill there is.

I used the image identitfcation libary because this would allow me to identify people and I used twillo because they make it easy and with limited code to be able to send messages.

Some chalenges that I have faced was being able to get the camera to work so I had looked up a lot of ways to do this and learned that they are all different ways to do the same thing so this is a lesson learned that there are always more than one way to do something. The other thing that was really had was the x11 server error and I just had to run it through a display and directly off the nano to fix it.



So to have this program work for you just have to copy and pasted it in your ide and then change and do a few things,
  First run
    pip3 install twilio
  Then make sure to have the jetson-inference libary
  After you have all those things go to twilio and get an free account to get a AuthToken and place that in where it says [AuthenToken] 
  Then make sure you have a display to work and boom your done



CREDITS
My teachers from id camp

  and a few more I dont know then name
  
https://github.com/Futruo/jetsonai
https://www.twilio.com/en-us
