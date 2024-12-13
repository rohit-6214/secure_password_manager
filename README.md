## 🔐 Secure Password Manager 🔐

This Python script provides a secure and convenient way to manage your passwords. 

**Key Features:**

* **🔐 Encryption:** Employs the robust `cryptography.fernet` library to encrypt your passwords, ensuring their confidentiality.
* **🚀 Password Generation:** Generates strong passwords with customizable length and strength (weak, medium, strong) to enhance security.
* **😊 User-Friendly Interface:** Offers an intuitive menu for easy navigation and password management.
* **🔄 Flexibility:** Allows you to store your own passwords or generate them on-the-fly for added convenience.

### Requirements

* Python 3.x

### Installation

1. **Clone or download** the repository containing this script.
2. **Install dependencies:** Run `pip install cryptography` in your terminal.

### Usage

1. **Run the script:** Execute `python password_manager.py` (replace `password_manager.py` with the actual filename).
2. **Select an option:** Choose from the menu:
    * **1. Generate Password** 
    * **2. Store Password** 
    * **3. Retrieve Password** 
    * **4. Update Password** 
    * **5. Exit** 

3. **Provide details:** When prompted, enter information such as service name, username, password strength (if generating), and new password (for updates).

### Example Usage

**1. Generate a Strong Password:**

   - Choose option 1 (Generate Password).
   - Specify the desired password length (e.g., 16 characters).
   - Select "strong" password strength.
   - The script will display the generated password.

**2. Store a Password:**

   - Choose option 2 (Store Password).
   - Enter the service name (e.g., "Email").
   - Provide your username for that service.
   - Enter your password or press Enter to have one generated for you.
   - Choose a password strength (if generating a password).
   - The script will securely store the encrypted password in a JSON file.

**3. Retrieve a Password:**

   - Choose option 3 (Retrieve Password).
   - Enter the service name.
   - Provide your username for that service.
   - The script will display your decrypted password if found.

**4. Update a Password:**

   - Choose option 4 (Update Password).
   - Enter the service name to update.
   - Provide your username for that service.
   - Enter your new password or press Enter to generate one.
   - Choose a password strength (if generating a password).
   - The script will update the encrypted password in the JSON file.

### Security Considerations ⚠️

While this tool enhances password security, remember these crucial tips:

* **Choose strong, unique passwords** for each service.
* **Protect** the encryption key file (`secret.key`) and the password file (`passwords.json`) carefully. 
* Consider using a dedicated password manager to store this script's password itself.

### Additional Notes

* Feel free to customize this script to suit your specific needs.
* This script is provided for educational and informational purposes.

### Disclaimer

This code is provided as-is without any warranty. The author is not responsible for any misuse or security vulnerabilities arising from its use.
