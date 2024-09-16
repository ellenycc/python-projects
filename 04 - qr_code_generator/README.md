# QR Code Generator

### Goal

Write a program to generate a QR code based on user input, such as text or a URL. The QR code should be saved as an image file that can be scanned with a smartphone.

### Solution

1. As we are going to use the library, first, we create a virtual environment to allow each project to have seperate librairies. Type the following command in the terminal:
   ```sh
   python3 -m venv venv
   ```

Create a file called .gitignore in the root of our projcet and add `venv/` to the file, because we don't want to commit all the files in the bin file to our repository.

Activate the environment in the terminal:

```sh
  source venv/bin/activate
```

Once the virtual environment is activated, any packages will be installed in this isolated workspace. When we are done, we can deactivate it by typing `deactivate`.

2. Install the qrcode package

   ```sh
   pip install qrcode[pil]
   ```

3. Import the qrcode module

4. Ask user to enter the text or URL and the filename. It's a good practice to remove any whitespaces from the user input using `strip()`.

   ```python
   data = input("Enter the text or URL you want to encode in QR code: ")
   file_name = input("Enter the file name for the QR code image: ")
   ```

5. Following the isntructions on [this page](https://pypi.org/project/qrcode/) to create a QR code object and generate the QR code.
   ```python
   qr = qrcode.QRCode(box_size=10, border=5)
   qr.add_data(data)
   image = qr.make_image(fill_color="black", back_color="white")
   image.save(file_name)
   print(f"QR code image saved as {file_name}")
   ```
