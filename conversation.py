import requests

A = "http://localhost:8001/chat"
B = "http://localhost:8002/chat"
C = "http://localhost:8003/chat"


message = "Should artificial intelligence be developed openly or with strict controls?"

for round_number in range(3):

    print(f"\n========== ROUND {round_number + 1} ==========\n")

    # A
    response = requests.post(
        A,
        json={"message": message}
    )

    message = response.json()["response"]

    print("A:", message)

    # B
    response = requests.post(
        B,
        json={"message": message}
    )

    message = response.json()["response"]

    print("B:", message)

    # C
    response = requests.post(
        C,
        json={"message": message}
    )

    message = response.json()["response"]

    print("C:", message)