# Inventory Management System

Welcome to the **Inventory Management System (IMS)** repository! This Python-based application uses SQLite as its database to manage all aspects of an inventory system. 

## Features
- **User Authentication:** Includes a login/logout system to manage access.
- **Employee Records:** Stores and manages employee details.
- **Category Management:** Add, view, and update various product categories.
- **Supplier Integration:** Easily manage supplier databases.
- **Product Management:** Maintain product records, prices, stocks, etc.
- **Sales Dashboard:** Displays current total sales, products, categories, and employee statistics.
- **Billing:** A comprehensive system for generating and managing customer bills.
- **Reports:** Overview of inventory activities and transactions.

## Technology Stack
- Language: Python 3.9+
- Database: SQLite
- GUI Framework: Tkinter

## Dependencies
Ensure the required Python packages are installed. Use the `requirements.txt` file for direct installation:
```bash
pip install -r requirements.txt
```

## Database Initialization
The application uses an SQLite database file `ims.db`. To create the database with its required tables, run the command:
```bash
python create_db.py
```

## Usage
- To launch the IMS system:
```bash
python dashboard.py
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/samyogbhatta/Inventory-Management-System.git
   ```
2. Navigate into the directory:
   ```bash
   cd Inventory-Management-System
   ```
3. Run the `create_db.py` to initialize tables:
   ```bash
   python create_db.py
   ```
4. Start the program:
   ```bash
   python dashboard.py
   ```

## Contributing
We welcome contributions! Feel free to open issues or submit a pull request.

## Acknowledgements
Thanks to all contributors who have supported this project.

For any queries or technical issues, contact the repository owner.

---