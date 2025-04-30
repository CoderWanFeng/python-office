from office.core.TestTypes.RuimingType import MainRuiming
from office.lib.utils.except_utils import except_dec

ruiming = MainRuiming()



def screen_unmarked_image(dir_path):
    ruiming.screen_unmarked_image(dir_path)



def change_label_in_xml(dir_path, old_label, new_label):
    ruiming.change_label_in_xml(dir_path, old_label, new_label)



def screen_without_label_json_file(dir_path):
    ruiming.screen_without_label_json_file(dir_path)