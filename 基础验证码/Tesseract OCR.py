import requests
from PIL import Image, ImageEnhance
from io import BytesIO
import pytesseract


class CaptchaCrawler:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def preprocess_image(self, image):
        image = image.convert('L')  # 转为灰度
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2)  # 增强对比度
        image = image.point(lambda x: 0 if x < 180 else 255)  # 二值化
        return image

    def solve_captcha(self, image_url):

        response = self.session.get(image_url, headers=self.headers)
        image = Image.open(BytesIO(response.content))

        processed_image = self.preprocess_image(image)


        captcha_text = pytesseract.image_to_string(processed_image).strip()
        return captcha_text

    def submit_form(self, login_url, data):

        response = self.session.post(login_url, data=data, headers=self.headers)
        return response.status_code == 200


if __name__ == "__main__":
    crawler = CaptchaCrawler()

    CAPTCHA_URL = "http://example.com/captcha.jpg"
    LOGIN_URL = "http://example.com/login"

    captcha = crawler.solve_captcha(CAPTCHA_URL)
    print(f"识别结果: {captcha}")

    # 构造表单数据
    form_data = {
        'username': 'your_username',
        'password': 'your_password',
        'captcha_code': captcha
    }

    # 提交登录请求
    if crawler.submit_form(LOGIN_URL, form_data):
        print("登录成功！")
        # 后续爬取操作...
    else:
        print("登录失败，请检查验证码识别结果")