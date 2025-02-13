import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Steganography")
        self.root.geometry("800x600")
        
        # Initialize variables
        self.original_image_path = ""
        self.encrypted_image_path = ""
        
        # Create main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create encryption tab
        self.encryption_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.encryption_tab, text="Encryption")
        self.create_encryption_ui()
        
        # Create decryption tab
        self.decryption_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.decryption_tab, text="Decryption")
        self.create_decryption_ui()
        
        # Image preview
        self.image_preview = ttk.Label(self.main_frame)
        self.image_preview.pack(pady=10)

    def create_encryption_ui(self):
        # Encryption UI elements
        ttk.Label(self.encryption_tab, text="Original Image:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.enc_image_entry = ttk.Entry(self.encryption_tab, width=50)
        self.enc_image_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.encryption_tab, text="Browse", command=self.browse_original_image).grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(self.encryption_tab, text="Secret Message:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.message_entry = ttk.Entry(self.encryption_tab, width=50)
        self.message_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.encryption_tab, text="Password:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.password_entry = ttk.Entry(self.encryption_tab, show="*", width=50)
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(self.encryption_tab, text="Encrypt", command=self.encrypt).grid(row=3, column=1, padx=5, pady=10)

    def create_decryption_ui(self):
        # Decryption UI elements
        ttk.Label(self.decryption_tab, text="Encrypted Image:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.dec_image_entry = ttk.Entry(self.decryption_tab, width=50)
        self.dec_image_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.decryption_tab, text="Browse", command=self.browse_encrypted_image).grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(self.decryption_tab, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.dec_password_entry = ttk.Entry(self.decryption_tab, show="*", width=50)
        self.dec_password_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(self.decryption_tab, text="Decrypt", command=self.decrypt).grid(row=2, column=1, padx=5, pady=10)
        
        self.decrypted_message = ttk.Label(self.decryption_tab, text="")
        self.decrypted_message.grid(row=3, column=1, padx=5, pady=5)

    def browse_original_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.original_image_path = file_path
            self.enc_image_entry.delete(0, tk.END)
            self.enc_image_entry.insert(0, file_path)
            self.show_image_preview(file_path)

    def browse_encrypted_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.encrypted_image_path = file_path
            self.dec_image_entry.delete(0, tk.END)
            self.dec_image_entry.insert(0, file_path)
            self.show_image_preview(file_path)

    def show_image_preview(self, image_path):
        try:
            image = Image.open(image_path)
            image.thumbnail((200, 200))
            photo = ImageTk.PhotoImage(image)
            self.image_preview.config(image=photo)
            self.image_preview.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Error loading image: {str(e)}")

    def encrypt(self):
        msg = self.message_entry.get()
        password = self.password_entry.get()
        
        if not self.original_image_path:
            messagebox.showerror("Error", "Please select an image file")
            return
            
        if not msg:
            messagebox.showerror("Error", "Please enter a secret message")
            return
            
        try:
            img = cv2.imread(self.original_image_path)
            d = {chr(i): i for i in range(256)}  # Include all ASCII values from 0 to 255
            
            # Store the length of the message in the first pixel
            msg_length = len(msg)
            img[0, 0, 0] = msg_length  # Store the length in the red channel
            
            m, n, z = 0, 1, 0  # Start encoding from the second pixel
            for i in range(len(msg)):
                img[n, m, z] = d[msg[i]]
                n += 1
                m += 1
                z = (z + 1) % 3
                
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")]
            )
            if save_path:
                cv2.imwrite(save_path, img)
                messagebox.showinfo("Success", f"Image encrypted and saved to:\n{save_path}")
                self.show_image_preview(save_path)
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        password = self.dec_password_entry.get()
        image_path = self.dec_image_entry.get()
        
        if not image_path:
            messagebox.showerror("Error", "Please select an encrypted image")
            return
            
        try:
            img = cv2.imread(image_path)
            c = {i: chr(i) for i in range(256)}  # Include all values from 0 to 255
            
            # Read the length of the message from the first pixel
            msg_length = img[0, 0, 0]
            
            message = ""
            m, n, z = 0, 1, 0  # Start decoding from the second pixel
            for _ in range(msg_length):
                message += c[img[n, m, z]]
                n += 1
                m += 1
                z = (z + 1) % 3
                    
            self.decrypted_message.config(text=f"Decrypted message: {message}")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
