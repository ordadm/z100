import sys
import time


def updt(total, progresss, start_time, positiv):
    #    start_time = time.time()
    """
    Displays or updates a console progress bar.

    Original source: /questions/27978/python-progress-bar/205178#205178
    """
    barLength, status = 80, ""
    progress = float(progresss) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.04f}% {}".format(
        "#" * block + "-" * (barLength - block), round(progress * 100, 4),
        status)  +  "---осталовь %s минут ---"  % round(
        ((((time.time() - start_time) / progress) - (time.time() - start_time)) / 60),
        2) + " текущий процент успешно пройденных миссий " + f'{round(positiv/progresss*100 , 2)} % '
    sys.stdout.write(text)
    sys.stdout.flush()

# runs = 300
# for run_num in range(runs):
#     time.sleep(.1)
#     updt(runs, run_num + 1)
