import random
 
def your_story(template):
    if template == "random":
        template1 = random.randint(1, 3)
    else:
        template1 = int(template)
        
    if template1 == 1:
        number = input("Enter a number:")
        measure_of_time = input("Enter a measure of time:")
        mode_of_transportation = input("Enter a mode of transportation:")
        adjective = input("Enter an adjective:")
        adjective2 = input("Enter an adjective:")
        noun = input("Enter a noun:")
        color = input("Enter a color:")
        part_of_the_body = input("Enter a part of the body:")
        verb = input("Enter a verb:")
        number2 = input("Enter a number:")
        noun2 = input("Enter a noun:")
        noun3 = input("Enter a noun:")
        part_of_the_body2 = input("Enter a part of the body:")
        verb2 = input("Enter a verb:")
        noun4 = input("Enter a noun:")
        adjective3 = input("Enter an adjective:")
        silly_word = input("Enter a silly word:")
        noun5 = input("Enter a noun:")
    
        story = f"It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. " \
        f"The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. " \
        f"There are nurses here who have {color} {part_of_the_body}. " \
        f"If someone wants to come into my room, I told them that they have to {verb} first. " \
        f"I've decorated my room with {number2} {noun2}. " \
        f"Today I talked to a doctor and they were wearing a {noun3} on their {part_of_the_body2}. " \
        f"I heard that all doctors {verb2} {noun4} every day for breakfast. " \
        f"The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}!"
     
        return story
 
    elif template1 == 2:
        person_name = input("Enter a proper noun (person's name):")
        noun = input("Enter a noun:")
        adjective1 = input("Enter an adjective (feeling):")
        verb1 = input("Enter a verb:")
        adjective2 = input("Enter an adjective (feeling):")
        animal = input("Enter an animal:")
        verb2 = input("Enter a verb:")
        color = input("Enter a color:")
        verb3 = input("Enter a verb (ending in -ing):")
        adverb = input("Enter an adverb (ending in -ly):")
        number = input("Enter a number:")
        measure_of_time = input("Enter a measure of time:")
        color2 = input("Enter a color:")
        animal2 = input("Enter an animal:")
        number2 = input("Enter a number:")
        silly_word = input("Enter a silly word:")
        noun2 = input("Enter a noun:")
        
        story = f"This weekend I am going camping with {person_name}." \
        f"I packed my lantern, sleeping bag, and {noun}." \
        f"I am so {adjective1} to {verb1} in a tent." \
        f"I am {adjective2} we might see a(n) {animal}, I hear they’re kind of dangerous." \
        f"While we're camping, we are going to hike, fish, and {verb2}." \
        f"I have heard that the {color} lake is great for {verb3}." \
        f"Then we will {adverb} hike through the forest for {number} {measure_of_time}. " \
        f"If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet!" \
        f"At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!! " \
        
        return story
 
    elif template1 == 3:
        person_name = input("Enter a proper noun (person's name):")
        adjective1 = input("Enter an adjective:")
        color = input("Enter a color:")
        animal = input("Enter an animal:")
        place = input("Enter a place: ")
        adjective2 = input("Enter an adjective:")
        magic_creature = input("Enter a magical creature(plural): ")
        adjective3 = input("Enter an adjective:")
        magic_creature2 = input("Enter a magical creature(plural): ")
        room = input("Enter a room in a house: ")
        noun = input("Enter a noun: ")
        noun2 = input("Enter a noun: ")
        noun3 = input("Enter a plural noun: ")
        adjective4 = input("Enter an adjective: ")
        noun4 = input("Enter a plural noun: ")
        number = input("Enter a number: ")
        time = input("Enter a measure of time: ")
        verb = input("Enter a verb(ending in ing): ")
        adjective5 = input("Enter an adjective: ")
        noun5 = input("Enter a noun: ")
        
        story = f"Dear {person_name}, I am writing to you from a {adjective1} castle in an enchanted forest." \
        f"I found myself here one day after going for a ride on a {color} {animal} in {place}." \
        f"There are {adjective2} {magic_creature} and {adjective3} {magic_creature2} here!" \
        f"In the {room} there is a pool full of {noun}." \
        f"I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}." \
        f"It feels as though I have lived here for {number} {time}. " \
        f"I hope one day you can visit, although the only way to get here now is {verb} on a {adjective5} {noun5}!!" \
        
        return story
    
    
 
template = (input("Choose a template number (1, 2, or 3) or I can choose randomly if you write 'random': "))
story = your_story(template)
print("Here is your generated story:")
print(story)