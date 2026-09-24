import re
import struct
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "index.html"
LOGO_PATH = ROOT / "assets" / "brand" / "zbrain-logo.png"
FAVICON_PATH = ROOT / "assets" / "brand" / "zbrain-favicon.ico"


class ZbrainBrandContractTests(unittest.TestCase):
    def setUp(self):
        self.html = HTML_PATH.read_text(encoding="utf-8")

    def test_public_identity_is_zbrain_and_changpeng_zhao_brain(self):
        self.assertIn("<title>ZBRAIN</title>", self.html)
        self.assertIn(">ZBRAIN</a>", self.html)
        self.assertIn("Changpeng Zhao's brain", self.html)
        self.assertIn('ticker: "$ZBRAIN"', self.html)
        for stale in ["JEANPHIL", "Jeanphil", "jeanphil", "$JPHIL", "bowl cut", "mustache"]:
            self.assertNotIn(stale, self.html)

    def test_generated_character_logo_replaces_embedded_legacy_images(self):
        self.assertIn('src="assets/brand/zbrain-logo.png?v=1"', self.html)
        self.assertIn('href="assets/brand/zbrain-favicon.ico?v=1"', self.html)
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


if __name__ == "__main__":
    unittest.main()
