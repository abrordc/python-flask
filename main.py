from groq import Groq
from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

AI_KEY = "screat ai anda"

client = Groq(api_key=AI_KEY)

def ai_call(year):
    try:
       chat_completion = client.chat.completions.create(
           messages=[
               {
                   "role": "user",
                   "content": f"berikan 1 fakta menarik seputar teknologi pada tahun {year}",
                   
               }
           ],
           model="llama-3.2-1b-preview",
           stream=False
       ) 
       
       ai_output = chat_completion.choices[0].message.content
       return ai_output
    except Exception:
        return "maaf ai sedang tidur ngantuk soalnya 😁"
        
    
    
@app.route("/", methods=['GET','POST'])
def main():
    hasil = None
    ai_output = None
    if request.method == "POST" :
        tahun_lahir = request.form['tahun']
        tahun_sekarang = datetime.now().year
        umur = tahun_sekarang - int(tahun_lahir)
        ai_output = ai_call(tahun_lahir)
        hasil = umur
    return render_template('index.html', data = "Hitung Umur Dengan Tahun",usia=hasil,ai_output=ai_output)


@app.route("/card")
def card():
    url = 'abrordc'
    return f"card belum jadi <a href={ url }>card</a>"

@app.route("/abrordc")
def abrordc():
    return redirect("https://card-abrordc.vercel.app")


if __name__ == "__main__" :
    app.run(debug=True)