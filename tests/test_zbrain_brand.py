import re
import struct
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "index.html"
LOGO_PATH = ROOT / "assets" / "brand" / "greenczbrain-logo.png"
FAVICON_PATH = ROOT / "assets" / "brand" / "greenczbrain-favicon.ico"


class ZbrainBrandContractTests(unittest.TestCase):
    def setUp(self):
        self.html = HTML_PATH.read_text(encoding="utf-8")

    def test_public_identity_is_green_cz_brain(self):
        self.assertIn("<title>GreenCZBrain</title>", self.html)
        self.assertIn(">GreenCZBrain</a>", self.html)
        self.assertIn("BNB is running to $2,000", self.html)
        self.assertIn('ticker: "$GREENBRAIN"', self.html)
        for stale in ["JEANPHIL", "Jeanphil", "jeanphil", "$JPHIL", "bowl cut", "mustache"]:
            self.assertNotIn(stale, self.html)

    def test_generated_character_logo_replaces_embedded_legacy_images(self):
        self.assertIn('src="assets/brand/greenczbrain-logo.png?v=2"', self.html)
        self.assertIn('href="assets/brand/greenczbrain-favicon.ico?v=2"', self.html)
        self.assertNotRegex(self.html, r'class="brand"[^>]*>\s*<img src="data:image')
        self.assertNotRegex(self.html, r'class="portrait" src="data:image')
        self.assertNotRegex(self.html, r'class="fallback">\s*<img src="data:image')

    def test_generated_logo_is_a_real_512_square_png(self):
        data = LOGO_PATH.read_bytes()
        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
        width, height = struct.unpack(">II", data[16:24])
        self.assertEqual((width, height), (512, 512))
        self.assertTrue(FAVICON_PATH.exists())

    def test_computer_channel_promotes_the_book_instead_of_the_old_feature(self):
        self.assertIn('t: "Buy My Book"', self.html)
        self.assertIn('t: "购买我的书"', self.html)
        self.assertIn('img: "book"', self.html)
        self.assertIn('if (k === "book")', self.html)
        self.assertIn('localized().canvas.buyBook', self.html)
        self.assertIn('localized().canvas.byZbrain', self.html)
        self.assertNotIn('k === "network"', self.html)

    def test_old_social_identity_is_not_published(self):
        self.assertNotIn("https://x.com/zbrainBNB", self.html)
        self.assertIn('x: ""', self.html)

    def test_bnb_chart_and_four_second_green_rush_exist(self):
        self.assertIn("const BNBChart", self.html)
        self.assertIn("phase >= 8 && phase < 12", self.html)
        self.assertIn('document.body.classList.toggle("green-rush", active)', self.html)
        self.assertIn("brainCore.color.copy(brainBaseCoreColor).lerp(brainGreenColor", self.html)
        self.assertIn('finalGreenImage.src = "assets/brand/green-rush-screen.png?v=1"', self.html)
        self.assertIn("G.drawImage(finalGreenImage, dx, dy, dw, dh)", self.html)


if __name__ == "__main__":
    unittest.main()
