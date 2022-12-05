from typing import Any, Tuple

def create_qr_code(
    data: Any,
    background_color: Tuple[int, int],
    shape_color: Tuple[int, int],
    image_name : str,
    icon_path:str = None
    ) -> None:
    """
    creates a qr code with the provided data and saves it into the same directory where the script livs
    """
    import qrcode

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L if not icon_path else qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )

    qr.add_data(data)
    qr.make(fit=True)

    if icon_path:
        from qrcode.image.styledpil import StyledPilImage
        qr_image = qr.make_image(
            image_factory=StyledPilImage,
            embeded_image_path=icon_path
            )
    else:
        qr_image = qr.make_image(back_color=background_color, fill_color=shape_color)
    qr_image.save(f"./{image_name}.png")

def askii_qr_code(data: Any):
    """
        prints a QR code in the terminal with the data in it
    """
    import io
    import qrcode
    qr = qrcode.QRCode()
    qr.add_data(data)
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())

if __name__ == "__main__":
    # create's a normal QR code
    create_qr_code(
        data= "https://github.com/CanaanGM",
        background_color=(255,255,255),
        shape_color=(224,17,95),
        image_name="canaan_github_url"
        )

    # create's a QR with an Icon, needs the error correction to be on high
    create_qr_code(
        data= "https://github.com/CanaanGM",
        background_color=(255,255,255),
        shape_color=(224,17,95),
        image_name="canaan_github_url_with_icon",
        icon_path="./osaka_got_mixed_up.png"
        )

    askii_qr_code(
        data="https://github.com/CanaanGM"
    )