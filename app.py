import qrcode
from PIL import Image

def tao_qrcode_du_co_logo(du_lieu, ten_file, co_logo=False, duong_dan_logo=None):
    """
    Hàm tạo QR code, có thể chèn logo nếu muốn.

    Tham số:
    - du_lieu: Nội dung cần mã hóa trong QR (chuỗi)
    - ten_file: Tên file đầu ra (VD: 'ma_qr.png')
    - co_logo: True nếu muốn chèn logo
    - duong_dan_logo: Đường dẫn đến file logo (phải là file ảnh PNG/JPG)
    """

    # Tạo đối tượng QRCode
    qr = qrcode.QRCode(
        version=4,  # Kích thước QR (1-40), càng cao càng chứa nhiều dữ liệu
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Cần thiết nếu có logo
        box_size=10,  # Kích thước mỗi ô vuông
        border=4,     # Viền (số ô)
    )
    qr.add_data(du_lieu)
    qr.make(fit=True)

    # Tạo ảnh QR code cơ bản
    img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    if co_logo and duong_dan_logo:
        try:
            logo = Image.open(duong_dan_logo)

            # Tính toán kích thước logo để phù hợp
            logo_size = int(min(img_qr.size) * 0.25)  # logo chiếm 25% chiều ngang/chiều cao QR
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

            # Tính vị trí để dán logo vào giữa
            pos = (
                (img_qr.size[0] - logo_size) // 2,
                (img_qr.size[1] - logo_size) // 2
            )

            # Dán logo lên ảnh QR code
            img_qr.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

        except Exception as e:
            print("❌ Lỗi chèn logo:", e)
            print("⚠️ QR-code sẽ được tạo không có logo.")

    # Lưu ảnh QR code
    img_qr.save(ten_file)
    print(f"✅ Đã tạo QR-code tại: {ten_file}")

# ==== Khởi tạo QR code ====
du_lieu_qr = "https://iuh.edu.vn"   # Có thể đổi thành nội dung khác
ten_file_qr = "ma_qrcode.png"       # Tên file đầu ra

# Trường hợp không có logo
tao_qrcode_du_co_logo(du_lieu_qr, ten_file_qr)

# Trường hợp có logo
tao_qrcode_du_co_logo(du_lieu_qr, "ma_qrcode_logo.png", co_logo=True, duong_dan_logo="iuh.png")