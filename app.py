from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/aritmatika', methods=["POST","GET"])
def aritmatika():
    hasil_suhu = None
    hasil_kalkulator = None
    if request.method == "POST":
        if request.form.get("form_name") == "suhu":
            try:
                operasi1 = request.form.get("operasi1")
                operasi2 = request.form.get("operasi2")
                angka = float(request.form.get("angka"))

                if operasi1 == "celcius" and operasi2 == "fahrenheit":
                    hasil = ((9/5) * angka) + 32
                elif operasi1 == "celcius" and operasi2 == "reamur":
                    hasil = ((4/5) * angka)
                elif operasi1 == "celcius" and operasi2 == "kelvin":
                    hasil = (angka + 273)
                elif operasi1 == "reamur" and operasi2 == "celcius":
                    hasil = ((5/4) * angka)
                elif operasi1 == "reamur" and operasi2 == "fahrenheit":
                    hasil = ((9/4) * angka + 32)
                elif operasi1 == "reamur" and operasi2 == "kelvin":
                    hasil = ((5/4) * angka + 237)
                elif operasi1 == "fahrenheit" and operasi2 == "celcius":
                    hasil = ((5/9) * (angka - 32))
                elif operasi1 == "fahrenheit" and operasi2 == "reamur":
                    hasil = ((4/9) * (angka - 32))
                elif operasi1 == "fahrenheit" and operasi2 == "kelvin":
                    hasil = ((5/9) * (angka - 32) + 273)
                elif operasi1 == "kelvin" and operasi2 == "celcius":
                    hasil = (angka - 32)
                elif operasi1 == "kelvin" and operasi2 == "reamur":
                    hasil = ((4/5) * (angka - 32))
                elif operasi1 == "kelvin" and operasi2 == "fahrenheit":
                    hasil = ((9/5) * (angka - 32) + 273)
                else:
                    hasil = "program selesai"
            except:
                hasil = "input tidak valid"
            
        elif request.form.get("form_name") == "kalkulator":
            try:
                angka1 = float(request.form.get("angka1"))
                angka2 = float(request.form.get("angka2"))
                operasi = request.form.get("operasi")

                if operasi == "+":
                    hasil = angka1 + angka2
                elif operasi == "-":
                    hasil = angka1 - angka2
                elif operasi == "*":
                    hasil = angka1 * angka2
                elif operasi == "**":
                    hasil = angka1 ** angka2
                elif operasi == "%":
                    hasil = angka1 % angka2
                elif operasi == "//":
                    hasil = angka1 // angka2
                elif operasi == "/":
                    if angka2 != 0:
                        hasil = angka1 / angka2
                    else:
                        hasil = "Error! Tidak bisa dibagi 0"
            except:
                hasil = "Input tidak valid"
    return render_template("aritmatika.html", 
                           hasil_suhu=hasil_suhu, hasil_kalkulator=hasil_kalkulator)
            
            

if __name__ == "__main__":
    app.run(debug=True)
