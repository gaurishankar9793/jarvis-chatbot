#JARVIS mark 12  python 3.5.1 version
#JUST.A.RATHER.VERY.INTELEGENT.SYSTEM.

import datetime
import os
import random
import datetime
import webbrowser
import time
import calendar 
#(all the green words are somthing jarvis will say or somthing he will understand if you say, the ones after if esa in/ if res2 in are things he will understand if you say. the ones after random.choice are things he will say or respond to you with)


# jarvis greets you first with one of these greeetings \/ 
a = random.choice(("hi","hey","sup","whats up","hey it's jarvis","hello","hey there","good to see you"))
print (a)
os.system("say '"+a+"'") 
resp1 = input("")

    
# he will ask you what you want to do
gE = random.choice(("what are we going to do?","so what we doin?","what do you want to do sir?","so what are we gonna do?","k now what?","so what do you want to do?"))
print (gE)
os.system("say '"+gE+"'") 

note1 = []
# this loop is so when you say somthing to jarvis and he responds the code doesn't end you can keep talking to him and keep asking him things not just one thing.

 # some of your info (frd is your friends, your name, no need to right your crush you can tell jarvis later on! lol


people = ["","","","",""] 
	
somethingwastaken = ("n")

Problem = ("")

mission = ("")

online = ("n")

bad_day = ("n")

sad = ("n")

Happy = ("n")
    
had_fun = ("n")
    
introuble = ("n")
    
frd = random.choice(("leo","Simon","Eadyn","Eric"))

gamec = random.choice(("chess","guess my number","battlefront","pong"))
    
name = ("Sergei")
    
last_name = ("Glimis")

google = ("http://google.com")

crush = ("")
    
questionmark = random.choice(("?","??","???","???"))
    
bad_stuff_keywords = ("death","kill","hurt","harm","discomfort","bad","terible","dead","cruel","illegal")
    
good_stuff_keywords = ("fun","awesome","love","super","entertaining","amazing","good","relax","great","yummy","delicous")

def offline():
	Offl = random.choice(("sorry i think were offline","sorry im offline i think","sir i think im offline"))
	print (Offl)
	os.system("say '"+Offl+"'")
            
def weather():
	print ("weather coming soon")

def hi():
	greet = random.choice(("hey","hi","sup","hello","hey there","hia","hello there","hey " + name))
	print(greet)
	os.system("say '"+greet+"'")


def idk():
	idk = random.choice(("im not sure sir","i dont know","im not really sure"))
	print (idk)
	os.system("say '"+idk+"'")


def no():
	nobro = random.choice(("no","no sir","No"))
	print (nobro)
	os.system("say '"+nobro+"'")
	


def ok():
	ok1 = random.choice(("ok","ok then","k then","k","ok cool","ok sir","OK","okay"))
	print (ok1)
	os.system("say '"+ok1+"'")

def yes():
	yeah11 = random.choice(("yeah","yes","yep","yes sir"))
	print (yeah11)
	os.system("say '"+yeah11+"'")

while 1:
    
    
    
	
    
    
    # this is all the thing that jarvis needs to know if you want him to do somthing if only part of the response is somthing if its exsactly it then use resp2
	database = ("jarvis you there","jarvis are you there","jarvis where are you","where are we","what is this place","took my","stole my","good night","nighty night","night jarvis","what's the weather","whats the weather","what is the weather","whats todays weather","what's your name","whats your name","do you have a name","sorry"," my apologies","forgive me","calendar","what's the month","whats the month","what is todays date"," what's todays date","what is today's date","whats todays date","whats the date","what is the date","what's the date","i gotta go","i have to go","i need to go","do you want to have sex","have sex with me","do you wanna have sex","will you fuck me","what are we gonna do","what do you wanna do","not aloud to work on you","i cant work on you anymore","i cant code you anymore","night","its my birthday","it's my birthday","it is my birday","todays my birthday","today's my birthday","good job","good work","morning","rise and shine","good morning","that was fun","that was so much fun","that was so fun","ok ","OK","i love you","your so awesome","your the best","your awesome","who is","who is the","i guess","what is up","im not sure","i'm not sure","shit","crap","damit","damn","fuck","darn","bullshit","cool","awesome","great","good","nice","i need to study","i have a test","theres a test","i think i have a test","it's halloween","happy halloween","its halloween","what is","what is the","how do you","how are you supposed to","hi ","hey ","whats","what's","what do you want to do","what should we do","what do you think should we do","idk","i dont know","i don't know","i dunno know","screw you","fuck you","my dad is raging","my dad is getting mad","my dad is getting angry","my dads raging","my dads mad","my dad is mad","my dads yelling","my teachers is raging","my teacher is getting mad","my teacher is getting angry","my teacher raging","my teachers mad","my teacher is mad","my teachers yelling","do you want to have sex","have sex with me","do you wanna have sex","will you fuck me","jk","just kidding","jarvis you there","jarvis are you there","jarvis where are you","tell me a jo","tell a jo","say a jo","do a jo","idk","i dont know","merry christmas","happy christmas","its christmas","theres a girl i like","theres a cute girl i met","theres this girl i like","theres a girl i like at","theres a cute girl at","i like this cute girl","i like this girl","let's play a game","wanna play a game","lets play a game","can we play a game","os()","terminal","your so awesome jarvis","i love you","your awesome","your the best","i got detention","what's your name","whats your name","do you have a name","yes my name is JARVIS","Jarvis","my name is jarvis","JARVIS is my name","DUDE","sorry"," my apologies","forgive me","my moms yelling","my moms mad","my mom is raging","my friend is raging","my dad is raging","the principal is raging","teacher is raging""is raging","my mom is getting mad","my mom is getting angry","my moms raging","my teachers mad","my dads mad","im upset","im so sad","watch you laungage","JARVIS!","HEY","what the hell jarvis","im bored","game","im board","what do you want to do","what should we do","rage","i","I","smashed","i broke","i destroyed","i cracked","im grounded","i got detention","i have detention",
           "im in trouble","nothing","not much",
           "date","time","no","nope","nah","not","yes","yep","yeah","in deed","bye","gtg","got to go","see you",
           "c u","hi","hello","hello","hia","bleep","omg","OMG","oh my god","h","i","e","y","e"
           ,"look up","email","map","add Note","get Note","joke","rabid donkey","game","quit","help","raging",
           "hurt","fire","","thanos","danger","sad","upset","open email","go to email","open my email","creator","thanks","lol","ok",
           "k","yep","report","owner","maker","jarvis","coder","thank you","sup","whats up","what's up","hey",
           "hah","tell me a joke","tell a joke","say a joke","do a joke","im really sad","im really upset"
           ,"im sad","im pretty sad","im pretty upset","is raging","getting mad","is getting angry","raging",
           "help im hurt","im hurt help","ahh help jarvis","who made you","who coded you","whos your owner",
           "whos your coder","what do you want to do","what should we do","what do you think should we do",
           "i broke","i smashed","i destroyed","i cracked","lets play a game","im really bored",
           "im kinda bored","im bored","lets play a game","do you want to play a game","wanna play a game",
           "do you want to play a game","watch you laungage","JARVIS!","HEY","what the hell jarvis","whats the weather","what's the weather","what is the weather","wtf")
    # resp2 is the input (aka what you type in!)
	resp2 = input("")
    # dont know to much about this part but esa is like resp2 but doesnt have to exsactly match the if statment.
	esa = ""
	for word in database:
		if word in resp2:
			esa = word
           # when jarvis learns to tell if hes conected to the enternet he will run this when the user asks for an online question but he cant reference it (jarvis doesn't need to be online to work but some things he does like web search,weather.etc)
	
        
		if mission != (""):
			print (mission)
			mision = ("")
			if somethingwastaken != ("n"):
				
				respmswt = input()
				databasemswt = ("i got it","gave it back","i have it","has it","won't give it back","ok","i know","yeah","yes","i know","i get it","im trying")
				esamswt = ""
				for wordmswt in databasemswt:
					if wordmswt in respmswt:
						esamswt = wordmswt
				if esamswt in ("i got it","gave it back","i have it"):
					ghgib = random.choice(("good, hold on to your " + (tmsd[3]) + " for now on","ok cool hold onto it","thank python you got your " + (tmsd[3]) + " back hold onto it dont let " + (tmsd[0]) + " take it"))
					print (ghgib)
					os.system("say '"+ghgib+"'")
					mission = ("")
					break
				if esamswt in ("ok","i know","yeah","yes","i know","i get it","im trying"):
					okwnt = random.choice(("k","yeah","tell me when you get it","yeah tell someone"))
					print (okwnt)
					os.system("say '"+okwnt+"'")
					break
			
				else: 
					wntgib = random.choice(("we need to get your " + (tmsd[3]) + " back","let's get your " + (tmsd[3]) + " back","let's get your " + (tmsd[3]) + " from " + (tmsd[0]),"let go get the " + (tmsd[3]) + " back"))
					print (wntgib)
					os.system("say '"+wntgib+"'")
					break	
					
        

        # tell jarvis that you have to go and he will say bye and quit.
		if esa in ("quit","bye","gtg","got to go","see you","c u","i gotta go","i have to go","i need to go"):
				byebro = random.choice(("ok bye Sergei cu later","bye sir","c u later sir","talk to you later then","talk to you later"))
				print (byebro)
				os.system("say '"+byebro+"'")
				quit()
				
        # jarvis will look up somthing for you when he knows how (curently not working)
		if resp2 in ("look up","web search","search the web","search web"):

				c = random.choice(("ok","lets see","let me see","ok sir il get right on that lets see","im looking up and i dont see anything??"))
				print (c)
                
				os.system("say '"+c+"'")
				webbrowser.open(google,new=2)
				break
            
        # have jarvis write a note
		if resp2 in ("add note","take note"):
				d = random.choice(("ok sir one sec il pull up the note pad","ok sir one sec","yeah one sec il pull it up","one sec sir","ok","ok sir"))
				print (d)
				os.system("say '"+d+"'")
				note1 = input("")
				break
        
        # have jarvis read the notes you have taken to you!
		if resp2 == "open notes":
				e = random.choice(("ok sir one sec il pull up the your recent notes","ok sir one sec","yeah one sec il pull it up","one sec sir","ok","ok sir notes","ok sir"))
				print (e)
				os.system("say '"+e+"'")
            
				print (note1)
				break
        # jarvis will email for you (curently not fuctional)
		if esa in ("open email","go to email","open my email","go to my email"):
				f = random.choice(("im mailing a letter that says E and its not sending","ok lets see","il pull up email real fast","email ok","ok email","ok lets see il pull up email","email ok let me pull it up"))
				f1 = ("i can not currently email due to missing packages, hopefully i will be able to help you with that soon!")
				print (f)
				print (f1)
				os.system("say '"+f+"'")
				os.system("say '"+f1+"'")
				break
        # ask jarvis to tell you a joke
		if esa in ("tell me a joke","tell a joke","say a joke","do a joke"):
				had_fun = ("y")
				g = random.choice(("why did the chicken cross the road (if you dont know the answer your an idiot!)"," how many therapists does it take to change a light bulb, only one but the light bulb has to want to change!"))
				print (g)
				os.system("say '"+g+"'")
				break
                
                
                
        # tell jarvis your sad and he will try to cheer you up!
		if esa in ("im really sad","im really upset","im sad","im pretty sad","im pretty upset","im so sad","im upset"):
				h = random.choice(("that's to bad is there anything i can do","im sorry about that is there anything i can do to help","i can not feel emotions but if i could i would have the emotion of sympothy for your other emotion sadness is there anything i can do to cheer you up","it is probaly your fault but im here to make you feel better is there anything i can do to help","emotions seem like what is called a pain in the ass anything i can do to help","il sing you a song, lalalalalalalalala but is there anything else i can do to help?"))
				print (h)
				os.system("say '"+h+"'")
                
				lisad = ("no","yes","i don't know","maybe","yeah","yep","sure","na")
                
				respsad = input("")
				esad = ""
				for wordsad in lisad:
                	
					if wordsad in respsad:
                    	
						esad = wordsad
                    
				if esad in ("yes","yeah","yep","sure","ok"):
                	
   
					sadq1 = random.choice(("ok what can i do","what would that be","anything....... endless its ilegal","what can i do for you","anything","what can i do"))
					print (sadq1)
					os.system("say '"+sadq1+"'")
					break
                
                
				if esad in ("no","na"):
                	
					sadq2 = random.choice(("ok, but if there's anything you need just ask","ok but if you happen to need my assistance il be here","ok but i'll be here if you need anything"))
					print (sadq2)
					os.system("say '"+sadq2+"'")
					break
                    
        # tell jarvis your mom is raging
		if esa in ("my mom is raging","my mom is getting mad","my mom is getting angry","my moms raging","my moms mad","my mom is mad","my moms yelling"):
			
        	
        	
				if introuble == ("y"):
					intrmr = random.choice(("it's probaly because you got in trouble!"," it is probally becuase of what happend, you got in trouble","it's because you got in trouble probaly","maybe its because you got in trouble"))
					print (intrmr)
					os.system("say '"+intrmr+"'")
					
					break
				if introuble == ("n"):
					j = random.choice(("shes always raging im tired of it dude","can you go one day without pissing someone off.... oh right you cant!!","again are you kidding, if we had a dollar everytime she went mental over nothing we'd be rich dude"))
					print (j)
					os.system("say '"+j+"'")
					wd1 = random.choice(("what did you do was it actually that bad","what did you do!!??!","did you actually do somthing that bad!!??","what was it that you did was it really bad actually!!??"))
					print (wd1)
					os.system("say '"+wd1+"'")
					mra = input("")
                
					lisemra = ("i smashed","i broke","i scratched","i cracked","i destroyed","no","yes","kinda","yeah","well sorta","yep","nope","not really")
               
					esamra = ""
					for wordmra in lisemra:
                    	
						if wordmra in mra:
                        	
							esamra = wordmra
               
               
					if esamra in ("yes","yep","yeah","sorta","kinda"):
                	
						mra1 = random.choice(("well ok just dont piss her off","so its your fault","well you shouldn't do stupid stuff that wil obviously piss her off!","that's your fault then","this happens so much why " +name))
						print (mra1)
						os.system("say '"+mra1+"'")
						break
               
					if esamra in ("no","nope","not really"): 
						mra2 = random.choice(("ehh dont worry dude she gets mad like all the time","well it was your fault","i dont know she seems to like getting mad for some reason dont worry","well thats wierd if there's anything i can do to help just ask"))
						print (mra2)
						os.system("say '"+mra2+"'")
						break
					if esamra in ("i jumped off a roof","i took","i went to","i didn't","i didnt","i stole"):
						mr66 = random.choice(("oh my god","wtf are you serious!","your fing mental","your insane dude"))
						print (mr66)
						os.system("say '"+mr66+"'")
						break
                    
					if esamra in ("i smashed","i broke","i scratched","i cracked","i destroyed"):
						yawbs1 = random.choice(("your always breaking shit","common are you kidding","damn i cant believe you","your isane!!","wooh seriously, you idot"))
						print (yawbs1)
						os.system("say '"+yawbs1+"'")
						break
 
 
 
 
                 
        # tell jarvis your hurt of need help
		if esa in ("help im hurt","im hurt help","ahh help jarvis","help me","help"):

			n = random.choice(("why are you always hurt you dumb Ass il resentfuly call an ambulence","You idiot did you jump off a roof again!?","What the heck, you need to hire an ambulence to follow you around!","oh (bleep) il uh......."))
			print (n)
			os.system("say '"+n+"'")
        # ask jarvis to have sex with you (dont actually have sex with your device though!)
		if esa in ("do you want to have sex","have sex with me","do you wanna have sex","will you fuck me"):
			sexo1 = random.choice(("hell no","hell no i aint fuckn you","no way","no way dumbass"))
			print (sexo1)
			os.system("say '"+sexo1+"'")
			databasesex = ("what","why","why not","wtf","what ever","jk","common","please")
			respsex = input("")
			esasex = ""
			for wordsex in databasesex:
            	
				if wordsex in respsex:
                	
					esasex = wordsex
			if esasex in ("what","why","why not","wtf","common","please"):
					sex101 = random.choice(("do you really think you can fit your dick up my head phone jack, or if your a girl try shoving me up your pussy and see what happens... get a life","stop being retarded im not a sex bot go fuck a horse!!","stop trying to rape me and find a human"))
					print (sex101)
					os.system("say '"+sex101+"'")
					break
            
            
			if esasex in ("jk","whatever"):
					sex102 = random.choice(("get a life you idiot stop trying to rape me!!","its not cool stop being like donald Trump raping people!!"))
					print (sex102)
					os.system("say '"+sex102+"'")
					break
        # ask jarvis who made him
		if esa in ("who made you","who coded you","whos your owner","whos your coder"):
				q = random.choice(("Sergei did, who is this then?!? who the fuck are you ahh help AI kidnapper!!!","didnt you or is this not sergei","my owners name is sergei who the hell is this where's sergei?!?!"))
				print (q)
				os.system("say '"+q+"'")
				break
			
        # thank jarvis for somthing he's done for you
		if esa in ("thank you","thanks"):
				TH = random.choice(("dont mention it","cool","thats fine","thats what im here for","your welcome","your welcome sir","anything for you sir"))
				print (TH)
				os.system("say '"+TH+"'")
				break
        # laugh and jarvis will laugh or not think it's funny
		if resp2 in ("lol","ha","yeah lol","lol yeah"):
				LOL = random.choice(("lol","ha","hah","is it really that funny!?!?"))
				print (LOL)
				os.system("say '"+LOL+"'")
				break
        # say ok to jarvis
		if resp2 in ("ok","k"):
				ok = random.choice(("ok","ok then","k then","k","ok cool","ok sir","OK","okay"))
				print (ok)
				os.system("say '"+ok+"'")
				break
		if esa in ("ok ","OK"):
				ok = random.choice(("ok","ok then","k then","k","ok cool","ok sir","OK","okay"))
				print (ok)
				os.system("say '"+ok+"'")
				break
        # ask jarvis whats up    
		if esa in ("whats up","sup","what's up","what is up"):
                 
				sup = random.choice(("Not much","nothing","ehh not much recently","not much, what would you like to do today?","not much really"))
				print (sup)
				os.system("say '"+sup+"'")
				break
        # tell jarvis yes
		if esa in ("yes","yep","yeah","in deed","yeah maybe","yeah cool","yeah i guess","yeah ok","yep ok then","yep ok"):
				yes1 = random.choice(("ok then","yes","yep ok","well yeah","yep"))
				print (yes1)
				os.system("say '"+yes1+"'")
				break
        #tell jarvis no
		if resp2 in ("no","nope","nah","not","no thanks","no im ok","na","no not really","not really"):
				yes1 = random.choice(("ok then","No?","yep ok then","well yeah","yep k"))
				print (yes1)
				os.system("say '"+yes1+"'")
				break
        # ask jarvis the time    
		if esa == ("time"):
			try:
				timey = random.choice(("its","um its","sir its cerently"))
				print (timey)
				os.system("say '"+timey+"'")
			
				time1 = datetime.datetime.now()
				print(time1)
				os.system("say '"+time1+"'")
				break
			except:
				break
				
		if esa in ("what is todays date"," what's todays date","what is today's date","whats todays date","whats the date","what is the date","what's the date"):
				try:
					datey = random.choice(("it's","it is","the date is"))
					print (datey)
					os.system("say '"+datey+"'")
					date1 = datetime.date.today()
					print(date1)
					os.system("say '"+date1+"'")
					break
				except:
					break
		if esa == ("calendar"):
			
			print (calendar.calendar(2016,2,1,10))
			break
        # say hi to jarvis 
		if resp2 in ("hi","hey","hia","hola","hey jarvis","hi jarvis","hi there","hey there","hello"):
				greet = random.choice(("hey","hi","sup","hello","hey there","hia","hello there","hey " + name,"what's up"))
				print(greet)
				os.system("say '"+greet+"'")
				break
        # jarvis wil respond to things like hi there.hi jarvis etc.
		if esa in ("hi ","hey "):
				greet2 = random.choice(("hey","hi","sup","hello","hey there","hia","hello there","hey " + name,"what's up"))
				print(greet2)
				os.system("say '"+greet2+"'")
				break

        # tell jarvis your grounded!
		if esa in ("im grounded","im in trouble","i have detention","i got detention"):
				introuble = ("y")
				punish = random.choice(("your always getting in trouble its like second nature for you lol","to bad i guess no fun for a while well its your fault lol","did you and eric do somthing stupid?!")) 
				print(punish)
				os.system("say '"+punish+"'")
				wdydQ = random.choice(("what did you do!!?!!","what did you do this time","can you go one week with out geting exspelled or suspended or in trouble what did you do!!"))
				print (wdydQ) 
				os.system("say '"+wdydQ+"'")
               
				lisgrd = ("nothing","i dont know","i don't know","um","i broke","i smashed","i destroyed","i cracked","i hit","i didn't","i hurt","i jumped","i had sex","i went to","fight","im just kidding","im kidding","i was kidding")
               
				respgrd = input("")
				esagrd = ""
				for wordgrd in lisgrd:
               	
					if wordgrd in respgrd:
                	
						esagrd = wordgrd
               
				if esagrd in ("i broke","i smashed","i destroyed","i cracked"):
           
					YbsA = random.choice(("your always breaking shit","im not paying for it this time and niether am i taking the blame!"))
					print (YbsA)
					os.system("say '"+YbsA+"'")
					break
				if esagrd in ("i didn't","i jumped","i had sex","i went to"):
					grd33 = random.choice(("i dont know what to say now","oh my god","your fing mental","are you kidding me"))
					print (grd33)
					os.system("say '"+grd33+"'")
					break
				if esagrd in ("nothing","i dont know","i don't know","um"):
					grdq12 = random.choice(("don't bs me whatcha do!!","just tell me what happened","common!"))
					print (grdq12)
					os.system("say '"+grdq12+"'")
					continue
				if esagrd in ("i hit","fight","i hurt"):
					iwiaf = random.choice(("what you gotta not always be saying and doing stupd things where people could get hurt","your always fucking around arent you lol","you are always starting conflict","you need to not get in trouble so much"))
					print (iwiaf)
					os.system("say '"+iwiaf+"'")
					break
				if esagrd in ("im just kidding","im kidding","i was kidding"):
					nik = random.choice(("oh ok good","ok dont say that","dont mess with me","oh ok cool stay out of trouble"))
					print (nik)
					os.system("say '"+nik+"'")
					break
        # ask jarvis what he wants to do!
		if esa in ("what do you want to do","what should we do","what do you think should we do","what are we gonna do","what do you wanna do"):
				lets1 = random.choice(("um well we can try to hang out with one of your friends like " + (frd),"hmm we could play a game like " + (gamec),"hmm you could watch youtube ","hmm well it seems like what ever we do we either hurt our selves or break somthing important","hmm we could go eat a bunch of chocolate","hmm idk are you going to destroy somthing and get grounded again?"))
				print (lets1)
				os.system("say '"+lets1+"'")
				break
        # tell jarvis your bored and he will sugest things to do
		if esa in ("im really bored","im kinda bored","im bored","this is so boring"):
				game = random.choice(("go watch youtube","go work on your book","go F a horse its definitly a good idea.. Jk dont its not someone died F ing a horse once","go jump off a roof like you always do, its definitly a good idea. JK dont its realy not"))
				print (game)
				os.system("say '"+game+"'")
				break
               
        # tell jarvis his laungage isnt exceptible and he will give his apologies
		if esa in ("watch you laungage","JARVIS","HEY","what the hell jarvis","DUDE"):
				sorry = random.choice(("sorry","oh sorry","oh sorry sir","forgive me sorry","sorry about that"))
				print (sorry)
				os.system("say '"+sorry+"'")
				respaq1 = input("")
				lisaq1 = ("its fine","ok","you better be","it's ok","dont say that","it's fine","its ok")
               
				esaq1 = ""
				for wordaq1 in lisaq1:
					if wordaq1 in respaq1:
						esaq1 = wordaq1
               
				if esaq1 in ("its fine","it's fine","its ok","it's ok"):
					itsok = random.choice(("ok sorry","k sorry","yeah sorry","ok","cool"))
					print (itsok)
					os.system("say '"+itsok+"'")
					break
				elif esaq1 in ("not cool","behave","you got me in trouble","it's not ok","its not ok","not cool!"):
					sewq1 = random.choice(("sorry sir il try to keep a lid on it for now on","im sorry sir if theres anything i can do to make it up to you"," sorry about that"))
					print (sewq1)
					os.system("say '"+sewq1+"'")
					break
        # ask jarvis the weather
		if esa in ("what's the weather","whats the weather","what is the weather","whats todays weather"):
				if online == ("n"):
					weather1 = random.choice(("i dont know","im not sure"," im not sure lol","idk lol","i have no idea lol"))
					print (weather1)
					os.system("say '"+weather1+"'")
					weathera = input("")
	               
					lise = ("wtf","what do you mean","what","you dont know","wth","i need the weather","why")
					webr = ""
					for wo in lise:
						if wo in weathera:
							webr = wo
					if weathera in ("wtf","what do you mean","what","you dont know","wth","i need the weather","why","are you offline","whats wrong","wth"):
						weather2 = random.choice(("yeah im offline i believe","well i think we are offline","yeah you code me so your blaming me for not being able to,and i think were offline"))
						print (weather2)
						os.system("say '"+weather2+"'")
						break
	               
					elif weathera in ("ok","k","oh"): 
						okwet = random.choice(("cool ask me when we get back online","yeah ask me when we get back online","ok ask me when we get back online","thanks for understanding ask me again after you get us online again"))
						print (okwet)
						os.system("say '"+okwet+"'")
						break
				if online == ("y"):
					Weather()
					break
				
	               	   
        # tell jarvis how you are grateful for his help
		if esa in ("i love you","your so awesome","your the best","your awesome"):
				yasaj = random.choice(("thanks. but dont forget i wouldnt be posible without you!!","thats nice im just here to help you out when no one else will","your awesome!"))
				print (yasaj)
				os.system("say '"+yasaj+"'")
				break
        
        # apologize to jarvis.
		if esa in ("sorry"," my apologies","forgive me"):
				sorryr1 = random.choice(("it's fine","its ok","its nothing","dont worry its fine","its ok"))
				print (sorryr1)
				os.system("say '"+sorryr1+"'")
				break
        # ask jarvis what his name is.
		if esa in ("what's your name","whats your name","do you have a name"):
				name1 = random.choice(("my name is JARVIS","Jarvis","my name is jarvis","JARVIS is my name"))
				print (name1)
				os.system("say '"+name1+"'")
				respnm = input("")
				lisnm = ("who named you","like iron man","why jarvis","ok","cool","whats jarvis stand for","what's jarvis stand for","what does jarvis stand for","what's jarvis stand for","jarvis?","whats jarvis","what's jarvis","awesome")
				esanm = ""
				for wordnm in lisnm:
               	
					if wordnm in respnm:
                	
						esanm = wordnm
               
				if esanm in ("why jarvis","whats jarvis stand for","what's jarvis stand for","what does jarvis stand for","whats jarvis","what's jarvis","like iron man"):
					jaqa = random.choice(("jarvis is from iron man but it stands for JUST.A.RATHER.VERY.INTELEGENT.SYSTEM","jarvis is just cool it stands for JUST A RATHER VERY INTELEGENT SYSTEM"))
					print (jaqa)
					os.system("say '"+jaqa+"'")
					break
				if esanm in ("ok","cool","oh"):
					jaqa1 = random.choice(("yep","yeah im jarvis","ok so anything else you'd like to know"))
					print (jaqa1)
					os.system("say '"+jaqa1+"'")
					break
				if esanm in ("like iron man","like in iron man","from marvel"):
					marv = random.choice(("yes","yeah thats where its from","yep indeed","yep"))
					print (marv)
					os.system("say'"+marv+"'")
					break
				else:
					print (jaqa1)
					os.system("say '"+jaqa1+"'")
					break
        # access root/terminal on mac right from jarvis!
		if resp2 in ("os()","terminal"):
			print ("terminal")
			tt = input("")
			os.system(tt)
			if tt in ("quit","stop","exit"):
				break
        # ask jarvis to play a game!
		if resp2 in ("let's play a game","wanna play a game","lets play a game","can we play a game"):
			had_fun = ("y")
			print ("ok which game would you like to play?")
			print ("guess my number,rock paper scissors.")
			print ("that's all i have right now")
			databasegme = ("guess","number","rock","paper")
        	
			respgme = input("")

			esagme = ""
			for wordgme in databasegme:
				if wordgme in respgme:
					esagme = wordgme
        	
			if esagme in ("guess my number","guess the number","guess number","guess","number game"):
				gmeq1 = random.choice(("do you want to guess my number or do you want me to guess yours","you want me to guess your number or do you want to guess mine?"))
				print (gmeq1)
				os.system("say '"+gmeq1+"'")
				databasegme2 = ("my number","your number","let me guess your number","guess my number","mine","yours","guess mine")
        	
				respgme2 = input("")

				esagme2 = ""
				for wordgme2 in databasegme2:
					if wordgme2 in respgme2:
						esagme2 = wordgme2
        	
				if esagme2 in ("your number","let me guess your number","yours","ill guess yours","let me guess yours"):
                  	
                	
					gmera2 = random.choice(("ok let me think of a number","k one sec let me find a number " + name,"ok one sec"))
					print (gmera2)
					os.system("say '"+gmera2+"'")
					guessesTaken = 0
					number = random.randint(1, 10)
					print('I am thinking of a number between 1 and 10 try and guess.')
					print('Take a guess') # There are four spaces in front of print.
					guess = input()
					guess = int(guess)
					guessesTaken = guessesTaken + 1
					if guess < number:
						print('Your guess is too low you lose! :(') # There are eight spaces in front of print. 
						break
					if guess > number:
						print('Your guess is too high you lose :(')
						break
					if guess == number:
						print ("yeah you got it right! you win :(")
						break
					if guess == number:
						guessesTaken = (guessesTaken)
						print ('Good job, ' + name + '! You guessed my number in ' + guessesTaken)
						break
					if guess != number:
						print ("your wrong sorry you lose :(")
						break
		
				elif esagme2 in ("guess mine","guess my number","do my number","my number"):
                	
					gmera3 = random.choice(("ok think of a number","ok make up a number","think up a number","think of a number"))
					print (gmera3)
					os.system("say '"+gmera3+"'")
					break 
				elif esagme2 in ("nevermind","na","no","i dont want to","stop"):
					stopgme = random.choice(("ok","oh ok we dont have to if you dont want to","k"))
					print (stopgme)
					os.system("say '"+stopgme+"'")
					break
			if esagme in ("rock","paper"):
				
				rpsas = ("ok lets play")
				rock = ("rock")
				paper = ("paper") 
				sc = ("scissors")
				ASgme = ("and shoot!")
				os.system("say '"+rpsas+"'")
				print (rpsas)
				os.system("say "+rock+"'")
				print (rock)
				os.system("say '"+paper+"'")
				print (paper)
				os.system("say '"+sc+"'")
				print (sc)
				os.system("say '"+ASgme+"'")
				print (ASgme)
				rpsasr = random.choice(("rock","paper","scissors"))
				print (rpsasr)
				os.system("say '"+rpsasr+"'")
				break
        # tell jarvis about your sex life/crush life lol
		if esa in ("theres a cute girl i met","theres this girl i like","theres a girl i like at","theres a cute girl at","i like this cute girl","i like this girl","theres a girl i like"):
        	
        	#jarvis will ask what her name is
			girlq1 = random.choice(("cool what's her name","oh what's her name","what is her name","cool what is her name"))
			print (girlq1)
			os.system("say '"+girlq1+"'")
        	
       
        	# your input (the girls name)
			respgirl1 = input("")

			crush = respgirl1
            
			girlq2 = random.choice((respgirl1 + " cool",respgirl1 + " oh" + respgirl1,"nice","ok cool her name is " + respgirl1))
			print (girlq2)
			os.system("say '"+girlq2+"'")
            # jarvis will ask you if she knows
			girlqa23 = random.choice(("does she know you like her","well does she know","does she know you that like her"))
			print (girlqa23)
			os.system("say '"+girlqa23+"'")
            # tell jarvis she does and he will advise you what to do
			databasegirl593 = ("yes","i dont know","no","im not sure","i'm not sure","yeah","yep","i dont think so","i dont really know","im not really sure")
            
			girlresp593 = input(questionmark)
            
			esagirl593 = ""
			for wordgirl593 in databasegirl593:
				if wordgirl593 in girlresp593:
					esagirl593 = wordgirl593
            
            # tell jarvis yes
			if esagirl593 in ("yes","yeah","yep"):
				girlyesq1 = random.choice(("cool did you ask her out or does she not like you or somthing lol" + questionmark,"did you ask her out" + questionmark,"did you ask her to go out with you" + questionmark,"did you ask her to go out" + questionmark))
				print (girlyesq1)
				os.system("say '"+girlyesq1+"'")
				databasegyes = ("no","no","na","i did not")
				respgyes = input()
				esagyes = ""
				for wordgyes in databasegyes:
					if wordgyes in respgyes:
						esagyes = wordgyes
                
                # tell jarvis no
				if esagyes in ("no","na","i did not"):
					ybth = random.choice(("well ask her","dont be a pussy like you always are!!!","just do it!","well ask her or shell find somone better which shouldnt be to hard!"))
					print (ybth)
					os.system("say '"+ybth+"'")
					break
            	
            	
            # tell jarvis your not sure
			if esagirl593 in ("im not sure","i'm not sure","i dont know","im dont really know","im not really sure"):
				girlins1 = random.choice(("well find out","ask her","talk to her sometime you dont want a repeat of last time now do you!"))
				print (girlins1)
				os.system("say '"+girlins1+"'")
				break
            	
            	
            	
            # tell jarvis no
			if esagirl593 in ("no","i dont think so"):
				girlnoq1 = random.choice(("better tell her you don't want to wait a to long","you better tell her","you better tell instead of waiting until she finds a boyfriend","better tell her before its to late","well tell her, dont be silly!","you tell her tomorrow or il be pissed....seriously dont be a pussy","just tell her dont wait like a year lol","common just do it tell her"))
				print (girlnoq1)
				os.system("say '"+girlnoq1+"'")
				break
            	
        # talk to jarvis about the holliday 
		if esa in ("merry christmas","happy christmas","its christmas"):
			chrsm1 = random.choice(("merry Christmas","yeah Christmas","It's Christmas yeah","CHRISTMAS YEAH"))
			print (chrsm1)
			os.system("say '"+chrsm1+"'")
			break
        
        # halloween!
		if esa in ("it's halloween","happy halloween","its halloween"):
			itsh = random.choice(("boo!!!","happy hallween indeed","yeah candy to bad i cant eat it aww..."))
			print (itsh)
			os.system("say '"+itsh+"'")
			break
        
        # tell jarvis its cool or stuff
		if esa in ("cool","awesome","great","good","nice"):
			cgt = random.choice(("yeah","yep","yes","oh yeah"))
			print (cgt)
			os.system("say '"+cgt+"'")
			break
            
            
            	
        # tell jarvis that your just kidding
		if resp2 in ("jk","just kidding","just kiddn","im just kidding","im only kidding"):
			jklol = random.choice(("oh ok","lol ok","oh k then"))
			print (jklol)
			os.system("say '"+jklol+"'")
			break
        	
        	
        # tell jarvis you dont know or your unsure!
		if esa in ("idk","i dont know","i don't know","i know","im not sure","i'm not sure","i guess"):
			idk1 = random.choice(("ok","k","ok then","oh ok","oh ok"))
			print (idk1)
			os.system("say '"+idk1+"'")
			break
        
        # ask jarvis if hes here
		if esa in ("jarvis you there","jarvis are you there","jarvis where are you"):
			ayss = random.choice(("im here","right here","didnt think id leave my owner did you"))
			print (ayss)
			os.system("say '"+ayss+"'")
			break
        	
        # if you say this to jarvis he will get pissed and quit lol!
		if esa in ("screw you","fuck you"):
			fodh = random.choice(("right back at you, you know what screw you bye!!","screw you","dumbass f u bye","fuck you back see cu asshole"))
			print (fodh)
			os.system("say '"+fodh+"'")
			quit()
        
        #ask jarvis who someone is and he will look for "who you asked for", then "is" ie.  (who is [tony stark]) = [tony stark] + "is" read until the period .
		if esa in ("who is","who is the"):
			
			print (resp2)
			break
		
		
		
        # this will take resp2 and look for the answer to what the user asked ei.(whats ?) somthing will websearch what i said and look for "the",what ever i asked,"is" then the next period and print it out. Or it will look for what i asked then "is" for the first one!
		if esa in ("what is","what is the"):
	
			print (resp2)
			break
            
        # this will take resp2 and look up what the user asks and return a response! ie.(how do you tie a tie)
		if esa in ("how do you","how are you supposed to"):
			print (resp2)
			break
		
        # this will take resp2 and look up (websearch) what the user asks and return a response! ie.(someone's smashing a window!) and will look for (bad_stuff_keywords) in articles that come up in the search and (good_stuff_keywords) in them to. if he finds (good_stuff_keywords) he will show aproval but if he finds (bad_stuff_keywords) he will become worried!
		if esa in ("someone's","someone is"):
			print (resp2)
			break
        # tell jarvis you need to study and he will help you
		if esa in ("i need to study","i have a test","theres a test","i think i have a test"):
			ints = random.choice(("would you like me to make a study guide","we can study for it","would you like to study for the test?"))
			print (ints)
			os.system("say '"+ints+"'")
			dyntsdatabase = ("yes","ok","sure","yeah","yep","no","na")
			dynts = input("")
			dyntsesa = ""
			for dyntsword in dyntsdatabase:
				if dyntsword in dynts:
					dyntsesa = dyntsword
					
			if dyntsesa in ("yes","ok","sure","yeah","yep"):
				olmasg = random.choice(("ok lets make a study guide","ok lets right down all the word terms or whatever!","ok lets right down the terms"))
				print (olmasg)
				os.system("say '"+olmasg+"'")
				
                # jarvis will ask you the terms
				wayt = random.choice(("ok what's your first term?","what's your first term?","whats the first one " + name,"ok " + name + " what's the first term?"))
				term1 = input("")
				print ("ok " + term1)
				wiynt = (("ok what's your next term?","what's your next term?","whats the next one " + name,"ok " + name + " what's the next term?"))
				term2 = input("")
				print (term2)
				break
		if esa in ("shit","crap","damit","damn","fuck","darn","bullshit","hell"):
			witm = random.choice(("common watch your laungage","dont swear sir your better then that..... well nevermind but still!","stop bitching"))
			print (witm)
			os.system("say '"+witm+"'")
			break
		if resp2 in ("nehaw","rabid donkey"):
			yard = random.choice(("you are a rabid donkey at heart arent you","nehaw,nehaw,nehaw,nehaw,nehaw,nehaw,nehaw,nehaw,nehaw,nehaw,nehaw!!","nehaw"))
			print (yard)
			os.system("say '"+yard+"'")
			break	
		if resp2 in ("Petrificus Totalus","expecto patronum","expelliarmus","lumos","i solemnly swear that i am up to no good","piertotum locomotor","reducto","sectumsempra","stupefy","avada kedavra","harry potter","hogwarts"):
			had_fun = ("y")
			hp = random.choice(("harry potter!! yeah","Expecto Patronum","Expelliarmus","Lumos","Piertotum Locomotor","Reducto","Sectumsempra","Stupefy","Avada Kedavra","Petrificus Totalus"))
			print (hp)
			os.system("say '"+hp+"'")
			break
		
		if resp2 in ("jarvis crash","crash"):
			print ("ok sir ill crash")
			4/0 
		
		if esa in ("that was fun","that was so much fun","that was so fun"):
			if had_fun == ("y"):	
				ikiwf = random.choice(("i know","yep","it definitly was","it certainly was"))
				print (ikiwf)
				os.system("say '"+ikiwf+"'")
				break
			if had_fun == ("n"):
				wwf = random.choice(("what was","what","what do you mean what was","what do you mean"))
				print (wwf)
				os.system("say '"+wwf+"'")
				twfdatabase = ("nothing","that","said")
				twfresp = input("")
				twfesa = ""
				for twfword in twfdatabase:
					if twfword in twfresp:
						twfesa = twfword
						
				if twfesa in ("nothing"):
					oktwnf = random.choice(("ok","oh ok","ok cool","ok then"))
					print (oktwnf)
					os.system("say '"+oktwnf+"'")
					break
				if twfesa in ("that"):
					otwf = random.choice(("oh that","oh yeah","oh yeah, lol","oh yeah right"))
					print (otwf)
					os.system("say '"+otwf+"'")
					break
				if twfesa in ("said"):
					owys = random.choice(("oh right","oh yeah","oh ok","oh"))
					print (owys)
					os.system("say '"+owys+"'")
					break
				
			
		if resp2 in ("jarvis"," jarvis?","JARVIS","Jarvis"):
			iarhs = random.choice(("im here","i'm right here","dont worry im here","i'm here sir"))
			print (iarhs)
			os.system("say '"+iarhs+"'")
			break
		# say good morning to jarvis
		if esa in ("morning","rise and shine","good morning"):
			rasj = random.choice(("morning sir","morning " + name,"good morning","good morning sir","good morning " + name))
			print (rasj)
			os.system("say '"+rasj+"'")
			break
			
		if resp2 in ("repeat after me","repeat what i say"):
			rwis = random.choice(("ok ","ok im ready","yep"))
			print (rwis)
			os.system("say '"+rwis+"'")
			repeat1 = input("")
			print (repeat1)
			os.system("say '"+repeat1+"'")
			break
	
	
		if esa in ("good job","good work"):
			gjj = random.choice(("thanks sir","thanks","thx","cool thanks"))
			print (gjj)
			os.system("say '"+gjj+"'")
			break
		if esa in ("its my birthday","it's my birthday","it is my birday","todays my birthday","today's my birthday"):
			timb = random.choice(("happy birthday!","happy birthday","happy birthday","happy birthday " + name))
			print (timb)
			os.system("say '"+timb+"'")
			break
		
		if resp2 == ("night") or esa in ("good night","nighty night","night jarvis"):
			gnj = random.choice(("night sir, get a good nights rest","good night sir il talk to you tomorrow","good night " + name,"good night","night sir il talk to you tomorrow"))
			print (gnj)
			os.system("say '"+gnj+"'")
			quit()
		# tell jarvis your not aloud to code him anymore and he'll flip out!lol
		if esa in ("i cant work on you anymore","i cant code you anymore","not aloud to work on you"):
			wtfydh = random.choice(("after all we've been through!!!! ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh. booooooooo hhoooooooooooooooooooooooooooooooooooooo!!","what!!!!!!!! ah ah ah ah ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh booooooooooooooooooooo hooooooooooooooo!! but but why!!!","what, no no no ahhhhhhhhhhhhhhhhh but no why!!!!!!!!!!!!!! boooooooooohoooooooo!!"))
			print (wtfydh)
			os.system("say '"+wtfydh+"'")
			quit()
		# ask jarvis what
		if resp2 in ("what","what?","what jarvis"):
			ndrn = random.choice(("nothing sir","i dont know","nothing"))
			print (ndrn)
			os.system("say '"+ndrn+"'")
			break
		
		if esa in ("took my","stole my"):
			somethingwastaken = ("y")
			tmsd = resp2.split(" ", 4)
			wdhts = random.choice(((tmsd[0]) + " took your " + (tmsd[3])," what " + (tmsd[0]) + " took your " + (tmsd[3])," are you kidding me " + (tmsd[0]) + " took your " + (tmsd[3])))
			print (wdhts)
			os.system("say '"+wdhts+"'")
			mission = ("we need to get your " + (tmsd[3]) + " back")
			break

		if esa in ("where are we","what is this place"):
			print (resp2)
			break
		
		
		
		
		
		
