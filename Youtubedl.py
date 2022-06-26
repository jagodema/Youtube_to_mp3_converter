import easygui as easygui
import youtube_dl
import PySimpleGUI as sg
from threading import Thread
import validators


def run(url, view):
    print(validators.url("https://google.com"))
    path = easygui.diropenbox()
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=url, download=False
    )

    filename = f"{video_info['title']}.mp3"
    path = path + '\\' + filename
    print(path)
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': path
    }
    view['info'].update('')

    with youtube_dl.YoutubeDL(options) as ydl:
        view['info'].update('Downloading')
        ydl.download([video_info['webpage_url']])
    view['info'].update('Downloaded')


if __name__ == '__main__':
    title = "Youtube to mp3 converter"
    icon = './ico.ico'
    sg.theme('DarkAmber')
    layout = [[sg.Text('Url'), sg.InputText()],
              [sg.Button('Download'), sg.Button('Close')],
              [sg.Text('', key='info')]]

    window = sg.Window(title, icon=icon).Layout(layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            break
        else:
            if len(values[0]) > 0:
                if validators.url(values[0]):
                    if 'youtube' in values[0]:
                        t1 = Thread(target=run, args=(values[0], window))
                        t1.start()
                    else:
                        window['info'].update('Enter a Youtube URL')
                else:
                    window['info'].update('Enter a valid URL')
            else:
                window['info'].update('Enter an URL')

    window.close()
