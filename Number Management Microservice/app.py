from flask import Flask, jsonify, request
from random import randint


app = Flask(__name__)


@app.route("/numbers/fibo")
def fibo_numbers():
    f0, f1, c = 1, 1, 2
    fibo_numbers = [f0, f1]
    while c < 8:
        f2 = f0 + f1
        fibo_numbers.append(f2)
        f0, f1 = f1, f2
        c += 1 
    return jsonify(numbers=fibo_numbers)
app.add_url_rule("/numbers/fibo", "fibo_numbers", fibo_numbers)

@app.route("/numbers/odd")
def odd_numbers():
    odds = []
    for num in range(24):
        if num % 2 != 0:
            odds.append(num)
    return jsonify(numbers=odds)
app.add_url_rule("/numbers/odd", "odd_numbers", odd_numbers)

@app.route("/numbers/rand")
def random_numbers():
    random_nums = []
    for _ in range(13):
        temp = randint(1, 76)
        random_nums.append(temp)
    return jsonify(numbers=random_nums)
app.add_url_rule("/numbers/rand", "random_numbers", random_numbers)

@app.route("/numbers/primes")
def prime_numbers():
    isPrime = False
    primes = [2]
    n = 14; count = 0
    for num in range(1, n):
        for j in range(2, num):
            if num % j == 0:
                isPrime = False
                break
            else:
                isPrime = True
        if isPrime:
            primes.append(num)
        else:
            pass
    return jsonify(numbers=primes)
app.add_url_rule("/numbers/primes", "prime_numbers", prime_numbers)

@app.route("/numbers", methods=["POST"])
def get_unique_numbers():
    fibo_nums = fibo_numbers().get_json()["numbers"]
    prime_nums = prime_numbers().get_json()["numbers"]
    odd_nums = odd_numbers().get_json()["numbers"]
    random_nums = random_numbers().get_json()["numbers"]
    unique_nums = []
    for x in fibo_nums:
        unique_nums.append(x)
    for x in prime_nums:
        unique_nums.append(x)
    for x in odd_nums:
        unique_nums.append(x)
    for x in random_nums:
        unique_nums.append(x)    
    unique_nums = sorted(list(set(unique_nums)))
    return jsonify(unique_numbers = unique_nums)

if __name__ == '__main__':
    app.run(port=8008, debug=True)
