import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "index.html"


class ZbrainI18nContractTests(unittest.TestCase):
    def setUp(self):
        self.html = HTML_PATH.read_text(encoding="utf-8")

    def test_chinese_is_the_real_first_paint_language(self):
        self.assertIn('<html lang="zh-CN">', self.html)
        self.assertIn('<title>ZBRAIN</title>', self.html)
        self.assertIn("赵长鹏的大脑，实时运行中。", self.html)
        self.assertIn("让它思考", self.html)
        self.assertIn("切换频道", self.html)
        self.assertIn("大脑监视器", self.html)

    def test_language_toggle_is_fixed_bottom_left_and_starts_as_en(self):
        self.assertRegex(
            self.html,
            r'<button[^>]+id="languageToggle"[^>]*>EN</button>',
        )
        self.assertIn("#languageToggle", self.html)
        self.assertRegex(self.html, r"#languageToggle\s*\{[^}]*position:fixed")
        self.assertRegex(self.html, r"#languageToggle\s*\{[^}]*left:")
        self.assertRegex(self.html, r"#languageToggle\s*\{[^}]*bottom:")

    def test_bilingual_dictionary_covers_static_and_dynamic_surfaces(self):
        self.assertIn("const I18N = {", self.html)
        self.assertIn("zh: {", self.html)
        self.assertIn("en: {", self.html)
        for key in [
            "navBrain", "heroTitle", "brainMonitor", "changeChannel",
            "howTitle", "aboutTitle", "tokenTitle", "disclaimer",
            "loaderSteps", "marquee", "jokes", "articles", "programs",
            "feed", "canvas",
        ]:
            self.assertRegex(self.html, rf"\b{key}\s*:")

    def test_toggle_changes_language_without_reload_and_updates_dynamic_ui(self):
        self.assertIn('let currentLanguage = "zh";', self.html)
        self.assertRegex(self.html, r"function setLanguage\(language\)")
        self.assertIn('document.documentElement.lang = language === "zh" ? "zh-CN" : "en";', self.html)
        self.assertIn('languageToggle.textContent = language === "zh" ? "EN" : "中文";', self.html)
        self.assertIn('languageToggle.addEventListener("click"', self.html)
        self.assertNotRegex(self.html, r"languageToggle[^\n]{0,180}(location\.reload|location\.href)")
        self.assertIn("renderMarquee();", self.html)
        self.assertIn("refreshLocalizedRuntime();", self.html)

    def test_brand_and_token_identifiers_are_not_translated(self):
        self.assertIn(">ZBRAIN</a>", self.html)
        self.assertIn('ticker: "$ZBRAIN"', self.html)
        self.assertNotIn("智脑", self.html)


if __name__ == "__main__":
    unittest.main()
