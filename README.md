# Image Steganography

## Overview
This project is an **Image Steganography** application that allows users to hide secret messages within images. The application provides a graphical user interface (GUI) for easy interaction, enabling users to encrypt and decrypt messages seamlessly.

## Features
- **Encrypt Messages**: Hide a secret message inside an image without altering its appearance.
- **Decrypt Messages**: Retrieve the hidden message from the image.
- **User-Friendly GUI**: Simple and intuitive interface for both encryption and decryption processes.
- **Message Length Handling**: Automatically stores the length of the message in the image to ensure accurate decryption.

## Technologies Used
- **Python**: The programming language used to develop the application.
- **OpenCV**: A library for image processing.
- **Tkinter**: A library for creating the GUI.
- **Pillow**: A library for image handling and displaying previews.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone git@github.com:patil-digvijay/aicte-project.git
   cd aicte-project
   ```

2. **Install Required Libraries**:
   Make sure you have Python installed, then run:
   ```bash
   pip install opencv-python pillow
   ```

3. **Run the Application**:
   Execute the following command in your terminal:
   ```bash
   python GUIstego.py
   ```

## How to Use
### Encrypting a Message
1. Open the application.
2. Navigate to the **Encryption** tab.
3. Click on **Browse** to select an image file.
4. Enter your secret message in the provided text box.
5. Click on **Encrypt** to hide the message in the image.
6. Save the new image file when prompted.

### Decrypting a Message
1. Open the application.
2. Navigate to the **Decryption** tab.
3. Click on **Browse** to select the image with the hidden message.
4. Click on **Decrypt** to retrieve and display the hidden message.

## Example
- **Encrypt**: If you enter "Hello, World!" as your secret message, the program will hide this message in the selected image.
- **Decrypt**: When you load the modified image, the program will display "Hello, World!" as the retrieved message.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- Thanks to the contributors and libraries that made this project possible.

---
