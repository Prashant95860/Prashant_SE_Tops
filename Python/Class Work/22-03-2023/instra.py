# pip : python index package  install in python (pip install instaloader)
import instaloader

name = input("Enter Username : ")
insta = instaloader.Instaloader()

insta.download_profile(name,profile_pic_only=True)