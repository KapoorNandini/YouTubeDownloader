# Youtube Downloader With GUI
# Copyright (C) 2021 @IshanSingla
#
# This file is a part of < https://github.com/IshanSingla/YouTubeDownloader/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/IshanSingla/YouTubeDownloader/blob/main/LICENSE/>.

import tkinter
from pytube import YouTube

root = tkinter.Tk()
root.geometry('1000x600')
root.resizable(0,0)
root.title("Youtube Video Downloader (By IshanSingla)")
tkinter.Label(root, text ='Youtube Video Downloader\nBy IshanSingla\n', font ='arial 20 bold').pack()

#Input Box
link = tkinter.StringVar()
tkinter.Label(root, text ='Paste Link Here:', font ='arial 15 bold').place(x= 400, y = 200)
link_enter = tkinter.Entry(root, width = 140, textvariable = link).place(x = 64, y = 300)

#function to download video
def Downloader():
    try:
        url =YouTube(str(link.get()))
        video = url.streams.first()
        video.download()
        tkinter.Label(root, text ='DOWNLOADED', font ='arial 15').place(x= 420, y = 410)
    except Exception as w:
        print(f"Error: You Have not put the Valid Link")

#Download Button
tkinter.Button(root, text ='DOWNLOAD', font ='arial 15 bold',fg='white', bg ='red', padx = 2, command = Downloader).place(x=420, y = 400)
root.mainloop()
