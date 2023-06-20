<br>
<p align="center">
    <img src="./chin.png" alt='Logo' width=100>

<h3 align="center">Chin ( Discord Music Bot )</h3>

<p align="center">
    Chinchinator is a Discord Music Bot built with Python & uses Command Handler from [discord.py guide](https://discordpy.readthedocs.io/en/stable/).
</p>

#
<p align="center"

![ga](https://img.shields.io/badge/Python-3.6-blue?style=for-the-badge&logo=)
![si](https://img.shields.io/badge/Academical%20Project-No-red?style=for-the-badge&logo=) 
![si](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=)
![si](https://img.shields.io/badge/Repo%20Size-8Kb-yellow?style=for-the-badge&logo=)
<p align="center">

## Too lazy to set up the bot ? 
> Make my bot join your server !  
https://discord.com/api/oauth2/authorize?client_id=887881573297451011&permissions=4331689984&scope=bot

## Requirements ![a](https://img.shields.io/badge/pip-v1.3-red)
1. Discord Bot Token [Guide](https://www.pythondiscord.com/pages/guides/python-guides/discordpy/)  
1.1. Enable 'Message Content Intent' in Discord Developer Portal    
2. Python3  
3. pip package installer  

## 🐘 Getting Started  
```cmd
git clone https://github.com/Owzok/Chinchinator3000.git
cd Chinchinator3000
pip install -r requirements.txt
```
After installation finishes follow configuration instructions then run ```python3 main.py``` to start the bot. 

## ⚙️ Configuration
Rename in the main.py file the "Chinchinator_token" for your discord provided token:  
```client.run(os.environ.get("Chinchinator_token"))```  
You can add an enviroment variable called "Musicbot_token" or whatever you want and assign the token or just add your token there.
In this case I used an enviroment variable because I was going to make this a public repo.  
#### Solution for newbies:
1. Create an environment variable called Chinchinator_token and assign your token as its value.  
2. Create another environment variable calles as you want and change the ```"Chinchinator_token"``` for ```"Your Variable Name"```.  
3. Forget environment variables and change the line to ```client.run("Write your token here")```.  

⚠️ Note: Never commit or share your token or api keys publicly ⚠️  

## 📝 Features & Commands  
🎶 Play music from YouTube via url  
```-p https://www.youtube.com/watch?v=GLvohMXgcBo```

🔎 Play music from YouTube via search query  
```-p tengen toppa opening 1```

Join (-join)  
Leave (-leave)  
Play (-p)  
Show Queued Songs (-queue)  
Skip Song (-skip)  
Pause (-pause)  
Resume (-resume)  
Remove song # from queue (-remove)  
Show Discord Bot ping (-ping)  
Shuffle queue (-shuffle)  
Clear queue (-clear)  

>[todo] Loop  
[todo] Lyrics  
[todo] Volume  
