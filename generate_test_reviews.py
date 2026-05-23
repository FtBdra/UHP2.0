import csv
import os
import random

# Directory output
output_dir = 'UMKM-data'
os.makedirs(output_dir, exist_ok=True)

# Templates for generating diverse Indonesian reviews
pos_subjects = ["Produknya", "Pelayanannya", "Barang", "Kualitas", "Layanan admin", "Kemasan", "Proses pengiriman", "Aplikasi pemesanan"]
pos_adjectives = ["sangat bagus", "luar biasa mantap", "sangat memuaskan", "cepat dan ramah", "konsisten dan terjaga", "rekomendasi sekali", "sangat responsif", "terbaik dan oke"]
pos_conjunctions = ["dan", "serta", "juga"]
pos_closings = ["recommended banget!", "puas belanja di sini.", "pasti repeat order lagi.", "sukses terus untuk usahanya!", "sesuai ekspektasi.", "suka sekali dengan kualitasnya."]

neg_subjects = ["Pengiriman", "Respon admin", "Kualitas produk", "Stok barang", "Layanan toko", "Kemasan paket", "Proses checkout", "Harga barang"]
neg_adjectives = ["sangat lambat", "mengecewakan sekali", "buruk dan tidak responsif", "mahal tapi kurang bagus", "sering bermasalah", "tidak konsisten", "sangat jelek", "banyak masalah"]
neg_conjunctions = ["dan", "malah", "bahkan"]
neg_closings = ["bikin kecewa.", "kapok belanja di sini.", "perlu banyak perbaikan.", "tidak sesuai deskripsi.", "layanan tidak membaik.", "kecewa berat."]

neu_subjects = ["Kualitas", "Pelayanan", "Harga barang", "Pengiriman", "Secara keseluruhan", "Produk"]
neu_adjectives = ["biasa saja", "cukup standar", "lumayan oke", "sesuai harga", "tidak terlalu istimewa", "kurang lebih standar", "cukup baik", "sedang-sedang saja"]
neu_conjunctions = ["tapi", "namun", "dan"]
neu_closings = ["sesuai lah dengan harganya.", "tidak mengecewakan tapi tidak wah juga.", "seperti biasa.", "cukup oke untuk dicoba.", "standar saja.", "lumayan."]

def generate_positive_reviews(n=100):
    reviews = []
    used = set()
    while len(reviews) < n:
        sub = random.choice(pos_subjects)
        adj = random.choice(pos_adjectives)
        conj = random.choice(pos_conjunctions)
        adj2 = random.choice(pos_adjectives)
        while adj2 == adj:
            adj2 = random.choice(pos_adjectives)
        closing = random.choice(pos_closings)
        
        review = f"{sub} {adj}, {conj} {adj2}. {closing}"
        if review not in used:
            used.add(review)
            reviews.append(review)
    return reviews

def generate_negative_reviews(n=100):
    reviews = []
    used = set()
    while len(reviews) < n:
        sub = random.choice(neg_subjects)
        adj = random.choice(neg_adjectives)
        conj = random.choice(neg_conjunctions)
        adj2 = random.choice(neg_adjectives)
        while adj2 == adj:
            adj2 = random.choice(neg_adjectives)
        closing = random.choice(neg_closings)
        
        review = f"{sub} {adj}, {conj} {adj2}. {closing}"
        if review not in used:
            used.add(review)
            reviews.append(review)
    return reviews

def generate_neutral_reviews(n=100):
    reviews = []
    used = set()
    while len(reviews) < n:
        sub = random.choice(neu_subjects)
        adj = random.choice(neu_adjectives)
        conj = random.choice(neu_conjunctions)
        adj2 = random.choice(neu_adjectives)
        while adj2 == adj:
            adj2 = random.choice(neu_adjectives)
        closing = random.choice(neu_closings)
        
        review = f"{sub} {adj}, {conj} {adj2}. {closing}"
        if review not in used:
            used.add(review)
            reviews.append(review)
    return reviews

# Write CSV files
def write_csv(filename, reviews):
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Ulasan']) # Column header compatible with UHP
        for review in reviews:
            writer.writerow([review])
    print(f"Berhasil membuat: {filepath} ({len(reviews)} baris)")

if __name__ == '__main__':
    random.seed(42)
    pos_reviews = generate_positive_reviews(100)
    neg_reviews = generate_negative_reviews(100)
    neu_reviews = generate_neutral_reviews(100)
    
    write_csv('ulasan_positif_100.csv', pos_reviews)
    write_csv('ulasan_negatif_100.csv', neg_reviews)
    write_csv('ulasan_netral_100.csv', neu_reviews)
