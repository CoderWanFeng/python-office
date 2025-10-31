import povideo

# 从视频里提取音频




def video2mp3(path, mp3_name=None, output_path=r'./'):
    """将视频文件转换为mp3音频文件。
    
    Args:
        path (str): 视频文件的路径
        mp3_name (str, optional): 输出mp3文件的名称，如果未提供，默认为原视频文件名
        output_path (str, optional): 输出mp3文件的路径，默认为当前目录
    
    Returns:
        None，但会在指定输出路径下生成mp3文件
    """
    povideo.video2mp3(path, mp3_name, output_path)

def audio2txt(audio_path, appid, secret_id, secret_key):
    """从音频里提取文字。
    
    注意：本地语音文件不能大于5MB。
    
    Args:
        audio_path (str): 音频文件路径
        appid (str): 语音识别API的应用ID
        secret_id (str): 语音识别API的密钥ID
        secret_key (str): 语音识别API的密钥
    
    Returns:
        None
    """
    povideo.audio2txt(audio_path, appid, secret_id, secret_key)



def mark2video(video_path, output_path=r'./', output_name=r'mark2video.mp4', mark_str: str = "www.python-office.com",
               font_size=28,
               font_type='Arial', font_color='white'):
    """给视频添加水印。
    
    Args:
        video_path (str): 视频地址
        output_path (str, optional): 输出地址，默认为当前目录
        output_name (str, optional): 输出名称，记得带'.mp4'，默认为'mark2video.mp4'
        mark_str (str, optional): 水印内容，只支持英文，默认为'www.python-office.com'
        font_size (int, optional): 水印字体大小，默认为28
        font_type (str, optional): 水印字体类型，默认为'Arial'
        font_color (str, optional): 水印颜色，默认为'white'
    
    Returns:
        None
    """
    povideo.mark2video(video_path, output_path, output_name, mark_str, font_size, font_type, font_color)



def txt2mp3(content='程序员晚枫', file=None, mp3=r'./程序员晚枫.mp3', speak=True):
    """文本转语音。
    
    Args:
        content (str, optional): 需要转换的内容，默认为'程序员晚枫'
        file (str, optional): 指定读取的文件，优先级最高
        mp3 (str, optional): 需要保存的mp3位置和名称，填None不保存，默认为'./程序员晚枫.mp3'
        speak (bool, optional): 是否阅读，默认为True
    
    Returns:
        None
    """
    return povideo.txt2mp3(content, file, mp3, speak)
