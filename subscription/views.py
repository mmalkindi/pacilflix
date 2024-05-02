from django.shortcuts import render

paket = [["basic", "Rp25000", "720", "handphone"], 
         ["standard", "Rp50000", "1080", "handphone, tablet, laptop"], 
         ["premium", "Rp70000", "2160", "handphone, tablet, laptop, smart tv"]]

# Create your views here.
def show_main(request):
    paket_aktif = [paket[2], "02/04/2024", "02/05/2024"]
    riwayat_transaksi = [["basic", "30/01/2024", "02/03/2024", "Transfer Bank", "30/01/2024", "Rp25000"], 
                         ["standard", "02/04/2024", "02/05/2024", "E-Wallet", "02/04/2024", "Rp50000"]]
    context = {
        'paket_aktif': paket_aktif,
        'semua_paket': paket,
        'riwayat_transaksi': riwayat_transaksi
    }

    return render(request, "subscription.html", context)

def show_buy_page(request):
    paket_dipilih = paket[2]
    context = {
        'paket_dipilih': paket_dipilih
    }

    return render(request, "buy.html", context)