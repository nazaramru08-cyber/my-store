from flask import Flask, render_template, request
app = Flask(__name__)

# Data produk unggulan perusahaan (PlayStation 5, HP Gaming, Laptop Gaming)
PRODUK_UTAMA = [
    {
        "id": 1,
        "nama": "PlayStation 5 Pro Edition",
        "kategori": "Console Gaming",
        "harga": "Rp 11.499.000",
        "deskripsi": "Konsol game generasi berikutnya dengan performa grafis 4K tingkat lanjut dan teknologi ray tracing super cepat.",
        "badge": "Best Seller"
    },
    {
        "id": 2,
        "nama": "Nexus X Alpha Gaming Phone",
        "kategori": "Mobile Gaming",
        "harga": "Rp 13.999.000",
        "deskripsi": "Smartphone gaming berperforma ekstrem dilengkapi sistem pendingin cair ruang uap dan layar 165Hz AMOLED.",
        "badge": "New Release"
    },
    {
        "id": 3,
        "nama": "Titanium Pro 16 Gaming Laptop",
        "kategori": "Laptop Gaming",
        "harga": "Rp 28.500.000",
        "deskripsi": "Laptop gaming kelas profesional dengan GPU seri RTX terbaru dan prosesor berkecepatan tinggi untuk gaming tanpa kompromi.",
        "badge": "Flagship"
    }
]

@app.route('/')
def home():
    return render_template('index.html', produk=PRODUK_UTAMA)

@app.route('/produk/<int:id_produk>')
def detail_produk(id_produk):
    # Mencari produk berdasarkan ID
    produk_terpilih = next((p for p in PRODUK_UTAMA if p["id"] == id_produk), None)
    if not produk_terpilih:
        return "Produk tidak ditemukan", 404
    return render_template('detail.html', produk=produk_terpilih)

@app.route('/checkout/<int:id_produk>', methods=['POST'])
def checkout(id_produk):
    produk_terpilih = next((p for p in PRODUK_UTAMA if p["id"] == id_produk), None)
    nama_pembeli = request.form.get('nama')
    alamat_pembeli = request.form.get('alamat')
    
    return render_template('sukses.html', produk=produk_terpilih, nama=nama_pembeli, alamat=alamat_pembeli)

if __name__ == '__main__':
    app.run(debug=True)
