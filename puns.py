import sqlite3

#Connect to sqlite db or create it if it doesn't exist
conn = sqlite3.connect('puns.db')
cursor = conn.cursor()

#Create Table for puns
cursor.execute("CREATE TABLE IF NOT EXISTS puns (id INTEGER PRIMARY KEY AUTOINCREMENT, pun TEXT NOT NULL)")

#List of puns (tuples) 
puns = [
    ("Why was the cat sitting on the computer? It wanted to keep an eye on the mouse!",),
    ("What\'s a cat\'s favorite color? Purr-ple.",),
    ("What do you call a pile of kittens? A meowtain!",),
    ("Why don\'t cats play poker in the jungle? Too many cheetahs.",),
    ("What do cats like to eat on a hot day? Mice cream.",),
    ("What\'s a cat\'s favorite magazine? Good Mousekeeping.",),
    ("Why was the cat bad at storytelling? It kept meow-ming the plot.",),
    ("What did the cat say when it fell off the table? \'Me-ow!\'",),
    ("Why do cats make terrible DJs? They always scratch the records.",),
    ("What\'s a cat\'s favorite movie? The Sound of Mew-sic.",),
    ("What do you call a cat who lives in the desert? Sandy Claws.",),
    ("Why don\'t cats like online shopping? They prefer cat-alogs.",),
    ("How does a cat end a fight? By saying, \'Paw-don me!\'",),
    ("What\'s a kitten\'s favorite sport? Hairball!",),
    ("What do cats say when they\'re surprised? \'Well, paw my whiskers!\'",),
    ("Why do cats always get their way? They\'re purr-suasive.",),
    ("What\'s a cat\'s favorite instrument? A purr-cussion set.",),
    ("Why was the cat so good at video games? It had nine lives.",),
    ("How do cats like their steak? Rare—meow and bloody.",),
    ("What kind of cat works in construction? A claw-tractor.",),
    ("What do you call a cat who becomes a detective? Sherlock Bones.",),
    ("Why was the cat so agitated? It was in a bad meowd.",),
    ("What\'s a cat\'s favorite dance move? The catwalk.",),
    ("Why are cats so good at math? They\'re great at paw-sitive numbers.",),
    ("What kind of books do cats read? Paw-sitive tales.",),
    ("What do you call a cat who loves to bowl? An alley cat!",),
    ("Why did the cat sit on the photocopier? To make paw-traits!",),
    ("How do cats end phone calls? \'Stay paw-sitive!\'",),
    ("What\'s a cat\'s favorite subject in school? Hiss-tory.",),
    ("Why did the cat join the Red Cross? It wanted to be a first-aid kit.",),
    ("How do you fix a broken cat? With fur-st aid.",),
    ("Why do cats hate Mondays? They\'re too paw-ful.",),
    ("What do you call a cat that loves karaoke? A meow-sician.",),
    ("What do cats call a big celebration? A claw-some party.",),
    ("Why do cats like sitting on keyboards? Because they like to keep in touch.",),
    ("What do you call a cat in a station wagon? A car-pet.",),
    ("How do cats like their eggs? Purr-fectly scrambled.",),
    ("Why did the cat wear a fancy dress? It wanted to look purr-suasive.",),
    ("What do you call a cat with no legs? It doesn\'t matter—it\'s not coming!",),
    ("Why do cats make terrible singers? They only hit flat meow-notes.",),
    ("What did the cat say to the fish? \'I\'m hooked on you!\'",),
    ("Why did the cat cross the road? To prove it wasn\'t chicken.",),
    ("What\'s a cat\'s favorite type of humor? Paw-ns!",),
    ("What kind of sports car does a cat drive? A Furr-ari.",),
    ("What\'s a cat\'s least favorite vegetable? As-purr-agus.",),
    ("How do cats stay in shape? By doing purr-lates.",),
    ("What did the cat say to the dog? \'Purr-sonally, I prefer naps.\'",),
    ("Why was the cat so grouchy? It was in a claw-ful mood.",),
    ("What do you get when you cross a cat with a ball of yarn? A string-along partner.",),
    ("What\'s a cat\'s favorite type of coffee? A cappurr-cino.",),
    ("What do you call a cat who\'s a magician? Purr-dini.",),
    ("How do cats resolve arguments? They hiss and make up.",),
    ("Why did the cat get detention? It was a litterbug.",),
    ("What\'s a cat\'s favorite dessert? Chocolate mouse.",),
    ("Why did the cat join the army? To become a claw-nel.",),
    ("What do you call a cat wearing shoes? Puss in boots.",),
    ("Why did the cat start a fight? Because it felt claw-strophobic.",),
    ("What\'s a cat\'s favorite drink? Purr-rier water.",),
    ("What do you call a cat with a smartphone? A paw-ditive influencer.",),
    ("Why do cats hate rain? It\'s wet and clawful.",),
    ("How do cats keep order? They follow the claw.",),
    ("What kind of car do cool cats drive? A Catillac.",),
    ("What\'s a cat\'s favorite place to visit? The meow-seum.",),
    ("Why don\'t cats use GPS? They always land on their paws.",),
    ("What\'s a cat\'s favorite breakfast? Pawncakes.",),
    ("What do cats say when they get hurt? \'Me-ouch!\'",),
    ("Why do cats love sitting in boxes? Because it\'s purr-sonal space.",),
    ("What kind of jobs do cats have? Purr-sonal assistants.",),
    ("Why are cats so great at parties? They\'re the life of the paw-ty.",),
    ("What do cats wear to sleep? Paw-jamas.",),
    ("What do you call a cat who loves crime dramas? Claw-lock Holmes.",),
    ("How do cats stay cool in the summer? With their paw-sicle fans.",),
    ("What do you call a cat that works for the government? A paw-litician.",),
    ("What do you call a big group of musical cats? A meowchestra.",),
    ("Why do cats make great singers? They have purr-fect pitch.",),
    ("What\'s a cat\'s favorite candy? KitKats.",),
    ("Why do cats never play hide and seek? Because they\'re always spotted.",),
    ("What\'s a cat\'s favorite type of movie? Cat-astrophic dramas.",),
    ("How do cats like to spend weekends? Meow-sing around.",),
    ("Why did the cat go to school? To get litter-ate.",),
    ("What\'s a cat\'s least favorite chore? Doing the litterbox laundry.",),
    ("Why was the cat so bad at directions? It always paws-ed to think.",),
    ("What\'s a cat\'s favorite kitchen appliance? The paw-sta maker.",),
    ("Why do cats love the internet? It\'s full of cat memes.",),
    ("What do you call a cat who works out? A purrr-sonal trainer.",),
    ("Why don\'t cats like fast cars? They\'re too claw-some to handle.",),
    ("What do cats say after a bad day? \'It was hiss-terical!\'",),
    ("What\'s a cat\'s favorite holiday? Meow-loween.",),
    ("What do you call a sneaky cat? A purr-lion.",),
    ("Why was the cat a great cook? It mastered the art of paw-stry.",),
    ("What do cats eat for breakfast? Mew-sli.",),
    ("What\'s a cat\'s favorite dance? The meowmba.",),
    ("Why do cats love gardening? They have a green paw.",),
    ("What do you call a cat who wins an award? A claw-some champion.",),
    ("What do cats say before starting a race? \'Paw-sition yourself!\'",),
    ("Why don\'t cats like jokes? They always purr-fer to be serious.",),
    ("How do cats order their drinks? Purr-on the rocks.",),
    ("What\'s a cat\'s favorite type of story? A claw-sic tale.",),
    ("Why are cats terrible at soccer? They\'re afraid of the ball of yarn.",)]

#Insert sample puns
cursor.executemany("INSERT INTO puns(pun) VALUES (?)", puns)

conn.commit()
conn.close()