## Reference your JS Landscaper HW from Unit 1

## Make an "alert" introducing the game
    
# Welcome message
print("Welcome to Landscaper!!!")

## Game State

game = {"tool": 0, "money": 0}

tools = [
    {"name": "your teeth", "revenue": 1, "cost": 0},
    {"name": "rusty scissors", "revenue": 5, "cost": 5},
    {"name": "old-timey push mower", "revenue": 50, "cost": 25},
    {"name": "battery-powered lawn mower", "revenue": 100, "cost": 250},
    {"name": "team of starving students", "revenue": 250, "cost": 500}
]

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
## What happens when I  run out of tools? (if statement)
## Do I have enough money?
def upgrade():
    if (game["tool"] >= len(tools) - 1):
        print("no more upgrades")
        return 0
    next_tool = tools[game["tool"]+1]
    if (next_tool == None):
        print("There are no more tools")
        return 0
    if (game["money"] < next_tool["cost"]):
        print("not enough to buy tool")
        return 0
    print("You are upgrading your tool")
    game["money"] -= next_tool["cost"]
    game["tool"] += 1

## Win condition
def win_check():
    if(game["tool"] == 4 and game["money"] >= 1000):
        print("You Win!!!")
        return True
    return False

## Make Player functionality/The game playable...create While Loop
while (True):

    i = input("[1] Mow Lawn [2] Check Stats [3] Upgrade [4] Quit")

    i = int(i)

    if (i == 1):
        mow_lawn()
    
    if (i == 2):
        check_stats()

    if (i == 3):
        upgrade()

    if (i == 4):
        print("You quit the game")
        break

    if (win_check()):
        break