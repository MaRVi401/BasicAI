def simple_chatbot():
    """
    Program chatbot sederhana berbasis aturan.
    """
    print("Halo! Saya adalah chatbot sederhana. Anda bisa menyapa atau bertanya.")
    print("Ketik 'keluar' atau 'bye' untuk mengakhiri percakapan.")

    while True:
        user_input = input("Anda: ").lower().strip() # Mengambil input pengguna, mengubah ke huruf kecil, dan menghapus spasi di awal/akhir

        if user_input in ["keluar", "bye", "selesai"]:
            print("Chatbot: Sampai jumpa! Senang berbincang dengan Anda.")
            break # Keluar dari loop

        elif "halo" in user_input or "hai" in user_input or "hei" in user_input:
            print("Chatbot: Halo juga! Ada yang bisa saya bantu?")

        elif "apa kabar" in user_input:
            print("Chatbot: Saya baik-baik saja, terima kasih sudah bertanya!")

        elif "nama kamu siapa" in user_input or "siapa namamu" in user_input:
            print("Chatbot: Saya adalah Simple Chatbot. Saya tidak punya nama pribadi.")

        elif "bantu" in user_input or "tolong" in user_input:
            print("Chatbot: Tentu, saya akan coba bantu. Anda butuh bantuan apa?")

        elif "cuaca" in user_input:
            print("Chatbot: Maaf, saya tidak memiliki informasi cuaca saat ini.")

        elif "terima kasih" in user_input or "makasih" in user_input:
            print("Chatbot: Sama-sama! Senang bisa membantu.")

        else:
            print("Chatbot: Maaf, saya tidak mengerti. Bisakah Anda mengulang atau bertanya hal lain?")

# Panggil fungsi chatbot untuk menjalankannya
if __name__ == "__main__":
    simple_chatbot()