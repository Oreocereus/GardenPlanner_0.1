from tkinter import *
from trees import trees
from functools import partial

# Set up window
window = Tk()
window.title("Garden Planner - Trees")
BACKGROUND_COLOUR = "#34733D"
BACKGROUND_COLOUR_2 = "#378943"
BACKGROUND_COLOUR_3 = "#AA3F3A"
BACKGROUND_COLOUR_4 = "#AF743A"
FILL_COLOUR = "#FFFFFF"

# Set up canvas
canvas = Canvas(width=600, height=800, bg=BACKGROUND_COLOUR)
canvas.pack()

canvas1 = Canvas(width=600, height=800, bg="#B49E3A")
canvas1.pack_forget()

canvas2 = Canvas(width=400, height=500, bg="#AF743A")
canvas2.pack_forget()

# Define tree aspects
tree_size = []
tree_season = []
tree_merit = []
tree_photos = []
tree_photo = canvas2.create_image(300, 300, image="")


# Create end screen
def end_screen(y):
    canvas.pack_forget()
    canvas1.pack()
    canvas2.place(x=120, y=100)
    plant_name = canvas1.create_text(320, 50, text=y, fill=FILL_COLOUR, font=("Ariel", 20, "italic"))
    plant_description = canvas1.create_text(320, 700, text=trees[y]["description"], fill=FILL_COLOUR, font=("Ariel", 12))
    canvas2.itemconfig(tree_photo, image=tree_photos[trees[y]["photo"]])


# Filter trees by size
def filter_trees_by_size(size):
    for n in trees:
        if trees[n]["size"] == size:
            tree_size.append(n)
    season_choice()


# Filter trees by season
def filter_trees_by_season(season):
    for n in tree_size:
        if trees[n][season]:
            tree_season.append(n)
    decorative_merit_choice()


# Filter trees by merit
def filter_trees_by_merit(merit):
    global new_tree_button
    clear_screen()
    z = -50
    for n in tree_season:
        if trees[n][merit]:
            tree_merit.append(n)

# Show end screen
    for n in tree_merit:
        z += 100
        new_tree_button = Button(canvas, text=n, height=4, width=30, command=partial(end_screen, n))
        new_tree_button.place(x=200, y=z)
    canvas.configure(bg=BACKGROUND_COLOUR_4)


# Clears screen
def clear_screen():
    canvas.delete("all")
    pretty_flowers_button.place_forget()
    edible_fruit_button.place_forget()
    interesting_bark_button.place_forget()
    evergreen_button.place_forget()
    deciduous_button.place_forget()


# Creates screen for decorative merit choice page
def decorative_merit_choice():
    global pretty_flowers_button, edible_fruit_button, interesting_bark_button, evergreen_button, deciduous_button
    canvas.delete("all")
    autumn_button.place_forget()
    winter_button.place_forget()
    spring_button.place_forget()
    summer_button.place_forget()
    pretty_flowers_button = Button(text="Pretty Flowers", height=4, width=30, command=lambda: filter_trees_by_merit("pretty_flowers"))
    pretty_flowers_button.place(x=200, y=300)
    edible_fruit_button = Button(text="Edible Fruit", height=4, width=30, command=lambda: filter_trees_by_merit("edible_fruit"))
    edible_fruit_button.place(x=200, y=385)
    interesting_bark_button = Button(text="Interesting Bark", height=4, width=30, command=lambda: filter_trees_by_merit("interesting_bark"))
    interesting_bark_button.place(x=200, y=470)
    evergreen_button = Button(text="Evergreen", height=4, width=30, command=lambda: filter_trees_by_merit("evergreen"))
    evergreen_button.place(x=200, y=555)
    deciduous_button = Button(text="Deciduous", height=4, width=30, command=lambda: filter_trees_by_merit("deciduous"))
    deciduous_button.place(x=200, y=640)
    canvas.create_text(320, 150, text="What would\nyou like?", fill=FILL_COLOUR, font=("Ariel", 50))
    canvas.configure(bg=BACKGROUND_COLOUR_3)


# Creates screen for season choice page
def season_choice():
    global autumn_button, winter_button, spring_button, summer_button
    canvas.delete("all")
    large_button.place_forget()
    medium_button.place_forget()
    small_button.place_forget()
    autumn_button = Button(text="Autumn", height=5, width=30, command=lambda: filter_trees_by_season("autumn"))
    autumn_button.place(x=200, y=300)
    winter_button = Button(text="Winter", height=5, width=30, command=lambda: filter_trees_by_season("winter"))
    winter_button.place(x=200, y=413.33)
    spring_button = Button(text="Spring", height=5, width=30, command=lambda: filter_trees_by_season("spring"))
    spring_button.place(x=200, y=526.66)
    summer_button = Button(text="Summer", height=5, width=30, command=lambda: filter_trees_by_season("summer"))
    summer_button.place(x=200, y=640)
    canvas.create_text(320, 150, text="Which season\ninterests you\nthe most?", fill=FILL_COLOUR, font=("Ariel", 50))
    canvas.configure(bg=BACKGROUND_COLOUR_2)


# Home screen
def home_screen():
    global large_button, medium_button, small_button
    canvas.pack()
    question = canvas.create_text(320, 150, text="What size tree\nwould you like?", fill=FILL_COLOUR, font=("Ariel", 50))

    # Buttons
    large_button = Button(text="Large", height=8, width=30, command=lambda: filter_trees_by_size("large"))
    large_button.place(x=200, y=300)
    medium_button = Button(text="Medium", height=8, width=30, command=lambda: filter_trees_by_size("medium"))
    medium_button.place(x=200, y=450)
    small_button = Button(text="Small", height=8, width=30, command=lambda: filter_trees_by_size("small"))
    small_button.place(x=200, y=600)


# Add tree photos
tree_photos.extend([
    PhotoImage(file="trees/prunus_avium_sunburst.png"),
    PhotoImage(file="trees/laburnum_alpinum.png"),
    PhotoImage(file="trees/platanus_x_hispanica.png"),
    PhotoImage(file="trees/acer_griseum.png"),
    PhotoImage(file="trees/parrotia_persica.png"),
    PhotoImage(file="trees/Tilia tomentosa.png"),
    PhotoImage(file="trees/citrus_x_limon_gareys_eureka.png"),
    PhotoImage(file="trees/taxus-baccata.png"),
    PhotoImage(file="trees/1200px-TrachycarpusFortunei.png"),
    PhotoImage(file="trees/Aesculus-indica-19480162-A-2000x1125.png"),
    PhotoImage(file="trees/Araucaria_en_Parque_Nacional_Conguillio.png"),
    PhotoImage(file="trees/eucalyptus-pauciflora-niphophila-tree-p820-7679_image.png"),
    PhotoImage(file="trees/Grizzly_Giant_Mariposa_Grove.png")])

# Call home screen function
home_screen()

window.mainloop()
