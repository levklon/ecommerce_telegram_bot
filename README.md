# E-commerce Telegram Bot

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-red.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-4.4+-green.svg)
![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-v.5.3-blue.svg)
![Stripe](https://img.shields.io/badge/Stripe-API-blue.svg)

---

## Overview

The **E-commerce Telegram Bot** is a powerful solution designed to enable users to browse products, add items to their cart, and complete purchases directly within Telegram. Built with Python, Flask, and MongoDB, and integrated with the Stripe API, this bot provides a seamless and secure shopping experience. It is an ideal tool for modern businesses looking to expand their sales channels through Telegram, offering both convenience and efficiency.

## Features

- **Product Browsing**: Users can easily browse products categorized for better organization and navigation.
- **Cart Management**: Users can add products to their cart, view the cart, and make adjustments before purchasing.
- **Secure Checkout**: Payments are processed securely via the Stripe API.
- **Order History**: Users can view their past orders, providing them with a convenient way to track their purchases.
- **Admin Panel**: A simple admin interface for managing products, categories, and viewing order statistics.

## Technologies Used

- **Programming Language**: Python
- **Framework**: Flask
- **Database**: MongoDB
- **APIs**:
  - **Telegram Bot API**: For integrating with Telegram.
  - **Stripe API**: For handling payment processing.
- **Environment Management**: Python-dotenv for managing environment variables.

## Installation

### Prerequisites

- **Python 3.x**
- **MongoDB**
- **Telegram Bot Token**
- **Stripe API Keys**

### Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/levklon/ecommerce_telegram_bot.git
    cd ecommerce_telegram_bot
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux and MacOS
    venv\Scripts\activate  # For Windows
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MongoDB database:

   - Ensure MongoDB is installed and running on your machine or use a cloud-hosted MongoDB service.
   - Update the `config.py` file with your MongoDB connection string.

5. Configure environment variables:

   - Create a `.env` file in the root directory of the project.
   - Add your Telegram Bot Token and Stripe API Keys to the `.env` file as follows:

     ```env
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token
     STRIPE_API_KEY=your_stripe_api_key
     MONGO_URI=mongodb://username:password@localhost/dbname
     ```

6. Initialize the database and run migrations:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

7. Start the server:

    ```bash
    flask run
    ```

## Usage

Once the server is running, the bot will be live and ready to use on Telegram. Users can interact with the bot to browse products, manage their cart, and securely make purchases through Stripe. Additionally, admins can log in to the admin panel to manage product listings, categories, and view order statistics.

## Future Enhancements

- **Multi-language Support**: Implementing multi-language support to cater to a broader audience.
- **Additional Payment Gateways**: Integrating more payment gateways to provide users with more payment options.
- **User Notifications**: Implementing push notifications to inform users about new products, special offers, and order updates.
- **Integration with E-commerce Platforms**: Extending the bot's functionality by integrating with popular e-commerce platforms like Shopify or WooCommerce.

## Contribution

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, create a feature branch, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE] file for details.

