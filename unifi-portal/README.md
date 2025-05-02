# UniFi Captive Portal Add-on for Home Assistant

This repository contains a custom add-on for Home Assistant that provides a captive portal to connect to a UniFi WiFi network.

## Features
- Captive portal web page for WiFi connection.
- Integration with UniFi API for guest access management.

## Getting Started

### Prerequisites
- Home Assistant installed and running.
- Docker installed (required for Home Assistant add-ons).
- Access to a UniFi Controller with API credentials.

### Installation
1. Clone this repository into your Home Assistant `addons` folder.
2. Build and install the add-on using the Home Assistant Supervisor.

### Configuration
Update the `config.json` file with your UniFi Controller details and other settings.

### Usage
Start the add-on from the Home Assistant Supervisor and access the captive portal page.

## Development
This add-on is built using Docker. To develop or modify the add-on:
1. Edit the `Dockerfile` and other source files.
2. Rebuild the add-on using the Home Assistant Supervisor.

## License
This project is licensed under the MIT License.
