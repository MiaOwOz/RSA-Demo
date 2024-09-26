from math import gcd

# Find the nearest coprime number to n between 2^16 and 2^64
def find_coprime(n: int) -> int:
    for i in range(2**16, 2**64):
        if(gcd(n, i) == 1):
            return i

class RSA():
    def __init__(self, p: int, q: int):
        # p and q are both prime numbers. They're essential to the RSA algorithm
        self.p = p
        self.q = q

        self.n = self.p * self.q
        # Phi(n) =  Phi(p-1) * Phi(q-1) = (p-1) * (q-1), necessary to calculate the multiplicative inverse of e
        self.phi_n = (self.p - 1) * (self.q - 1)

        # e must be coprime to Phi(n), so we'll use the method find_coprime() to find a suitable number
        # yes the implementation is shit. should use the extended euclidian algorithm, but nah
        # time complexity of find_coprime(n) is probably something like O(n^2) or sum shit
        self.e = find_coprime(self.phi_n)

        # d is the multiplicative inverse of e modulo Phi(n)
        # it's automatcially assigned to d after calling btw, i don't know why I did it like this.
        # makes no sense but ok
        self.mod_inverse(self.phi_n, self.e)
        
    # calulate the multiplicative inverse of e modulo phi(n)
    def mod_inverse(self, phi_n: int, e: int) -> int:
        for i in range(0, phi_n):
            if((e * i) % phi_n) == 1:
                self.d = i
                break

    # Create the RSA keys. Returns a tuple of the format (public_key, private_key)
    def construct_keys(self) -> tuple:
        public_key = (self.e, self.n)
        private_key = (self.d, self.n)

        return (public_key, private_key)

    # encrypt the given message with the public key. Returns a list of the encrypted numbers
    def encrypt(self, public_key: list, message: str) -> list:
        encrypted_contents: list = []
        for c in message:
            # We need to convert the current character to a number to apply math
            # otherwise the world is going to blow up (or at least the program will crash)
            number = ord(c)
            
            # RSA encryption: c = m^e mod N
            # m is the current clear text character, e the first number of the public key tuple, N the second one
            encrypted_number = (number**public_key[0]) % public_key[1]
            encrypted_contents.append(encrypted_number)
        
        return encrypted_contents

    # decrypt the given message with the private key. Returns a list of decrytped numbers
    def decrypt(self, private_key: list, message: list) -> list:
        decrypted_contents: list = []
        for c in message:
            # We don't need to do any char magic, as the argument message is already an integer list
            # RSA encryption: m = c^d mod N
            # c is the current cipher text character, d the first number of the private key tuple, N the second one
            decrypted_number = (c**private_key[0]) % private_key[1]
            decrypted_contents.append(decrypted_number)

        return decrypted_contents

def main():
    p = 13
    q = 11

    rsa = RSA(p, q)
    keys = rsa.construct_keys()

    original_message = "Long a$$ f!cking t/xt bec)ause i w§nt t0 te\"t how it en=rypts s%mb&ls"

    encrypted_message = rsa.encrypt(keys[0], original_message)
    decrypted_message = rsa.decrypt(keys[1], encrypted_message)

    print(f"Original message: {original_message} | Encrypted message: {encrypted_message}")

    decrypted_message_text: str = ""

    for i in decrypted_message:
        c = chr(i)
        decrypted_message_text += c

    print(f"Decrypted message text: {decrypted_message_text}")

if __name__ == "__main__":
    main()