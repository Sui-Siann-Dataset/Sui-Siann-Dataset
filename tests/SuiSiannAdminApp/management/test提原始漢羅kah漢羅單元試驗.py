from django.test.testcases import TestCase
from SuiSiannAdminApp.models import 句表
from SuiSiannAdminApp.management.提原始漢羅kah漢羅 import 提原始漢羅kah漢羅


class 提原始漢羅kah漢羅單元試驗(TestCase):
    def test_提兩筆(self):
        句1 = 句表.objects.create(
            原始漢字="媠姑娘",
            原始臺羅="suí koo-niû",
            漢字="媠",
            臺羅="suí"
        )
        pk1 = str(句1.pk)
        句2 = 句表.objects.create(
            原始漢字="豬",
            原始臺羅="ti",
            漢字="豬仔",
            臺羅="ti-á"
        )
        pk2 = str(句2.pk)
        self.assertEqual(提原始漢羅kah漢羅(), (
            [
                pk1, "媠姑娘", "suí koo-niû", pk2, "豬", "ti",
            ], [
                pk1, "媠", "suí", pk2, "豬仔", "ti-á",
            ],
        ))
