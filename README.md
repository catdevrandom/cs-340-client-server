# CS 340 - Client/Server Development

**Southern New Hampshire University**  
**Author:** Juan Gil

---

## About This Repository

This repository contains coursework from CS 340: Client/Server Development. The project demonstrates the development of a full-stack client/server application using Python, MongoDB, and Dash.

---

## Project Overview

### Grazioso Salvare Animal Shelter Dashboard

A web-based interactive dashboard built for Grazioso Salvare, an international rescue animal training company. The application allows users to query and visualize animal shelter data to identify dogs that are good candidates for search-and-rescue training.

---

## Technologies Used

- **Python** - Core programming language
- **MongoDB** - NoSQL database for storing and querying animal shelter data
- **PyMongo** - Python driver for MongoDB
- **Dash** - Python framework for building the interactive web dashboard
- **Plotly** - Data visualization library used within Dash
- **Pandas** - Data manipulation and analysis
- **Jupyter Notebook** - Development environment

---

## Files

| File | Description |
|------|-------------|
| `animal_shelter.py` | Python CRUD module for interfacing with MongoDB |
| `ProjectTwoDashboard.ipynb` | Jupyter Notebook containing the Dash web application |

---

## CRUD Module

The `animal_shelter.py` module provides Create, Read, Update, and Delete (CRUD) operations for the MongoDB animal shelter database. It is used as the data layer for the dashboard application.

**Key Methods:**
- `create(data)` - Inserts a new document into the collection
- `read(query)` - Retrieves documents matching the given query
- `update(query, update_data)` - Updates documents matching the given query
- `delete(query)` - Deletes documents matching the given query

---

## Dashboard Features

- Filter animals by rescue type: Water Rescue, Mountain/Wilderness Rescue, Disaster/Individual Tracking
- Interactive data table displaying shelter animal records
- Geolocation chart showing the location of the selected animal
- Pie chart visualizing breed distribution based on the active filter

---

## How to Run

1. Ensure MongoDB is running and the AAC database is loaded with shelter data
2. Confirm that `animal_shelter.py` is in the same directory as the notebook
3. Open `ProjectTwoDashboard.ipynb` in JupyterLab
4. Run all cells to launch the Dash application
5. Open the provided local URL in a browser to interact with the dashboard

---

## Contact

Juan Gil  
Southern New Hampshire University
