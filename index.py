from slithering import Frog, Lizard, Newt, Snake, Spider
from swimming import Crustacean, Duck, Fish, Goose, Swan
from walking import Cow, Donkey, Goat, Llama, Pig

miss_fuzz = Llama("Miss Fuzz", "domestic Llama", "morning")

stan = Donkey("Stan", "American Mammoth Jackstock", "midday")

peter = Goat("Peter", "Pygmy Goat", "afternoon")

short_stack = Cow("Short Stack", "Shetland Cow", "morning")

kiki = Pig("Kiki", "Kunekune", "midday")
print(f"{kiki.name} the {kiki.species} is available to pet during the {kiki.shift}")
noodle = Snake("Noodle", "Western Hognose")

beardo = Lizard("Beardo", "Bearded Dragon")

graham_chapman = Newt("Graham Chapmam", "Chinese Fire Belly")

hopper = Frog("Hopper", "Poison Dart Frog")

spinner = Spider("Spinner", "Red-Knee Tarantula")

mckoi = Fish("McKoi", "Koi")

daffy = Duck("Daffy", "Black Swedish")

grey = Goose("Grey", "Canadian Goose")

tilda_swanton = Swan("Tilda Swanton", "Trumpeter Swan")

sebastian = Crustacean("Sebastian", "Blue Crab")
