from win32com.client import Dispatch, constants
import win32com



def file_to_excel(excel_path:str,file_path:str):
    '''
    将文件添加到excel对象
    '''
    xlApp = win32com.client.Dispatch('Excel.Application')
    xlBook_1 = xlApp.Workbooks.Open(excel_path)

    xlSheet_1 = xlBook_1.Worksheets(1)
    xlSheet_1.Shapes.AddOLEObject(Filename=file_path,Link=False)#,DisplayAsIcon=True
    xlBook_1.Close(True)
   
    xlApp.Quit()


if __name__=="__main__":
    #该主函数脚本为批量添加对象文件到excel
    import sys
    print(sys.argv)
    try:
        argv_list = sys.argv
        argv_list.pop(0)
        excel_path =""
        for idx in argv_list:
            if ".xlsx" or ".xls" in idx:
                excel_path = idx
                break
        argv_list.remove(excel_path)
        [file_to_excel(excel_path,idy) for idy in argv_list]
    except Exception as e:
        print(e)
    finally:
        input("done..")
    