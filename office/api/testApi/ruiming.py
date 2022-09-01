from office.core.TestTypes.RuimingType import MainRuiming
from office.lib.utils.except_utils import except_dec

ruiming = MainRuiming()


@except_dec()
def screen_unmarked_image(dir_path):
    ruiming.screen_unmarked_image(dir_path)
