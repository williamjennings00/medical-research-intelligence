# Configuration System

## Overview

The configuration system provides a way to manage application settings. 

The app loads configuration values from environment variables. This keeps sensitive information secure and makes it easier to change settings between development, testing, and production environments.

---

## Purpose

The configuration system controls:

- Application settings
- Database connections
- Selenium browser behavior
- Scraper settings
- File storage locations
- Logging preferences

All components of the application access settings from one location.

---

## How It Works

Application startup flow:

1. The application starts.
2. The configuration loader reads environment variables.
3. Values are validated.
4. Settings are stored in a configuration object.
5. Other modules import the configuration when needed.



