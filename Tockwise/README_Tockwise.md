# Tockwise

Tockwise is a commercial-grade time tracking system developed in Python. It uses a Microsoft SQL Server backend and includes secure login, activity monitoring, idle detection, and separate dashboards for Admin and Employee roles.

## Features

- Secure login with bcrypt password hashing
- Time tracking with check-in/check-out logging
- Idle time tracking with automatic detection
- Microsoft SQL Server integration via pyodbc
- Admin and Employee dashboards built with PyQt5
- Background tracking with system input monitoring
- Optional auto-launch at Windows startup

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Tockwise.git
   cd Tockwise
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure database connection:**

   Update `db.py` with your MSSQL server details (server name, username, password).

4. **Set up the database:**

   Use the SQL commands in `OfficeTimeTrackerDB.sql` to create the necessary tables and an admin account.

5. **Run the application:**

   ```bash
   python main.py
   ```

6. **Build to .exe (optional):**

   ```bash
   pyinstaller --onefile --windowed main.py
   ```

7. **Add to Windows startup (optional):**

   Run the included `installer.bat` file to copy the built `.exe` to the Windows startup folder.

## Login

- **Email:** admin@office.com
- **Password:** admin123

## License

This project is licensed under the MIT License.
