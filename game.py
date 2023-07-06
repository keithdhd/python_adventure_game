from player import Player
from item import Item
from location import Location

# Create player
player = Player("Player1")

# Create locations
kitchen = Location("Kitchen", "A small, cluttered kitchen.")
living_room = Location("Living Room", "A cozy living room.")
bedroom = Location("Bedroom", "A comfortable bedroom.")

# Connect locations
kitchen.add_connection("north", living_room)
living_room.add_connection("south", kitchen)
living_room.add_connection("east", bedroom)
bedroom.add_connection("west", living_room)

# Create items
key = Item("Key", "a small, rusty key.")
note = Item("Note", "a handwritten note.")

# Assign items to locations
kitchen.add_item(key)
bedroom.add_item(note)

# Set starting location for the player
player.move(kitchen)

# Game loop
while True:
    # Display current location and description
    current_location = player.location
    print(f"\n--- {current_location.name} ---")
    print(current_location.get_description())

    # Prompt player for input
    command = input("Enter a command (or quit): ")

    # Process player input
    if command == "quit":
        break
    elif command.startswith("go "):
        direction = command.split()[1]
        if direction in current_location.connected_locations:
            new_location = current_location.connected_locations[direction]
            player.move(new_location)
        else:
            print("You can't go that way!")
    elif command.startswith("take "):
        item_name = command.split()[1]
        for item in current_location.items:
            if item.name.lower() == item_name.lower():
                player.take_item(item)
                current_location.items.remove(item)
                print(f"You picked up the {item.name}.")
                break
        else:
            print("You can't take that!")
    elif command.startswith("use "):
        item_name = command.split()[1]
        for item in player.inventory:
            if item.name.lower() == item_name.lower():
                item.use()
                break
        else:
            print("You don't have that item!")
    else:
        print("Invalid command!")
