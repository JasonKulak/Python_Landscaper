## Reference your JS Landscaper HW from Unit 1

## Game State

game = {"tool": 0, "money": 0}

tools = [
    {"name": "your teeth", "revenue": 1, "cost": 0}
    {"name": "rusty scissors", "revenue": 5, "cost": 5}
    {"name": "old-timey push mower", "revenue": 50, "cost": 25}
    {"name": "battery-powered lawn mower", "revenue": 100, "cost": 250}
    {"name": "team of starving students", "revenue": 250, "cost": 500}
]

## What do the player(s) need to win?
# player = {
#     "money": 0,
#     "tool": 0,
#     "won_game": False
# }

## What happens when I mow a lawn? need a "function to mow lawn"
def mow_lawn():
    tool = tools[game["tool"]]
    print(f"You mow a lawn with you {tool["name"]} and make {tool["revenue"]}")
    game["money"] += tool["revenue"]

## Check your progress
def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have {game["money"]} and are using a {tool["name"]}")

## What happens when I upgrade my tools?
def upgrade():
    next_tool = tools[game["tool"]+1]
    if (next_tool == None):
        print("There are no more tools")
        return 0
    if (game["money"] < next_tool["cost"]):
        print("not enough to buy tool")
        return 0
    game["money"] -= next_tool["cost"]
    game["tool"] += 1


## What happens when I  run out of tools? (if statement)
## Do I have enough money?


## Make an "alert" introducing the game
    
# Welcome message
print("Welcome to Landscaper!!!")

## Make Player functionality/The game playable...create While Loop
