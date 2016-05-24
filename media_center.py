from media.media import Movie, Serie
from web import web

#movies
furious = Movie("Fast and Furious",
                "The best racing movie in the world",
                "http://i2.wp.com/cdn.bgr.com/2015/04/the_fast_and_the_furious_024-there-have-been-more-than-just-gear-changes-for-the-cast-of-the-fast-and-the-furious.jpeg?w=625",
                "https://www.youtube.com/watch?v=ZsJz2TJAPjw",
                "93 min",
                "2001")

the_social_network = Movie("The social Network",
                "The facebook history",
                "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ8CIh0VXqEkoA_X-cJatn1Dr7vFVvBX2g7Nya9Ji56lSyOSPK7DA",
                "https://www.youtube.com/watch?v=2RB3edZyeYw",
                "121 min",
                "2010")

jobs = Movie("Jobs",
                "The Steve Jobs history",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZxjaxfsBPZ54X-DOu9nc8agNbHmJ29GlNtb9O3W0v23ew9pvapg",
                "https://www.youtube.com/watch?v=zXzyLxad6xk",
                "127 min",
                "2013")

#series
breaking_bad = Serie("Breaking Bad",
                     "The history of the weirdest drug diller in the world",
                     "https://s-media-cache-ak0.pinimg.com/736x/f2/be/41/f2be41b3bd54ac7049ef0ba79c6620a3.jpg",
                     "https://www.youtube.com/watch?v=lrcqbavlbyQ",
                     "5 seasons",
                     "AMC")

mr_robot = Serie("Mr Robot",
                     "A history about hacking",
                     "http://thelowdownunder.com/wp-content/uploads/2016/01/Mr-Robot-Poster.jpg",
                     "https://www.youtube.com/watch?v=YibylhkLwGo",
                     "2 seasons",
                     "USA Network")

new_girl = Serie("New Girl",
                     "My GirlFriend Serie",
                     "http://www.finalreel.co.uk/wp-content/uploads/2014/08/New-Girl-Season-4-Poster.jpg",
                     "https://www.youtube.com/watch?v=D1NDNFZGY7k",
                     "5 seasons",
                     "Fox")

#build the content dictionary
content = {"movies":[furious, the_social_network, jobs], "series":[breaking_bad, mr_robot, new_girl]}

#launch the website
web.startSite(content)
