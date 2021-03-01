from werkzeug.security import generate_password_hash, check_password_hash


if __name__ == "__main__":
    password = "test"
    hashed_password = generate_password_hash(password, method="sha256")
    print(hashed_password)



