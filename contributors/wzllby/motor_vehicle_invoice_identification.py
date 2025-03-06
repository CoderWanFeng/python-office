import os.path

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
from utils import *

import json
import pandas as pd


class MotorVehicleInvoiceIdentificaion():

    def __init__(self):
        self.api_key = "ocr.tencentcloudapi.com"

    def get_tencent_secret(self, csv_path):
        df = pd.read_csv(csv_path)
        secret_id = df["SecretId"][0]
        secret_key = df["SecretKey"][0]
        return [secret_id, secret_key]

    def get_img_info(self, img_path, secret_id, secret_key):
        try:
            # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
            cred = credential.Credential(secret_id, secret_key)
            httpProfile = HttpProfile()
            httpProfile.endpoint = self.api_key
            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = ocr_client.OcrClient(cred, "", clientProfile)
            req = models.RecognizeGeneralInvoiceRequest()
            encode_str = get_base64_by_img(img_path)
            params = {
                "ImageUrl": "",
                "Types": [12],
                "ImageBase64": encode_str
            }
            req.from_json_string(json.dumps(params))
            resp = client.RecognizeGeneralInvoice(req)
            if resp.MixedInvoiceItems[0].Code == 'OK':
                motor_vehicle_sale_invoice = resp.MixedInvoiceItems[0].SingleInvoiceInfos.MotorVehicleSaleInvoice

                result = {
                    "购买方名称": motor_vehicle_sale_invoice.Buyer,
                    "发票号码": motor_vehicle_sale_invoice.Number,
                    "发票代码": motor_vehicle_sale_invoice.Code,
                    "纳税人识别号/统一社会信用代码/身份证号码": motor_vehicle_sale_invoice.BuyerTaxID,
                    "车辆类型": motor_vehicle_sale_invoice.VehicleType,
                    "厂牌型号": motor_vehicle_sale_invoice.VehicleModel,
                    "产地": motor_vehicle_sale_invoice.Origin,
                    "合格证号": motor_vehicle_sale_invoice.CertificateNumber,
                    "发动机号码": motor_vehicle_sale_invoice.VehicleEngineCode,
                    "车辆识别代号/车架号码": motor_vehicle_sale_invoice.VIN,
                    "价税合计": motor_vehicle_sale_invoice.TotalCn,
                    "价税合计(小写)": motor_vehicle_sale_invoice.Total,
                    "销货单位名称": motor_vehicle_sale_invoice.SellerAddress,
                    "电话": motor_vehicle_sale_invoice.SellerTel,
                    "纳税人识别号": motor_vehicle_sale_invoice.SellerTaxID,
                    "账号": motor_vehicle_sale_invoice.SellerBankAccount,
                    "地址": motor_vehicle_sale_invoice.SellerAddress,
                    "开户银行": motor_vehicle_sale_invoice.SellerBank,
                    "增值税税率或征收率": motor_vehicle_sale_invoice.TaxRate,
                    "增值税税额": motor_vehicle_sale_invoice.Tax,
                    "主管税务机关及代码": motor_vehicle_sale_invoice.TaxAuthorities + motor_vehicle_sale_invoice.TaxAuthoritiesCode,
                    "不含税价": motor_vehicle_sale_invoice.PretaxAmount,
                    "开票日期": motor_vehicle_sale_invoice.Date,
                    "开票人": motor_vehicle_sale_invoice.Issuer,
                    "备注": motor_vehicle_sale_invoice.Remark
                }
                return result
            return None
        except TencentCloudSDKException as err:
            print(err)

    def copy_rename_invoices(self, source_dir, target_dir='./result/new_dir'):
        """
        遍历目录，查找机动车发票下的新车发票文件，复制并重命名
        :param source_dir: 源目录路径
        :param target_dir: 目标目录路径
        :return: 新文件路径列表
        """
        # 创建目标目录（如果不存在）
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)
        os.makedirs(target_dir, exist_ok=True)

        # 初始化计数器和结果列表
        counter = 1
        new_file_paths = []

        # 遍历所有目录和文件
        for root, dirs, files in os.walk(source_dir):
            # 检查是否存在"机动车发票"目录
            if "机动车发票" in dirs:
                motor_dir = os.path.join(root, "机动车发票")

                # 遍历该目录下的所有文件
                for filename in os.listdir(motor_dir):
                    file_path = os.path.join(motor_dir, filename)

                    # 检查是否为文件且包含"新车发票"
                    if os.path.isfile(file_path) and "新车发票" in filename:
                        # 分离文件名和扩展名
                        _, ext = os.path.splitext(filename)

                        # 生成新文件名（新车发票_数字.扩展名）
                        new_filename = f"新车发票_{counter}{ext}"
                        new_filepath = os.path.join(target_dir, new_filename)

                        # 复制文件并保留元数据
                        try:
                            shutil.copy2(file_path, new_filepath)
                            new_file_paths.append(new_filepath)
                            counter += 1
                        except Exception as e:
                            print(f"复制文件 {file_path} 失败: {str(e)}")
        return new_file_paths

    def main_exec(self, origin_zip_file, result_excel_file):
        if not os.path.exists(origin_zip_file):
            print("需要解压的zip文件不存在！")
            return
        # 删除上次生成的excel文件
        if os.path.exists(result_excel_file):
            os.remove(result_excel_file)
        process_file_path = None
        try:
            # 获取解压后的文件路径
            process_file_path = process_zip(origin_zip_file)
            if not process_file_path:
                print("没有解压文件！")
                return
            # 参数为秘钥文件,在官网控制台 https://console.cloud.tencent.com/cam/capi 点击新建密钥,然后点击下载CSV文件,不需要可以注释
            secrets = self.get_tencent_secret("SecretKey.csv")
            if secrets is None or len(secrets) != 2:
                print("获取密钥有误,请检查密钥文件！")
                return
            # 获取所有的发票并且移动到新的文件中
            new_invoice_path = self.copy_rename_invoices(process_file_path)
            result = []
            count = 1
            for new_path in new_invoice_path:
                print(f"正在识别第{count}张文件!")
                count += 1
                # 解析文件获取信息 第二个和第三个参数可直接在网站复制
                result_info = self.get_img_info(new_path, secrets[0], secrets[1])
                if result_info is not None:
                    result.append(result_info)
            df = pd.DataFrame(result)
            # 写入excel
            df.to_excel(result_excel_file, index=False)
        finally:
            if process_file_path:
                shutil.rmtree(process_file_path)

    def main_exec_single(self, origin_zip_file, result_excel_file):
        if not os.path.exists(origin_zip_file):
            print("需要识别的文件不存在！")
            return
        # 删除上次生成的excel文件
        if os.path.exists(result_excel_file):
            os.remove(result_excel_file)
        # 参数为秘钥文件,在官网控制台 https://console.cloud.tencent.com/cam/capi 点击新建密钥,然后点击下载CSV文件,不需要可以注释
        secrets = self.get_tencent_secret("SecretKey.csv")
        if secrets is None or len(secrets) != 2:
            print("获取密钥有误,请检查密钥文件！")
            return
        # 解析文件获取信息 第二个和第三个参数可直接在网站复制
        result_info = self.get_img_info(origin_zip_file, secrets[0], secrets[1])
        df = pd.DataFrame([result_info])
        # 写入excel
        df.to_excel(result_excel_file, index=False)


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)
    mon = MotorVehicleInvoiceIdentificaion()
    # 第一个参数为zip文件的路径  第二个文件为生成的excel的文件路径
    mon.main_exec("file/样例.zip", "./result/output_result.xlsx")
    mon.main_exec_single("file/样例.jpg", "./result/output.xlsx")
