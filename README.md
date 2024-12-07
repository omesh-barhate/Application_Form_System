# Application Form System 

## Overview

The **Application Form System** is a web application for submitting and managing forms with dynamic, real-time data visualization. It uses **Django** for the backend, **MySQL** for the database, and **AJAX**, **JavaScript**, and **ApexCharts** for the frontend.

## Technologies

- **Backend**: Django (Python), MySQL.
- **Frontend**: HTML, CSS (custom), JavaScript (AJAX, jQuery), ApexCharts.
- **Database**: MySQL.

## Features

- **Form Submission**: Users can submit applications via a dynamic form.
- **Real-Time Data Visualization**: Visualize submitted data with interactive charts using **ApexCharts**.
- **AJAX Integration**: Seamless submission and data updates without page reloads.
- **Admin Panel**: Manage submitted data using Django's built-in admin interface.

## Usage

1. **Submit Form**: Users fill out the form at the main page (`/`) and submit it without reloading the page.
2. **View Results**: Submitted data is shown in real-time charts powered by **ApexCharts**.
3. **Admin Panel**: Django's admin panel (`/admin/`) allows managing and viewing submissions.

## Customization

- **Charts**: Update `static/js/charts.js` to modify chart types or data sources.
- **AJAX**: Adjust `static/js/form.js` for custom AJAX request handling.
