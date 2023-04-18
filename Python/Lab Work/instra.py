import instaloader
n = input("Enter your Username : ")
insta = instaloader.instaloader()

insta.download_proofile(n,profile=True)
