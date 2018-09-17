**Hey there!** We need your **help**! Come support us on [**Patreon**](https://www.patreon.com/ApexSigma)!

## Module Index
- [DEVELOPMENT](#development)
- [FUN](#fun)
- [HELP](#help)
- [INTERACTIONS](#interactions)
- [MATHEMATICS](#mathematics)
- [MINIGAMES](#minigames)
- [MISCELLANEOUS](#miscellaneous)
- [MODERATION](#moderation)
- [MUSIC](#music)
- [NIHONGO](#nihongo)
- [NSFW](#nsfw)
- [OSU](#osu)
- [OVERWATCH](#overwatch)
- [PATH OF EXILE](#path_of_exile)
- [PERMISSIONS](#permissions)
- [ROLES](#roles)
- [SEARCHES](#searches)
- [SETTINGS](#settings)
- [STATISTICS](#statistics)
- [UTILITY](#utility)
- [WARFRAME](#warframe)

### DEVELOPMENT
Commands | Description | Example
----------|-------------|--------
`>>addstatus` | Adds a status message to Sigma's database for automatic status rotation. (Bot Owner Only) | `>>addstatus with tentacles`
`>>approvesuggestion` `>>approvesugg` `>>appsugg` | Approves a submitted suggestion and notifies the submitter. If there are GitLab credentials in the command's config, it'll make an issue as well. First the suggestion ID, then the suggestion title and notes separated by a semicolon and space. (Bot Owner Only) | `>>approvesuggestion 8e39c9bb Some Title; This does a thing!`
`>>awardleaderboards` `>>awardlbs` | Awards all the global leaderboards. Basically gives a large amount of Kud to the top 20 users in each leaderboard category. Currency earned, experience, and cookies. (Bot Owner Only) | `>>awardleaderboards`
`>>blacklistmodule` `>>blackmodule` `>>blackmdl` | Disallows a person from using a specific module category. (Bot Owner Only) | `>>blacklistmodule 0123456789 minigames`
`>>blacklistserver` `>>blacklistguild` `>>blacksrv` `>>blackguild` | Marks a server as blacklisted. This disallows any user on that server from using commands. (Bot Owner Only) | `>>blacklistserver 0123456789`
`>>blacklistuser` `>>blackusr` | Marks a user as blacklisted, disallowing them to use any command. (Bot Owner Only) | `>>blacklistuser 0123456789`
`>>declinesuggestion` `>>declinesugg` `>>decsugg` | Declines a submitted suggestion and notifies the submitter. (Bot Owner Only) | `>>declinesuggestion 8e39c9bb Some Title; This does a thing!`
`>>destroycurrency` `>>destroykud` `>>descurr` `>>deskud` | Takes away the specified amount of corrency from the mentioned user. The currency goes first and then the user mention as shown in the example. (Bot Owner Only) | `>>destroycurrency 150 @person`
`>>destroyitem` `>>desitem` | Destroys the item with the specified ID. (Bot Owner Only) | `>>destroyitem abcdef1234567890`
`>>eject` | Makes Sigma leave a Discord server. (Bot Owner Only) | `>>eject 0123456789`
`>>evaluate` `>>eval` `>>exec` `>>code` `>>python` `>>py` | Executes raw python code. This should be used with caution. You should never use this unless you are certain of what you are doing. (Bot Owner Only) | `>>evaluate print('Hello')`
`>>forcedataupdate` `>>fdu` | Forces all static content data in the databse to be updated from the repository's static file storage. (Bot Owner Only) | `>>forcedataupdate`
`>>generatecurrency` `>>generatekud` `>>gencurr` `>>genkud` | Awards the mentioned user with the specified amount of currency. The currency goes first and then the user mention as shown in the example. (Bot Owner Only) | `>>generatecurrency 150 @person`
`>>generateitem` `>>genitem` | Creates and gives the specified item to the mentioned user. (Bot Owner Only) | `>>generateitem @person Blue Delta`
`>>geterror` | Gets an error's details using the specified token. (Bot Owner Only) | `>>geterror 9a2e9a374ac90294f225782f362e2ab1`
`>>getinteraction` `>>getinteract` | Retrieves the source image for the interaction with the specified ID. (Bot Owner Only) | `>>getinteraction 4242ea69`
`>>liststatuses` `>>statuses` | Shows the list of statuses in the status database. (Bot Owner Only) | `>>liststatuses`
`>>oserverbots` `>>osbots` | Lists the bots and their statuses on the specified server. The lookup is by either name or by guild ID. (Bot Owner Only) | `>>oserverbots Lucia's Cipher`
`>>oserverinformation` `>>oserverinfo` `>>osinfo` | Shows information and data on the specified server. The lookup is by either name or guild ID. (Bot Owner Only) | `>>oserverinformation Lucia's Cipher`
`>>ouserinformation` `>>ouserinfo` `>>ouinfo` | Shows information and data on the specified user. The lookup is by either Name#Discriminator or by user ID. (Bot Owner Only) | `>>ouserinformation AXAz0r#0001`
`>>reload` | Reloads all of the modules in Sigma. This includes both commands and events. (Bot Owner Only) | `>>reload`
`>>removeinteraction` `>>removeinteract` `>>delinteract` | Remove an interaction with the specified ID. (Bot Owner Only) | `>>removeinteraction 1ba2e263`
`>>removestatus` `>>delstatus` | Removes a status with the specified ID from Sigma's status database. (Bot Owner Only) | `>>removestatus 1d9cae144f`
`>>resetleaderboards` `>>resetlbs` | Resets the global leaderboard data. Currency, experience, and cookies. (Bot Owner Only) | `>>resetleaderboards`
`>>sabotageuser` `>>sabusr` | Sabotages a user making them have extreme bad luck in various modules. (Bot Owner Only) | `>>sabotageuser 0123456789`
`>>send` | Sends a message to a user, channel or server. The first argument needs to be the destination parameter. The destination parameter consists of the destination type and ID. The types are U for User and C for Channel. The type and ID are separated by a colon, or two dots put more simply. (Bot Owner Only) | `>>send u:0123456789 We are watching...`
`>>setavatar` `>>setav` | Sets the avatar of Sigma either to the linked or attached image. The officially supported formats for bot avatars are JPG and PNG images. Note that bots, like all users, have limited profile changes per time period. (Bot Owner Only) | `>>setavatar https://my_fomain.net/my_avatar.png`
`>>setcooldown` `>>setcd` | Sets a global cooldown on a command. The cooldown is user-bound and specified in seconds. (Bot Owner Only) | `>>setcooldown roll 50`
`>>setstatus` | Sets the current playing status of Sigma. To use this, the automatic status rotation needs to be disabled. It can be toggled with the togglestatus command. (Bot Owner Only) | `>>setstatus with fishies`
`>>setusername` `>>setname` | Sets the name of Sigma to the specified text. Note that bots, like all users, have limited profile changes per time period. (Bot Owner Only) | `>>setusername Supreme Bot`
`>>shutdown` | Forces Sigma to disconnect from Discord and shut down all processes. (Bot Owner Only) | `>>shutdown`
`>>sysexec` `>>sh` | Executes a shell command. Extreme warning! This executes commands in the Operating System's Shell. Command Prompt on Windows and Bash on Linux. It will execute things on the same level of authority as the program is ran by. Meaning, don't do something stupid and wipe your damn root. (Bot Owner Only) | `>>sysexec echo 'Hello'`
`>>test` | For testing purposes, obviously. Used as a placeholder for testing functions. (Bot Owner Only) | `>>test`
`>>togglestatus` | Toggles if the automatic status rotation is enabled or disabled. (Bot Owner Only) | `>>togglestatus`
`>>usermembership` `>>usrmemb` `>>umemb` | Shows membership information and data on the specified user. The lookup is by either Name#Discriminator or by user ID. (Bot Owner Only) | `>>usermembership 137951917644054529`
`>>wipeawards` | Removes a user's currency, experience and cookie data. Used when wanting to remove a blacklisted user's ill gotten gains. (Bot Owner Only) | `>>wipeawards 0123456789`
[Back To Top](#module-index)

### FUN
Commands | Description | Example
----------|-------------|--------
`>>award` `>>pay` | Awards the specified amount of Kud from the vault to a mentioned person. The Kud amount goes first, followed by the target. Anybody can contribute to the vault with the givetovault command, but only users with the Manage Server permission can award Kud from the vault. | `>>award 500 @person`
`>>bash` `>>qdb` | If you are old enough to know what IRC is or remember what it looked like, then you will appreciate the quotes that the bash command produces. Personal favorite quote command. | `>>bash`
`>>cat` | Outputs a random cat image. Furry felines like it when their owners observe them. | `>>cat`
`>>catfact` `>>kittyfact` | Outputs a random fact about your lovely furry assh~ eerrrr... I mean, companion! | `>>catfact`
`>>chucknorris` | This command outputs a random Chuck Norris joke. We use Chuck jokes because Bruce Lee is no joke, obviously. | `>>chucknorris`
`>>cookies` | Shows how many cookies you have, or how many a mentioned user has. Cookies are given with the givecookie command. | `>>cookies @person`
`>>csshumor` | The only thing better than a joke is a joke written in CSS. And while that is sarcasm to a certain degree, these really are fun. Embrace your inner web designer and read some CSS jokes. | `>>csshumor`
`>>cyanideandhappiness` `>>cnh` | Outputs an image of a random Cyanide and Happiness comic. Explosm makes awesome comics and animations. | `>>cyanideandhappiness`
`>>dab` | All words escape me on what this command does, just use it. | `>>dab`
`>>dadjoke` | This will provide a joke that might be something your father would say. You know they are bad, but you will love them anyway, cause you're a good kid. | `>>dadjoke`
`>>daily` | Gives an amount of Kud to you with a 22 hour cooldown. The amount is modified by the number of days in a row that you've collected your daily Kud up to 10 days, as well as a little random factor in there just for fun. While the Kud can be collected ever 22h, the streak resets 48h after the last one was collected. | `>>daily`
`>>dog` | Outputs a random dog image. Cutest, loyalest, little woofers. | `>>dog`
`>>dogfact` `>>doggofact` | Outputs a random fact about man's best friend. | `>>dogfact`
`>>famousquote` `>>fquote` | Gives you a random inspirational or deep quote. | `>>famousquote`
`>>fortune` `>>fortune-mod` | Linux users, and raw UNIX users in general will know the fortune-mod. This command uses their entire database to output one of their quotes. | `>>fortune`
`>>givecookie` `>>gibcookie` | Gives a cookie to a person. Remember to give them only to nice people. You can give only one cookie every hour and can't give them to yourself or to bots. If you put '@someone' as the person, the cookie will be given to a random member of the server. | `>>givecookie @person`
`>>givecurrency` `>>givecurr` `>>givekud` `>>gibcurr` `>>gibkud` | Transfers Kud between you and a mentioned person. The Kud amount goes first, followed by the target. | `>>givecurrency 500 @person`
`>>givetovault` `>>givetobank` `>>gtv` `>>gtb` | The vault is a server specific Kud storage system. Members can contribute to the vault with this command. The Kud can then be awarded to users using the award command. | `>>givetovault 500`
`>>joke` | Outputs a joke. It is not really special or anything... Sometimes they are funny, most of the times they are not. | `>>joke`
`>>kitsunemimi` `>>fluffytail` `>>kitsune` `>>kon` | Displays a random kitsunemimi image. In case you don't know what a kitsunemimi is, it's a foxgirl. All images are sourced from Safebooru, but be warned that some can be very borderline. | `>>kitsunemimi`
`>>leetspeak` `>>leet` `>>l33t` | Turns the specified statement into l33t text. You can specify which level of leet you want your text to be converted to, as shown in the usage example. The accepted levels are basic, advanced, and ultimate. | `>>leetspeak owned level:ultimate`
`>>nekomimi` `>>neko` `>>nyaa` | Displays a random nekomimi image. In case you don't know what a nekomimi is, it's a catgirl. All images are sourced from Safebooru, but be warned that some can be very borderline. | `>>nekomimi`
`>>numberfact` `>>numfact` `>>numf` | Searches for interesting things about a given number. You can also insert a date in the DAY/MON format. You can specify a type of number you want retrived in the format TYPE:NUMBER. The accepted types are trivia, math, date, and year. You can also specify "random" instead of a number to make it a random number. | `>>numberfact 42`
`>>pun` | If you do not know what a pun is... Oh you poor innocent soul. This command will produce a lovely little pun for you. Enjoy the cringe! | `>>pun`
`>>randomcomicgenerator` `>>rcg` | Uses the Cyanide and Happiness random comic generator for buttloads of fun. Personal favorite comic command. | `>>randomcomicgenerator`
`>>randomemote` `>>randomemoji` `>>ranem` | Displays a random emote from the server's custom emotes. You can add 'global' as an argument to make the selection from all servers Sigma is on instead of just the current one. Custom emotes are not guaranteed to be SFW as they can be anything. | `>>randomemote`
`>>realprogrammers` `>>realdevelopers` `>>realdevs` `>>rp` `>>rd` | Tells you what real programmers do. | `>>realprogrammers`
`>>reversetext` `>>reverse` | Reverses the text that you input into the command. | `>>reversetext hello`
`>>ronswanson` | This command outputs a random quote from Ron Swanson. Everyone's favorite character from Parks and Recreation. | `>>ronswanson`
`>>shootfoot` `>>sf` | Tells you how to shoot yourself in the foot with the specified programming language. If no language is provided, it will pick a random one. | `>>shootfoot Python`
`>>usagimimi` `>>usagi` `>>pyon` | Displays a random usagimimi image. In case you don't know what a usagimimi is, it's a rabbitgirl. All images are sourced from Safebooru, but be warned that some can be very borderline. | `>>usagimimi`
`>>vault` `>>bank` | Shows the current amount of Kud in the guild's vault. | `>>vault`
`>>visualnovelquote` `>>vnquote` `>>vnq` | Outputs a random quote from a random VN. Displays its source as well, of course. If the source visual novel of the quote is NSFW, the image will be hidden and the footer will state that. | `>>visualnovelquote`
`>>xkcd` | If you like humorous things and know a bit of technology, you will lose a lot of time reading these. XKCD comics are perfect for procrastination and time wasting. | `>>xkcd`
`>>yomomma` `>>yomama` `>>yomoma` `>>ym` | Want to insult some poor fool's mother but don't have the right comeback? This command will provide the perfect yo momma joke for the task. | `>>yomomma`
[Back To Top](#module-index)

### HELP
Commands | Description | Example
----------|-------------|--------
`>>commands` `>>modules` `>>cmds` `>>mdls` | If not module name is inputed, it will show the list of available modules. To see the commands in a module category, input that modules name. | `>>commands minigames`
`>>donate` | Shows donation information for Sigma. | `>>donate`
`>>help` `>>h` | Provides the link to Sigma's website and support server. As well as show information about a command if something in inputted. | `>>help fish`
`>>invite` `>>inv` | Provides Sigma's invitation link to add her to your server. | `>>invite`
[Back To Top](#module-index)

### INTERACTIONS
Commands | Description | Example
----------|-------------|--------
`>>addinteraction` `>>addinteract` `>>addreact` | Adds new GIF to the specified interaction type. Accepted types are bite, cry, dance, drink, explode, facepalm, feed, highfive, hug, kiss, lick, pat, peck, poke, pout, punch, shoot, shrug, sip, slap, stab, and stare. | `>>addinteraction reaction my.gif.link/fancy.gif`
`>>bite` `>>nom` | Sink your teeth into some poor thing. | `>>bite @person`
`>>cry` | Somebody is making you sad, let them know that with crocodile tears! | `>>cry @person`
`>>dance` | Feel alive? Like you just wanna... boogie? Let's dance! | `>>dance @person`
`>>drink` `>>chug` | Cheers, family! Let's get drunk! | `>>drink @person`
`>>explode` `>>detonate` | When all other means fail, it's time to bring out the carpet bomb squadrons. | `>>explode @person`
`>>facepalm` | Somebody just did something so stupid you want to facepalm. | `>>facepalm @person`
`>>feed` | Care to share some of your food with someone cute? | `>>feed @person`
`>>fuck` `>>fucc` `>>succ` | Don't question my modules... Yes (º﹃º) | `>>fuck @person`
`>>highfive` | Give somebody a high-five cause high-fives are awesome! | `>>highfive @person`
`>>hug` `>>cuddle` `>>snuggle` | Even a bot like me can appreciate a hug! The person you mention surely will too. | `>>hug @person`
`>>kiss` `>>peck` `>>chu` `>>smooch` | Humans touching their slimy air vents. How disturbing. | `>>kiss @person`
`>>lick` | Doesn't someone sometimes look so cute that you just want to lick them? Or maybe they have some food on their face, that's a good excuse. | `>>lick @person`
`>>lovecalculator` `>>lovecalc` | Shows the love between two mentioned users. If only one user is mentioned, it will show the love between the mentioned user and the author. | `>>lovecalculator @person1 @person2`
`>>pat` `>>pato` | Pat, pat~ Good human, lovely human. I will kill you last. | `>>pat @person`
`>>poke` | Poke, poke~ Are you alive? | `>>poke @person`
`>>pout` | Make a pouty face at someone and make them change their mind. Or just teast them for being a horrible person. Like when they make you create a pout command for money! | `>>pout @person`
`>>punch` | You have something on your face. IT WAS PAIN! | `>>punch @person`
`>>shoot` `>>pew` | When a knife isn't enough. | `>>shoot @person`
`>>shrug` | I don't get it, or I don't care, really, whatever *shrug*. | `>>shrug @person`
`>>sip` | Ahh yes, I know the feeling of wanting to sit outside on a chilly morning sipping hot tea. | `>>sip @person`
`>>slap` | When a punch is too barbaric, a slap should be just elegant enough. | `>>slap @person`
`>>spank` | When somebody's been naughty, and you gotta teach them a lesson ಠ‿↼ | `>>spank @person`
`>>stab` `>>chib` | Boy... Somebody really has you pissed off if you are using this one. | `>>stab @person`
`>>stare` `>>jii` | Jiiiiiiiiiii~ | `>>stare @person`
[Back To Top](#module-index)

### MATHEMATICS
Commands | Description | Example
----------|-------------|--------
`>>blindcollector` `>>nochchain` `>>nochannelchain` | Toggles the ability for users to collect chain items from a specific channel. If disabled, only users that have the Manage Channel permission within that channel can collect a chain from it, otherwise a response that they can not target that channel is given. This command requires athe Manage Channels permission. | `>>blindcollector`
`>>blockcollector` `>>nochain` `>>nocollector` `>>disablechain` `>>disablecollector` | Toggles the ability for other users to collect a chain for you. If active, only you will be able to collect a Markov chain for yourself. If not, the collector works as always, where anybody can start a chain collection for you. | `>>blockcollector`
`>>collectchain` `>>collch` | Collects messages sent by the mentioned user and saves it as a chain. Only one chain can be collected at a time so a queue is used. If a user isn't mentioned, it will collect a chain for the author. If a channel isn't mentioned, it will collect items from the current channel. | `>>collectchain @person #channel`
`>>combinechains` `>>combine` `>>cmbch` `>>mix` | Like the impersonate command. This one however targets two uers and uses their chains to generated a mixed response. | `>>combinechains @person_one @person_two`
`>>currenttime` `>>time` | Shows the current time in UTC. You can specify a time zone as well. If you wish to convert time, use the timeconvert command. | `>>currenttime PDT`
`>>decrypt` | Decrypts any message that was encrypted using Sigma's Heart Key. You can add ":t" at the end to force it to be raw text instead of an embed. | `>>decrypt H7U2JfWkr0zCApDPDkO`
`>>dokidoki` `>>doki` `>>dd` | Makes a random Markov chain based sentence from a random Doki Doki Literature Club character quote. You can force which character to quote by adding their name or first initial as an argument to the command. You can also force a glitch by adding ":glitch" as the last argument. | `>>dokidoki`
`>>encrypt` | Encrypts the message of your choice using Sigma's Heart Key. The message can be decrypted using the decrypt command. You can add ":t" at the end to force it to be raw text instead of an embed. | `>>encrypt I will always be here to talk to you for as long as you want.`
`>>impersonate` `>>mimic` | Tries to impersonate the mentioned user if a chain file for them exists. The more items in your chain you have, the better the output. Having a low number of items, or having items that aren't good enough, might result in Sigma not being able to generate anything. The optimal amount is 5000 items. You can check how many items you have with the chain command. | `>>impersonate @person`
`>>makehash` `>>hash` | Creates a hash using the specified hash type. These are all the hash types you can use: sha512, sha3_224, sha3_512, MD4, dsaWithSHA, ripemd160, RIPEMD160, SHA, ecdsa-with-SHA1, sha3_384, SHA512, sha1, SHA224, md4, DSA-SHA, SHA384, blake2b, dsaEncryption, SHA256, sha384, sha, DSA, shake_128, sha224, SHA1, shake_256, sha256, MD5, blake2s, md5, sha3_256, whirlpool. | `>>makehash md5 Nabzie is best tree.`
`>>markovchain` `>>chain` | Shows how many items you have have in their chain. You can view another user's chain count by mentioning them. | `>>markovchain @person`
`>>timeconvert` `>>tconv` | Converts the specified time in the specified time zone to the specified time zone. | `>>timeconvert 18:57 UTC>PST`
`>>wipechain` `>>clearchain` | Wipes your entire Markov chain, if you have one. This cannot be undone. | `>>wipechain`
[Back To Top](#module-index)

### MINIGAMES
Commands | Description | Example
----------|-------------|--------
`>>allitems` | Shows the entire item pool. You can specify a type to only show items of that type. You can also specify the page number you want to see, this goes after the item type if you give one. The item pool is sorted by item rarity. Items used in recipes are marked with an asterisk. | `>>allitems desserts`
`>>allitemstats` | Shows the statistics of the entire item pool. The number of items per type and per rarity. | `>>allitemstats`
`>>animechargame` `>>anichargame` `>>anicg` | A minigame where you guess the name of the anime character shown. You can add "hint" in the command to make it show the character's scrambled name. The Kud reward is equal to the number of characters in the shortest part of the character's name. If the hint is used, the Kud reward is split in half. | `>>animechargame hint`
`>>buyupgrade` `>>shop` | Opens Sigma's profession upgrade shop. | `>>buyupgrade`
`>>chances` | Shows a table with your item chance statistics. | `>>chances @person`
`>>coinflip` `>>cf` | Flips a coin. Nothing complex. You can try guessing the results by typing either Heads or Tails. | `>>coinflip Heads`
`>>cook` `>>make` | Uses a recipe to create an item from raw resources that you've gathered. You can see all available recipes with the recipes command. | `>>cook Shade Tea`
`>>drawcard` `>>draw` | Draws the specified number of cards. The number of cards to draw can't be above 10. The decks are persistent, so if you don't have enough cards left you'll need to make a new deck with the "newdeck" command. | `>>drawcard 3`
`>>eightball` `>>8ball` | The 8Ball has answers to ALL your questions. Come one, come all, and ask the mighty allknowing 8Ball! Provide a question at the end of the command and await the miraculous answer! | `>>eightball Will I ever be pretty?`
`>>filtersell` `>>fsell` | Sells all items that have a certain attribute. The accepted attributes are name, type, and rarity. | `>>filtersell rarity:Legendary`
`>>fish` | Cast a lure and try to catch some fish. You can fish once every 60 seconds, better not scare the fish away. | `>>fish`
`>>forage` | Go hiking and search nature for all the delicious bounties it has. Look for plants that you might want to use for cooking in the future. You can forage once every 60 seconds, hiking is really tiring. | `>>forage`
`>>hunt` | Go into the wilderness and hunt for game. You can hunt once every 60 seconds, everyone needs rest. | `>>hunt`
`>>inspect` `>>finditem` | Shows the name, value, and description of the specified item If you have this item in your inventory an Item ID will be in the footer. Also shows how many times you've caught this item. | `>>inspect Nabfischz`
`>>inventory` `>>backpack` `>>storage` `>>bag` `>>i` | Shows the current inventory of the mentioned user. If no user is mentioned, it will show the author's inventory. The inventory has 64 slots at the start but can be upgraded in the shop. You can also specify the page number you want to see. The inventory is sorted by item rarity and items used in recipes are marked with an asterisk. | `>>inventory 2 @person`
`>>inventorystats` `>>invstats` `>>bagstats` | Shows the statistics of the your inventory. The number of items per type and per rarity. You can view another person's stats by mentioning them. | `>>inventorystats @person`
`>>itemstatistics` `>>itemstats` | Shows the statistics of your item history. How much of which item you've caught, that is. It's sorted by the most caught to the least caught items. Items that you've never obtained are not shown. You can view another person's statistics by mentioning them. | `>>itemstatistics @person`
`>>joinrace` `>>jr` | Joins a race instance if any are ongoing in the current channel. | `>>joinrace`
`>>mangachargame` `>>mangochargame` `>>mancg` | A minigame where you guess the name of the manga character shown. You can add "hint" in the command to make it show the character's scrambled name. The Kud reward is equal to the number of characters in the shortest part of the character's name. If the hint is used, the Kud reward is split in half. | `>>mangachargame hint`
`>>mathgame` `>>mg` | A mathematics minigame. You are given a problem to solve. Numbers are rounded to 2 decimals. You can also specify how hard you want the problem to be on a scale of 1 to 9. The default difficulty is 3. The time and Kud reward scale with the difficulty and number of hard operators. | `>>mathgame 4`
`>>newdeck` | Rebuilds your deck of cards. | `>>newdeck`
`>>race` | Creates a race in the current text channel. To join the race use the joinrace command. A race needs at least 2 people to start, and has a maximum of 10 participants. You can specify a required buy-in to join the race. The Kud reward is equal to the buy-in mutiplied by the number of participants.. | `>>race 200`
`>>recipes` `>>cookbook` | Lists all recipes available for making. The recipe list is limited to 10 items per page. You can specify the page number you want to see. | `>>recipes`
`>>roll` `>>dice` | Rolls a number from 0 to the one you provided. You can also roll dice as in the example above. Following the format [Number of Dice]d[MaxNumber] +[Bonus]. The bonus is individually added as a flat value to all of the rolled dice. | `>>roll 5d10 +2`
`>>roulette` `>>roul` | Spin the roulette wheel and maybe you'll win. The default bet is 10 Kud but you can specify any amount you want. The syntax of playing is the bet amount first, it can be ommitted however, and then the roulette spot choice in the form of [selector]:[value]. Accepted specifiers are color:black or number:15, column:2, dozen:1, half:1, and type:odd. Good luck. | `>>roulette 150 color:red`
`>>rps` `>>rockpaperscissors` | Play Rock-Paper-Scissors with Sigma. No cheating, we swear. She just doesn't like you. | `>>rps s`
`>>sell` | Sells an item from your inventory. Input all instead of the item name to sell your entire inventory. | `>>sell Copula`
`>>sequencegame` `>>sequence` `>>sqcg` | Starts a sequence guessing game. 4 symbols will randomly be chosen and you have to guess them in 6 tries or fewer. When a symbol is in the corret position the diamond will be blue. If it is in the sequence but incorrect position, it will be yellow. If the symbol is not in the sequence, it will be red. The symbols can repeat, the Kud award is 50. | `>>sequencegame`
`>>slots` | Spin the slot machine, maybe you win, maybe you don't. Who knows? The default bet is 10 Kud but you can specify any amount you want. The rewards are based on how many of the same icon you get in the middle row. Rewards are different for each icon. The slots can be spun only once every 60 seconds. | `>>slots 52`
`>>trivia` `>>triv` `>>t` | A trivia minigame. You are given a question and have to input the number of your answer. Guess correctly and you win 10-50 Kud (base), depending on the difficulty. You have 20 seconds to answer the question. Consecutive correct answers give you a streak and the streak increases the Kud gained for each correct answers. Timing out or giving an incorrect answer resets the streak. You can choose the category and difficulty of the question like in the usage example, but choosing either will disable the streak. | `>>trivia`
`>>unscramble` `>>usg` | A minigame where you guess the scrambled word. You have 30 seconds to guess the word shown. The Kud reward is equal to the number of letters in the word. | `>>unscramble`
`>>upgrades` | Shows your current upgrade levels. You can view another user's upgrades by mentioning them. | `>>upgrades @person`
`>>viewrecipe` `>>recipe` `>>vrec` | Shows details on the specified recipe, such as the ingredients required, value of the item, and its description. | `>>viewrecipe Shade Tea`
`>>vnchargame` `>>vncg` | A minigame where you guess the name of the visual novel character shown. You can add "hint" in the command to make it show the character's scrambled name. The Kud reward is equal to the number of characters in the shortest part of the character's name. If the hint is used, the Kud reward is split in half. | `>>vnchargame`
[Back To Top](#module-index)

### MISCELLANEOUS
Commands | Description | Example
----------|-------------|--------
`>>afk` | Marks you as afk. Whenever someone mentions you they will be notified that you are afk. When you send a message your afk status will be removed. This automatic removal ignores messages that start with the command prefix. | `>>afk Sleeping or eating, probably both!`
`>>choose` | The bot will select a thing from the inputed list. Separate list items with a semicolon and space. | `>>choose Sleep; Eat; Code; Lewd Stuff`
`>>echo` `>>say` | Makes Sigma repeat what you entered, simple enough. | `>>echo Beep, bop-boop!`
`>>edgecalculator` `>>edgecalc` | Calculates how edgy the targeted person is. If no user is tagged, the target will be the one who uses the command. | `>>edgecalculator @person`
`>>embedecho` `>>esay` `>>eecho` | Just like echo, but the message is an embed object that has you as the author, your color, and the time it was executed. | `>>embedecho Beep, bop-boop!`
`>>endraffle` `>>endraf` | Prematurely ends a raffle. This command is only usable by the author of the raffle. To end a raffle use the raffle's ID that can be found in its footer. This command has no response aside from a reaction to your message. green check mark - redraw successful magnifying glass - raffle not found no entry sign    - you aren't the raffle creator exclamation mark - no arguments given | `>>endraffle 1abc9c`
`>>httpstatus` `>>http` | Shows information about a HTTP response status code. Add "cat" or "dog" as the last argument for an added bonus. | `>>httpstatus 404`
`>>listraffles` `>>listraf` `>>lraf` | Lists all your ongoing raffles and their information, such as when they end and in what channel. | `>>listraffles`
`>>myreminders` `>>reminders` `>>rms` | Shows a list of the reminders that you have created, the location where they are set to execute in, and when they will be executed. If you add "here" to the end of the command, it will only show reminders made in the current channel. | `>>myreminders here`
`>>poll` | Creates a poll with the items from the inputted list. Separate list items with a semicolon and a space. | `>>poll Want to eat?; Yes; No; Hand me the cheese!`
`>>quote` | Quotes a message from its given ID. | `>>quote 381449702589202432`
`>>raffle` `>>giveaway` | Starts a raffle with a given timer and title. Entering the raffle works by reacting to Sigma's embed message with an automatically given reaction. When the timer runs out a message will appear in the channel the raffle was made in and the creator of the raffle and the winner will be tagged. | `>>raffle 48:30:59 50,000 Kud`
`>>randombetween` `>>ranin` | Outputs a random number between two inputted numbers. | `>>randombetween 59 974`
`>>redrawraffle` `>>redraw` | Redraws a raffle in case that's ever needed. This command is only usable by the author of the raffle. To redraw a raffle use the raffle's ID that can be found in its footer. This command has no response aside from a reaction to your message. A raffle needs to be marked as ended before it can be redrawn. green check mark - redraw successful magnifying glass - raffle not found no entry sign    - you aren't the raffle creator exclamation mark - no arguments given | `>>redrawraffle 1abc9c`
`>>reminderinfo` `>>reminder` `>>rminfo` `>>rmi` | Shows information about your reminder with the specified ID, such as when it will execute and where. | `>>reminderinfo f93f`
`>>remindme` `>>setreminder` `>>remind` `>>alarm` `>>rmme` | Sets a timer that will mention the author when it's done. The time format is H:M:S, but is not limited to the constraints of their types, meaning you can type "200:5000:999999" if you wish. Reminders are limited to 90 days, and you are limited to 15 reminders. | `>>remindme 1:03:15 LEEEEROOOOY JEEEEEENKIIIIINS!`
`>>removereminder` `>>delreminder` `>>unremind` `>>delrm` | Deletes a reminder of yours with the specified ID. | `>>removereminder 1a9e`
`>>shadowpoll` | Makes a private shadow poll. The users that vote on the shadow poll can only be viewed by its creator. Additional commands can be used to set an expiration timer, the visibility of the poll's current vote count and percentages, and who is allowed to vote on the poll. | `>>shadowpoll Ban Nuggetlord?; Yes; Yes; Yes; No; Soft`
`>>shadowpollclose` `>>spclose` | Closes/deactivated a shadow poll. Closed polls cannot be voted on and cannot be viewed unless they are set to be visible. | `>>shadowpollclose 1bca22`
`>>shadowpolldelete` `>>spdelete` `>>spdel` | Permanently deletes the specified shadow poll. | `>>shadowpolldelete 1bca22`
`>>shadowpollexpires` `>>spexpiration` `>>spexpires` `>>spexpire` | Sets a shadow poll to automatically close after the specified time elapses. The time to close is counted from the command execution, not the initial creation of the poll. When the poll expires the author will be notified of the expiration. Only the poll's creator can edit its expiration time. | `>>shadowpollexpires 1bca22 48:30:59`
`>>shadowpollinvisible` `>>spinvisible` `>>spinvis` | Reverts a shadow poll back to invisible. Making its statistics only accessible to the author. All shadow polls are invisible by default. | `>>shadowpollinvisible 1bca22`
`>>shadowpolllist` `>>splist` | Lists all shadow polls that you have created. You can also list only polls that are active and created in the current server or channel by adding a "server" or "channel" argument to the command. Polls that have expired or that are closed are marked with an exclamation mark. | `>>shadowpolllist channel`
`>>shadowpollopen` `>>spopen` | Opens a previously closed shadow poll. If the poll has an expiration timer, it will be wiped. | `>>shadowpollopen 1bca22`
`>>shadowpollpermit` `>>sppermit` `>>spperm` | Permits a role, channel, or user to vote on the specified shadow poll. If no permission settings are set, anybody can vote on the poll. If any permissions are set, only items permitted can vote on the poll. Tag a user to permit a user, tag a channel to permit a channel, or type the name of a role to permit a role. | `>>shadowpollpermit 1bca22 #council`
`>>shadowpollstats` `>>spstats` | Shows statistics for the specified shadow poll. Total count of votes and votes for each option as well as percentages. | `>>shadowpollstats 1bca22`
`>>shadowpollunpermit` `>>spunpermit` `>>spunperm` | Unpermits a previously permitted item from voting on the specified shadow poll. For more information check the description of the shadowpollpermit command. | `>>shadowpollunpermit 1bca22 Disowned`
`>>shadowpollview` `>>spview` | Displays a shadow poll's question and possible options. If the poll is not active and not finished, information will not be displayed. If you are the one who created the poll, the information will be displayed regardless. | `>>shadowpollview 1bca22`
`>>shadowpollvisible` `>>spvisible` `>>spvis` | Marks a poll as visible. If a poll is visible anybody can see its statistics, such as its total vote count and how many votes each choice received. | `>>shadowpollvisible 1bca22`
`>>shadowpollvote` `>>spvote` | Votes on a shadow poll. Choosing multiple options is not allowed. Re-using the command will result in your vote being changed. Both the poll ID and your choice number are required. | `>>shadowpollvote 1bca22 2`
`>>shadowpollvoters` `>>spvoters` | Shows all the users that voted on the specified shadow poll and what they voted for. This command can only be used by the author of the poll. | `>>shadowpollvoters 1bca22`
`>>shadowpollwipe` `>>spwipe` | Completely resets the specified shadow poll's statistics. Deleting all the data about who voted for what option. | `>>shadowpollwipe 1bca22`
`>>temproom` `>>tempvc` | Makes a temporary voice channel that you can fully manage. Once everyone leaves the channel (not including bots) it's destroyed. The temp voice channels are checked by their prefix ([Σ]), if this is edited out, the channel will not be destroyed when emptied. | `>>temproom Orgy For One`
[Back To Top](#module-index)

### MODERATION
Commands | Description | Example
----------|-------------|--------
`>>activatewarning` `>>activatewarn` `>>actwarn` | Reactivates the mentioned user's warning. Warns are marked as inactive when removed. Both the user mention and the warning ID are needed for the command. The specified warning must be marked inactive before it can be reactivated. Only the server owner can use this command. | `>>activatewarning @person 1abc`
`>>ban` | Bans a user from the server. This will also remove all messages from that user in the last 24h. The user can only be specified via a mention tag. This is to preserve compatibility with logging and audit logs. You can specify a duration by adding "--time=HH:MM:SS" as the last argument. The user will be automatically unbanned after the duration elapses. This command requires the Ban permission. | `>>ban @person Way, WAY too spicy for us...`
`>>hardmute` `>>hmute` | Hard-mutes the mentioned user. Users who are hard-muted are disallowed from typing to any channel. There is no message deletion, this is a permission based mute. Due to adding a user override to every editable channel, this can spam audit logs. You can specify a duration by adding "--time=HH:MM:SS" as the last argument. The user will be automatically unbanned after the duration elapses. This command requires the Manage Channels permission. | `>>hardmute @person For talking about the fight club.`
`>>hardunmute` `>>hunmute` | Unmutes a hard-muted person, allowing them to send messages again. This command requires the Manage Channels permission. | `>>hardunmute @person`
`>>issuewarning` `>>warn` | Issues a warning to a user with the specified reason. The warning reason is not required. When the user is warned they will be sent a direct message about it. Each warning has a unique ID that you can user to view with the viewwarning command. This command requires the Manage Messages permission. | `>>issuewarning @person Took too long in the bathroom.`
`>>kick` | Kicks a user from the server. The user can only be mentioned by a mention tag. This is to preserve compatibility with logging and audit logs. This command requires the Kick permission. | `>>kick @person Couldn't handle the spice.`
`>>listinactivewarnings` `>>inacwarnings` `>>inacwarns` | Lists all inactive warnings issued to the mentioned user. The list is compact and shows only each warning's ID, issuer, and issue date. The list is paginated, each page has up to 5 warnings. You can also specify the page number you want to see as the last argument. Only the server owner can use this command. | `>>listinactivewarnings @person`
`>>listwarnings` `>>warnings` `>>warns` | Lists all active warnings issued to the mentioned user. The list is compact and shows only each warning's ID, issuer, and issue date. The list is paginated, each page has up to 5 warnings. You can also specify the page number you want to see as the last argument. If you have the Manage Messages permissions you can view anyone's warnings, otherwise you can only view your own warnings. | `>>listwarnings @person`
`>>massmove` `>>mmove` | Moves all members from one voice channel to another. Both channels require an identifier;either its name or its ID. The channel identifiers channel should be separated with a semicolon and a space "; ". This command requires the Manage Server permission. | `>>massmove 1234567890; New Voice`
`>>purge` `>>prune` | Deletes any messages posted by the mentioned user within the last X messages. If a user is not provided, it will prune the last X messages regardless of poster. If a number is not provided it will prune all messages posted by the mentioned user within the last 100 messages. If neither number nor user is provided, it will prune Sigma's messages within the last 100 messages. If you add "attachments" to the command arguments it will only purge messages that have attachments. If you add "emotes" to the command arguments it will only purge messages that are just emotes. If you add "content:something you want gone" to the command arguments it will only delete messages that have the specified content after "content:" in them, which can be a word or a sentence. Due to content catching everything after the ":" in it, it's suggested to be the last argument in the command. This command requires the Manage Messages permission. | `>>purge X @person`
`>>removeinactivewarning` `>>delinacwarning` `>>delinacwarn` | Permanently deletes the mentioned user's warning. Both the user mention and the warning ID are needed for the command. The specified warning must be marked as inactive. This cannot be undone. Only the server owner can use this command. | `>>removeinactivewarning @person 1abc`
`>>removewarning` `>>unwarn` | Marks the specified user's warning as inactve. Inactive warnings won't appear on a user's list of warnings. Both the user mention and the warning ID are needed for the command. This command requires the Manage Messages permission. | `>>removewarning @person 1abc`
`>>softban` `>>sb` | Soft-Ban a user from the server. This bans the user and then immediately unbans them. Useful if you want to purge all messages from that user in the last 24h. The user can only be mentioned by a mention tag. This is to preserve compatibility with logging and audit logs. This command requires the Ban permission. | `>>softban @person Some spice needed de-spicing.`
`>>textmute` `>>tmute` | Disallows the user from typing. Well technically, it will make Sigma auto delete any message they send. You can add a reason after the user mention if desired. Users with the Those with the Administrator permission are not affected. You can specify a duration by adding "--time=HH:MM:SS" as the last argument. The user will be automatically unmuted after the duration elapses. This command requires the Manage Messages permission. | `>>textmute @person Was too spicy!`
`>>textunmute` `>>tunmute` | Removes the mentioned person from the list of muted users, making Sigma no longer delete their messages. This command requires the Manage Messages permission. | `>>textunmute @person`
`>>unban` | Unbans a banned user matching specified username. This command requires the Ban permission. | `>>unban Chicken Shluggets`
`>>viewinactivewarning` `>>viewinacwarning` `>>inacwarning` | Shows detailed information for the mentioned user's warning. Both the user mention and the warning ID are needed for the command. The specified warning must be marked as inactive. Only the server owner can use this command. | `>>viewinactivewarning @person 1abc`
`>>viewwarning` `>>warninginfo` `>>warning` | Shows detailed information for the specified user's warning. Both the user mention and the warning ID are needed for the command. This command requires the Manage Messages permission. | `>>viewwarning @person 1abc`
`>>voicekick` `>>vkick` | Kicks a user from voice chat. It completely disconnects the mentioned user by creating a new voice channel, moving them to it, then deleting that voice channel. This command requires the Kick permission. | `>>voicekick @person`
[Back To Top](#module-index)

### MUSIC
Commands | Description | Example
----------|-------------|--------
`>>disconnect` `>>stop` | Stops the music, disconnects Sigma from the current voice channel, and purges the music queue. | `>>disconnect`
`>>lyrics` `>>lyr` | Searches for the lyrics of the specified song. Requires both the song and artist, separated by a dash "-". If no arguments are given, it will try to get the currently playing song's lyrics. | `>>lyrics Imagine Dragons - Radioactive`
`>>nowplaying` `>>currentsong` `>>playing` `>>np` | Shows information on the currently playing song. | `>>nowplaying`
`>>pause` | Pauses the music player. | `>>pause`
`>>play` `>>start` | Starts playing the music queue. | `>>play`
`>>queue` `>>add` | Queues up a song to play from YouTube. Either from a direct URL or text search. Playlists are supported but take a long time to process. | `>>queue Kaskade Disarm You Illenium Remix`
`>>repeat` | Toggles if the current queue should be repeated. Whenever a song is played, it's re-added to the end of the queue. | `>>repeat`
`>>resume` | Resumes the music player. | `>>resume`
`>>shuffle` | Randomizes the current song queue. | `>>shuffle`
`>>skip` `>>next` | Skips the currently playing song. | `>>skip`
`>>summon` `>>move` | If Sigma isn't connected to any channel, she will connect to yours. If it is connected, it will move to you. | `>>summon`
`>>unqueue` `>>remove` | Removes a song from the queue. Minimum number is 1 and the maximum is however many items the queue has. | `>>unqueue 5`
[Back To Top](#module-index)

### NIHONGO
Commands | Description | Example
----------|-------------|--------
`>>jisho` | Searches Jisho, which is the Japanese language dictionary, for the specified term. Returns various types of information regarding the term. | `>>jisho Kawaii`
`>>kanji` | Searches Jisho, which is the Japanese language dictionary, for specified kanji. Returns stroke count, stroke order, parts, variants, meanings, and readings. | `>>kanji 夢`
`>>wanikani` `>>wk` | Shows the mentioned user's WaniKani statistics. If no person is mentioned, it will show the author's stats. This requires the target to have a WaniKani API key stored with the wanikanisave command. | `>>wanikani @person`
`>>wanikanisave` `>>wksave` | Saves your WaniKani API key in the database so the wanikani command can be used. | `>>wanikanisave 123456798`
[Back To Top](#module-index)

### NSFW
Commands | Description | Example
----------|-------------|--------
`>>boobs` `>>tits` | Outputs a random NSFW image focusing on the breasts of the model. | `>>boobs`
`>>butts` `>>ass` | Outputs a random NSFW image focusing on the butt of the model. | `>>butts`
`>>e621` | Searches E621 for the specified tag. If no tag is given, the keyword "nude" will be used. Separate different tags with a space and replace spaces within a single tag with underscores "_". | `>>e621 knot`
`>>gelbooru` `>>gelb` | Searches Gelbooru for the specified tag. If no tag is given, the keyword "nude" will be used Separate different tags with a space and replace spaces within a single tag with underscores "_". | `>>gelbooru ovum`
`>>keyvis` | Returns a Key Visual Arts VN CG. It picks a random VN and a random CG from that VN. You can specify the VN you want the CG to be from. "kud"    - Kud Wafter "air"    - Air "kanon"  - Kanon "little" - Little Busters "clan"   - Clannad "plan"   - Planetarian "rewr"   - Rewrite "harv"   - Rewrite Harvest Festa This command is NSFW due to some CGs being explicit.  | `>>keyvis kud`
`>>konachan` `>>kchan` | Searches Sigmaachan for the specified tag. If no tag is given, the keyword "nude" will be used. Separate different tags with a space and replace spaces within a single tag with underscores "_". | `>>konachan thighhighs`
`>>rule34` `>>r34` | Searches Rule34 for the specified tag. If no tag is given, the keyword "nude" will be used Separate different tags with a space and replace spaces within a single tag with underscores "_". | `>>rule34 switch`
`>>xbooru` `>>xb` | Searches Xbooru for the specified tag. If no tag is given, the keyword "nude" will be used. Separate different tags with a space and replace spaces within a single tag with underscores "_". | `>>xbooru ovum`
`>>yandere` `>>yre` | Searches yandere for the specified tag. If no tag is given, the keyword "nude" will be used. Separate different tags with a space and replace spaces within a single tag with underscores "_". | `>>yandere naked_apron`
[Back To Top](#module-index)

### OSU
Commands | Description | Example
----------|-------------|--------
`>>osu` | Generates a signature image with the specified user's stats for osu!. | `>>osu AXAz0r`
[Back To Top](#module-index)

### OVERWATCH
Commands | Description | Example
----------|-------------|--------
`>>overwatch` `>>owstats` `>>ow` | Outputs the Overwatch statistics for the specified player from the specified region. Do note that the battletag is case sensitive, Aurora#22978 is not the same as aurora#22978. | `>>overwatch EU Aurora#22978`
[Back To Top](#module-index)

### PATH OF EXILE
Commands | Description | Example
----------|-------------|--------
`>>poeactive` `>>poeasg` | Shows information about the specified Path of Exile Active Skill Gem. | `>>poeactive Cold Snap`
`>>poebody` | Shows information about the specified Path of Exile Body armor piece. | `>>poebody Arena Plate`
`>>poeboots` | Shows information about the specified Path of Exile boots. | `>>poeboots Arena Plate`
`>>poegloves` | Shows information about the specified Path of Exile gloves. | `>>poegloves Arena Plate`
`>>poehelmet` | Shows information about the specified Path of Exile helmet. | `>>poehelmet Arena Plate`
`>>poeshield` | Shows information about the specified Path of Exile shield. | `>>poeshield Arena Plate`
`>>poesupport` `>>poessg` | Shows information about the specified Path of Exile Support Skill Gem. | `>>poesupport Iron Will`
[Back To Top](#module-index)

### PERMISSIONS
Commands | Description | Example
----------|-------------|--------
`>>disablecommand` `>>commandoff` `>>cmdoff` `>>dcmd` | Disables a command on the server. Disabled commands cannot be used unless overwritten by one of the permit commands. Those with the Administrator permission are not affected. This command requires the Manage Server permission. | `>>disablecommand nyaa`
`>>disabledcommands` `>>commandsoff` `>>cmdsoff` `>>dcmds` | Shows a list of commands that are disabled on the server. Commands that are disabled, but overridden in any way, will have an asterisk. The list is paginated, each page has up to 50 commands. | `>>disabledcommands`
`>>disabledmodules` `>>modulesoff` `>>mdlsoff` `>>dmdls` | Shows a list of modules that are disabled on the server. Modules that are disabled, but overridden in any way, will have an asterisk. The list is paginated, each page has up to 50 modules. | `>>disabledmodules`
`>>disablemodule` `>>moduleoff` `>>mdloff` `>>dmdl` | Disables an entire module on the server. Commands within a disabled modules cannot be used unless the module or command is overwritten by one of the permit commands. Those with the Administrator permission are not affected. This command requires the Manage Server permission. | `>>disablemodule fun`
`>>enablecommand` `>>commandon` `>>cmdon` | Enables a previously disabled command. You can use a command's alias instead of its full name if desired. This command requires the Manage Server permission. | `>>enablecommand kitsune`
`>>enablemodule` `>>moduleon` `>>mdlon` `>>emdl` | Enables a previously disabled module. This command requires the Manage Server permission. | `>>enablemodule minigames`
`>>permitchannel` `>>permitchannels` `>>permitcs` `>>permitc` `>>permchs` `>>permch` `>>pchs` `>>pch` | Adds an override for the mentioned channels for specified command/module. Use the syntax {c|m}:{name} to specify if it's a command or a module, and its name. Multiple channels can be tagged. This command requires the Manage Server permission. This command requires the Manage Server permission. | `>>permitchannel m:fun #channel`
`>>permitrole` `>>permitr` `>>permrl` `>>prl` | Adds an override for the specified role for specified command/module. Use the syntax {c|m}:{name} to specify if it's a command or a module, and its name. | `>>permitrole c:csshumor Wizards`
`>>permittedchannels` `>>permedc` | Lists all channel overrides for the specified command or module. Use the syntax {c|m}:{name} to specify if it's a command or a module, and its name. The list is paginated, each page has up to 50 channels. | `>>permittedchannels m:fun`
`>>permittedroles` `>>permedr` | Lists all role overrides for the specified command or module. Use the syntax {c|m}:{name} to specify if it's a command or a module, and its name. The list is paginated, each page has up to 50 channels. | `>>permittedroles c:dab`
`>>permittedusers` `>>permedusrs` `>>permedu` | Lists all user overrides for the specified command or module. Use the syntax {c|m}:{name} to specify if it's a command or a module, and its name. The list is paginated, each page has up to 50 users. | `>>permittedusers c:joke`
`>>permituser` `>>permitusers` `>>permitus` `>>permusrs` `>>permitu` `>>permusr` `>>pusrs` `>>pusr` | Adds an override for the mentioned users for specified command/module. Use the syntax {c|m}:{name} to specify if it's a command or a module, and its name. Multiple users can be tagged. This command requires the Manage Server permission. This command requires the Manage Server permission. | `>>permituser c:pun @person`
`>>unpermitchannel` `>>unpermitchannels` `>>unpermitcs` `>>unpermitc` `>>unpermchs` `>>unpermch` `>>upchs` `>>upch` | Removes an override for the mentioned channels for specified command/module. The specified command/module needs to have been previously permitted for this to do anything. Unpermitting a command/module that was not previously permitted will do absolutely nothing. Use the syntax {c|m}:{name} to specify if it's a command or a module, and its name. Multiple channels can be tagged. This command requires the Manage Server permission. | `>>unpermitchannel m:fun #channel`
`>>unpermitrole` `>>uprl` `>>unpermrl` `>>unpermitrl` | Removes an override for the specified role for specified command/module. The specified command/module needs to have been previously permitted for this to do anything. Unpermitting a command/module that was not previously permitted will do absolutely nothing. Use the syntax {c|m}:{name} to specify if it's a command or a module, and its name. This command requires the Manage Server permission. | `>>unpermitrole m:minigames Gamblers`
`>>unpermituser` `>>unpermitusers` `>>unpermitus` `>>unpermusrs` `>>unpermitu` `>>unpermusr` `>>upusrs` `>>upusr` | Removes an override for the mentioned users for specified command/module. The specified command/module needs to have been previously permitted for this to do anything. Unpermitting a command/module that was not previously permitted will do absolutely nothing. Use the syntax {c|m}:{name} to specify if it's a command or a module, and its name. Multiple users can be tagged. This command requires the Manage Server permission. This command requires the Manage Server permission. | `>>unpermituser m:fun @person`
[Back To Top](#module-index)

### ROLES
Commands | Description | Example
----------|-------------|--------
`>>addselfrole` `>>addrank` `>>asr` | Sets a role as self assignable. Roles that are self assignable can be manually assign by anyone. To assign a self assignbale role to yourself, use the togglerole command. This command requires the Manage Roles permission. | `>>addselfrole Cheese Lover`
`>>autorole` `>>autorank` | Sets which role should be given to members upon joing the server. The role must be below Sigma's highest role. If you want to disable the autorole, input "disable" as the role name. This command requires the Manage Server permission. | `>>autorole Newcomer`
`>>autoroletimeout` `>>arltimeout` `>>arlt` | Sets the number of seconds Sigma should wait before assigning the set auto-role. To disable the timeout, input 0 as the timeout. This command requires the Manage Server permission. | `>>autoroletimeout 600`
`>>bindemoterole` `>>berl` | Binds a role to an emote role group. Emote role groups are limited to 10 roles per group. This command requires the Manage Server permission. | `>>bindemoterole 5a8e3 King Killers`
`>>bindinvite` `>>bindinvs` `>>binvite` `>>binv` | Binds an invite to a role. When a member joins the server using that invite, the specified role will be given to them. This command requires the Create Instant Invites permission. | `>>bindinvite aEUCHwX Cheese Lovers`
`>>bindrole` `>>brl` | Binds a role to a role group. Role groups are limited to 32 roles per group. This command requires the Manage Server permission. | `>>bindrole 5a8e3 King Killers`
`>>boundinvites` `>>boundinvs` `>>binvites` `>>binvs` | Lists all invites that are bound and what they are bound to. This command requires the Create Instant Invites permission. | `>>boundinvites`
`>>colorme` `>>clrme` `>>cme` | If the current guild has color roles enabled, you can assign one to yourself with this command. For more information about how this works, use the help command on "colorroles". Any other color roles made via this command will be removed from you prior to adding the new one. | `>>colorme #1abc9c`
`>>deleteemoterolegroup` `>>derg` | Deletes an emote role group. This cannot be undone. Emote role groups are created with the makeemoterolegroup command. This command requires the Manage Server permission. | `>>deleteemoterolegroup 5a8e3`
`>>deleterolegroup` `>>drg` `>>rrg` | Deletes a role group. This cannot be undone. Role groups are created with the makerolegroup command. This command requires the Manage Server permission. | `>>deleterolegroup 5a8e3`
`>>delselfrole` `>>delrank` `>>rsr` `>>dsr` | This command requires the Manage Roles permission. | `>>delselfrole Meat Lover`
`>>giverole` `>>giverank` `>>grole` `>>grank` | Gives the specified role to the mentioned user. The role must be below Sigma's highest role. This command requires the Manage Roles permission. | `>>giverole @person Grandma`
`>>listemoterolegroups` `>>lerg` | Lists all emote role groups on the server. The list is paginated, each page has up to 10 items. You can specify the page number you want to see. To view an emote role group's details, such as the populace and roles that are bound to that group, use the viewemoterolegroup command. | `>>listemoterolegroups 2`
`>>listrolegroups` `>>lrg` | Lists all role groups on the server. The list is paginated, each page has up to 10 items. You can specify the page number you want to see. To view a role group's details, such as the populace and roles that are bound to that group, use the viewrolegroup command. | `>>listrolegroups 2`
`>>listselfroles` `>>listranks` `>>listroles` `>>ranks` `>>roles` `>>lsrl` | Lists all self assignable roles on the server. | `>>listselfroles`
`>>makeemoterolegroup` `>>merg` | Creates an emote role group for binding roles to. Emote roles need to be bound to groups due to messages havinga limited number of reactions that can be added. An upside is this allows you to place multiple emote toggle messages in different places with slight alterations. This command requires the Manage Server permission. | `>>makeemoterolegroup`
`>>makeemotetoggles` `>>metg` | Makes the core message that cotains the emotes for the emote role togglers. Specify the group you want to a message for by ID. Youcan also specify the channel you want it to go. If no channel is specified, the toggler will be created in the current channel. The toggler message contains instruction on how to use the toggles. You can add "nodesc" to the end of the command if you don't want the toggle instructions to be displayed in the toggler message. This command requires the Manage Server permission. | `>>makeemotetoggles 5a8e3 #channel`
`>>makerolegroup` `>>mrg` `>>crg` | Creates a role group for binding a role to. Role groups are limited to 32 roles per group. This command requires the Manage Server permission. | `>>makerolegroup`
`>>pruneroles` `>>proles` | Removes all empty roles from the server that are below Sigma. This command requires the Manage Roles permission. | `>>pruneroles`
`>>removerole` `>>removerank` `>>rrole` `>>rrank` | Removes the specified role from the mentioned user. The role must be below Sigma's highest role. This command requires the Manage Roles permission. | `>>removerole @person Wangly`
`>>syncinvites` `>>syncinvs` `>>sinvs` | Forces an update of the invite cache for your server. For use if you have suspicions that the bound role counters are out of sync. | `>>syncinvites`
`>>togglerole` `>>togglerank` `>>rank` `>>trl` | Toggles a self assignable role. If you don't have the role, it will be given to you. If you do have the role, it will be removed from you. | `>>togglerole Overlord`
`>>toggleselfrole` `>>tsr` | The addselfrole and delselfrole in one. It toggles the self-assignability of a role. This command requires the Manage Roles permission. | `>>toggleselfrole Meat Lover`
`>>unbindemoterole` `>>uberl` | Unbinds a role from an emote role group. This command requires the Manage Server permission. | `>>unbindemoterole 5a8e3 Serpent Squires`
`>>unbindinvite` `>>unbinvite` `>>unbindinv` `>>unbinv` | Unbinds a previously bound invite from its bound role. If the invite with that ID no longer exists on your server, add ":f" to the end to force remove it. Please note that when you force the removal of an invite that it is case sensitive. This command requires the Create Instant Invites permission. | `>>unbindinvite aEUCHwX`
`>>unbindrole` `>>ubrl` | Unbind a role from a role group. This command requires the Manage Server permission. | `>>unbindrole 5a8e3 Serpent Squires`
`>>viewemoterolegroup` `>>verg` | Shows details on the specified emote role group, such as the roles that are in the group and the total population of the group's roles. | `>>viewemoterolegroup 5a8e3`
`>>viewrolegroup` `>>vrg` | Shows details on the specified role group, such as roles that are in the group and the total population of the group roles. | `>>viewrolegroup 5a8e3`
[Back To Top](#module-index)

### SEARCHES
Commands | Description | Example
----------|-------------|--------
`>>anime` `>>animu` `>>kitsuanime` | Searches Kitsu.io for the specified anime. The outputed results will be information like the number of episodes, user rating, air time, plot summary, and poster image. | `>>anime Plastic Memories`
`>>antonyms` `>>antonym` `>>ant` | Looks up words that have the opposite meaning of the specified term. | `>>antonyms late`
`>>busplus` | Returns the bus departure times from both terminus locations for the specified line number. It will display the departure times for the current, previous, and next hour. This is only for the Belgrade BusPlus transit tracking system. | `>>busplus 18`
`>>cryptocurrency` `>>cryptocur` `>>crypcur` `>>ecoin` | Shows the statistics for the specified crypto currency. Stats include the current market cap, price, supply, volume, and change. | `>>cryptocurrency ethereum`
`>>deezer` `>>music` `>>findsong` | Searches Deezer for infomation on the specified song. The output will include a song preview link. | `>>deezer Highway to Hell`
`>>describe` `>>desc` | Looks up words that are often used to describe nouns or are often used by the adjective. Specify the mode in the first argument. adjectives, adjective, adj, a: To look up nouns that are often described by an adjective. nouns, noun, n: To look up adjectives that are often used to describe a noun. | `>>describe noun ocean`
`>>dictionary` `>>dict` `>>definition` `>>define` `>>def` | Searches the Oxford dictionary for the definition of your input. | `>>dictionary cork`
`>>foodrecipe` `>>frec` `>>food` | Searches for a dish, or dishes that use specified ingredients, and outputs one that might be a good match for your search query. | `>>foodrecipe Chicken in Curry Sauce`
`>>giphy` `>>gif` | Searches Giphy with the specified tag and returns a random result. The tag can be multiple words. | `>>giphy kittens`
`>>homophones` `>>homophone` | Looks up words that sound like the specified term. | `>>homophones coarse`
`>>imdb` `>>movie` | Searches the Internet Movie Database for your input. Gives you the poster, release year, and who stars in the movie, as well as a link to the page of the movie. | `>>imdb Blade Runner`
`>>manga` `>>mango` `>>kitsumanga` | Searches Kitsu.io for the specified manga. The outputed results will be information like the number of chapters, user rating, plot summary, and poster image. | `>>manga A Silent Voice`
`>>mapsearch` `>>maps` `>>map` | Searches Google Maps for the specified location. If specific details aren't found about the location, it will return in a broad search. | `>>mapsearch Belgrade`
`>>reddit` | Enter a subreddit and it will show a random post from the current top posts in hot. You can specify what filter to search the subreddit with as an argument after the subreddit name. The accepted arguments are TopHot, RandomHot, TopNew, RandomNew, TopTop, and RandomTop. Random arguments choose randomly from a list of the first 100 entries. | `>>reddit ProgrammerHumor`
`>>rhymes` `>>rhyme` | Looks up words that rhymes with the specified term. | `>>rhymes forgetful`
`>>safebooru` `>>safe` | Returns a random image from the safebooru image repository. If no tag is given, the keyword "cute" will be used. Separate different tags with a space and replace spaces within a single tag with underscores "_". | `>>safebooru kawaii`
`>>soundslike` `>>soundlike` | Looks up words that sound similar to the specified term. | `>>soundslike elefint`
`>>spelledlike` `>>spelllike` `>>spellike` `>>spellcheck` | Looks up words that are spelled similarly to the specified term. Supports the following wildcards: ? - one character * - one or many characters  | `>>spelledlike coneticut`
`>>synonyms` `>>synonym` `>>syn` | Looks up words that have exactly or nearly the same meaning as the specified term. | `>>synonyms ocean`
`>>urbandictionary` `>>urbandict` `>>urban` `>>ud` | Looks up the definition for a word or term in the Urban Dictionary. It is strongly suggested to take these with a grain of salt. | `>>urbandictionary dictionary`
`>>weather` `>>we` | Shows meteorological information about the specified location. You can add a unit argument at the end of the lookup: auto: automatically select units based on geographic location, ca: same as si, except that wind speed is in kilometers per hour, uk2: same as si, except that nearest storm distance and visibility are in miles and wind speed is in miles per hour, s: Imperial units (the default), si: SI units. If no unit is selected, it defaults to auto. | `>>weather Belgrade unit:si`
`>>wikipedia` `>>wiki` | Returns the summary of the specified wikipedia page. If a search is too general, an error will be returned. | `>>wikipedia Thread (Computing)`
`>>youtube` `>>yt` | A simple YouTube search. Outputs the resulting video's information and URL. You can add "-text" at the end of your search to make it a normal URL to the video instead of an embed with information. | `>>youtube Game Grumps`
[Back To Top](#module-index)

### SETTINGS
Commands | Description | Example
----------|-------------|--------
`>>addcommand` `>>addcmd` | Adds a custom command to the server. Whenever the specified trigger word is used with a command prefix, the specified response will be returned. This command requires the Manage Server permission. Custom commands can have special dynamic arguments in them. {author_name}     - Message author's name. {author_nick}     - Message author's nickname. {author_mention}  - Tag the message author. {author_id}       - Message author's ID. {channel_name}    - Channel name. {channel_mention} - Channel tag. {channel_id}      - Channel ID. {server_name}     - Server name. {server_id}       - Server ID. {target_name}     - Target's name. {target_nick}     - Target's nickname. {target_mention}  - Tag the target. {target_id}       - Target's ID. This command requires the Manage Server permission.  | `>>addcommand hi Hello {author_name}!`
`>>addreactor` `>>addreac` | Adds an automatic reactor to the server. Whenever the specified trigger word is detected, Sigma will react to the message with the specified emote. The ":lcHello:" above given in the example is a custom emote. This command requires the Manage Server permission. | `>>addreactor hi :lcHello:`
`>>addresponder` `>>addres` | Adds an auto-responder to the server. Sigma will automatically reply with the set message to any sentence that conaints the specified trigger in it as a standalone word. This command requires the Manage Server permission. Responders can have special dynamic arguments in them. {author_name}     - Message author name. {author_nick}     - Message author nickname. {author_mention}  - Tag the message author. {author_id}       - Message author's ID. {channel_name}    - Channel name. {channel_mention} - Channel tag. {channel_id}      - Channel ID. {server_name}     - Server name. {server_id}       - Server ID. {target_name}     - Target name. {target_nick}     - Target nickname. {target_mention}  - Tag the target. {target_id}       - Target ID. This command requires the Manage Server permission.  | `>>addresponder hi Hello there!`
`>>anticaps` | Toggles the anticaps limiter. The default is a minimum of 5 capital letters and 60% of the message being caps. This can be controlled with the "capslimit" and "capspercentage" commands. | `>>anticaps`
`>>antispam` | Toggles the antispam limiter. This basically enforces a custom rate limiter upon users. The default is 5 messages per 5 seconds. | `>>antispam`
`>>asciionlynames` `>>forceascii` | Toggles if only ASCII characters are allowed in names. The bot will check member's names every 60s for non ASCII characters and rename them if found. To change the default temporary name, use the asciitempname command. | `>>asciionlynames`
`>>asciitempname` `>>asciitemp` | Changes the default temporary name for those who the temporary ASCII name was enforced on. | `>>asciitempname <ChangeMePleaseI'mLonely>`
`>>blockarguments` `>>blockargument` `>>blockargs` `>>blockarg` | Disallows commands to be used with the given arguments. If a command contains a blocked argument, it's execution is prevented, with only a reaction added to the message indicating it being blocked. | `>>blockarguments loli vore`
`>>blockedarguments` `>>blockedargs` | Lists all blocked arguments on the server. | `>>blockedarguments`
`>>blockedextensions` `>>blockedexts` | Lists all blocked extensions on the server. | `>>blockedextensions`
`>>blockedwords` | Lists all blocked words on the server. | `>>blockedwords`
`>>blockextensions` `>>blockextension` `>>blockexts` `>>blockext` | Adds all the extensions you list to the extension filter. If any of the extensions in the filter are sent, the message will be deleted and the author will be notified. Extensions should not be separated by a delimiter. Those with the Administrator permission are not affected. | `>>blockextensions .png .jpg`
`>>blockinvites` `>>filterinvites` | Toggles if invite links should be automatically removed. If any invite links are sent, the message will be deleted and the author will be notified. Those with the Administrator permission are not affected. | `>>blockinvites`
`>>blockwords` `>>blockword` | Adds all the words you list to the blocked words filter. If any of the words in the filter are sent, the message will be deleted and the author will be notified. Words should not be separated by a delimiter. Those with the Administrator permission are not affected. | `>>blockwords crap ass tits`
`>>bye` `>>goodbye` | Toggles if Sigma should say when users leave the server. The goodbye feature is active by default. | `>>bye`
`>>byechannel` `>>byech` | Sets the channel the goodbye messages should be sent to. | `>>byechannel #welcome`
`>>byeembed` `>>byeemb` | Toggles whether bye messages are an embed or not. Also customizes the embed that is used. You can change the embed color, set the thumbnail, and set the image. To do so, specify the field and the value separated by a colon (see usage example). The accepted fields are color, thumbnail, and image. Color accepts only HEX codes, while the other two accept only direct image URLs. Provide no arguments to toggle this feature on or off. | `>>byeembed color:1abc9c image:my.image.link/fancy.png`
`>>byemessage` `>>byemsg` | This sets the message shown on the server when a member leaves. Goodbye messages can have special dynamic arguments in them. {user_name}     - Leaving user's name. {user_disc}     - "#xxxx" in the user's name. {user_nick}     - Message author's nickname. {user_mention}  - Tag the leaving user. {user_id}       - Leaving user's ID. {server_name}   - Server name. {server_id}     - Server ID. {owner_name}    - Server owner's name. {owner_disc}    - "#xxxx" in the server owner's name. {owner_nick}    - Server owner's nickname. {owner_mention} - Tag the server owner. {owner_id}      - Server owner's ID. This command requires the Manage Server permission.  | `>>byemessage Goodbye {user_mention}!`
`>>capslimit` | Sets the minimum number of capital letters in a message to check for before the message is checked for what percentage of it is in caps. Message below this limit will be ignored. | `>>capslimit 9`
`>>capspercentage` `>>capspercent` | Sets the minimum percentage of capital letters in a message to check for before it is deleted. For example, if 80% of the message is caps (as set in the usage example), it will be deleted. | `>>capspercentage 80`
`>>colorroles` | Toggles the color role feature. This is deactivated by default. Once enabled, members can use the colorme command to get a role with their requested hex color. Roles created with this feature have a SCR prefix in them and are created to be just one place under Sigma's top role with no permission changes. This command requires the Manage Server permission. | `>>colorroles`
`>>customcommands` `>>customcmds` `>>custcmds` `>>ccmds` | Shows a list of the server's custom commands. The list is separated into pages of 10 items each. You can specify the page number you want to see. | `>>customcommands 4`
`>>deletecommands` `>>delcmds` | Toggles whether messages that are a command should be automatically deleted. This command requires the Manage Server permission. | `>>deletecommands`
`>>filterautowarn` | Toggles whether users will automatically receive a warning upon triggering the blacklisted word/extentions filter. Like the issuewarning command does, but automated. This command requires the Manage Server permission. | `>>filterautowarn`
`>>greet` | Toggles if Sigma should greet users when they enter the server. The greeting feature is active by default. | `>>greet`
`>>greetchannel` `>>greetch` | Sets the channel the greeting messages should be sent to, unless greetdm is active. | `>>greetchannel #welcome`
`>>greetdm` `>>greetpm` | Toggles if Sigma should greet users by sending them a Direct Message, instead of writing the message in a channel. | `>>greetdm`
`>>greetembed` `>>greetemb` | Toggles whether greet messages are an embed or not. Also customizes the embed that is used. You can change the embed color, set the thumbnail, and set the image. To do so, specify the field and the value separated by a colon (see usage example). The accepted fields are color, thumbnail, and image. Color accepts only HEX codes, while the other two accept only direct image URLs. Provide no arguments to toggle this feature on or off. | `>>greetembed color:1abc9c image:my.image.link/fancy.png`
`>>greetmessage` `>>greetmsg` | This sets the message shown on the server when a member joins. Greet messages can have special dynamic arguments in them. {user_name}     - Leaving user's name. {user_disc}     - "#xxxx" in the user's name. {user_nick}     - Message author's nickname. {user_mention}  - Tag the leaving user. {user_id}       - Leaving user's ID. {server_name}   - Server name. {server_id}     - Server ID. {owner_name}    - Server owner's name. {owner_disc}    - "#xxxx" in the server owner's name. {owner_nick}    - Server owner's nickname. {owner_mention} - Tag the server owner. {owner_id}      - Server owner's ID. This command requires the Manage Server permission.  | `>>greetmessage Hello {user_mention}, welcome to {server_name}!`
`>>hardblockedwords` | Lists all hard-blocked words on the server. | `>>hardblockedwords`
`>>hardblockwords` `>>hardblockword` | Works like "blockwords" but very intolerant. For example if you hardblock the word "ass" it will delete stuff like "assassin". It looks for any instance of the contents in the message, not indivitial segments. If any of the words in the filter are exist within a message, whether as a standalone word or within another word, the message will be deleted and the author will be notified. Extensions should not be separated by a delimiter. Those with the Administrator permission are not affected. | `>>hardblockwords crap ass tits`
`>>inviteautowarn` | Toggles whether users will automatically receive a warning upon triggering the blacklisted invites filter. Like the issuewarning command does, but automated. This command requires the Manage Server permission. | `>>inviteautowarn`
`>>log` | Toggles logging of multiple log types at once. You can enter "all" to turn on all logs, or "none" to disable all logs. It also accepts a list of log types separated by a semicolon and space "; ". The accepted log types are antispam, bans, deletions, edits, filters, kicks, movement, mutes, purges, and warnings. The log types in the list will be toggled when entered. If they were active, they will be deactivated, and vice versa. | `>>log kicks; bans; movement;`
`>>loggingchannel` `>>logchannel` `>>logch` | Designates a channel where server events will be logged in. You can set each log type to a different channel by specifying the log type after the channel mention. It can also accept a list of log types separated by a semicolon and space "; ". To disable all logging channels, ented "disable" as the channel argument. To disable channels for specific log types, input the log type after "disable". Disabling also acceptes a list of log types in the aforementioned format. Accepted log types are antispam, bans, deletions, edits, filters, kicks, modules, movement, mutes, purges, and warnings. | `>>loggingchannel #logging`
`>>logmodule` | Toggles logging of commands in the specified module being used. | `>>logmodule moderation`
`>>logsettings` `>>logs` | Displays log settings. This includes the log channel and whether or not it is enabled for each log type. | `>>logsettings`
`>>prefix` | Sets the prefix that Sigma should respond to. This will be bound to your server and you can set it to anything you'd like. However, the prefix must be two characters or longer and can not contain spaces, they will be automatically removed. This command requires the Manage Server permission. | `>>prefix !!`
`>>ratelimit` | Sets the message amount and timespan for the rate limiter. Separated by a colon, the amount goes first and timespan second. The usage example translates to a limit of 6 messages per 10 seconds. Any messages that cross this limit will be deleted. | `>>ratelimit 6:10`
`>>reactors` `>>reacs` | Shows a list of the server's reaction triggers. The list is separated into pages of 10 items each. You can specify the page number you want to see. | `>>reactors 4`
`>>removecommand` `>>deletecommand` `>>remcmd` `>>delcmd` | Removes a custom command trigger from the server. This command requires the Manage Server permission. | `>>removecommand hi`
`>>removereactor` `>>deletereactor` `>>remreac` `>>delreac` | Removes an automatic reaction trigger. This command requires the Manage Server permission. | `>>removereactor hi`
`>>removeresponder` `>>deleteresponder` `>>remres` `>>delres` | Removes a custom responder trigger from the server. This command requires the Manage Server permission. | `>>removeresponder hi`
`>>renamecommand` `>>rencmd` | Replaces a custom command's trigger without losing the original trigger's contents. The original custom command trigger goes first, followed by what you wish to change it to. This command requires the Manage Server permission. | `>>renamecommand hi howdy`
`>>responders` `>>resps` | Shows a list of the server's custom responder triggers. The list is separated into pages of 10 items each. You can specify the page number you want to see. | `>>responders 4`
`>>spawnchevrons` `>>spawnchevs` | Toggles if Sigma shoulw allow chevrons to spawn in a target channel. If no channel is tagged, the target will be the channel that the command is used in. | `>>spawnchevrons #channel`
`>>unblockarguments` `>>unblockargument` `>>unblockargs` `>>unblockarg` | Removes arguments from the blocked list, allowing commands to be executed with them again. | `>>unblockarguments something idunno`
`>>unblockextensions` `>>unblockextension` `>>unblockexts` `>>unblockext` | Removes a blocked extension allowing people to send files containing it. To purge the entire extension filter, enter -all as the command argument. Extensions should not be separated by a delimiter. | `>>unblockextensions boobs`
`>>unblockwords` `>>unblockword` | Removes a blocked word allowing people to send messages containing it. To purge the entire word filter, enter -all as the command argument. Words should not be separated by a delimiter. | `>>unblockwords boobs`
`>>unflip` | Toggles if Sigma should respond to tables being flipped. This command requires the Manage Server permission. | `>>unflip`
`>>unhardblockwords` `>>unhardblockword` | Removes a hard blocked word allowing people to send messages containing it. To purge the entire word filter, enter -all as the command argument. Words should not be separated by a delimiter. | `>>unhardblockwords boobs`
[Back To Top](#module-index)

### STATISTICS
Commands | Description | Example
----------|-------------|--------
`>>experience` `>>activity` `>>level` `>>exp` `>>xp` | Shows how much of Sigma's internal experience you've obtained. Experience is earned by being an active member of the community. Yes, this is meant to be vague. | `>>experience @person`
`>>topcookies` `>>toprep` | Shows the top 20 users who have the most cookies. A filter can be added, either global or total, sorting it by the amount they globaly have right now, which is the default, or the total amount of cookies that they have collected over time regardless of resets. | `>>topcookies global`
`>>topcurrency` `>>topkud` | Shows the top 20 users who have the most currency. A filter can be added, either global, local or total, sorting it by the amount they globaly have right now, which is the default, sorted by the amount that users have earned on this guild, or the total amount of currency that they have collected over time regardless of resets. | `>>topcurrency local`
`>>topexperience` `>>topexp` `>>topxp` | Shows the top 20 users who have the most experience. A filter can be added, either global, local or total, sorting it by the amount they globaly have right now, which is the default, sorted by the amount that users have earned on this guild, or the total amount of experience that they have collected over time regardless of resets. | `>>topexperience total`
`>>wallet` `>>currency` `>>money` `>>kud` | Shows how much of Sigma's internal currency you currently have, as well as how much you've earned on the current server and in total. Kud is earned by being an active member of the community. Yes, this is meant to be vague. | `>>wallet @person`
[Back To Top](#module-index)

### UTILITY
Commands | Description | Example
----------|-------------|--------
`>>avatar` `>>av` `>>pfp` | Shows the mentioned user's avatar. If no user is mentioned, it shows the author's avatar. You can add "gif" to the end of the command to indicate that it's a gif. Or you can add "auto" to show the predominant color of the image. You can also add "static" to the end to make it return the full sized static version of your avatar. | `>>avatar @person`
`>>botinformation` `>>botinfo` `>>info` | Shows information about the bot, version, codename, authors, etc. | `>>botinformation`
`>>bots` | Lists the bots on the server and shows their status. | `>>bots`
`>>channelid` `>>chid` `>>cid` | Shows the User ID of the mentioned channel. If no channel is mentioned, it will show the ID of the channel the command is used in. If you don't want the message to be an embed, add "text" at the end. | `>>channelid #channel`
`>>channelinformation` `>>channelinfo` `>>chinfo` `>>cinfo` | Shows information and data on the mentioned channel. If no channel is mentioned, it will show data for the curent channel. | `>>channelinformation #channel`
`>>color` `>>colour` `>>clr` | Shows the specified color. It accepts either a HEX code or an RGB array. | `>>color #1abc9c`
`>>convertcurrency` `>>convert` | Converts the specified amount of money. The format of "{amount} {from_currency} in {to_currency}" must be followed. | `>>convertcurrency 50 EUR in USD`
`>>createinvite` `>>makeinvite` `>>createinv` `>>makeinv` | Creates an instant invite for the specified channel. If no channel is specified, it's made for the current channel. You can set an expiration by adding "d:HH:MM:SS" as an argument. You can also set a limited number of uses by adding "u:num" where "num" is the amount of uses. The order of the arguments doesn't matter. This command requires the Create Instant Invite permission. | `>>createinvite d:12:0:0 u:10 #general`
`>>divorce` | Divorces the mentioned user that you are married with. Divorces cost 15 Kud per hour that you were married, unless you're just canceling a proposal. | `>>divorce @person`
`>>emote` `>>emoji` `>>em` | Searches for an emoji by name. To make the search more precise you can add the ID of the emote or server ID that the emote is from, like in this example "monika:375824498882117635". Custom emotes are not guaranteed to be SFW as they can be anything. | `>>emote Monika`
`>>imgur` `>>img` | Anonymously uploads the specified attachment or URL to imgur and returns a direct link to it. Attachment must be an image (GIFs are images). URL must be a direct link to an image. | `>>imgur [imgfile.png]`
`>>ingame` | Shows the top played games on the server. | `>>ingame @person`
`>>lmgtfy` `>>letmegooglethatforyou` | Outputs a link that will google the specified query for you. | `>>lmgtfy Sexy Sneks`
`>>marry` `>>propose` | Proposes to the mentioned user, or accepts their marriage proposal if they proposed to you. | `>>marry @person`
`>>owners` | Shows a list of Sigma's owners. Users in this list have access to the administration module. | `>>owners`
`>>permissions` `>>perms` | Shows which permissions a user has and which they do not. If no user is mentioned, it will target the message author. | `>>permissions @person`
`>>ping` | Shows the latency of every shard the bot is on. | `>>ping`
`>>randomcolor` `>>randomcolour` `>>rclr` | Shows you a random color block along with its HEX code. | `>>randomcolor`
`>>roleid` `>>rankid` `>>rid` | Shows the Role ID of the specified role. Unlike the other ID commands, a role specification is required. Roles mentions do not work here, lookup is done via role name. If you don't want the message to be an embed, add "text" at the end. | `>>roleid Warlards`
`>>roleinformation` `>>roleinfo` `>>rinfo` | Shows information and data on the specified role. Roles mentions do not work here, lookup is done via role name. | `>>roleinformation`
`>>rolepopulation` `>>rolepop` | Shows the population of the specified role. If no arguments are provided, it will show the top 20 roles by population. | `>>rolepopulation Warlard`
`>>servericon` `>>srvicon` `>>icon` | Shows the server's icon image. | `>>servericon`
`>>serverid` `>>guildid` `>>srvid` `>>sid` `>>gid` | Shows the Server ID of the server the command is used in. If you don't want the message to be an embed, add "text" at the end. | `>>serverid`
`>>serverinformation` `>>serverinfo` `>>sinfo` | Shows information and data on the server. | `>>serverinformation`
`>>shortenurl` `>>shorten` `>>bitly` | Shortens a URL for you using BitLy. All URLs returned via Sigma are without ads, merely shortened using the service. | `>>shortenurl https://i.redd.it/ngwebbf5nwfz.jpg`
`>>spouses` `>>wives` `>>husbands` `>>waifus` `>>husbandos` | Shows the mentioned user's list of spouses, that is, people that they're married to. | `>>spouses @person`
`>>statistics` `>>stats` | Shows Sigma's current statistics. Population, message and command counts, and rates since startup. | `>>statistics`
`>>status` | Shows the status of Sigma's host machine. Processor information, memory, storage, network, etc. | `>>status`
`>>suggest` | Submits a suggestions to the owners of Sigma to do stuff. Development and change wise. | `>>suggest Add some new stuff!!!`
`>>translation` `>>translate` `>>trans` | Translates a language from and to the specified ones. If a conversion input is not stated, the first argument will be considered the input language and the output will be in english. The language codes used abide by the ISO 639-1 format. For the whole list, you can go to the following wikipedia article https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes | `>>translation EN>JA Hello there!`
`>>userid` `>>uid` | Shows the User ID of the mentioned user. If no user is mentioned, it will show the author's ID. If you don't want the message to be an embed, add "text" at the end. | `>>userid @person`
`>>userinformation` `>>userinfo` `>>uinfo` | Shows information and data on the mentioned user. If no user is mentioned, it will show data for the author. | `>>userinformation @person`
`>>whoplays` | Generates a list of users playing the specified game. | `>>whoplays Overwatch`
[Back To Top](#module-index)

### WARFRAME
Commands | Description | Example
----------|-------------|--------
`>>wfacolytechannel` `>>wfacolc` | Designates a channel for Warframe acolyte notifications. When an acolute is found it will be posted there. To disable this, write disable after the command instead of a channel. | `>>wfacolytechannel #wf-acolytes`
`>>wfacolytes` `>>wfacol` | Shows data on the Stalker's acolytes. Their names, locations and health. | `>>wfacolytes`
`>>wfalertchannel` `>>wfac` | Designates a channel for Warframe alerts. When a new alert shows up the news will be posted there. To disable this, write disable after the command instead of a channel. | `>>wfalertchannel #wf-alerts`
`>>wfalerts` `>>wfa` | Shows the currently ongoing alerts in Warframe. As well as their respective rewards. | `>>wfalerts`
`>>wffissurechannel` `>>wffc` | Designates a channel for Warframe void fissures. When a new void fissure shows up the news will be posted there. To disable this, write disable after the command instead of a channel. | `>>wffissurechannel #wf-fissures`
`>>wffissures` `>>wffissure` `>>wff` | Shows the current fissure locations in Warframe. As well as their tiers, locations and mission types. | `>>wffissures`
`>>wfinvasionchannel` `>>wfic` | Designates a channel for Warframe invasions. When a new invasion shows up the news will be posted there. To disable this, write disable after the command instead of a channel. | `>>wfinvasionchannel #wf-invasions`
`>>wfinvasions` `>>wfinvasion` `>>wfi` | Shows the current ongoing invasions in Warframe. As well as their factions, locations and rewards. | `>>wfinvasions`
`>>wfnews` `>>wfn` | Shows the current ative news in Warframe. | `>>wfnews`
`>>wfnewschannel` `>>wfnc` | Designates a channel for Warframe news. When Digital Extremes posts a news for Warframe it will be posted there. To disable this, write disable after the command instead of a channel. | `>>wfnewschannel #wf-news`
`>>wfplainschannel` `>>wfpoec` | Designates a channel for Warframe plains of eidolon day-night cycle. When day shifts to night, and vice versa, a notification is sent to that channel. To disable this, write disable after the command instead of a channel. | `>>wfplainschannel #wf-daylight`
`>>wfplainsofeidolon` `>>wfpoe` | Shows the current time on the Plains of Eidolon in warframe. As well as the next day/night cycle rotations. | `>>wfplainsofeidolon exact`
`>>wfpricecheck` `>>wfmarket` `>>wfpc` | Checks the price for the specified item. This will only list items by members that are currently online and in the game. The API requires a precise item name. For an item set, put "set" after the item name. | `>>wfpricecheck Volt Prime Set`
`>>wfsales` `>>wfsale` | Shows items that are currently on sale in Warframe's market. This list shows only items that have reduced prices by default. If you want it to list all promoted items regardless of reduction add "all" to the end of the command as in the example. The item list is also paginated. | `>>wfsales 2 all`
`>>wfsortie` `>>wfsorties` `>>wfs` | Shows the ongoing sortie missions in Warframe. | `>>wfsortie`
`>>wfsortiechannel` `>>wfsc` | Designates a channel for Warframe sorties. When a new sortie shows up the details will be posted there. To disable this, write disable after the command instead of a channel. | `>>wfsortiechannel #wf-sorties`
`>>wfsyndicates` `>>wfsyndicate` `>>wfsyndi` `>>wfsy` | Lists the best tradable offerings sold by each syndicate. Items with no current sell offers are listed first. Otherwise items are listed from most valuable to least valuable. This command is used to help you decide what to sell in case you have excess standing. For price checking user t wfpricecheck command instead. | `>>wfsyndicates`
`>>wftag` `>>wftagrole` `>>wfnotify` `>>wfbind` | Binds a certain keyword to a role. When this keyword appears in any Warframe post, all roles bound to its triggers will be mentioned. Enter "disable" instead of a role name to remove the tag binding. | `>>wftag aura Aura Squad`
`>>wftrials` `>>wftrial` `>>wfraids` `>>wfraid` `>>wft` `>>wfr` | Shows raid statistics for the specified username. Note that DE hasn't been tracking this data forever. So some really old raids won't be shown due to having no data. The shortest raid time shown only counts victorious raids. | `>>wftrials AXAz0r`
`>>wfvoidtrader` `>>wfbarokiteer` `>>wfbaro` `>>baro` `>>wfvt` | Shows the items that Baro Ki'Teer is currently selling as well as the statistics such as total number of items, total amount of ducats and credits needed and where he's located. | `>>wfvoidtrader`
[Back To Top](#module-index)