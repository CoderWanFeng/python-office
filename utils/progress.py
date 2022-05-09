# 进度条

from progress.bar import ChargingBar


# todo：待完善，用于所有的方法中
def progress_bar(max):
    bar = ChargingBar('Processing', max)
    for i in range(max):
        bar.next()
    bar.finish()
