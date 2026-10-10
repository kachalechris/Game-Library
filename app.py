from flask import Flask, render_template

app = Flask(__name__)

#classes to allow to tell the website where to get the names
class Game_Codec:
    def __init__(self, name, rating, icon, genre, description, screenshots, video, game_id):
        self.name = name
        self.rating = rating
        self.icon = icon
        self.genre = genre
        self.description = description
        self.screenshots = screenshots
        self.video = video
        self.game_id = game_id

class Game_Library:
    def __init__(self):
        self.games = []

    def add_games(self, games):
        self.games.append(games)


#Call the function
library = Game_Library()

#Calling each class in the code
library.add_games(
    Game_Codec(
        name= "Hollow Knight", 
        rating=9, 
        icon="images/hollow-knight/HKcover.jpg", 
        genre="Metroidvania . Action . 2D", 
        description="Hollow knight is a classically styled 2D action adventure across a vast interconnected world develloped by indie devs Team Cherry .So forge your own path through this ruined kingdom as u fight ur way through hiddens bosses and uncover many secrets and treasure.",
        screenshots= [
            "images/hollow-knight/Gameplay1.jpg",
            "images/hollow-knight/Gameplay2.jpg"
        ],
        video= "images/hollow-knight/HK-Trailer.mp4",
        game_id="hollow_knight"
    )
)

library.add_games(
    Game_Codec(
        name="Sensory Overload", 
        rating=9, 
        icon="images/sensory-overload/S.O_Cover.jpg", 
        genre=" Indie . Endless Runner . Obstacle Avoidance",
        description="Sensory overload a Dropper game designed to overwhelm your senses. Twisting tunnels, psychedelic patterns and breathing walls assauslt your sense of balance as the the chaos unfolds. The Game was developed by Pancake Studios.",
        screenshots=[
            "images/sensory-overload/S.O_1.jpg",
            "images/sensory-overload/S.O_2.jpg"
        ],
        video="images/sensory-overload/Sensory-overload-Gameplay.mp4",
        game_id="sensory_overload"
    )
)

library.add_games(
    Game_Codec(
        name="Titanfall 2", 
        rating=8, 
        icon="images/titanfall-2/TF_Cover.jpg", 
        genre="Sci-Fi . First Person Shooter. Mecha Shooter",
        description="Titanfall 2 is a game focused on advanced titan technological welfare and also adds a single player campaign where u fight different enemies to save the world from destruction. The game was developed by Respawn Entertainment.",
        screenshots=[
            "images/titanfall-2/TF_1.jpg",
            "images/titanfall-2/TF_2.jpg"
        ],
        video="images/titanfall-2/Titanfall-2-Gameplay.mp4",
        game_id="titanfall_2"
    )
)

#The route to display the Html Code
@app.route("/")
def home():
    return render_template("index.html", games=library.games)
if __name__ == "__main__":
    app.run(debug=True)      