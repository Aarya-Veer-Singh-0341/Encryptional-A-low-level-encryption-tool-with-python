# Encryptional-A-low-level-encryption-tool-with-python

This script provides a basic method for encrypting and decrypting integer data using a password. It works by converting both the data and the password into their binary representations and then performing a bitwise operation (similar to XOR, but with specific rules defined in the script) to encrypt the data. Decryption is done by applying the same bitwise operation with the correct password.

## How it Works

1.  **Data and Password Input:** The script prompts the user to enter the integer data they want to encrypt and an integer password.

2.  **Binary Conversion:** Both the data and the password are converted into lists of their binary digits (0s and 1s).

3.  **Equalizing Binary Lengths:** If the binary representations of the data and password have different lengths, the shorter one is padded with leading zeros to match the length of the longer one. This ensures that the bitwise operation can be performed element-wise.

4.  **Encryption:** The encryption process iterates through the binary digits of the data and the password. For each corresponding pair of bits, the following rules are applied to generate the encrypted bit:
    * If data bit is 1 and password bit is 1, the encrypted bit is 0.
    * If data bit is 0 and password bit is 0, the encrypted bit is 1.
    * If data bit is 1 and password bit is 0, the encrypted bit is 0.
    * If data bit is 0 and password bit is 1, the encrypted bit is 1.

5.  **Decryption (Password Verification):** To "decrypt" and verify the password, the script prompts the user to enter the password again. This entered password is also converted to its binary form and padded with leading zeros if necessary to match the length of the encrypted data.

6.  **Decryption Operation:** The same bitwise operation used for encryption is applied between the encrypted data's binary representation and the entered password's binary representation.

7.  **Verification:** The resulting binary data from the decryption operation is compared to the original binary data. If they are identical, the script outputs "Password is correct"; otherwise, it outputs "Password is incorrect".

8.  **Output:** Finally, the script prints the original binary data and the encrypted binary data.

## How to Run the Script

1.  Save the code as a Python file (e.g., `encryption.py`).
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the command: `python encryption.py`
5.  Follow the prompts to enter the data and passwords.

## Important Notes

* **Security:** This is a very basic encryption method and should **not** be used for securing sensitive data. It is primarily for educational purposes to demonstrate fundamental bitwise operations. A determined attacker could easily reverse this encryption.
* **Integer Input:** The script currently only works with integer inputs for both the data and the password.
* **Error Handling:** The script includes basic error handling to ensure that the input data for the `binary` and `decimal` functions are valid integers and binary lists, respectively.

## Further Improvements (Potential)

* Implement a more robust encryption algorithm (e.g., a simplified version of XOR encryption).
* Allow for non-integer data types.
* Provide a way to store and retrieve encrypted data.
* Add more sophisticated error handling and input validation.
* Implement a true decryption function that directly converts the "decrypted" binary back to its decimal representation.

This `README.md` provides a basic overview of the Python encryption script. Remember that this is a simplified example and not suitable for real-world security applications.