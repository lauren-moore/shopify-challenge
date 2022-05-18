# Shopify Backend Developer Challenge

- [Instructions](#instructions)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Features](#features)
- [Demo](#demo)
- [About the Developer](#about-the-developer)

## Instructions

Build an inventory tracking web application with CRUD operations.

- Create inventory items
- Edit Them
- Delete Them
- View a list of them

**Additional Feature:**

- Ability to create warehouses/locations and assign inventory to specific locations

## Tech Stack

- **Backend:** Python3, Flask, SQLAlchemy
- **Frontend:** HTML5, CSS3, Bootstrap
- **Database:** PostgreSQL

## Installation

### Requirements:

- [PostgreSQL](https://www.postgresql.org/)
- [Python 3.7+](https://www.python.org/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

To run Shopify Coding Challenge on your local machine, follow the instructions below:

Clone repository:

```
$ git clone https://github.com/lauren-moore/shopify-challenge.git
```

Create and activate a virtual environment inside your project directory:

```
$ pip3 install virtualenv
$ virtualenv env 
$ source env/bin/activate
```

Install the dependencies:

```
(env) pip3 install -r requirements.txt
```

Seed the database:

```
(env) python3 seed.py
```


Run the app:

```
(env) python3 server.py
```

You can now navigate to `localhost:5000/` to run the app.

## Features

- **Create a cat to add to inventory:**  methods=["POST"]

Users can create a cat to add to their inventory by providing the following information for the cat: name, gender, birthdate, color, neuter/spay status, adoption location. A relationship is established between the cat created and the adoption location. 


- **Create an Adoption Center (Inventory Warehouse):**  methods=["POST"]

When creating a cat, a drop down menu is provided for current adoption centers(warehouses) in the database to store the cat. Additionally, an option to create a new adoption center is provided. Users provide the name of the city that the center will be located in. This creates a new adoption center option in the database.


- **View all cats in inventory:**  methods=["GET"]

View all the cats currently in the inventory, including which adoption center they are stored at. 


- **Update cat in inventory:**  methods=["POST"]
  
Users can edit an existing cat in the database. They can edit any information about the cat, including name, gender, birthdate, color, spay/neuter status, and adoption center location. Doing so will update the existing cat in the database.


- **Delete cat from inventory:**  methods=["DELETE"]
  
Users can delete exisitng cats from the database. 


## Demo
- View on [Replit](https://replit.com/@laurencaroleen/shopify-challenge#server.py)
- Run the [demo](https://shopify-challenge.laurencaroleen.repl.co/)

## About the Developer

As a Hotel Administration graduate, Laurén's background is in all things hospitality. From being a floor manager and bartender at a fine-dining restaurant to being a flight attendant, she has a passion for making others smile. She also has experience as an E-Com Producer and Project Manager where she works on board and card games. This appreciation for games, puzzles, problem solving, and logic lead her to tech. After taking courses in Computer Science and Python, Laurén knew it was time to transition into a life of software engineering and joined Hackbright Academy. Since graduating in April, she has continued to expand her technical skills and practiced coding. She aspires to continue making a positive impact for others using her background in hospitality, passion for problem solving, and knowledge in Software Engineering. 

Let's connect on [LinkedIn!](https://www.linkedin.com/in/laurencaroleen/)

![image](/static/img/Business_card.jpg)