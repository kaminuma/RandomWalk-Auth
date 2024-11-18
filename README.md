# RandomWalk-Auth
A unique authentication system using random walks to enhance security. This project explores a novel approach to authentication without relying on traditional passwords or two-factor authentication.


# RandomWalk-Auth

## Overview
`RandomWalk-Auth` is an innovative authentication system that leverages the concept of random walks to provide a secure and efficient alternative to traditional authentication methods like passwords and two-factor authentication (2FA). By utilizing a user-provided seed, this system generates a random sequence of steps, which is then used to verify the user's identity through a challenge-response mechanism.

## Key Features
- **No reliance on traditional passwords**: Eliminates the risk of password leaks and brute-force attacks.
- **Unique challenge-response authentication**: Randomly selected steps from a generated random walk sequence are used for user verification.
- **User-controlled security**: The seed is managed entirely by the user, ensuring that sensitive information is not stored on the server.
- **Lightweight and simple implementation**: Built with Python (Flask) and JavaScript for easy deployment and integration.

## How It Works
1. **Registration**: The user generates a seed and a corresponding random walk sequence. The sequence's hash is stored on the server, while the seed remains solely with the user.
2. **Login**: The user inputs their seed, which is used to regenerate the random walk sequence. The server sends a set of random challenges based on the sequence, and the user responds with the appropriate steps.
3. **Verification**: The server verifies the user's responses against the stored hash to confirm their identity.

## Getting Started
This project is a proof of concept and is currently in the experimental phase. Contributions and feedback are welcome to help refine the system and explore its potential applications.

## Technologies Used
- **Backend**: Python (Flask)
- **Frontend**: HTML, JavaScript, CSS
- **Database**: In-memory storage (for demonstration purposes)

## Future Directions
While this system does not fully align with zero-knowledge proof protocols, it represents a novel approach to authentication. Future iterations may explore deeper integration with cryptographic techniques to enhance security and scalability.

---

If you're interested in contributing or have suggestions for improvement, feel free to open an issue or submit a pull request!
