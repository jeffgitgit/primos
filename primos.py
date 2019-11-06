#jefferson rubens da silva oliveira, ra: 1900363
#julio cesar santos azevedo, ra: 1900518

from flask import Flask
app = Flask(__name__)


def achar_primos():
    n = 100
    divisores = 0
    primos =[]
    
    for i in range(n, 0, -1):
        for divisor in range(1, n + 1):
            if n % divisor == 0:
                divisores += 1
        if divisores == 2 and (divisor == 1 or divisor == n):
            primos.append(n)
        n -= 1
        divisores = 0
    primos.reverse()
    return str(primos)

busca = achar_primos()


@app.route("/")
def index():
    return busca

if __name__ == "__main__":
    app.run()


