import instaloader

mod = instaloader.Instaloader()
username = input("Enter The User Name: ")
mod.download_profile(username,profile_pic_only=True)
