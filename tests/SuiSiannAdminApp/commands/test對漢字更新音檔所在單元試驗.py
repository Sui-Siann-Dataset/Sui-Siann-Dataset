from django.test.testcases import TestCase
from SuiSiannAdminApp.models import 句表
from SuiSiannAdminApp.management.commands.對漢字更新音檔所在 import 對漢字更新音檔所在
from django.core.exceptions import MultipleObjectsReturned


class 對漢字更新音檔所在單元試驗(TestCase):
    def test_改著一筆(self):
        漢 = "佇高雄左營區有一粒山，看起來誠特別。"
        羅 = "Tī Ko-hiông Tsó-iânn-khu ū tsi̍t lia̍p suann, khuànn--khí-lâi tsiânn ti̍k-pia̍t."
        結果 = "Oct 20, 2018 _38_after.wav"
        一句 = 句表.objects.create(
            音檔="_38.wav",
            漢字=漢,
            臺羅=羅,
            原始漢字="A",
            原始臺羅="a",
        )
        對漢字更新音檔所在(漢, 羅, 結果)
        音檔所在 = 句表.objects.get(pk=一句.pk).音檔
        self.assertEqual(音檔所在, 結果)

    def test_毋但一筆就跳錯誤(self):
        漢 = "佇高雄左營區有一粒山，看起來誠特別。"
        羅 = "Tī Ko-hiông Tsó-iânn-khu ū tsi̍t lia̍p suann, khuànn--khí-lâi tsiânn ti̍k-pia̍t."
        結果 = "Oct 20, 2018 _38_after.wav"
        句表.objects.create(
            音檔="_38.wav",
            漢字=漢,
            臺羅=羅,
            原始漢字="A",
            原始臺羅="a",
        )
        句表.objects.create(
            音檔="_38.wav",
            漢字=漢,
            臺羅=羅,
            原始漢字="A",
            原始臺羅="a",
        )
        with self.assertRaises(MultipleObjectsReturned):
            對漢字更新音檔所在(漢, 羅, 結果)
