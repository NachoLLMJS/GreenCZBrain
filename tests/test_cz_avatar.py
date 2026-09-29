import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
AVATAR = HTML.split("/* ================= BRAIN + CZ FEATURES ================= */", 1)[-1].split("/* ================= COMPUTER ================= */", 1)[0]


class CzAvatarContractTests(unittest.TestCase):
    def test_avatar_uses_cz_buzz_cut_instead_of_long_bowl_cut(self):
        self.assertIn("// CZ buzz cut: short dark dotted stubble", AVATAR)
        self.assertNotIn("// bowl cut: strands of dots", AVATAR)
        self.assertNotIn("yBot = -0.45", AVATAR)
        self.assertIn('C("#171717")', HTML)

    def test_avatar_is_clean_shaven_and_has_rectangular_glasses(self):
        self.assertNotIn("// mustache", AVATAR)
        self.assertNotIn("COL.orange", AVATAR)
        self.assertIn("// CZ rectangular glasses", AVATAR)
        self.assertIn("addGlassesFrame", AVATAR)
        self.assertGreaterEqual(AVATAR.count("head.add("), 8)

    def test_avatar_copy_matches_clean_shaven_cz_identity(self):
        for stale in ["Installing mustache", "mustache: attached", "Combing the bowl cut", "bowl cut: combed", "counting hairs in fringe"]:
            self.assertNotIn(stale, HTML)
        self.assertIn("Fitting CZ glasses", HTML)
        self.assertIn("buzz cut: ready", HTML)

    def test_avatar_keeps_point_cloud_and_solid_cores_in_sync(self):
        self.assertIn("const brainBaseCoreColor = new THREE.Color(0xD58B00)", AVATAR)
        self.assertIn("const hairCore = coreMat(0x171717)", AVATAR)
        self.assertIn("const glassesCore = coreMat(0x171717)", AVATAR)
        self.assertIn("brainGroup.add(glassesCoreGroup)", AVATAR)
        self.assertIn("new THREE.BoxGeometry(0.68, 0.018, 0.018)", AVATAR)

    def test_hair_reads_as_stubble_and_glasses_are_cz_proportioned(self):
        self.assertIn("const w = 0.68, h = 0.34", AVATAR)
        self.assertIn("Math.floor(9800 * Q)", AVATAR)
        self.assertIn("hairCore.userData.maxOpacity = 0.52", AVATAR)
        self.assertIn("glassesCore.userData.maxOpacity = 0.72", AVATAR)

    def test_hairline_is_shaped_into_the_existing_cap_without_triangle_overlay(self):
        self.assertIn("// CZ V hairline: receded temples with central widow's peak", AVATAR)
        self.assertIn("const widowPeak = Math.max(0, 1 - Math.abs(x) / 0.34)", AVATAR)
        self.assertIn("const templeRecession", AVATAR)
        self.assertIn("shapeCzHairline(domeGeometry)", AVATAR)
        self.assertNotIn("hairPeakCore", AVATAR)
        self.assertNotIn("Dense dotted central peak", AVATAR)
        self.assertNotIn("new THREE.ShapeGeometry", AVATAR)

    def test_eyes_are_black_straight_and_have_no_white_lens_strokes(self):
        self.assertIn("// Straight black eyes: no white curved eye strokes", AVATAR)
        self.assertIn("const eyeY = 0.13", AVATAR)
        self.assertIn("new THREE.BoxGeometry(0.34, 0.035, 0.02)", AVATAR)
        self.assertNotIn("COL.glass", AVATAR)


if __name__ == "__main__":
    unittest.main()
