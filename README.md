# CS 340 Portfolio – Client/Server Development

**Juan Gil | Southern New Hampshire University | CS 340**

---

## About This Repository

This repository contains the artifacts from CS 340 (Client/Server Development), including the MongoDB CRUD Python module and the Grazioso Salvare animal shelter dashboard built with Dash and MongoDB.

---

## Projects

- **Project One** – `animal_shelter.py`: A Python CRUD module using PyMongo to interface with a MongoDB animal shelter database.
- **Project Two** – `ModuleSixMilestone.ipynb`: An interactive Dash web dashboard that connects to the CRUD module to display and filter shelter animal data with an interactive data table and geolocation map.

---

## Reflection

### How do you write programs that are maintainable, readable, and adaptable?

Writing maintainable code comes down to separation of concerns — keeping each component focused on a single responsibility so it can be updated or reused without breaking everything else. In this course, that principle showed up clearly in the CRUD Python module from Project One. By encapsulating all database logic inside the `AnimalShelter` class, the module acted as a clean interface between the application layer and MongoDB. The dashboard in Project Two never needed to know how a query was constructed or how the connection was managed — it just called `read()`, and the module handled the rest. The advantage of working this way is that when something changes — a different database host, a new authentication method, or a schema update — only one file needs to change, not every widget in the dashboard. In the future, the same `AnimalShelter` module could be reused in a command-line reporting tool, a REST API, or a scheduled data pipeline with no modifications to its core logic.

---

### How do you approach a problem as a computer scientist?

My approach starts with understanding what the client actually needs before writing any code. For Grazioso Salvare, that meant reading the requirements carefully to identify what data needed to be stored, how it would be filtered, and what the dashboard needed to present. From there I worked bottom-up: get the data layer right first (the CRUD module and MongoDB collection), then build the interface on top of it. This differed from assignments in other courses that tended to be self-contained — here the work spanned multiple modules and had a real client use case, which meant decisions made early (like the structure of the CRUD class) had downstream consequences on the dashboard. Going forward, I would apply the same layered approach to other client requests: define the data model early, isolate database logic into a reusable module, and build the interface against that module rather than directly against the database.

---

### What do computer scientists do, and why does it matter?

Computer scientists translate real-world problems into systems that can process, organize, and surface information at a scale humans cannot manage manually. For an organization like Grazioso Salvare, the work in this course directly reduces the time staff spend searching through shelter data to identify animals suitable for rescue training. Instead of manually scanning spreadsheets, a shelter worker can filter by rescue type with one click and see a map of matching animals immediately. That kind of tool frees up time for the work that actually requires human judgment. More broadly, the ability to connect a database to an interactive interface — and to do it in a maintainable, modular way — is what allows small organizations to get the same data capabilities that used to require large IT departments.

---

## Tools and Technologies

- **Python** – Core programming language
- **PyMongo** – MongoDB driver for Python
- **MongoDB** – NoSQL database (database: `aac`, collection: `animals`)
- **Dash / Plotly** – Interactive web dashboard framework
- **Dash Leaflet** – Geolocation map component
- **JupyterLab** – Development environment (Codio cloud)

## Contact

Juan Gil  
Southern New Hampshire University
