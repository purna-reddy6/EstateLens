# EstateLens - Real Estate App

**Live demo:** https://purna-reddy6.github.io/EstateLens/

This project is a single-page web application (SPA) prototype for a modern real estate platform. It serves as an MVP (Minimum Viable Product) focused on browsing properties in Bangalore, combining an interactive map interface with a detailed "Trust Report" for each listing.

## Key Features

* **Interactive Map View:** Built with [Leaflet.js](https://leafletjs.com/), the map displays properties with custom pins (color-coded for rent/sale) and draws the exact property boundaries (polygons).
* **Synced List and Map:** Hovering over a listing in the side panel highlights its pin and boundary on the map, and vice-versa, for an intuitive browsing experience.
* **Dynamic Filtering:** Users can instantly filter the properties shown on both the list and the map to view "All," "For Sale," or "For Rent" listings.
* **Slide-In Details Panel:** Clicking a property opens a rich details panel that includes:
    * Property photos and key attributes (price, area, furnishing).
    * A **"EstateLens Trust Report"** detailing verified info like legal status, water source, and power backup.
    * A **"Liveability Index"** (rating Walkability, Safety, Noise, and Connectivity) visualized with a dynamic radar chart using [Chart.js](https://www.chartjs.org/).

## Technologies Used

* **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript
* **Mapping:** Leaflet.js
* **Data Visualization:** Chart.js
* **Local Server:** A simple Python `http.server` is included to run the project locally.

## How to Run

1.  Clone this repository to your local machine.
2.  Navigate to the project's root directory in your terminal.
3.  Run the local Python server:
    ```bash
    python server.py
    ```
4.  Open your web browser and go to `http://localhost:8000`.
