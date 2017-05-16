# coding=utf-8

import re
import json

sample_string = '''
05/13/17
-slept in until 11 and layed around in bed for a while on the internet
-ate some leftover pasta and watched some more of the hand maid's tale
-got showered and dressed to go to the night market and then bailed on everyone and just stayed home
-video called Ellen and caught up on each other's lives for a good while
-made some more dumplings for dinner and had a glass or two of wine and watched a tv show on netflix about country cottages and went to bed

05/12/17
-went early into work for an ease meeting followed by coffee with Michelle and then came into the office and did some demos and commitments
-went out to lunch with a good gang of people at gopoke and then ran back to the office for a quick reverse proxy meeting and then basically spent the afternoon doing the puzzle
-walked over to target and called up mummy, picked up my prescription, bought a bunch of stuff at tjmaxx, scored a sweet Scottish flag and ubered home
-had a glass of wine and curled my hair before Tim, Deepak, and Natalie came over and then walked over to a ramen place for food and more wine and meeting KJ
-came back to mine and accidentally stayed there until 2:30am talking, drinking, and making late night dumplings

05/11/17
-came into work and went to umbria with the whole team and came back to the office where i started my behavioral interview training
-had a teary meeting with Mark and found out I'm rotating 3 months early and then went to brgr bar with Tim, Deepak and KJ
-came back to the office and fucked around for a while, did some puzzle, and then went to dan's happy hour where I talked plants and hung out with COFI people
-took the streetcar home with Son Ca and got to work fixing all my database issues with five things after I ran my one time script
-integrated heroku with my app and had a glass of wine before going to bed

05/10/17
-walked into work and had standup followed by a quick coders check in meeting with mark
-went down to the loading dock and had marination station for lunch with the gang and played smash for a while
-messed around the office for a bit and then took the link over to cap hill with Merin and passed some time at goodwill
-went and saw our first apartment which was just okay and then hung out in cal anderson park to cool down before going to house number 2 and falling in love
-walked over to house number 3 which was okay and then walked over to manao for dinner and then came home to apply for the house and freak out with merin before getting ready for bed

05/09/17
-got up slowly and went into work for a quick standup and dealt with some hackathon stuff
-got poke for lunch in occidental where we all got in a pretty heated argument and then made up and were bff's again
-came back to the office and got our doc proc templates working and wrote our sql script
-took the streetcar home and then quickly left to go see a pretty meh apartment and then walked around a bit enjoying the sun before seeing another slightly better apartment
-walked around cap hill a ton, stopped in goodwill and then came home where me and Aimee decided to add a third roomie, Celia, who we talked to for a bit and then i did a bit more on five things before going to bed

05/08/17
-woke up and walked into work in the sun and sent out the big scary hackathon email invite
-went to grand central with merin where we ate super yummy goats cheese and beet sandwiches and talked about love languages
-came back into work and dug more into the stupid doc proc stuff and made more progress before street car'ing home
-got home and worked on five things for a bit and then started skyping with Katie and Brittany where we talked for ages about everything and anything
-finally said goodnight to the girls after a few glasses of wine and went for a shower before going to bed

05/07/17
-slept in on Aila's couch and then we went over to a cute pastry shop for breakfast and career talk
-walked around bellevue and did some shopping and went into the mall where I bought a few clothes and then took the bus back over to Seattle
-got off in westlake and did even more shopping and then came home and scarfed down my leftover pizza
-emailed a bunch of apartments and then Aneesha came over and we took up some leftovers to the roof, soaked up the sun and painted our nails
-walked over to goodwill for an unsuccessful trip and then over to Hot Cakes for yummy dessert and then came back home where I worked more on Five Things and got user specific accounts working!

05/06/17
-slept in and then got ready for the sounders game and then uber'd over to the stadium with Aneesha where we eventually made it inside to our seats
-watched a super fun game with really good seats and then took the streetcar back to my apartment where I decorated my pavlova and chilled for a minute
-took the bus over to bellevue with Aneesha and dropped off some stuff at Aila's before taking another bus to an indian market and then ubering to dinner
-ate an expensive pizza at Vivo 53 with Aila, Taylor, Maxim, Jeremy and Aneesha and watched them eat monster milkshakes
-walked over to Aila and Taylor's place and finished up our game of Outlast2 and ate pavlova and hung out before I got to crash on Aila's couch again 

05/05/17
-slept in and then spent the morning in bed trying every possible solution to my five things app before giving up for the morning
-went over to qfc and picked up some pavlova supplies and whipped a quick pavlova and then made some Italian sausage pasta for lunch
-walked downtown to the office where we all tested for a bit and then grabbed some yummy thai food and had some equal parts beer/tequila margs that mark made
-got pretty tipsy and hung out with the girls talking and then snuck around the office before playing a bit of smash
-got pretty giggly with merin, erin and mark making our fictional characters and then had the rest of the gang join in where we made up a crazy story and then finally wrapped up and merin dropped me home

05/04/17
-walked into work in the fog and went to a town hall by Yvette followed by another town hall for armada where we all got confused
-went out for Ardon's birthday and sat out in the sun with Ardon, Merin, Jeff, Brooke, Nik, and David and then stopped over at umbria for some gelato
-came back into work and drafted up our invitation to hack the dash and then went over to fx mcrory's with son ca and erin where we ate a ton of appetizers, drank wine and schmoozed with Yvette before streetcar'ing home
-got home and decided to start working on five things (while tipsy) then started to pretty sick (bad appetizers?) and took a nap to feel better
-stayed up late programming five things and didn't make it very far thanks to shitty JS

05/03/17
-walked into work and went to a few meetings and started talking to Nagkumar about my five things app
-ate my leftovers and played smash with the gang before messing around for a while
-went to an ease meeting and then bugged a bunch of people about PDFs before working with Nagkumar on python and streetcar'ing home
-went up to the roof and enjoyed the sun for a bit before getting changed and heading over to aneesha's where Sumit picked us up and took us to golden gardens
-huddled around the bonfire and met a few of sumit's friends and drank wine before coming home with freezing cold, black feet and hopping into the shower

05/02/17
-woke up and headed into work for a quick ease standup followed by a quick(er) fuji standup and then did some troubleshooting our api's and called up ease and they found their mistake
-heated up my lunch and went to occidental with merin where we ate in the sun and gossiped a lot before catching up with kj and natalie
-went back to the office and messed around for a while, started looking into pdf stuff and then walked downtown with erin, tara, eisha and son ca
-talked to a bunch of volunteer groups and hung out with some c1 girls before walking over to uber hq and listening to a good panel about culture in tech
-headed home (with some leftovers) and painted my nails, watched some handmaid's tale and then went to bed

05/01/17
-walked into work for another ease standup followed by an extremely long standup where we groomed a shit ton of stories
-got to work removing all of rekha's formatting on her api and then ate my lentils in the office and played a good bit of smash (and kicked some ass!)
-added a new helper function to our APIs and finished up the tidying of our endpoints
-streetcar/bus'd home (thanks mayday) and spent ages working on potential poster and logo ideas for our hackathon
-ate some lentils and had a glass of wine and watched some tv before heading into bed

04/30/17
-slept in after a late night out and then ate breakfast before riding the bus up to interlaken park and then into the arboretum
-collected quite a few pinecones and explored the other side of the arboretum and then made my way over to the japanese gardens
-walked the gardens and then snuck into a private tour where I learned a lot about the trees and the koi (thanks to the koi and pond experts hehe)
-took the bus over to trader joes where I bought a shit ton of food and then walked all the way home with my heavy bags
-made a thai curry with burnt rice (lol) and then made my lentil curry for the next day before settling into bed with a glass of wine and the handmaid's tale tv show

04/29/17
-woke up early and snuck out of aila's apartment for the bus ride back to Seattle and then chilled in bed for a while
-walked around cap hill with aneesha before settling on eltana's bagels and then took an uber down to Renton
-looked at a ton of couches and other assorted furniture (and was shocked by aneesha's taste) and ubered back up to Seattle where i messed around the apartment and curled my hair
-headed over to tim's place where i met him and his friends and went into cap hill to see Nagkumar and then settled in at capitol cider
-drank a few green ciders and had good talks before walking over to dicks and grabbing burgers and fries and then walked home and ate my burger and went to bed

04/28/17
-walked into work and then ubered downtown to the code writers workshop where i sat next to my friend from the night before and listened to nick do the keynote
-listened to a really good talk on negotiation and then quite a few really shitty talks then had a decentish lunch and avoided talking to non capital one people
-moved to the back of the room with ardon and sat through a bunch more boring and long talks before walking home in the sun with tim
-took the bus over to bellevue where i had the privelege of meeting "mr. wright" and then met aila, taylor, jeremy and maxim at MOD pizza
-headed back to taylors apartment, drank a lot of wine and played outlast 2 and screamed a lot before crashing on aila's couch

04/27/17
-woke up earlier than usual for an earlier standup and had a reverse proxy meeting where i mostly followed along
-went to lunch with two of Natalie's mentees and mostly played two truths and a lie and then went back to the office where we started onboarding our api's 
-had some mini photoshoots and printed lots of pictures of the team and then redecorated the office a bit before heading downstairs for a happy hour
-had some yummy tacos, drank a lot of wine and had some forced conversations with strangers
-hung about in the office a bit with tim, nagkumar and natalie before taking an uber home with a lot of leftovers and continued to drink wine and dance by myself

04/26/17
-had both my standups and then worked with ardon and mark to get the reverse proxy up and running again
-had a candidate lunch with super yummy mexican food and played smash where i won the marbles with a cheeky kill :) 
-went to a quick meeting and messed around for the afternoon before taking the bus up to wallingford and stopping into the glass studio to do some quick soldering
-walked around wallingford and bought a variety of essie nail polishes on sale and grabbed a dick's burger for dinner
-went back to the studio for class where we putty'd our windows and finished them up and I ubered home exhausted and showed off my panel to nada before going to bed super tired

04/25/17
-woke up and walked into work and had two boring stand ups before gossiping with ardon for a while and going to more and more api meetings
-had a delicious bbq lunch with armada where we kicked butt playing charades and trivia and then went back to doing nothing
-met up quickly with Natalie and then went to more extremely dull meetings about apis and finally went home
-ate some leftovers and then walked over to capitol cider where I met Julie for a few ciders and getting to know each other
-left cap cider and walked up to dicks and saw some police civilian violence, picked up some fries and then ate them while gossiping in cal anderson park

04/24/17
-woke up and took a shower and got ready, then walked with mum all the way to pioneer square where we said goodbye for a while and then i continued to work
-had two quick standups and then answered a bunch of emails and worked with erin and ardon for a bit before going to lunch at pho fuscia with Merin and Yasha
-came back and finished up a super quick story with ardon and then gossiped the rest of the afternoon away
-came home and messed around on the internet before walking over to qfc and picking up some more wine and cereal lol
-drank the wine and ate some leftovers, cleaned out my okcupid messages and continued messing around on the internet before showering and heading to bed

04/23/17
-woke up early again and once more went to eltana bagels before taking an uber up to freemont and bumping into Taylor
-walked around a bit and then started our lovely and yummy tour of theo chocolates and then did a proper look around of the Sunday market and popped into the freemont vintage mall
-walked back over to nosh for delicious fish and chips, sampled some gin and brandy and then walked the long way over to ballard in the freezing rain 
-made it to ballard and did a bunch of window shopping and walking in the rain and finally stopped in macleods for a drink and a moment to dry off
-froze our butts off at the bus stop and finally made it back to seattle where we did a bit more window shopping and then walked back home where we made more cocktails and had some good girl talk before going to bed

04/22/17
-woke up early with mum and headed over to Eltana's to try a variety of new cream cheeses and then unexpectedly join the march for science in cal anderson park
-got too cold in the march and headed up to the arboretum via bus and walked around all the lovely cherry blossoms and rhododendrons and then all the way up to the u district
-stopped in a Starbucks to warm up a bit, did some shopping and then got a bus back to capitol hill where we stopped for ice cream at cupcake royale
-came home and headed up to the roof where we made some fancy custom cocktails (lots of muddling) and enjoyed the wee bits of sun while they lasted
-slightly (quite) buzzed we went out to cap hill to find dinner and settled on pettirosso which was alright in the end and then headed back home
-watched some netflix together and then got super super sleepy way to early, skyped with Katie and Brittany from bed 

04/21/17
-woke up and went said bye to mum and went into work where i had a super long retro where i paid little attention
-watched some oculus demos before meeting mum and going to lunch at intermezzo where we ate delicious beets and then had our main courses which were totally fabulous
-took mum back to the office for a super quick tour and then said bye and went back to "working" with the gang
-got the streetcar home and met mum and we went for a walk around cap hill stopping at goodwill and then going all the way up to volunteer park after looking at lots of gorgeous houses and then taking a bus back down
-ate another fabulous dinner at machiavelli's with a glass or two of wine before heading up to pie bar for super yummy cocktails and then headed home to chill for a bit before heading to bed

04/20/17
-went into work in the sunshine and had my two standups before doing some more unit tests 
-ate some leftover pizza for lunch and played smash with the gang before finishing up some more testing
-messed around with the gang before taking the streetcar home and doing some last minute cleaning around the apartment and then going to cap hill to pick up mummy
-walked mum back to the apartment and dropped off her stuff and went to dinner at a thai restaurant that we had been to before when it was "boom"
-walked over to tavern law where we went up to the speakeasy and had some yummy custom cocktails made for us and gossiped for a while before heading back to home and falling asleep

04/19/17
-walked into work in the rain, had two standups, tried for ages to merge all of our code while being pulled into a meeting i didn't need to be there for
-had an interview lunch with a friendly candidate and then took him downstairs to play a bit of smash 
-ate more free random office food and worked more with mark and Rekha to finally get the code merged
-took the link home thanks to a mariners game and caught up with mum on the ride home before ubering up to my stained glass class
-learned how to solder, watched Alyssa nearly pass out, spent a ton of money on supplies, and headed home in the rain exhausted

04/18/17
-walked into work and went to my two standups and then worked with mark writing unit tests and making shit work
-went out in the sunshine to occidental with erin, Merin, Rekha and Yasha for poke before coming back and playing smash
-went to a dull meeting and then to Nathan's virtual reality world meeting before heading on home where I got a call from Stephanie and caught up with her on her new life as a mum!
-called up Alyssa and had our monthly catch up call while we both cleaned up our apartments
-ate leftovers from work and watched netflix before heading right to bed

04/17/17
-woke up early for my two standups (in fuji's we mostly just looked at Nathan's amazing demogorgons) and worked a bit more on my API adding a new feature
-grabbed lunch with tim from the food trucks and then brought it back to the office where we played smash and hung out
-fucked around for the rest of the afternoon, showed a TDP around for a bit, and gossiped the day away
-headed home where my new bookshelf had arrived and then spent ages assembling it and arranging the stuff on it
-felt kinda crazy so i made myself a cocktail and watched netflix and messed around on the internet before going to bed

04/16/17
-woke up and got ready and walked over to Witness for brunch with KK and her friend Julie
-walked around cap hill for a bit and then over to volunteer park where we sat down and made daisy chains and soaked up the sun
-came back home and messed around in the apartment for a while doing nothing
-cleaned up the apartment after nada's friends had been living in it for a while and did some laundry
-picked up a pizza from dominos and ate nearly half of it before watching netflix and then heading off to bed

04/15/17
-woke up and showered and took an uber to the stained glass studio where i finished leading my piece and talked to/creeped on the hottie working there
-walked over to the u district for some shopping before stopping at UW to admire some cherry blossoms before taking the link to capitol hill for more shopping (2 goodwills and 2 urban outfitters in one day lol)
-picked up a Starbucks and hung out on the roof in the sun for a bit before heading back inside and cleaning up the apartment a bit
-caught a ride from matt and Chris over to mox in bellevue to hang out with aila, taylor, jaime, kayla, Devin and emily for cider, coup, and codenames
-got back to Seattle and headed over to Tim's apartment where i met his flag football team, drank beer, and ate oreos before heading home

04/14/17
-woke up early and got ready and ubered up to the u district where I met my uber BBF, Valentina at Morsel where we took our biscuits back to her place and got to know each other better
-she dropped me at the stained glass studio where I worked for five hours on leading my piece (not easy!!)
-spent 30 mins trying to get an uber and finally got home and then took a bus over to Kirkland to see Merin
-went over to her apartment and watched her make onion and paneer pakoras, called the slightly drunk family and caught up with them
-ate pakoras until i felt like exploding and watched house hunters international with Merin and finally got to meet Ajay before getting a ride home from Merin

04/13/17
-went into work and had a standup and a retro and was able to make really good progress with mark on my unit tests
-went to occidental park with Ardon, Merin, Yasha and Nagkumar and then brought back our fajitas to eat while playing smash
-finished up my unit tests and then fucked around for a bit before taking the streetcar home
-took an uber with aneesha to Belltown pub for much better service and meeting a few fellow Texas exes
-walked over to world market and had a slightly buzzed shopping trip before ubering back home and falling right asleep

04/12/17
-walked in the rain, had my two standups, ate breakfast in a tdp meeting where we all didn't pay attention before doing some quick test work with mark
-went down to marination and picked up my fave salad before killing it in smash
-interviewed Michelle with mark and actually had a lot of fun before getting back to writing tests with mark and then finished off the day with some catching up with Merin
-took the streetcar home, ate some quick leftovers and then ubered over to stained glass where we learned how to lead our glass (omg so much information)
-got an uber home where I met Valentina thanks to our crazy uber driver who got in a crash right after i got out of the car, and ended the night with a glass of wine and some netflix

04/11/17
-woke up to another sunny morning and came in for standup(s) and then had to work with blazing noodles to try and sort out their mess
-watched a bit of the finale before going into a call with blazing noodles and then went out with David to pick up some lunch from sprout which i ate with David and tim at the office
-hit a roadblock with testing and mostly faffed around for a while before taking the streetcar home
-walked over to goodwill where i scored on a polaroid frame and then walked over to serious pie with nikhila where we found out it was restaurant week and had a delicious 3 course meal
-said bye and headed home where i went upstairs to the roof and finished cutting my stained glass pieces and then went to bed early

04/10/17
-came in early for my two daily standups and then did more work on the api
-went to lunch with tim, David and erin at a new sushi place for some decent sushi and good conversation
-missed some tournament games but still managed to play smash for a bit before walking over to the stadium with tim
-froze my butt off "watching" the baseball game and mostly talking to erin and tim and then got rained on walking back to the office before splitting an uber home with erin and tim
-got home and called Katie and Britt and then decided to skype Aimee from Australia and then went over to aneesha's for frozen Italian food and lots of good convo before canceling on nahkila and picking Aimee

04/09/17
-woke up and was picked up by aneesha and aila and went up to freemont for the Sunday flea market where we ate tamales and fish waffles
-walked around freemont and window shopped before stopping in the freemont vintage mall and picking up some art
-was dropped back down at my apartment where i hit up goodwill and called mum and dad for a bit and got some dealz
-came home again and cleaned up a bit around the apartment before cooking a bunch of dumplings for dinner
-got into bed and watched a few episodes of girls with a glass of wine before going off to bed

04/08/17
-woke up early, showered and took my supplies up to the roof where I started to cut out most of my stained glass pieces with about 90 percent success!
-headed out to cap hill to meet nakhila for molly moons where we talked a bit about expectations and our lives before starting to walk around all of north capitol hill
-called a few places and even got to tour one with nikhila and then took an uber over to Natalie's place for her housewarming party where i had a few glasses of wine, made some window clings, and hung out with James Pak and Deepak
-went out with the party gang to soi for more thai food and laughter with nabilah and Elyse followed by a stop at stout for no drinks and a sprinkling of Maddy drama
-went over to cupcake royale with Elyse and nabilah for my second ice cream of the day (uhoh) and then headed home exhausted

04/07/17
-walked into work again in rain and had a quick ease standup followed by the teams demo's and a retro
-felt like a zombie and grabbed a quick lunch with Eisha and Merin from cherry st and came back to play some more in the smash tournament
-fixed some more api's and sent a bunch of emails before heading to good bar with the tdp gang for a glass of wine before taking the streetcar home
-got absolutely soaked picking up an orchid and went to aneesha's to chill in her apt for a bit, and then went out to basically get kicked out of a restaurant and then found a new yummy thai place instead
-went back to Aneesha's place and slowly built half of her furniture before going home super tired

04/06/17
-walked in the rain and figured out my fancy new raincoat hood and then had an ease api meeting that got pretty heated between jenn and mark
-had some more meetings and found out i'm being taken off of demogorgon and put onto the ease api project as a "hot potato" and then talked grpc stuff
-dove into work on the ease project, grabbed a quick lunch with Ardon, got kicked out the first level of the smash tournament and finished up my work on the api for the day
-caught up with tim and parth for a bit before walking over to occidental park to do some really fun sketching and then meeting up with Natalie and Deepak where we headed towards cap hill
-hit up momiji and had a gorgeous roll before walking to trader joes (and calling Katie+Britt), and then taking our wine back to nat's apt for catching up, ten down, talking to drunk Adan and then walking home

04/05/17
-walked into work in the rain and spent all morning answering emails and coordinating things which actually felt productive
-went to lunch with Merin and Yasha where we brought back our Peruvian tacos and ate them while watching and playing in the smash tournament (where i beat erin and advanced!)
-did more emailing and helped out with other stories and then waited around till 5 with mark for tony who didn't show and then got some gossip from mark about potential reorgs before catching the streetcar
-got home and ate a quick snack before getting all my crap together and ubering up to Wallingford for the second stained glass class where we picked out our glass and cut out our patterns
-took another uber home (this time with tons of glass and hands totally full) and then basically collapsed into bed

04/04/17
-maximized the lying in bed time and then finally got ready and walked into work where i had a nice free breakfast
-did some work with erin on transitions before going to a lunch meeting about the ease api
-got back to work with erin and made some good progress on the navigation mobile view and went to a quick armada meeting before heading home for the day
-sketched out a few more stained glass designs before finally choosing two and sketching them out on the final pieces of paper
-made some dumplings and climbed into bed with a glass of wine and watched some girls episodes and read my new bohemians book 

04/03/17
-really struggled with getting out of bed and then went into work for standup and then 'worked' with Ardon on fixing an environment
-gave up on that for a bit and picked up lunch from a Peruvian food truck and brought it back to the office to eat and play smash
-worked with mark and Ardon and still failed to fix the environment before having a really productive ten-ten with mark and then catching up with erin
-took the bus to bellevue with Merin where we hit up a home depot and bought some plywood before doing some shopping in rei and then looking at every single thing in home goods
-Merin dropped me home and I made a quick grilled cheese and watched the walking dead with a glass of wine before bed

04/02/17
-woke up around 9 and got ready then walked to pacific place where i met up with matt, Chris, emily and Devin
-watched the film, ghost in the shell, which was pretty good and then walked over to the brand new din tai fung where we ate a shit ton of dumplings and pork buns
-said goodbye to the gang and went into forever 21 where i rummaged through the apocalyptic 3rd floor and ended up getting two shirts (one for free, some good cashier karma) 
-walked back up to the apartment and decided to rearrange all the furniture (then quickly decided not to and moved it all back), called mum for a wee bit and did some much needed cleaning in my room 
-ate more leftovers and finished off my netflix binge and showered and went off to bed

04/01/17
-slept in again and lazed around the apartment for ages watching girls and online shopping
-ate some leftovers and then went for a walk in the sun over to the urban outfitters in cap hill just to pass the time
-walked back home and continued to do nothing and just fuck around
-started watching a new show on netflix (an honourable woman) which i binge watched half the series in one sitting with a glass or two of wine
-headed into bed and sort of talked to Shonagh over whatsapp and found a new butterfly friend

03/31/17
-slept in again and then quickly showered and got ready and met up with aneesha and her her mum
-had some yummy eltana bagels and caught up with her before taking her and her mum on a walk around capitol hill
-headed back home for a bit before going back out into the sunshine, caught up with mum and the fam on the phone while walking over to goodwill and then back to the apartment before walking downtown
-did a bit of un-fruitful shopping before walking over to the office where i met the team for a deployment, played lots of smash, ate quite a few tacos, and drank some beers from nagkumar's kegerator (lolololol)
-after not too late of a night we all headed home and Merin gave me a ride home

03/30/17
-slept in all morning and had a shower and a big bowl of cereal before walking in the sunshine to work
-bumped into Merin and Yasha on their way to lunch and joined them at grand central before going back into the office to work with erin for a bit
-went to a haleakela meeting where i learned a ton about the mobile app and then came back to our desks and played a bit of smash and messed around
-headed downstairs with mark, erin and Ardon and tried our hardest not to mingle and instead ate yummy yummy food and quickly finished off their wine
-eventually was forced to do some networking before the night was over and then watched mark and Jamison and ying try some extremely hot sauce before streetcar'ing home with erin where i drank some wine and went on chatroulette before bed

03/29/17
-walked in a lovely mist into work and sat through the worlds longest meeting
-grabbed nosh in the mist and brought it back to the office to eat with Merin, Yasha and erin and did a bit more work before ubering over to suika with Deepak, tim, parth and David
-had a glass of wine, some poke, edamame and a macha creme brule before ubering up to my very first stained glass class where i had my hand at cutting glass (only bled a little!)
-walked to the u district and finally met up again with a now much drunker David, Deepak and tim where we squished into the busiest bar ever and complained the whole time
-finally got the hell out of the college shit show and came back to my apartment and brought a box of wine up and had a few more drinks and talked for ages

03/28/17
-walked into work and had standup and then went to work with Ardon trying to do some automated test api mockups
-went to occidental park with Ardon and Merin and brought back an eggplant dish to the office to eat and play smash
-worked more with Ardon and then teamed up with mark to really make progress on the mock APIs 
-took the streetcar home with erin and ate some leftovers while catching up with mum on the phone
-started tracing out a bunch of stained glass patterns for my class tomorrow, had a glass of wine and watched the walking dead and girls before showering and going to bed

03/27/17
-walked into work and had an informal standup before getting back to work on the navigation with erin
-picked up a falafel salad from occidental with Ardon and then walked to the office to eat and play smash
-did more work on the second level navigation with erin and eventually took the streetcar home
-watched a bit more of girls, surprisingly had a conversation with nada and ate leftovers for dinner
-climbed into bed with a glass of wine and watched grand designs and chilled out before going to bed

03/26/17
-slept in again and ate a bowl of cereal and lazed around in bed doing nothing
-watched a lot of Girls and did more lazing in bed and cleaned up the kitchen and living room
-made myself another lentil curry and enjoyed that and then called up Ellen to talk about interviews and studying
-caught up with JT on skype and ate some more lentils and then went back to watching more Girls
-had a glass of wine and lazed more, watched more girls, then took a shower and went to bed

03/25/17
-woke up to sunshine outside and then took a shower and got ready for the day
-met up with matt and Chris at cal anderson park for some frisbee tossing and some molly moons in the sunshine
-after laying on the ground in the sun for a while I headed home to chill out some more until meeting up with emily and Devin and ubering over to Belltown brewery for wine, a whole yummy pizza, and seeing matt, Chris and will
-after dinner moved over to Belltown pub for the worlds slowest service of all time, and eventually a glass of wine
-walked over to black bottle and had a couple of really really yummy cocktails, good convo, suddenly getting the spins, pretending I felt fine, and eventually taking an uber home

03/24/17
-walked in the rain to work and had a quick demo/retro before driving to cap hill as a team for a panic room
-we escaped the room with 2 minutes to spare and headed back to pioneer square where me, erin, Merin, Georgi, and son ca had lunch before heading back into the office
-did a bit of work with erin, assured Merin that i don't hate her and then headed home for the day pretty early
-got changed and took the bus from downtown over to bellevue where I met Aila, Taylor, Maxim and Jeremy for sushi and then headed over to a housewarming party
-played a bit of secret hitler, talked to a bunch of strangers, drank cider, accidentally bumped into nada (YES) and talked about potato cakes for ages with Jeremy and maxim before ubering back to bellevue and then ubering all the way home to Seattle at 2:30am

03/23/17
-came into work and did more work on stupid unit tests before going to a quick reverse proxy meeting 
-had a lunch meeting in which i was barely involved and then ate some bbq leftovers and played smash where I'm ranked as #2 
-got back to work, this time with help from mark and Ardon and made some small progress and lost a lot of will power
-took the streetcar home and then hit up qfc where i happened to bump into nada and picked up a bunch of brownies supplies
-started cooking the brownies and beer (first batch of brownies were a total failure) and watched girls and then frosted the decent-ish brownies

03/22/17
-walked into work and had standup as usual and then me and erin started trying to write unit tests
-had some super super delicious BBQ for a candidate lunch with the team and then played some smash and won the marbles game
-got back to work on the super frustrating tests with erin and got some help from mark and Ardon
-took the streetcar home and watched jane the virgin, painted my nails, smudged my nails, burnt some dumplings and watched bake off
-had a couple glasses of wine and got on chatroulette and ended up talking to one guy for ages and looked through our old tumblrs

03/21/17
-walked into work and had a quick standup before getting to work with erin and mark where we fixed the api and then reorganized our code 
-went to lunch with Merin and Yasha where we grabbed super yummy vegan food and ate it in the grand central basement and made a big yummy sloppy mess
-came back to the office, played a bit of smash and then optimized our code a bit and then started styling it
-after an actual long day of work, me and erin took the streetcar home and i ate some leftover pasta and talked to mum on the phone and caught up with each other
-started to catch up on jane the virgin and also on the walking dead with a glass of wine, then took a shower and went to bed early

03/20/17
-walked into work and had standup and then started up again on the search bar with erin
-was accidentally left behind by Merin and Yasha, so i played smash until they brought me an incredibly messy hotdog and we ate downstairs together
-ran into a bunch of problems with our code and had mark help us and then felt like we had a 100 more problems to solve
-took the streetcar home with Ardon and then got a call from Alyssa and we finally caught up on each others lives as I made myself dinner
-had a few glasses of wine and messed around on the internet before showering and heading to bed

03/19/17
-slept in again and woke up to a lovely sunny day, got dressed and packed a bag and walked over to eltana for a delicious bagel and a sad attempt at the crossword
-headed out on my walk towards volunteer park and soaked up the sun, bought a ticket and walked around the conservatory and admired all the pretty pretty plants
-found a sunny spot with a great view and finished my lena dunham book and then began my walk back 
-picked up a starbucks drink and headed up to the roof to enjoy the sun some more and catch up on these entries
-came back into the apartment cooked up some brussel sprouts and worked on styling my madlibs app over a few glasses of wine before going to bed

03/18/17
-slept in as much as I could to pass the time and then got up and cleaned up the apartment for a while
-finallllyyyy did laundry (way overdue) and hung around the apartment for a while doing nothing
-decided to go for an unexpectantly cold walk around the central district to pass the time
-came home and booked tickets to cancun and talked with the family before heading out to rockbox to meet the gang for karaoke
-sang our hearts out, drank champagne + jello shots and then headed over to lost lake where I drunkenly ate a whole cheeseburger and spilled my heart out about my Seattle loneliness and got mildly helpful words in response, and then walked home crying and faced another minor breakdown before bed

03/17/17
-went into work for another typical retro and then had my one on one with nick peddy which was pretty bland (as was expected)
-went to a lunch meeting for the greasiest pizza in the world, a lazy designer, and a decision that should have been made months ago
-talked with erin a bit about demogorgon and then worked on the release with Ardon for a while and mostly just hung out
-ended up splitting an uber home with James Pak and had the usual weird convos with him before getting home and eating leftovers
-watched moulin rouge, sang along and drank wine, messed around on the internet, and had another semi-breakdown before going to bed

03/16/17
-woke up and showered and walked into work in the sunshine and then got to work with Ardon on a last minute maintenance fix
-played smash first and then went at one with Merin and Yasha to il corvo where I filled them in on my crazy antics of the week
-came back in and finished up the story, messed around with Ardon, and decided it was too sunny to be in the office so I took a lyft home
-took my book up to the roof and chilled for a bit before walking to the station and riding over to UW where i walked around for a bit before making my way to the Neptune to surround myself with teenagers and awkwardly dance to the opening act
-waited a bit more then MØ came out and i sang my heart out, was right up at the front, danced like crazy, held her hand, supported her legs as she stood on the barrier, sang to each other directly, and finally grabbed the setlist before taking the link/lyft home and going to bed exhausted

03/15/17
-got to sleep in on a Wednesday :) and then got dressed and curled my hair before making the final touches to my second pavlova
-walked into work with my pavlova around 2pm, shared the pavlova and chatted for a bit with everyone before going to the geekwire bash with son ca
-we got registered and walked around the various booths, ping pong tables, dodgeball games, etc and had a beer and some tater tots and just kind of observed some of the Seattle software engineer culture
-split an uber home with son ca and right as i was about to open the front door to my apt was stopped by an amazon delivery driver who needed into the building and then ended up helping him deliver packages to a few floors before giving him my numbah :)
-got into my apt and had a call with Brittany and Katie and then got a text from Roman wanting to go out, so I crazily said yes and he picked me up and we then walked to capitol cider for a few drinks, getting to know each other (interesting guy but not for me), and then came back home feeling like a crazy person for doing something so out of character

03/14/17
-walked into work and got to work with erin where we worked on some demogorgon stuff and a fix for an obscure page's formatting
-ate some of my leftover poke from the day before and played some smash with the gang before helping Nagkumar a bit with his VM and getting it nearly perfect!
-????marko widgets????
-took the link home from work and stopped in at goodwill where i picked up a few new books and shopped around for a bit before walking home
-came home and cooked up another pavlova with my leftovers and then cooked curried lentils for dinner
-drank some wine, watched the film, Lion, and then had a small breakdown about life in Seattle, cried in the shower and finally made it to bed

03/13/17
-really didn't want to wake up thanks to daylight savings and then walked into work for another uneventful standup and then some demogorgon work with erin
-walked to the ID and picked up lunch from the poke place and came back to eat it in the office and watch smash and help Nagkumar with his dev vm
-got down to business fixing some css bug with erin for ageeess and finally finally got it working around five
-took the link home and got to work decorating the pavlova (which turned out great!) and then walked over to my bumble BFF, Jackie's place where i met a ton of bachelor people talked to a few, drank wine, ate cheese, tried some new secret starbucks drinks, and watched the bachelor
-served up my pavlova (genius idea) and then befriended some of the really drunk girls before sharing an uber home with them and then walking back from theirs feeling happy and optimistic

03/12/17
-slept in a bit and called up mum and Ellen to get their pavlova recipe
-got dressed and went out into the grey weather and walked to qfc to pick up supplies for my pavlova
-ate some more leftovers and then read my book for a while on the couch and hung about
-put the great British bake off on again and watched while nada tried to make herself spinach for 45 minutes and then got to work on my own bake off, my pavlova
-called mum and Ellen lots for advice and finally put it in the oven where I think it turned out okay(!) and then watched tv in bed for a while

03/11/17
-woke up late with a very mild hangover and went to work making the sweet potato and sausage hash again
-decided to go for a run in the gym downstairs and took the stairs all the way up and was exhausted, hot, and sweaty
-took a long long shower and then skyped with JT for a bit and painted my nails, ate dinner while talking and then said bye
-in the slim chance that nada was going to invite me out as she promised the night before i curled my hair(decently for once!), did my makeup, and then as it got late and no invite came started drinking oj +rum again
-got on good old chatroulette and talked to strangers, listened to the killers, and went to bed a lot drunker than I intended to be

03/10/17
-went into work and got soaked again and then had our weekly retro and sprint planning with the team
-ordered Mediterranean food for lunch and ate it with erin, Ardon, and chey before having a few macaroons and playing smash
-worked with erin some more on the demogorgon and made some good progress even though we didn't need to and worked on nagkumar's vm
-took the link home and tried and failed to get anyone to hang out without me so i started drinking oj + coconut rum, watched grand designs and great British bakeoff etc etc etc
-nada came home around midnight and i sort of confronted her about her not inviting me to things or meeting her friends, cried a lot, admitted my loneliness all the while not impacting how she feels about helping me

03/09/17
-another rainy walk into work where I worked with Ying and Nagkumar on their dev machines for a bit before going to a quick and low key coders meeting
-went on our lunch date with Merin and Yasha at Julie's garden and had a lovely lunch with them
-came back to the office and mostly messed around and then helped Nagkumar again with his machine
-took the link to capitol hill and then walked to my place where i had my leftovers from lunch and watched some always sunny before cuddling up into bed and watching the great British bakeoff
-netflixed a bit more and then talked to strangers on bumble and okcupid before showering and going to bed

03/08/17
-woke up and walked into work for a quicker standup and then helped Nagkumar set up his environment a little and worked with Nathan on his environment too
-grabbed an interview lunch and then got kicked out and proceeded to play smash for a while instead
-had a release planning meeting with the whole team and son ca, called and was intimidated by a TDP from SF, and then waited for an uber with Natalie
-got all the way to her apartment and realized she left her keys at the office so we went all the way back to the office and then back to pick up some groceries at trader joes
-made a super cheesy cauliflower cheese pizza with Natalie with a few glasses of lambrusco and said goodbye and got back into my book and chilled with the rest of the wine before bed

03/07/17
-went into work for another awk standup and then got to work with erin on the testing story again before finally getting to start properly on the demogorgon
-got lunch at intermezzo with the same asshole waiter who was slightly less of an asshole this time and caught up on the office gossip
-worked some more on the demogorgon and then headed home on the light rail and hit up goodwill for some new books and house stuff
-got stood up for Natalie for grocery shopping and hanging out, ate toast and cream cheese, questioned my life in Seattle, etc
-had some wine, settled into my beanbag and read lena dunham's book before heading to bed

03/06/17
-walked into work in a light drizzle, had a super long and boring stand up with son ca and then slowly and begrudgingly got to work on a supras testing story with erin and Ardon
-ordered lunch from amazon prime with Ardon and kicked some ass on smash as the wii fit trainer
-got back to work on the testing and hit a block so we hung around for a while and just kinda bitched
-took the link home because the streetcar is still broken and walked home super quick to catch the start of the bachelor which was just another alright episode
-watched a bit of the women tell all before giving up on it and working on my mad libs app instead

03/05/17
-woke up to more sunshine, took a shower and walked to eltana to pick up the bagels for the party
-came back and did some last minute cleaning before Jon, matt, and Chris arrived and we started on the bagels and mimosas
-aila, taylor, emily and Devin all arrived and we started playing board games, eating more bagels and drinking a lot of mimosas
-played lots of games and eventually said bye to the gang before settling into bed and watching moonlight
-had an impromptu skype call with Katie and Brittany where we caught up on business plans and other life events

03/04/17
-woke up to a little bit of sunshine and started to clean my apartment for the bagels+mimosa party tomorrow
-did more cleaning and ate chocolate and nadas tortillas for breakfast/lunch
-was picked up by Devin and emily where we drove over to total wine and beer and spent 100+ dollars on alcohol
-stopped at citizen for a flight of cider and a yummy dinner before heading over to their apartment in queen anne
-made dirty girlscouts and played a couple of really fun board games with Devin and emily before getting dropped off and then going to bed

03/03/17
-walked in to work and got rained on a bit and had our team's retro for the week
-decided to print out a giant van damme splits poster and spent a while cutting and putting it up on the wall and redecorated my cube
-me and Merin headed out at 2 and took the bus out to Kirkland where we stopped at her place, had an espresso, and then sat in traffic for an hour and a half to get to ikea
-arrived at ikea hella hungry and immediately went to the cafeteria and got some dinner before venturing into the store and picking up a few new things
-super hyper from the caffeine we ran in the wind and rain to the car with our stuff and drove over to home depot just before it closed and picked up a few new plants and then headed home where i showed Merin my place and said goodnight

03/02/17
-walked into work for another awkward standup with son ca, reviewed some pull requests and then had a coffee chat with son ca where I tried to be firm about my projects 
-helped Nathan on his VM and then went over to Nagkumar's apartment for pizza and meeting our new team member at his rooftop
-came back and had some cupcakes, worked on my devVM documentation and then had to take the link home again because the streetcar wasn't working
-hit up urban outfitters and a resale store and got a scarf for my desk and then walked back home
-made a grilled cheese and worked a lot on my madlibs app until i had to go to sleep

03/01/17
-walked into work in new shoes and got crazy blisters and then got to work on our automated test suite with erin
-grabbed a yummy salad from marination station with the team and then played some smash of course
-finished up our automated tests then had a 10:10 with mark where we discussed the impending doom of sonca. 
-took the link over to my favorite goodwill where I was unfortunately unlucky then walked home and ate some leftovers and watched a disappointingly short episode of the bachelor
-had a glass of wine, did some online shopping and caught up on the latest episodes of always sunny and then showered and went to bed

02/28/17
-woke up, showered, and called into standup before driving up to soco with mum to have delicious salads at vinaigrette
-parked the car and did some shopping around the cute boutiques on south congress for a present for caitlin's 18th
-had some amy's ice cream and then drove over to the apartment to charge up my phone, steal some things from Ellen, and say goodbye
-drove over to the airport and said bye to mum and then talked to Ardon for a bit before boarding the plane and eating my salad leftovers
-finally landed in Seattle and actually paid for an uber home where I took a shower and went to bed

02/27/17
-slept in again and then got up and showered before heading up to 24 diner with mum and Andrew for yummy hash brunch
-walked over to the graffiti park and looked at that for a bit before walking back to the car and then driving over to another austin mural for a photo op
-went over to hula hut to enjoy the nice weather and have a drink before driving back down to the house to let Andrew pack and then we took him to the airport
-did a bit of shopping with mum at TJmaxx and homegoods for some shoes and new nail polish and then came back home for leftovers and then got in an insane fight with the family about James' college choice :(
-was rescued up by Katie and we went up to Holla mode to meet Brittany and have one last hang out before i leave and then came back down south where me and mum had a glass of wine and talked it out

02/26/17
-woke up the middle of the night some where in the house shivering my ass off and bought Katie a car wash giftcard before going back to bed
-woke up and went to kerbey lane cafe with mum, Ellen, and Andrew and had a pretty queasy lunch
-came back home and tried to go to dads football but found out it was cancelled so we came back home and i took a nap on the couch
-went with the family to lockout austin where we had to track a rogue agent and stop world war three, which of course we did
-said bye to Ellen and picked up pterry's on the way home where we played cards and hung out for a while

02/25/17
-slept in a bit and then went to see hidden figures at the alamo with the family and had a yummy milkshake and sandwich
-came back home and showered and then drove waaay up to north austin for Stephanie's baby shower where she hadn't even arrived yet
-headed over to half priced books and grabbed a book and bumped into Brittany before heading back to Stephanie's party, which despite being 2 hours in had still not started
-awkwardly hung out there for a while before saying goodbye and going for a drive around austin and then finally making it to flores for dinner with the family
-came back home where me and Andrew rode downtown with Katie and met Brittany at lazarus brewing for a few drinks before saying bye to Brittany and hopping over to sixth street for lots of drinks with Andrew, the nicest jacket in austin, and then lots and lots of puking (thanks gin)

02/24/17
-got an entire row all to myself and slept a wee bit before getting picked up by James and then going back to bed
-woke up and said hi to the family, showered and then headed off to north austin for a round of top golf and then over to flyrite for lunch
-headed south and picked up the dogs and met Ellen at the greenbelt where we found a sunny spot by the water and hung out
-came home and then piled into the car and went to jack allens for yummy tequila drinks, yummy appetizers, and of course delicious ravioli
-moved on to drinking prosecco and played monopoly with the family and totally came back from barely scraping by to winning with nearly 9000 pounds at 1am

02/23/17
-woke up and walked into work where we dug right back into the market identifications and made very minor progress
-ate some leftover lentils in the office and played smash with the gang
-tried again to figure out what was going wrong in our code but had no luck and I gave up for the day and cleaned and rearranged my desk for a bit instead
-took the streetcar home and started to pack up my case and then called ashleigh on skype and caught up with her for a while before going out to pick up sushi and some chocolate
-took my frozen jam and suitcase and walked down to westlake station and took the link to the airport and took a plane ride to AUSTIN <3

02/22/17
-walked into work and had standup and talked about adding the search feature and then got back to work trying to get the market identifications working
-ate a bunch of leftover meats and cheeses from the office for lunch and played smash with the gang
-kept having trouble with the identifications and worked with erin, Ardon and Merin on trying to fix it before waiting forever on uber driver(s) with Merin
-finally arrived at the convention center for the plant and garden show where we saw beautiful show gardens, hung around a bunch of old ladies, picked up some plants, and then walked home
-made some pasta for dinner and got back to work on my madlibs app where i stayed up until 12 working and then finally went to bed

02/21/17
-woke up and got ready for work and then realized i was late for a meeting happening right as i was walking out the door and tried and failed to dial in
-had a standup and worked on testing the bid/ask stuff again before going to a super dull lunch meeting with pizza
-had a big food coma and sort of worked with Merin and Ardon for a while but mostly fucked around
-walked with Merin downtown and hit up target, tjmaxx, and urban outfitters where i got a plant stand for 60% off and then took a lyft home
-ate some leftover lentils and caught up on messages and sort of started working on a new android app

02/20/17
-woke up early as i have been and hung about the apartment writing in this book and cleaned up a bit
-headed out into capitol hill for a haircut at aveda where I got a few inches off and got my hair curled
-walked back home and did some more cleaning and then started to cook some lentils (and burned them) and then started watching the bachelor
-Tried again to make lentils and was much more successful and got to eat my curried lentils while finishing off the bachelor 
-Drank more wine and then had a long tear filled conversation with mum about James and UT before finally changing the convo to talk about Andrews stay and then headed to bed

02/19/17
-woke up and found out James didn't get into aerospace and was sad for him for a while and just kind of lounged about
-got to work cleaning the whole apartment, especially the bathroom, and finally took apart the big ass pile of cardboard boxes filling the apartment
-made a panini for lunch, did laundry and hung up my austin posters over their new position and went about hanging some other things
-watched la la land and listened to the music for a while and started working on a new poster and made pasta for dinner
-finished off the design documentary series while working on my poster and went to bed in freshly clean sheets

02/18/17
-woke up to rainy Saturday morning and lounged about for a while
-took a shower and then walked up madison to look at apartments for aneesha and talked with her for a bit before hitting up goodwill
-got some goodwill deals and walked back home where i "borrowed" some of nada's stained glass supplies and started on another faux stained glass piece
-drank some wine and ate more dumplings, watched more of the design documentary, painted my nails, did a bit of dancing and karaoke
-talked to JT on skype for a while about the bachelor, told him i'm coming to austin and not seeing him (anticlimactic), and caught up after a while of not talking and then went cozily to sleep

02/17/17
-went into work for a few demos and a retro before heading out for my first technical interview with mark which was very interesting
-had the candidate lunch with the team and learned about a bunch of indian games before playing smash
-talked with the team about our hackathon and then did some stuff for the release and chilled with Ardon for a bit
-went to the consensus meeting for the candidate which was super informative and then chilled at my desk for a bit before taking the streetcar home
-made some more dumplings for dinner, watched netflix and chilled out for the night

02/16/17
-came into work where ricks nephew joined us for stand up and then watched me and erin sit around confused
-went to delicatus for the first time with Merin and erin and had a super veggie sandwich and explained what goats cheese was to Merin
-came back and worked with Ardon on our tests but didn't really get very far and then after working on Nathan's vm for a bit headed home
-cooked some delicious frozen dumplings and messed around on the internet 
-drank some wine and watched Donald trumps press release, painted my nails, instagrammed and then went to bed nice and early

02/15/17
-took a quick pit stop into bartells to grab an umbrella for the rainy walk to work and another normal standup
-got to work with Ardon on a DB script and got help from Jeff and shahryar and then had a candidate lunch with the team and played smash
-went to a quick deployment meeting and then messed around for a while before helping christian and then Nathan with their dev VMs
-took the street car home and had a panini and messed around on the internet for a while before calling James and getting to talk to mum and Ellen also
-drank some wine, watched tv, and took a shower before an early night in bed

02/14/17
-woke up and headed into work for standup and then some test writing with Erin
-grabbed lunch togo with erin and Merin from grand central and ate it in the office with newly handicapped Yasha
-went to a phone call meeting and cut out paper flowers for Ardon's wife and then grabbed a free v-day cupcake and finished his bouquet with Merin where we got a bit carried away...
-left work and walked downtown and hit up my usual shopping spots and got some crazy deals at forever21 (five things for 13 bucks!) and then took a lyft home
-drank wine and watched the newest episode of the bachelor

02/13/17
-woke up and walked to work for a casual standup and then started building the basis for the demogorgon app and ate leftovers for lunch and played smash
-messed around drawing demogorgons with erin before going downstairs with the team for the american outback event where we ate some snacks and then got into teams
-did a bunch of silly team challenges which we lost and then headed back up and found out matt is leaving the team
-street car'd home and called Ellen and mum at the same time and talked summer plans
-ate some leftovers and had a cider while applying to a ton of jobs for Ellen

02/12/17
-woke up to some texts from Natalie wanting to hang out so i hopped in the shower and she picked me up and took me to city people's
-city people's prices were insane so we drove over to a lowe's and bought two new fabulous plants and then headed back to my apt to drop them off and then went to TJs for groceries for our brunch
-cooked a super yummy sausage and sweet potato hash and then i walked back to mine for officially arranging and cleaning my plants and having a snack
-met up with Natalie and walked all around capitol hill and all the way up to volunteer park and up the tower to see the sunset over the city
-walked back to her place and grabbed some supplies and then drove over to mine for more cooking and hanging out while her clothes ran through my washer/dryer

02/11/17
-woke up and then realized that my big brothers interview was today and not Sunday and then quickly got showered and ready
-took an uber to the u district and met my interviewer in a starbucks where she asked a bunch of questions and i think i did alright
-did some shopping around the area getting some deals at goodwill and then walked around the UW campus for a bit before ubering back to my side of town
-got dropped off at goodwill number two and shopped around before heading to qfc for some cereal and wine (lol) 
-came back to the apartment and talked to Ellen on the phone for a while and caught up on her life before skyping with aneesha about Seattle and then drank some wine and went on chatroulette

02/10/17
-headed into work for a pretty quick retro followed by a bunch of faffing around doing demos afterwards
-ate leftovers for lunch and played smash with the gang 
-did nothing all afternoon except occasionally talking about the reverse proxy and then headed home nice and early
-came home and picked up my new chair and decided that i had to rearrange the entire apartment, dragged the furniture into five hundred different arrangements and finally settled on one that I really like
-grabbed an uber with Matt and went over to Devin and emily's place for an intense game of scythe, cheese, and wine before heading home and heading to bed

02/09/17
-woke up and faffed about before going into work where we reviewed mark's reverse proxy code
-went to a meeting with the team and discussed milestones for our projects before going to pick up lunch with Merin and Yasha and then coming back to the office to eat and gossip
-came back from lunch and worked a bit on the documentation, gossiped with Ardon, had a minor nerf war, was accidentally shot by mark, and then made our way to the promotions celebration
-did dumb networking and schmoozing in between talking to my friends and eating delicious food
-took home a bunch of free fancy food and wine and brought back Natalie, tim, and Deepak to my place where we ate cheese, drank, sang karaoke and hung out before going to bed 

02/08/17
-walked into work and hung about before having a TDP rotation call and then sort of supervised Erin working on our toggle
-went to another good candidate lunch with the team and ate chicken pot pie and played smash with the team and the candidate
-did a bit more work on the toggle and then worked on setting up Nathan's VM and started typing up the documentation and even stayed a little bit late working on it
-took the streetcar home and called up mum and caught her up on my life and i caught up on hers while eating leftovers and cleaning the apartment
-skyped with Brittany for a while and heard about her life and filled her in on mine and then watched always sunny and had a glass of wine before heading to bed

02/07/17
-walked into work and had a quick standup before going into a coders meeting followed by my EOY review where I got a 8.5 percent raise heyoo
-got lunch with Merin at grand central and really caught up on each others lives
-came back and worked with erin on some unit tests for our last toggle and then headed home for the day
-made my way to qfc where right as i called Natalie bumped into Sylvain and Vivian and then she came and took me to TJs where i had a blast and got a ton of crap
-came back to my place and started cookin with our curried lentils and had good girl talk and gossip and some more lambrusco before saying bye and showering and heading off to bed

02/06/17
-woke up and it was still snowing! walked to work in the flurries and was awe struck by all the snow
-came into work for a lonely standup with erin and then fucked around for a while before going to a meh lunch in the ID with Deepak, tim, and Sylvain
-came back and talked to navdeep on the phone and then did a modal fix with erin and then streetcar'd home
-immediately put on the bachelor ate a grilled cheese and watched the episode with nada
-messed around on the internet and generally did nothing

02/05/17
-slept in and then got busy around the apartment cleaning up sweeping a lot
-started filing my taxes, did my nails, and curled my hair to pass the time
-headed out in the cold cold rain and walked to trader joes to pick up some party supplies before heading over to natalies to hang with a bunch of Natalie and maddy's friends and ate wings and pretzels while totally ignoring the game and even the commercials
-left before halftime and walked over to matt's place to finish watching the game with him, emily and Devin, with chips and salsa and a much more chill classy environment
-finished the game and got a lift home with emily and Devin in the snow and immediately went up to the roof to make a badass snowman and then came back to the warmth for a glass of wine and coziness

02/04/17
-slept in until 10 and then lazed about the apartment for a while
-finally made my home depot purchase using my spot award and contemplated buying that target chair for a good while 
-ate leftovers for lunch and had a lengthy snapchat conversation with Katie and Brittany 
-watched the first episode of lost for some reason and then took a shower and made myself some roasted asparagus and brussel sprouts
-had a glass of wine and watched the movie super bad before messing around on the internet for a while and then going to bed

02/03/17
-walked into work and lead our team's retro for the week and did sprint planning
-went to an interview lunch with the whole team and Natalie and had a very enjoyable time before coming back and playing a little smash
-came back to the desk, did some online shopping and ended the day with helping Nathan set up his dev vm
-came home and ate leftovers while asking for Ellen's advice for a bit and then had some wine and messed around on the internet
-decided to get on chatroulette and talked to some strangers while drinking wine and then finally headed off to bed

02/02/17
-woke up and walked into work for stand up and then dug into the feature toggle unit tests with erin
-ate leftover pizza for lunch, bought plane tickets to go back to austin, played smash with the team and then got back to work with erin and mark
-finished up the feature toggle for the header on adaptive web and then took the streetcar to goodwill
-bought 10 dollars of glasses and pottery from goodwill and walked back in the chilly cold to eat more leftovers and skype with jt for a bit
-got down to business and finished up my flip clock app and then published it to the play store before showering and going to bed

02/01/17
-came into work and rewrote a lot of old yucky code with erin and did more unit testing
-ate my leftover spaghetti squash pad thai for lunch and played smash with the gang
-got stuck with stupid dev environment issues and worked on those for a while before heading home for the day
-finished my new zealand poster and hung it up and did more apartment cleaning 
-caught up on always sunny and hanging around with a glass of wine or two

01/31/17
-woke up before the sunrise and headed into work for our meeting with Tony where I presented what plans we had so far with navigation
-had a good ten ten with mark and then got down to business with erin on the feature toggle part two before going to lunch with Merin and Yasha at the food trailers where Merin bitched about JJ
-came back to the office and worked more on our toggles and tried to do unit testing but kind of failed and were corrected by mark
-headed home and got pissed at nada about dishes and shit, sent her annoyed messages, cleaned up, and then finally talked to her (she was initially pissed but then i talked her down haha)
-went to trader joes with Natalie and picked up supplies then went back to her place and made spaghetti squash pad thai and ubered home 

01/30/17
-woke up and went into work for a quick stand up and then started working on making some feature toggles
-grabbed lunch from the food trailers and ate at grand central and talked about the state of our government
-came back to the office and finished up our feature toggle stories and then went home early to catch the bachelor and replant Natalie's dying plant
-watched the bachelor with jt, both of which were a little disappointing and then said bye and had a glass of wine and worked on my poster some more
-took a really long shower and then tried to go to bed early for waking up early the next day

01/29/17
-slept in and instagrammed on the couch for a bit before finally talking to mum on the phone and catching up on each other's lives
-had some leftover sushi before heading out to goodwill where i was very unsuccessful in finding anything and then walked over to urban outfitters for more unsuccessful shopping and then all the way over to retrofit home where i also didn't buy anything
-headed over to qfc and picked up some essentials and came home to look a flights a bit and mess around on the internet
-started working on a big Scotland/new zealand poster and then skyped with dan and caught up on his richmond life
-continued on the poster and finished up the lettering while watching the great British bakeoff and then going to bed

01/28/17
-slept in a bit, showered and then made my way over to poquitos for an expensive lunch with matt, emily, jaime and Chris
-walked back up to matt and Chris' place for many rounds of various board games and talking
-had a bit of Chris' spaghetti and watched dumb youtube videos before walking back to cap hill to meet up with taylor and aila at capitol cider 
-had a few rounds of cider and all caught up together and got decently buzzed
-brought Chris and emily back to my place where we chilled on the couch/bean bag and drank more cider and stayed up pretty pretty late talking

01/27/17
-woke up, showered, and headed into work where i looked over marks new restyling of cookies and ip and started on my own changes
-ate some snacks and played smash and then scavenged for food with the team for lunch
-messed around a bit more on the cookies and ip app and did some photoshopping before reorganizing the office space and neatly sorting all of our snacks and then headed home
-picked up sushi for dinner and then did more instagramming and got lots of new followers
-spent ages listening to music and cutting and gluing cardboard to make bunting before finally heading off to bed

01/26/17
-eventually made it out of bed and the apartment and went into work for standup/coffee and then worked more on my cookies and IP app with mark
-got lunch at Julie's garden with Yasha and Merin and then headed back to the office for a bit of smash
-got down to business trying to work with a marko template bug with Ardon and then had a quick glass of wine with the tdps 
-walked over to kraken for their happy hour and had some yum brussel sprouts and caught up with everyone
-ubered over to James and deepak's place for talking, being attacked by a cat, and watching always sunny before heading home and watching bake off and going to bed nice and early

01/25/17
-woke up after lazing around in bed for a while and headed into work for standup and then got to work on the reverse proxy set up with mark and Ardon
-went to the food trailers with Merin, erin and son ca and had some nosh fish and chips and gossiped for a bit
-came back and worked on more reverse proxy stuff and eventually finished the second reverse proxy story!
-worked with Ardon on getting his cloudformation working and then headed home where i called Ellen to talk about plants and life in general
-made myself a bowl of cereal and skyped with Brittany until my internet cut out for a while before coming back just in time to watch the part of bachelor i had missed and then going to bed

01/24/17
-woke up ate a banana and came into work for a run to umbria with the team and then sort of worked with Ardon on reverse proxy for a bit
-went to lunch with erin, Merin, and Yasha at pho fuchsia and had good convos and noodles
-came back and fucked around "working" on our navigation proposal and gossiped and giggled with the team
-headed home and did some online shopping at home depot before meeting Natalie downstairs and walking to safeway for dumplings ingredients and a new diva plant
-walked back to Natalie's for wine drinking, dumpling shaping and eating, and lots and lots of good talks, then took a lyft home with my diva plant

01/23/17
-woke up and instagrammed instead of getting out of bed and then eventually headed into work
-grabbed lunch with Ardon, Merin, and Yasha in occidental and brought back my falafel to eat at my desk and play smash
-worked a little more on the navigation proposal and then found a defect in the develop branch which i helped debug for a while
-came home and immediately turned on the bachelor (and missed the first 20 mins!) and worked on my new cute little plant diary
-finished up the plant diary while watching nada attempt to cook paella and watched some great British bake off before going to bed

01/22/17
-woke up and lazed about in bed for a while before getting up to have breakfast
-took a warm shower and brought some plants in for the humidity and then made myself a grilled cheese
-worked on my instagram some more and of course did more online shopping
-ate some of nada's leftovers that were surprisingly okay and hung about the apartment listening to sad songs and generally doing nothing
-watched more of the great British bake off and took a shower before going to bed

01/21/17
-woke up and created an instagram for the apartment and then spent many many hours working on it
-made myself a grilled cheese and worked on my insta more before making pasta for second lunch
-watched an episode of the crown and ate leftovers and then took a weed brownie which at first seemed to have no effect so i had a glass of wine 
-watched the great British bake off and some British quiz shoes ate another grilled cheese and some chocolate and then got preeetty high
-jt called me on skype and i was ridiculous and high and we somehow ended up talking politics and i disagreed with him on a lot of things and talked a bit more about his arrest and all that drama and then finally we said goodnight and i fell asleep

01/20/17
-got to sleep in thanks to a deployment day at work and messed around the apartment enjoying a slow morning
-headed out to goodwill where i got some dealz on things for my new bar cabinet and then returned a too small pot and exchanged it for a new plant
-came home and unpacked all my goodies and got to work installing my under cabinet glass rack, which was a total bitch to install
-walked downtown and into pioneer square for a release night where we ate pie and played smash (11 kills with bowser say whaat) and then headed home by 10
-opened up a box of wine and finished off a series of unfortunate events and got wine drunk for the first time in ages and fell asleep on the couch waiting for nada to get home because i'm nosy hehe

01/19/17
-woke and up and walked into work for a lowkey stand up and then some brainstorming with erin and Ardon on the navigation
-found free food in the 6th floor with Ardon and hung out and played smash at our desks
-did more brainstorming with mark and erin and came up with a little more concrete answers
-headed home for where i picked up my new cabinet, cleaned the apartment and then headed to qfc to grab food and then invited emily over
-started to build the furniture, drank cider, ate pizza, did some bonding and eventually eventually finished the "most difficult to build piece of furniture of all time" before fucking around on the internet and going to bed

01/18/17
-walked to work in the pouring pouring rain and had a slow standup which led into getting to work on me and erin's very first story
-grabbed lunch from marination station in the dock with kj and Merin and talked for ages about life, politics etc as you usually do when talking to kj
-had a boring meeting with markit and then got down to business with erin and finished up our very first story :')
-took a ride downtown again to pick up a lightbulb and get a super cute ottoman from urban outfitters and then headed home
-talked to Ellen on skype for a while, ate my leftovers, watched a series of unfortunate events in my super cozy living room

01/17/17
-woke up early again to go to work and walked in the rain and then went to a coffee stand up
-worked with Erin some more before going to a welcome lunch with the team and tony at girin
-came back and fixed more environment issues and then started working on figuring out our text change story
-took a lyft downtown with Merin and did some shopping in target, tjmaxx, and then later without Merin earthbound and got a hella sweet deal on a lamp from urban outfitters
-came home and then went out again to grab manao thai with Natalie and then catch up back at her place before coming home and heading off to bed

01/16/17
-tried to sleep in but ended up getting up at 9 anyway and tried to eat breakfast but it still tasted kind of weird
-hung around the apartment and watched netflix and read more of my book with coco
-ventured out into the cold and went over to goodwill where i got new margarita glasses, a new vase, and some cute sake glasses all for 6 dollars whaattt
-came home and rearranged plants again before eating nada's leftovers and settling in to watch the bachelor live
-curled up on the couch and finished the glass castle before watching more netflix and waiting up for aila to come pick up coco

01/15/17
-slept in and hung out with coco in my room for a while messing around on the internet
-rearranged some plants and started to read the glass castle
-ate leftover pizza for lunch and did some writing in this journal, watched a series of unfortunate events and read more of my book
-waited for 3 hours for nada to come home so that I could go out with my friends (which ended up falling through)
-had a very very mild confrontation with nada which ended up with me finding out she is somehow spending all of her money and then went to bed

01/14/17
-slept in and cleaned the apartment before meeting Aila and taking Coco into the apartment 
-Hung out on the couch with Coco and listened to music and read my book for a while
-Ate some bread for lunch and then took Coco to the roof where he peed in the elevator awkwardly 
-read more and more and watched Coco's craziness and then ventured out into the cold to get dominos
-ate dinner and showered and then finished my book (in one day!) And went to bed fingers crossed that if Coco pees it's on one of his little pads

01/13/17
-woke up and headed into work where we eventually had our demos which turned into mostly trouble shooting
-Grabbed lunch at biscuit bitch with Erin and Merin and Yasha and couldn't really eat very much
-came back and played smash and helped Erin with her dev VM and then headed home on the street car with her 
-came home and then went out to Rhein house with Matt, Chris, Emily and Devin and tried to eat soup
-walked over to their place for a cozy fire and more great conversation before heading home with frozen toes at 1am

01/12/17
-woke up and finally felt better!! walked into work and grabbed coffee with the team before helping erin set up
-grabbed lunch at cherry st with Yasha and talked about us both being sick
-came back in and played smash and then set up a lot more of erin's VM and then took the streetcar back to capitol hill
-shopped around goodwill and got some books and a new plant pot and then walked back home
-ate strawberries for dinner and called Ellen for a bit to catch up and then bought more things for the apartment before showering and going to bed

01/11/17
-woke up early and scheduled a doc appt and tried to sleep through the worst ear ache
-woke up again and walked over to the urgent care where i waited for a bit and then quickly saw a nurse who diagnosed me with a cold and an ear infection
-came home and ate some bread before ubering over to target to pick up my meds and do some house shopping
-came home and cleaned up the kitchen (thanks nada) and watched oceans eleven before taking a nap on the couch
-ordered some more art for the apartment and instagrammed plant hoarders for a while before heading to bed

01/10/17
-woke up in the middle of the night with a bad earache and then later woke up with my alarm and eyes that were basically crusted together
-went into work and greeted erin and got to know her a little and helped her set up and then grabbed lunch and played smash together
-helped erin some more and talked with the team about upcoming projects before heading home for the day on the streetcar
-worked furiously on my bachelor bracket and then skyped with jt for ages watching the bachelor
-went to bed and ended up waking up over and over again all night thanks to a killer ear ache

01/09/17
-woke up early and coughed my lungs up and got ready for work where i felt like an old person because i cant hear from one ear very well
-came in and tried not to cough onto anyone and worked with Ardon on a quick story
-grabbed a lunch that i couldn't taste with Merin and Yasha and caught up with them and then worked more with Ardon
-finished up the gossip and then headed home and then out to the pie bar to meet up with kj, tim, Maddy and Deepak and then walked all the way back to mine
-hung out on the roof and watched my friends drink beer and eat pie and talked for ages before going to bed

01/08/17
-slept in and of course woke up coughing and wheezing
-took more cold medicine and messed around on the internet for a while
-had some bread for lunch and then took a nap or two
-got ready to go out (shocking) and then when it was cancelled just hung out with nada for a bit and picked up some hot chocolate mix and chilled
-rearranged some plants and obsessed over jungalows on instagram before going to bed

01/07/17
-slept in again and woke up to another morning of mucus and coughing
-Officially lost my sense of smell and taste so I ate rice for lunch and watched sherlock and messed around on the internet
-ears started popping and i read a lot of mamrie hart's book and took a nap
-headed out in the cold and bought some cold medicine (probably should have done that four days earlier....)
-headed to bed nice and early to try and get better

01/06/17
-slept in and coughed a lot and fucked around on the internet for a while
-caught up on some tv and exhausted every corner of the internet
-finally left the apartment and took the streetcar into work where I talked to my first humans of 2017!
-ate potato chips and rice and hung out with mah girl Merin, played smash a bit, gossiped, and of course coughed a lot
-headed out not too late this time and went back home straight to bed

01/05/17
-woke up with a nice cough and weird taste buds 
-Tried to eat and almost went to work and then decided nahh and went back to bed 
-Read a lot of Americanah and then talked to mum and dad and Ellen and James on the phone while we all coughed and sounded hoarse
-had a Skype call with Katie and Brittany and had a blast
-finished reading Americanah and went off to bed

01/04/17
-woke up and again decided i was too sick to go to work and went back to sleep
-fucked around on the internet for ages and then ventured outside to go to toppot to grab a few donuts
-ate the donuts which tasted yucky thanks to my cold and continued to fuck around on the internet
-read americanah for a while on the bean bag before making another grilled cheese and catching up on the walking dead
-cozied up in bed, read more and then took a shower and went to bed

01/03/17
-woke up early and decided that i was feeling too crappy to go into work and went back to bed
-messed around on the internet for a while did research on investing and finance
-finally felt like eating and had grilled cheese and watched before the flood
-caught up with nada while she made the biggest mess in the kitchen and i bean-bagged it out
-got back on the internet and did nothing and eventually went to bed

01/02/17
-woke up bright and early and got squished my suitcase and headed to the airport for a sad goodbye with dad
-sat around in the airport feeling pretty rubbish and got on the world hottest plane where i had to rub ice cubes against my body to stop from overheating
-took a taxi home and then headed out to eltana for a welcome home bagel and then to qfc to restock for a few days
-unpacked a little and then worked on making a flip clock android app for my new kindle
-cleaned up nada's mess and then watched the season premiere of the bachelor and also wall-e before going to bed nice and early

01/01/17
-danced a bit more with dad and Shonagh and Niall, slowly destroyed my vocal chords, and sat around a fire singing songs until 4 am (last ones to leave woohoo!)
-had a lovely lie in and woke up with barely a voice and sat out in the sun with mum and dad for a while before going to circle c park to test out dad's new drone
-grabbed Ellen and the poodles and made our way out to mckinney state park for more sunshine and dog walking in gorgeous weather
-picked up a quick pterrys and went home to eat that and hang with the family for a while before packing up all my crap
-played banagrams and chicken foot bingo with the family and then had tearful goodbyes with the family and headed off to bed

12/31/16
-woke up and took a shower with jt and then said our goodbyes for a while
-drove to Tarrytown and met up with Stephanie and gave her a wee christmas gift and caught up a bit
-came back home and did some errands with dad and then went for lunch/dinner at jack allen's where we ate like kings and got drunk at 4pm on new years eve
-took a nap on the couch and then got ready for the smith's nye party and headed over to quickly change outfits and hang out with the old gang
-danced a wee bit, drank red wine and champagne, missed the countdown but still celebrated with the family, listened to bagpipes and watched fireworks

12/30/16
-made JT wake and we took a shower before heading out for lunch with dad
-met dad at tamale house east for yummy (and hella cheap) tamales before trying and failing to meet up with Stephanie
-headed back down south and played banagrams with the family before heading over to the real house where me and Ellen were super silly in the car while mum and dad dealt with a bunch of crap
-came home and took a nap on the couch and ate a wee bit of dinner before watching the fam play pandemic and hanging with mum and then driving up to jt's
-drank wine, did a bit of ceildh dancing and two stepping before watching inception, being interrupted :), having another lovely massage, and falling asleep together

12/29/16
-slept in and then took a shower and headed over to Brittany's new house on the east side
-grabbed lunch at counter cafe and caught up and talked new business ideas (plant truck hello!) 
-talked to Katie on the phone and drove over to the east austin succulent place and ooh'd and aah'd at all the pretty little plants
-had a lovely pedicure with Ellen and mum and then went with the family downtown to z tejas for an okay macaroni and cheese but still a nice family dinner
-headed back south and then drove up to see JT where we tried and failed to make margaritas, hung out on the couch :) and watched the notebook before falling asleep

12/28/16
-slept in with jt and then found a way to wake ourselves up :) and then took a shower
-went across the street to in-and-out for cheapo burgers and then i headed back down south for banagrams in the sun with Ellen and the poodles
-hit the mall with mum and Ellen and bought baby clothes for Stephanie, some new shoes and jeans and then headed back home
-picked up Shonagh from harrison's with Ellen and went to torchy's for queso and tacos and catching up
-headed back to her house and did some practice ceilidh dancing and then hung out in her room before heading back home to chill on the internet for a while

12/27/16
-slept in again and had a slow morning in with James with ping pong and bananagrams
-said bye to the family and drove up to jt's place where we shared pics, played some video games and had a proper reunion :)
-headed out to pappasito's for some mediocre texmex in a huggge family style place with the worlds sugariest marg/sangria
-drove to the cinema to watch the alright "doctor strange" and then went back to his place and then to heb and then back to drink wine
-received a lovely lovely massage from jt, wore a new outfit, exercised the outfit, hopped in the bath, and stayed up late talking and cuddlin'

12/26/16
-slept in and woke up for a long walk in the greenbelt with a lot of sweating
-ate breakfast and played a bunch of games of banagrams before eating leftovers for lunch and continuing to play bananagrams
-headed downtown to the panic room where we were soooo close to breaking out (it was due to a technicality!)
-walked around downtown with mum and Ellen and did a bit of shopping before coming back down south
-ate some turkey curry and then played another winning match of pandemic and then going to bed

12/25/16
-slept in and woke up with christmas cuddles and competitive ping pong games before going on a walk with the family in the greenbelt
-took a shower and helped mum cook the christmas dinner and talked to lorna and David and then gran and grandad on the phone
-ate our fabulous christmas dinner at the weirdly shaped table, popped crackers, and enjoyed ourselves at the table
-had Ellen deliver all of our presents and opened lots of lovely things and thoroughly enjoyed ourselves
-headed over to the cairn's for desserts and good company where i finally was "cool" to highschoolers (thanks to the free booze) and then took care of them with toast and water before coming home and heading to bed feeling nicely buzzed and happy :)

12/24/16
-had an uncomfy flight into austin and landed at 5am where i said hi to mum and dad picked me up and took us too our airbnb
-finally got some sleep and woke up to go grab a bagel from wholy bagel with mum and ate it with dad back at the real house
-waited around with mum with ping pong before going shopping with James at the mall and picking out some things and organizing christmas presents
-came back home with the fam and picked up some burgerfi and yaghi's and then won our very first game of pandemic with the family
-stayed up late talking to dad about politics and life in general and then went to bed

12/23/16
-walked in the cold cold cold rain into work for a quick retro, some gossip and a silent film premiere
-headed out in Yasha's car to nouveaux bakery with Ardon and Merin for a yummy sandwich and some desserts to go
-came home and danced to christmas music while it snowed outside and i packed my suitcase
-took a nap, snooped in nada's room, painted my nails, and worked on our silent film more before going to the airport FINALLY with a talkative taxi driver
-got to the airport and walked around and got starbucks and walked around some more before finally getting on the plane and heading towards austin

12/22/16
-came into work and went to the world's most boring meeting that we ducked out of early
-tried to eat a few busy places before settling on the carpet teriyaki place with Ardon and Yasha and ate spicy spicy teriyaki
-came back to the office won the marbles game of smash and gossiped as we usually do
-came home and tried to convince nada to clean the apartment (failure), cleaned by myself, ate my lunch leftovers, and watched eye in the sky
-stayed up late working on the old french horror film and turned it into a silent horror film

12/21/16
-slept in thanks to planned power outage at work and headed in around 10:30
-had a quick ten ten with mark and then had a lunch meeting about coders
-came back from the meeting and worked on writing some more tests with mark and then worked on setting up the android environment
-walked downtown and passed some time in target before going to the waxing place and getting the worlds fastest brazilian wax and then went back to target for shopping and then over to earthbound for more shopping and a quick fun uber ride home
-ate the last piece of food in the apartment, FINALLY finished gilmore girls, drank wine and fucked around

12/20/16
-went into work and goofed around for a while as usual
-did a lunch interview with akansha where i just watched and was nosy 
-didn't actually eat lunch but played smash and then worked on some tests with mark and then schemed with Ardon about $$$ for a while
-came home from work and ate leftover pizza and worked on my austin alphabet some more
-drank wine and helped nada rearrange her bedroom like 500 times and then went to bed 

12/19/16
-went into work and messed around all morning because we had nothing to do
-had lunch at pho fuchsia with Merin and Yasha and gossiped as per usual
-came back to the office and goofed off more with Merin and Ardon and started to work on my austin alphabet more
-came home on the streetcar and had a two hour long phone call with the family back home while we planned xmas dinner, talked about the alphabet, and giggled a lot
-drew nearly all of my letter's first drafts and started inking a few of them before going to bed

12/18/16
-slept in until the afternoon and then slowly scrolled through facebook and waking up
-finished westworld and did nothing on the internet for ages
-took a shower and then caught up with nada for a bit before finallyyyyy finishing all 7 seasons of gilmore girls
-went to dinner at manao thai with aila and nada where i voiced my loneliness and was ignored
-came home quickly drank wine and got ready for bed and watched some of the new gilmore girls

12/17/16
-slept in again and lazily browsed the internet for a while
-watched more of westworld and wrote down a ton of these journal entries in an effort to actually catch up
-got ready to go out to dinner with aila and nada and then realized that we were actually eating the next day so instead got drunk and skyped with Brittany for ages and caught up on each others lives
-messed around on the internet for a while before skyping with jt for ages
-nada finally came home from her secret outing and then she "talked" to me for ages about nothing while i made faces at jt before going cozily off to bed

12/16/16
-bundled up and went out into the cold and sat around for a while before having our retrospective
-played smash and won(!) and then went to cafe paloma with Ardon and Merin and hung out for a while
-merged a bunch of pull requests and played pictionary as a team
-carpooled over to the mall where we grabbed french fries and popcorn and slushies and watched the new star wars movie with capital one investing
-was dropped off home and then i drank a lot of wine, jammed to music and then talked to strangers (one of them for the second time) and then went to bed nice and tipsy

12/15/16
-woke up early and showered and went into work where i had a meeting about coders with tony and Natalie and Eleanor 
-went downstairs for the town hall with the new cto who seems cool and then had a free lunch with some coworkers
-came back and had another meeting with armada, worked on merging a bunch of code with the team and then ended the day with a ten ten with tony
-streetcar'd home and ate an apple and watched gilmore girls and then caught up with mum and dad and was filled in on the kitchen gossip
-watched more westworld and did nothing for a while

12/14/16
-went into work and worked out a lot of hidden problems with Shonagh and tried to hide anger and tears at work
-had lunch with interview guy who was pretty much a squid but still had a good time thanks to the good company
-worked on JJ's story with yogesh after he left sick and we finished their work up
-streetcar'd to momiji with the TDPs and had a yummy all expense dinner and caught up with Natalie before going back to my roof for wine and fireball
-ubered down to the skating place where we continued to drink, roller skate, listen to karaoke and finally get the hang of doing crossovers 

12/13/16
-went into work and helped out occasionally on stories and tried to listen to the tdp all hands
-went to lunch at intermezzo with Merin, Yasha, Eisha and kavitha where we had an incredibly rude waiter (again ugh) but yummy yummy food
-worked on some stuff with the team and then headed home for the day
-got my amazon package and started to plant all my new jade plant babies and called up JT where we skyped for a while
-started to watch westworld with jt and got a fright and spilled my wine all over my mattress and then went to sleep nice and early

12/12/16
-came into work and sorted out what the team would do this week and started working on a story with yogesh
-grabbed a poke lunch with Merin, Ardon and teffrie in the international district
-worked on more stories and made a whole bunch of slack emojis of my friends and then headed home
-went with nada to the gym again and ran some more on the treadmill
-got a sudden burst of energy again at like 11:30 and stayed up fucking around on the internet

12/11/16
-slept in and was woken up by nada who wanted to go get breakfast
-took nada to eltana and had a delicious bagel and talked with nada
-did a lot of online shopping for christmas and organized my brand new jade cuttings
-convinced nada to go for a run with me and ran for around 30 mins before coming back and taking a shower
-felt super sleepy and laid around for a while before weirdly getting a lot of energy and organizing all my plants and hot gluing and hanging pinecones lol

12/10/16
-slept in and then talked to James for ages about presents and finally sorted out everyone's presents
-watched a lot of gilmore girls, cleaned the apartment and hung out 
-was picked up by Natalie, Maddy, kj, Deepak and Amelia and headed out towards the vashon via the ferry and ended up at a dive bar and watched the sounders game and headed over to judah's party
-ate delicious grown up food, oogled at plants, had good convos, and left the party with a bag full of plant cuttings
-got in a big argument from the back of a minivan with Maddy and cried a little bit while waiting for a dumb ferry and then finally got home around 2

12/09/16
-slept in and had a very lazy morning in the apartment
-took the stairs down to the gym where i went on the treadmill for an hour (sayyy whattt) and listened to the moth
-Jon came over and watched part of twister with me while sitting too close and awkwardly making a move on me that i awkwardly avoided and ignored
-got the hell out of there and went into work for cold pizza and tequila, making puzzles and playing smash
-told the team about rahul and we continued to troll him as a team, drink more tequila, occasionally test, and fuck around with synthesizers and then uber'd home

12/08/16
-went into work and demo'd some stories and fucked around for awhile 
-had a lunch with an interview candidate which was mildly awkward but interesting
-came back to the team and gossiped about the interviews before going home and catching up with nada and hearing about her "SAD"
-watched westworld with nada and indian food and then noticed the snow and ran up to the roof for seeing my first ever flurries
-played in the snow for two hours, making snowmen, throwing snowballs, and taking endless amounts of pictures and then skyped with jt for a while

12/07/16
-went into work and had a really great meeting with mark where he told me i'm "exceptional", a director in 10 years, promotion ready, etc etc :)
-grabbed a thank you lunch with Natalie at intermezzo and caught up on each others lives and handed out advice to each other
-came back and worked on me and yogesh's story and wrapped it up with some help from mark
-watched videos and gossiped with Merin and Ardon before street caring home and watching gilmore girls
-called up mumma and talked kitchen with her and caught up and then talked to James for another hour and a half and planned out the family's xmas presents

12/06/16
-walked in the cold cold cold to work and started again on me and yogesh's story which we basically had to rewrite
-went to the id with KJ and tried out the super delicious poke at gopoke and then headed back to work
-worked with Ardon for a while trying to fix his problem in his code that suddenly and randomly started working again for no reason
-took the street car home and watched a crazy amount of gilmore girls and made grilled cheese and drank wine and went to bed

12/05/16
-woke up and skipped around the apartment with christmas music because it was snowing and then ubered to work with tim because it was icky and cold
-came into work and made good progress on our new story and the gossiped before heading over to the holiday party
-drank wine and ate snacks and painted some award winning pieces of art and finally won a raffle
-abused the free drinks and took a ton of photobooth pics with the tdps and hung out with them before heading out to cap hill to poquitos with tim, Deepak and KJ for more drinks and talking before heading over to gokan for a round of sushi, and a lot of sake for everyone else
-brought everyone back to my place for red wine drinking, drunken bitching, secret telling, glasses wearing, and roof top chilling before going to bed

12/04/16
-slept in again and then lazily got ready before heading out to brunch with matt, Jon, and Erica
-had a burger at lost lake and fun conversation before walking back in the cold to the safe warm and cozy apartment
-put on gilmore girls and cleaned out my room and the apartment (much needed)
-had a two hour phone call with Brittany and Katie where we caught up on each others lives and gossiped and reminisced and drank wine
-called up jt and talked about our lives for a bit and then went to bed nice and early and cozy, fingers crossed for snow in the morning!

12/03/16
-slept in and had a cozy morning inside where I listened to hamilton all the way through and started to clean the apartment
-showered and then invited Jon over where we watched friends, drank wine, and started messing with rahul on okcupid
-headed over to the Seattle center to grab a dinner togo and then watched the new harry potter movie with snacks and imax :)
-walked to emily and devins and then ubered over to cap hill to go to six arms where we met up with Chris and Jon's friend Andrew and had a round or two and good laughs
-brought the gang back over to my apartment where we had another round of drinks and watched a very interesting six hour long netflix show about Norwegian fire and timber

12/02/16
-headed into work where we had our retro and were pretty happy with how our first week of work went and then got really really into building slack bots
-grabbed a falafel lunch with Merin and Ardon and ate in our little basement again before going back to do more slackbot things and talking to big brothers big sisters
-left work with Natalie and went to the grocery store to pick up a bunch of food for maddy's party and then came back to theirs and washed a bazillion dishes and helped cook and made my prosciutto wrapped asparagus
-the guests arrived and we surprised Maddy and ate my amazing asparagus, cake, and chicken and drank wine and talked
-was kicked out of the house and went back home cozy and wine drunk and sang annoying songs annoyingly loud

12/01/16
-came into work and put the finishing touches on me and yogesh's story
-grabbed a late lunch with Merin from cherry st cafe and ate it during a meeting with the team
-gossiped the afternoon away and then had a ten ten with tony and ate a lovely snowman cookie
-went to target with Merin where I showed her the wonders of target, picked up my prescription and let Merin buy tons of things
-walked over to ross and continued to buy more things before walking home, hitting up qfc for maddy's birthday food, and then coming home to test run my side, drink cider, and then talk to jt

11/30/16
-was greeted with a surpassingly high number of good mornings on the way into work and then worked with yogesh on our story
-grabbed another massive fish and chips lunch with KJ, Merin, Eisha, Son Ca and Yasha and ate in the basement of an old building
-came back and did a little more work and gossip before heading out with Deepak, Tim, and Sylvain for a belated birthday happy hour for Deepak
-walked all the way from sylvains over to rheinhouse for wine and football and talking to kj, Maddy, and Natalie
-headed home and called mum and dad and caught up on the latest kitchen drama before skyping with jt, extending my christmas trip and then going to bed early

11/29/16
-woke up and walked into work where Merin got me a lovely succulent present and then grabbed coffee with the team and got a cupcake
-worked with yogesh and really made good progress on our story and then went to lunch at a fancy new place with slow service, yummy, salty food with coworkers
-came back and worked a bit more but mostly gossiped and then went to kraken with the tdps for margs and brussel sprouts 
-headed out with Natalie and went with Maddy to a christmas tree lot where picked and loaded up a tree on their car and brought it home
-walked over to momiji where I met all my UT friends and had an amazing sushi roll (007) and had good convos before coming back home and going to bed early after being spoiled all day

11/28/16
-woke up and showered and then pumped myself up with taylor swift on the way to work
-had a meeting where I actually spoke up for once and then tried to fix my website and then gave up
-grabbed lunch with Merin at il corvo and filled her in on the drama and realized again why i love Merin so much
-came back and started to work on a story with yogesh and made pretty good progress
-took the streetcar home with Ardon and ignored all the shit i had to do and watched netflix and painted my nails and went to bed 

11/27/16
-woke up in a panic an hour late for my flight and rushed to the airport experiencing my first ever panic attack
-spent 400 bucks on a new flight and went back to jt's for on the floor meltdowns, trying to sleep, cuddling, circles, waiting during trips to cvs, toothbrushes, and then trying to sleep again
-still freaked out we went to lunch at hopdoddy's and then found out my flight was delayed, but maybe not really so we rushed to the airport to find it was delayed and so i got a new flight
-headed over to the animal shelter with jt to play with puppies and kittens and feel better before mum came and took me home for a nap before heading to heb for food, having a minor panic attack, and then finally going to the airport for the last time
-had a huge birthday ice cream from amy's, ate sushi, took a flight full of tears to Denver, took a flight full of bad sleeping, and took a taxi back home to finally arrive in Seattle 17 hours late

11/26/16
-woke up and went with mum and dad to bageltown and then read up on wine facts on the way north with mum and dad where we picked out some tiles for the house
-was dropped off at Brittany's place where I met her dog, exchanged birthday presents and then drove off to amy's for ice cream and catching up and then came back down south and took the dogs for walk in the greenbelt
-grabbed pterry's and then went downtown with mum and dad for Alison's 50th birthday where I had a few glasses of wine before jt picked me up and headed back to his
-drank some more wine and then was joined by Stas, madeline, and raj for kings cup, hot tubbing, lots more wine, and good fun
-kicked everyone out and had some fun with ties, went into zombie trance mode, fell asleep in the bath, and then stupidly stupidly went to sleep

11/25/16
-got up and took a shower before going out to north austin to look at granite with dad and Ellen
-came back down south and had some delicious rudys and then went back home
-killed a very scary spider with James and then took a nap before going black Friday shopping with Ellen
-went to trattoria lisina with the whole family where we were treated to fancy cocktails, classy wine, yummy salad, meatballs, pasta, calamari, cheesecake and tiramisu
-came back home and played a game of cards or two and then stayed up with mum and dad playing guitar and chilling out

11/24/16
-woke up and packed up and stopped in at buccees for the bathroom and a big ass slushie
-drove back to austin and jt dropped me at the parents where i said hi to everyone and took a much needed shower
-headed over to the devlins where we met the whole gang and caught up and had delicious dinner with fabulous asparagus and brussel sprouts
-played a Wyllie v everyone game of fishbowl and hung out with the kiddos
-drank more bubbly and talked with the mums before heading back home to the poodles and the noisy kitchen

11/23/16
-woke up bright and early and taxi'd to the airport where I waited to board
-slept sort of and listened to music and podcasts and then landed in austin where i saw mum quickly at work and then was picked up by JT
-headed over to Ellen's to see her and lily and grab the camping stuff and then went to torchy's for queso before hitting up heb and then starting the drive over
-set up the tent and went on an "illegal" walk to a "scenic" overlook and then went back and built a fire (after a lot of failure and a quick trip to bucees) and then made quesadillas and snuggled and celebrated hehe our fire
-after the fire died down we headed into the tent and snuggled for warmth and had a cozy night hehe

11/22/16
-went to work and fucked around helping Ardon and yogesh with their vm's
-went with Natalie to gaba sushi were i had a sushi bowl and we caught up on each others lives and plans
-fucked around at work with Merin and Ardon and then finally got to go home
-watched a bit of netflix and ate granola before finally slowly starting to pack for the trip back to austin
-watched the movie up in the air and took a shower and went to sleep for a short four hours

11/21/16
-walked into work and went straight to a long team meeting where we talked goals and plans for the team
-got lunch at cafe paloma with Merin and Yasha and had a delish panini before heading back to the office
-finished drawing out a useless calendar on a whiteboard and then headed to flatstick with tim where we played giant jenga and then I left
-walked downtown into the beautiful olympic fairmont hotel and got my first ever brazilian wax which was actually not that bad
-came home, ate leftovers, talked to mum, and watched jane the virgin with nada and then went to bed

11/20/16
-woke up and said bye to Radha and then crawled back into bed and watched the walking dead
-walked downtown and stopped in tjmaxx and bought more nail polishes and then walked over to bell and whete for bottomless mimosas and brunch with matt, Chris, emily, Devin, aila and her boyfriend
-slightly buzzed headed over to matt and Chris' place for shadow hunters, codenames, and bang with the gang and then walked home
-cleaned up the hot mess that was our apartment and watched some gilmore girls
-ate leftovers and talked to jt for ages where we caught up while i painted my nails and did my makeup before showering and going to bed early

11/19/16
-woke up and took Radha to eltana for yummy bagels and then back to the apartment where i chilled solo for a while and read my book on the roof next to the fire
-walked over to barrio where I was the first one and sat for 15 mins solo waiting before KK, patrick, nada, Radha, and Puja showed up for yummy enchiladas and sangria
-said bye to kk and patrick and went back to the apartment to chill and gossip over red wine before heading out into cap hill again to catch aila and her guy
-missed aila and her guy and went to comet for a bit and then to grime's for a rum and coke and sort of having boys talk to us
-met up with Sai and his friends at reinhouse where we grabbed a table and sat for a while talking, feeling tired, and trying to look bored enough so someone cute would talk to me lol (worked once haha) and then finally headed home 

11/18/16
-walked into work and got back to do doing as usual and then was grabbed by tim for a quick and strange coffee with Navdeep and then we caught up for ages in the kitchen
-met Radha at work for lunch at intermezzo where we gossiped and talked about our last 6 months
-went back to work I gossiped with Merin, played jenga with tim, and waited around for the release to end
-came home and met Radha again and we went to dinner with madeline, matt, and Chris at a sushi place
-went to uncle ikes and got some edibles and watched cadet kelly and funny youtube videos and was extremely tired 

11/17/16
-went into work which was extremely quiet and had a weird vibe
-took Merin to il corvo
-continued to do nothing at work
-went to suika and got pie
-talked to Ellen

11/16/16
-went into work without Merin
-grabbed fish and chips with kj 
-probably did nothing at work
-talked to mum about her kitchen situation
-stayed up late talking to JT and drinking wine until i got kicked out of the living room by nada

11/15/16
-came into work and finally got my dev vm working with mark and worked some more on Merin's
-walked over to el camion for lunch with kj and Merin and had a yummy mutila and talked about the state of the world again
-came back to the office and said bye to Merin who wasn't feeling well and then worked on a database change and fixed a bug with it and just hung out for a while
-came home and went to qfc in the freezing cold rain and carried all my crap home while freezing my ass off and then had an apple for dinner and watched gilmore girls for a while
-snuggled up in bed in the cold apartment and watched jane the virgin, took a shower and went to bed

11/14/16
-woke up super sleepy and headed into work for a pretty informal standup and then some testing of more cascading stories
-realized that we couldn't actually do one of the cascading and then worked on dev vm's some more
-grabbed lunch with Merin and kj at a vietnamese place and took two hours just talking and not working
-gossiped until the end of the day and then went home where i finished the hand maid's tale and joined Maddy, Natalie, and kj at momiji for edamame and talking
-said bye to kj and went to stout for girl talk and hella cheap flatbread and then walked home in the freezing cold

11/13/16
-slept in until 11 and had a bunch of interesting dreams before messing around on the internet for ages
-went for a shower and then watched more netflix and then walked downtown to the bus stop with nada and caught up for a while
-took the bus all the way into bellevue and met up with aila in the mall where we grabbed beechers and then headed into our movie
-ate yummy grilled cheese and mac n cheese while watching the amazing movie Arrival and then headed back to ailas to play with coco and catch up
-ubered back home and got into bed with some wine and leftover indian food and talked to JT and then also my whole family at the same time 

11/12/16
-tried my best to sleep in despite going to bed at 10:30 and had a lazy morning in bed and called dad for a while
-ventured out into the wind and walked to goodwill where i bought four books for 10 dollars and then went to eltana for a bagel and a half finished crossword
-came back to the apartment and watched netflix and called Katie for ages and finally caught up
-decided to go back out into the cold (thanks to empty fridge) and grabbed indian food from cap hill and ate it while watching gilmore girls
-got wine drunk and went on chatroulette where me and Katie tried and succeeded to find each other and talk for a bit

11/11/16
-woke up after having weird wedding stress dreams and went into work where no one was there...
-lunch at casco
-happy hour at flatstick
-band awards and netflix
-going to bed at 10:30

11/10/16
-walked to work through the fog and then sat at my desk doodling on post it notes for a while after I finally got my vm's code to build
-grabbed lunch with Natalie, Deepak, tim, and Sylvain in the ID where we ate dumplings (and avoided the chicken hearts and pork ears) and had lots of mildly awkward silences
-came back doodled some more and then worked with Merin on finishing her vm and sat in really comfy bean bags
-rode back home and did a good cleanup of the apartment and then met nada at our sushi place to catch up and have dinner
-walked home and read my book with a glass of wine then watched new girl with nada before going to bed nice and early

11/09/16
-walked into work in drizzly rain and talked sad sad election results with the team
-did some vm work before going to the thanksgiving lunch and further talking election results with KJ and some other work people
-listened to a boring yet slightly informative talk from some investing execs and then went back upstairs to slowly slowly slowly work on the vm
-took the streetcar home and read the hand maid's tale for a while while eating yogurt 
-drank wine and talked with JT

11/08/16
-went to work and had another standup without much excitement and then started working on the dev vm again
-went to occidental park with Merin where I had pasta from a food trailer and enjoyed the sunshine
-came back and did some more "work" on the vm and then went to a happy hour with the guild at a pool bar where I did surprisingly okay in the first game but still lost, was carried to victory by tony, and then lost again with parth
-street car'd home and then walked over to Jon and matt's to watch the election where we slowly realized that trump would actually win
-avoided thinking about the election and went to the movies downtown to watch Hacksaw Ridge and then discovered that trump had been elected :(

11/07/16
-walked into work and had our first stand up in ages and then grabbed coffee with the team
-started working on my new dev vm and then went to lunch at il corvo with Jon where we caught up and had yummy pasta
-came back to the office and continued slowly working our way through the vm crap while gossiping and playing jenga
-left the office and read the handmaid's tale for a while before eating leftovers and catching up on walking dead and jane the virgin
-took a shower and had an early night in with netflix

11/06/16
-slept in and woke up with sun miraculously shining in the sky and in my eyes
-fucked around the apartment for ages, mostly eating leftovers and watching gilmore girls
-decided at the last minute not to go to JJ's party and instead got quite wine drunk talking with JT and had a blast
-got super wine sleepy and decided to go to bed at 9:30 but then got a text from Natalie inviting me out for late night sushi so I get out of bed and go all the way to momiji
-eat a hella yummy and cheap sushi roll and with nat and her interesting friend Kyle, and then walked over to reinhouse to satisfy Natalie's pretzel cravings before walking home and actually going to bed

11/05/16
-slept in again and then lounged around in bed for ages and ate a sad bowl of cereal with the milk ratio all wrong
-got up and showered and then lounged about for ages on the couch watching netflix
-headed out into the rain to buy some ingredients for the dinner i was going to make with nada but ended up just making solo
-enjoyed my fabulous dinner, drank some wine, and watched more netflix before ubering over to Jon, matt, and Chris' place where we headed out to smith for drinks
-after a drink and a brownie we walked down the street to a pizza bar for more convo and then i took an uber home at 12 and went right to sleep

11/04/16
-slept in and then took a shower and headed over to Jon's place in the central district
-ate an edible and then walked down madison to buy some new houseplants and then went to safeway where we bought a ton of snacks and food
-sat down on the couch and scarfed down food while watching Maury and laughed and said dumb things and twitched and then eventually fell asleep for a while
-walked home super sleepy and then took the streetcar into the office for a late night deployment with tequila and smash and yummy dinner
-occasionally did some testing, scavenged the empty office, decorated my new desk, and then took an uber back home at 2 am

11/03/16
-went into work where i was the only one actually physically present and went about debugging our 500 error
-got a fancy Italian lunch with Natalie and Courtney rosser who was actually not that bad of a person???
-came back and got down to business and figured out some issues and did our best to fix them before heading home for the day
-ate leftovers and watched netflix before skyping JT and having a blast gossiping and then made my way over to a Microsoft happy hour at garage and meeting some sort of interesting people
-walked with Natalie to R place where we danced and watched a few drag queens strut their stuff before walking home at 2am supah tired

11/02/16
-walked to work in the pouring rain and then made a big spreadsheet of testing data
-waited around for Merin to finish ctr and then went to lunch at intermezzo and had a delicious pasta and dessert
-came back and eventually started testing but ran into a lot of weird errors and bugs
-headed home and then walked to Natalie's to join her and tim for grocery shopping before beginning our apartment tour at Tim's and then walking over and finally revealing my lovely furnished apartment
-went back to natalies where we made delicious dumplings all ourselves and ate a ton of them, played poker, and had a very cozy evening in before walking home in the pouring rain with tim and Natalie

11/01/16
-walked to work for another low key stand up before pretending to do work for ages
-went to gaba sushi for lunch with Merin and Yasha and caught up on the gossip and had yummy sushi
-came back and actually did some work creating accounts and then went to a meeting where we found out we might change teams
-gossiped a bit at our desks before heading home on the streetcar and having reheated pizza for dinner
-filled out my election ballot and watched netflix before walking in the cold/rain to blicks to buy some frames and then hang up my new austin art and then chillin out for a while

10/31/16
-woke up nice and early and headed out into some pretty heavy rain and string winds and tested my new umbrella
-found my new desk and set it up and fucked around for a while before going to the halloween chili cookoff with the team and caught up with Tim and Natalie and watched rugrats
-played smash for a long while and then went back to my desk and looked up big brothers big sisters stuff for ages before heading home for the day
-came back home and went straight to qfc for (the best) tortilla chips of my life and other assorted things and then back home and had frozen pizza for dinner
-collected all nada's boxes and squashed em, cleaned the floors and kitchen and then drank wine and caught up with JT before another early nights sleep

10/30/16
-woke up and packed up all my stuff into my completely full suitcase and then said goodbye to Kevin and dan before grabbing an uber
-arrived nice and early at the airport and talked to mum for a good while before boarding the flight
-watched Room on my phone during the flight and then arrived in Detroit where i hauled ass to get to my next flight
-watched Joy and Mad Max on the long flight to Seattle and then took the link back home and called JT for a bit
-walked from the station with all my heavy crap in the rain and found an apartment covered in boxes and sticky stains and then built a tv stand with nada and then went to bed at 10:30

10/29/16
-woke up on the air mattress and then headed out with Dan and Kevin to Katie's rugby game
-went to lunch at a little cafe and then back to the apartment where we packed up a blanket and headed out
-sat in the sun and read my book and napped for a while at the vmfa
-went back and then met Julius at citizen burger for interesting conversations...
-said bye to Julius and went over to Cole's place where we played drinking games with their friends and convinced a bunch of people I was an ex air force pilot turned commercial pilot

10/28/16
-woke up and packed up the hotel room and had one last hotel breakfast and dropped my suitcase at the boy's place and then walked over to the tedx talk and heard some really cool talks from women
-walked around carytown and then went back for more tear jerking/hilarious/inspiring stories and then had lunch in carytown and called Ellen while shopping
-spent ages in the vmfa admiring art and then read my book in the sun before heading to the boys and then going to get sushi with their friends with wine
-went back to their place to get dressed, pregame and then went next door to a party where we talked to strangers
-walked downtown and went to a dancing place where we got pretty drunk and danced (flirted???) And then headed back exhausted and sore and tried to wash the black out of my hair and slept on an air mattress in Kevin's room

10/27/16
-ate the hotel breakfast and headed over to the boys place and then back to campus to finish up the project and eat lunch in the cafeteria
-drove back over to the hotel and watched a ton of the same boring presentations and presented our work in front of the group
-left the hotel and went back to their apartment and played pandemic and ate a bunch of chips and didn't save the world
-went to the grocery store with dan and picked out the stuff needed for Danny sauce and then headed back to their place to make the sauce and get to know dan
-ate some Danny sauce and hung out before watching the start of oceans 13 and then watching Daniel's drug deal before heading back to the hotel for the night

10/26/16
-woke up and had cereal in the hotel and then froze my butt off at the boys place before going to the hotel to start on our project
-due to bad bad internets we left the hotel and went to campus where we worked Some more and ate lunch with Cole
-got back to business and nearly finished up before heading to happy hour at BJ's for tons of apps and ciders
-left BJ's with the boys and Larry and Zach and headed back to their place for baseball, kings cup (briefly), 7/11, polaroids, and being "socially jaded"
-decided to hit up tobacco company again but it and all the other bars in downtown rva were closed so we all ubered back home and went to bed

10/25/16
-woke up and had the hotel breakfast and headed to the boys house for carpooling into work just in time for 2 truths and a lie
-listened to lectures and then went to lunch in the Nordstrom's cafe with Kev and Dan and then back to class for more lessons
-left early because of internet problems and went back to the boys place and then walked around Byrd park with Dan and then went to dinner at the daily with Dan, Kiev, Katie and Cole
-left dinner and went to the children's museum for drinks and art and messing around like a kid before going back and doing some puzzles
-came back to the hotel, hot tubbed for a bit, then talked to Ellen and went to bed

10/24/16
-woke up early after tossing and turning for ages and took an uber to dan, Kev, and Daniel's place and reunited before heading into work for a sad cornbread breakfast
-listened to some pretty basic presentations and did some group work with our table and then had a sad chicken parm lunch and wandered around the mall nextdoor with dan and Kev
-went back to doing more simple presentations and avoided doing any work for the rest of the afternoon and then went back to the gang's house and went for a walk around carytown, bought a board game and then went to a restaurant for pumpkin beer and dinner
-headed back to their place where their friends cole and Katie joined us where we became bean farmers from the deep south
-ubered back to the hotel and talked to Ellen about interviews and life in general then showered and headed to sleep

10/23/16
-woke up early and grabbed all my things together and took an uber to the airport
-went through security and bought some snacks and then boarded the flight to Minneapolis
-watched finding dory and my big fat Greek wedding two and then rushed to my connection which was actually running late and hadn't started boarding
-sat next to a guy who talked to me about his credit cards and listened to music and chilled until landing in Richmond and ubering to the hotel
-checked in and ordered myself a room service cheeseburger, took a long and kind of scary shower, and watched Netflix and applied an assortment of strange lotions to myself

10/22/16
-woke up with a lovely hangover and then had my wonderful new table delivered (early!) and then went out to eltana's for a hangover breakfast
-walked from eltanas to downtown where i stopped into a ross, that earthbound place (for hella good dealz on plates and a planter) and then to world market to spend a 10 coupon
-met up with Jon and Chris nearby and took a bus back to theirs and then ubered over to the u district where we had a blast trying on weird costumes and Yu then ended up getting a second costume from goodwill
-ubered back to his and walked home with the heavy backpack and talked to mum and dad on the walk
-tried and failed to finish my hamburger costume and then packed and did laundry and watched netflix while still feeling gross

10/21/16
-woke up and called into standup where i found out that i actually did need to do work today
-fixed some minor cases in the modal and tested them for a while then responded to pull request comments for ages
-grabbed lunch from marination station and watched a bit of netflix while waiting for the deployment to start and then tested one little story
-watched netflix and chilled for the rest of the night until midnight where i had two screwdrivers, danced in my room and then headed drunk over to natalies where we then went to lindas
-met up with tim and his girlfriend and Deepak and Maddy and had some good talks with them and then headed(ran with glee) home

10/20/16
-woke up earlier than usual and walked in the pouring rain (getting soaked) to go into work and send a stupid email
-kept myself busy by sorting out the new cube situation and talking to KJ
-went to lunch with Yasha at an Italian place where i ate the worlds cheesiest meal and then came back to play smash with the gang
-went to the 'sip n share' where we listened to boring talks, didn't win canoes, and drank at work and then attended scotch Thursday for the first time
-walked home with tim and talked about relationships and dream jobs and then did nothing at home for a while

10/19/16
-woke up after a not so good sleep and then went into work where i deployed my story and then learned that i have nothing new to work on 
-did nothing for ages and then went to a pho place for lunch with Merin and Yasha and then came back to the office to play smash
-did some CTR emails and did some online shopping/pinteresting while not working at all and then left work
-came home and got some milk and ate leftovers before going to the comet to watch the debate with KJ and Maddy
-went to wild rose for another drink after the debate and then came home to watch netflix and shower

10/18/16
-came into work and fixed some UI stuff with my modal and gossiped as per usual
-went to lunch with Merin and got teriyaki and ate back at the office and talked about people
-came back and worked some more on the UI changes and then gossiped with Merin and tim for ages while waiting on Deepak to finish
-took the streetcar with Deepak and tim and went to hotel sorrento for tarot readings but left after seeing the line and went up the street to Italian family pizza for informal card readings and big ass pizza and wine
-came back home and called James and talked for ages before going to bed at like 9:45 after being tired for no real reason

10/17/16
-woke up to an ominous email from tony and headed into work 
-gossiped for a while about possibly getting fired and then finally went into our meeting with tony where we found out that we were going to be the few people who stuck around
-gossiped with everyone for ages trying to figure out what happened and then left early with Merin where we went to chinatown and did some shopping and talking
-came back home and caught up with mum and dad, watched netflix and then went to get sushi with nada
-came back super full and talked to JT for a while

10/16/16
-slept in and then did nothing on the internet
-binge watched black mirror on netflix and did more nothing
-went for a walk around the central district with nada and admired lots of pretty houses and talked 
-grabbed cheap burgers from Freda's with nada and then went back to the apartment to do nothing again
-when nada came back home we stayed up drinking wine and swiping dudes on tinder

10/15/16
-woke up early and said bye to Stas and Jon before going back to sleep again and then going out to brunch with nada in the rain and wind
-ordered a super yummy pumpkin spice milkshake and then waited an hour for our yummy food which ended up being free and then took an uber downtown with nada
-got a new coat and booties in tjmaxx and went into lots of other downtown shops with nada
-came home and talked with nada for a bit and then called JT to hear about cringey acm camping
-got wine drunk and sang songs out loud and bought tickets to austin and ate late night gauc

10/14/16
-woke up and decided to "work from home" where I just sent out an email and then went on Pinterest for ages
-the power went out so I twiddled my thumbs for a while and cleaned the apartment
-power was restored and my door was fixed and I hung up pics in the bathroom before going to dinner with Stas, Devin and Emily at an expensive sushi place
-walked over to Emily's and Devins apartment where we had yummy tequila and won a nerdy board game and then was joined by Jon and Eddie
-continued drinking and playing board games and then went pretty drunk we headed out in the typhoon and went to dicks where we ate tons of food and then headed back to my place with Jon and Stas where we stayed up and talked for a while

10/13/16
-tried out my raincoat and rain boots in a "typhoon" and got pretty damp on the way to work
-had a standup with just me and matt and everyone else on the phone and then waited on James to finish his part for a while
-went to il corvo with Tim, Deepak, and Sylvain for super yummy pasta and then back to the office for some smash
-finished up the modal and fucked around at work before heading home with KJ and then building some chairs!
-went to machiavelli's with nada for yummy pasta and then rearranged the living room before working on some more art for the bathroom

10/12/16
-woke up and headed into work where i started again on the modal and mostly waited around on JJ
-went to a meeting with free pizza during lunch and then played smash for ages
-laughed at Merin having an admirer and gossiped for a while
-headed home from work and ate sad leftovers and started working on my halloween costume
-skyped with JT and caught up in a sober way this time haha

10/11/16
-woke up and headed into work on a sunny/chilly morning
-worked on the citizenship modal again and started to match up to what jj was doing
-ordered Chinese for lunch and then played smash with the gang and ate said Chinese
-worked on the modal briefly and mostly just sat around building and waiting for the page to load before going home
-went to QFC and made dinner and then ate a special chocolate and spent the rest of the night very very high with JT where we giggled a shit ton

10/10/16
-snoozed for ages instead of taking a shower and braced the cold to get to work
-had a quick standup and went to work with Merin on the modal which mark helped us fix our problem
-grabbed a brussel sprout and french fry lunch with Merin and Yasha and gossiped as per usual
-came back to the office and played some smash and then went for a long walk with Tim and Natalie before doing nothing for a while with Merin
-street car'd home and went for a run (whaaa??) and then messed around on okcupid for ages

10/09/16
-slept in and lounged about in bed for a good cozy while
-watched netflix and played solitaire in bed for ages
-started working on new art for the bathroom while watching netflix
-went to skillet for an average dinner with people who i realize don't actually care about me: aila and nada and then watched the hilarious bridget jones movie
-came home feelin kinda lonely and sad until i talked to jt who made me smile and also made me super super miss him

10/08/16
-slept in and then looked at furniture on the internet for absolutely ages
-ate granola and yogurt and watched netflix for a bit
-finally got out of bed properly and took a shower and then went to a haunted house outside of Seattle with Natalie, Maddie, Deepak, Sylvain, and Vivian, where i was not even scared at all 
-came back to natalies place where we watched the ring and i snuggled with cats for a while
-walked home in the cold and rain back home where i went straight into bed

10/07/16
-slept in on a Friday and then walked over to the aveda school where I got 4 inches off my hair
-came home and curled my hair, did laundry, cleaned the apartment, and watched netflix
-went out to marination station for lunch for "Ali" and then came back and ate it in bed with a netflix movie
-left the apartment at 7:30 in the dark and headed into work where we ate reheated pizza, played a lot of smash (and i won my 2nd ever game!) and then each had two very large shots of very disgusting rum
-the ladies got pretty drunk fast and we kept playing smash and occasionally testing before finally being allowed to go home at 2:30 where Merin dropped me home

10/06/16
-woke up tired and sore with a lovely headache and then went into work
-grabbed coffee with the team and then got flu shots together before going to an extremely dull meeting where all i could think about was my hangover and how starving i was
-ate a hotdog in occidental park with Yasha and finally relieved my hunger
-went back in and still felt like death and then finally fixed the bug in my story with Merin and gossiped for ages
-came home opened a forever 21 package and then just let my body relax and ate yogurt, strawberries, and brussel sprouts for dinner

10/05/16
-wore my first scarf of the season and went into work we me and Merin looked into my bug
-grabbed yummy fish and chips in occidental with Merin and gossiped as usual
-watched a presentation from KJ's team and then went back with the rest of the team where we all did nothing and then left for home
-cleaned the whole apartment and disassembled that toilet shelf thing, then ate an apple before going for a good fast long walk with Natalie followed by wine at her place with Maddie
-Headed out for pizza and drinks at the place next door, then over to R place for another drink and a midnight drag show

10/04/16
-came into work and dug deep into my edit citizenship modal
-had a much more talkative lunch with Yasha and Merin where I ate a burger
-came back and won my first ever game of smash and worked some more and talked with James about other changes to make
-talked to Alyssa on the phone while eating leftovers and mostly bitched about roommates
-got drunk, curled my hair, and sent suggestive snaps to jt and went to bed early lololol

10/03/16
-snoozed for ages and then finally got up and got ready and went into to work
-grabbed coffee with the team then worked on the citizenship modal before leaving for lunch
-went to an asian place in the ID with Deepak and Sylvain and was bored the whole time
-came back and realized the enormity of my story and tried working on it with JJ
-left work and came home and cleaned and then got drunk and Skyped with jt and had a good time 

10/02/16
-woke up and took a shower and then headed out into capitol hill and went to the art store to buy supplies for my halloween costume
-walked around the farmers market and ate apple samples and then wandered around cap hill before going to qfc
-headed up to the roof to soak up the sun and catch up on writing these entries actually in the notebook
-came back inside and made sweet potatoes and brussel sprouts for dinner
-ate some weed chocolate watched youtube videos, saw some really weird shit on chatroulette, ate sharp cheddar, and giggled quietly so sleeping nada on the couch wouldn't wake up

10/01/16
-slept in for the first time in ages and then hopped in the shower and went to the rei garage sale with KK and Patrick
-waited in line for ages and then didn't buy anything and then went upstairs to the regular clearance and bought a lot of purple stuff
-after not eating all day we finally left rei and went to 8oz burger co for breakfast/lunch/dinner and nada joined for a bit
-we headed back home to sort out bills and then started working on my halloween costume
-snuck into my room and drank wine while finishing off narcos and fucking around

09/30/16
-showered and went into work for a quick standup and some team effort reporting
-worked with JJ on a story and then went out to lunch with Merin and Yasha for a while
-came back to the office and played smash for an hour and then went to work for a little bit on the citizenship modal
-left work super early and shopped around downtown before coming home for dinner and a glass of wine and a movie
-went out to capitol cider with patrick and kk and shruti for good fun and then lots of introductions to Microsoft people, then headed to tomas' place for dull dull convos and wanting to leave and then back home where nada caught me back up on the drama

09/29/16
-woke up and showered and then went into work for stand up and coffee
-tried to do a bunch of expense reports and booked my travel to richmond
-worked on a story with JJ and then went to lunch with the team 
-came back and did some more work on a modal before heading home for the day
-repotted and arranged all 10 of my plants and drank cider and watched netflix

09/28/16
-slept in and then moved out of the hotel with JT and then went back to his place after dropping off packages
-drove over to Gus fruh and went for a swim in the sun and then headed to sno beach for snocones
-said goodbye to JT and then went to Cabo Bob's with mum for a last Austin meal and then dessert at Amy's then drove over to the airport
-sat on what seemed like an endless plane ride and then finally landed in Seattle where i got an uber back home
-caught up with nada a bit and enjoyed being back in my own bed

09/27/16
-woke up and headed downstairs and picked up our shit and went to campus
-waited ages for chickfila and then talked to tons of people about capital one for ages
-talked with old friends and then went back to the hotel where jt picked me up and then we went to hopdoddys
-headed back to the JT's where we played smash for a while, fell asleep during bachelor in paradise, then smashed ? and he tried to get me to dance and then went to the hotel to shower and get ready
-drove to north campus and brought Stas and Madeline to rajs place for pregaming and then drove downtown to sixth for drinks with Raj and jt and then back to the hotel for ?with a view

09/26/16
-woke up nice and early thanks to help from JT hehe and went into campus with Adan
-started tabling and talking to a ton of freshman and gave away tons of donuts
-grabbed lunch with Adan from oddduck and then headed back to campus to catch up with Stas
-headed back to the hotel and met up with Stephanie and Carlos for a bit and then walked to Amy's with Stephanie and then back to the hotel to hang by the pool
-grabbed dinner with them at home slice and then went back for the debate and then went to JT's for hottubbing with the gang and then back to the hotel for ? with windows

09/25/16
-finally got to sleep in and then went to torchys with mummy and had yummy queso and tacos
-sped over to dad's football and then back to the house to work on James essays again
-picked up burgerfi and had dinner with the family before heading back north with Ellen and Lily
-Ellen dropped off me and jt at my hotel where we met Adan and went to dinner at 24 diner where we had drinks and ketchup
-came back to the hotel with JT and got back to our usual antics 

09/24/16
-slept a bit on the plane and finally landed in austin where jt picked me up and showed me his new apartment
-Ellen picked me up and we headed south where i went back to bed for a while
-woke up again and went to the greenbelt with mum and dad and the poodles where we sat in a shallow river and cooled off
-came home and worked on James essay before napping and then going to the salt lick with the Scottish family
-brought the gang back and drank more and talked before going to bed

09/23/16
-took a shower and then went into work and went straight into a big demo of all of our aml stuff
-started regression testing and found some bugs with affiliate :/
-grabbed lunch with Merin and Yasha and then played a bit of smash before going back to issues
-started to do the testing for the release and then left work early to head home and get ready to fly back to austin
-took the link to the airport, went to three different gates, talked to the guy next to me, Gus, about living in trucks, rafting, and life in general, and tried to sleep

09/22/16
-found some new issues with relationship validation so i dug around in that for a while
-continued to debug and try to find the issue and then went to cherry st for a yummy sandwich and back to the office for some smash
-worked with KJ for a bit and then went back up where me and kavitha figured out the problem and fixed it with KJ
-came home and cut up a bunch of sweet potato, brussel sprouts, garlic, and an apple and had a delicious entirely plant based dinner 
-watched netflix and chilled and then went to bed early

09/21/16
-snoozed a bunch then went into work for a quick standup and coffee/pokemon go trip
-made some changes to the affiliate css and then started working on validation errors with KJ
-hurried over to the water taxi with KJ and ventured out over to west Seattle and ate a yummy hawaiian lunch at marination station and then wandered around until the taxi came back
-felt what 30 knots feels like and then dug back into the validation stuff with KJ
-took the link home because of traffic with James Pak, picked up all nadas packages, made more grilled cheese and chilled out

09/20/16
-woke up and got dressed and headed out to work in the cold and went to a long standup
-grabbed 'coffee' and then wrapped up my story before eating leftovers and then playing smash for ages
-made my first pull request and managed to survive! 
-left work and walked over to target to buy some new jeans and then got a ride back home where i called Ellen and made a yummy grilled cheese
-curled into bed with netflix and cider and then took a shower

09/19/16
-woke up and showered and then said bye to Brittany and walked to work
-worked on my express setup story for the morning and then grabbed a delicious sandwich from cherry st coffee and talked Ellen through career fair stuff
-went back to work and further test my story and then gossiped with Merin and kavitha for a bit before heading home
-went to QFC for much needed groceries then went home and started to make lemon cilantro chicken and talked to JT also about career fair
-decided to try curling my hair and then watched stranger things and took a shower

09/18/16
-woke up showered and then went to eltana with Brittany and tried to do a crossword
-saw a bomb(?) and then walked to the farmers market where we got apples and tomatoes and then picked up mimosa supplies from qfc
-took the stuff up to the roof and drank mimosas and ran away from bees while eating an apple
-took an uber to madison beach and sat in the sun and tried again to finish a crossword puzzle
-ate an okay dinner in madison valley then headed back up and went to molly moons, then drank wine for the rest of the night

09/17/16
-we ate breakfast at cafe pettirosso with nada and Brittany and then ubered over to freemont
-went to theo chocolate for a delicious tour and free samples
-walked around freemont and looked in vintage stores and then walked over to Ballard, did some shopping and walking
-went to kangaroo & kiwi for connect four, free cacti, and drinks and a yummy sausage roll
-came back to the apartment and drank wine and talked and listened to music

09/16/16
-had another lonely morning without most of the team but got a lot of work done
-went to lunch with tim, Sylvain, and David at a philly cheesesteak place
-did a bit more half assed work and then headed downtown to meet Brittany and then we went to machiavelli's for a salads and wine
-walked over pie bar where we had a huge ass peanut butter pie and really sweet cocktails
-came back and talked to Katie then ate some special chocolate and settled in with bugs life, sparkly cows, marketing and giggles

09/15/16
-woke up and listened to my old ipod on the way to work after sneezing into my cereal and making a big mess
-had a lonely stand up with just me and matt and then got down to business on removing the express setup 
-went to lunch with Sylvain, tim, and olya at hotpot where i burned my tongue and drank tea(?)
-came back to the office and worked some more before heading home to clean up and then met Brittany and went to suika for sushi and catching up
-went to capitol cider again and sat on the couch and gossiped before heading back home for the night

09/14/16
-woke up one last time with mum and said bye to mum before walking to work (hobo says i have nice perfume)
-arrived at work and actually got down to business and made some real progress
-went to occidental park and had fish and chips with Merin and Yasha and tried not to stuff myself
-gossiped and gossiped with Merin for hours and told each other our life stories and ate gelato instead of working
-came home, did laundry, finally got to talk to JT, cleaned the tiniest bit and started a new netflix show and drank wine

09/13/16
-went to work
-ate a hotdog in occidental with mum
-leaving work early and rushing to the OBGYN where they made me wait for 45 minutes before the doc saw me, found out my problems have no real solutions
-came back to the apartment and went downtown to pick up my prescriptions and then shopped around for a bit with mum
-took an uber back to cafe pettiroso and had a yummy dinner and a few cocktails before coming back to the apartment very sleepy and cozy

09/12/16
-woke up and showered and said bye to mum and listened to a sad sad podcast on my way to work
-looked over Merin's code and walked through it with her and felt productive
-met mum for lunch and we went to a mexican place for yummy enchiladas and a good break from "work"
-came back and worked with James on his story for a bit and then started and then worked on my own then left work with mum
-went to Machiavellis with mum for yummy ravioli then to the cider bar for drinks, rummiqub, and finding out secrets about mum and dad hehehe

09/11/16
-woke up early and realized you don't have to pay for parking at Sunday then got ready and then went to cafe pettirosso for a fabulous breakfast with mum
-started out on the long drive out to port angeles with car singing and talking and then went to cafe new day again and had a delicious burger again
-feeling incredibly full we drove up to hurricane ridge where the sky was clear and the views even better than before and then we headed back down and started to drive to lake crescent
-sat in some chairs in the sun on the shore of lake crescent and ate our desserts and then drove the 3 hour drive back to Seattle where we (eventually) returned the rental car
-walked back home and ate naan bread and drank wine and relaxed

09/10/16
-woke up showered and dried my hair then walked to get bagels with mum
-convinced her to get a rental car so we walked to the place, found out they were sold out, took a train to the airport and picked up a rental car
-drove out to snoqualmie falls and sweated hard climbing up and down and then had a rubbish sandwich in snoqualmie
-drove out to twin falls for a more picturesque but also challenging and sweaty walk and then drove to Ikea to buy plants!
-found parking nearby home and walked exhausted to get Indian food and ate it on the couch and planned out the next day

09/09/16
-morning showered again and then went into work and did nothing 
-went to lunch with Merin and James at the food trailers where i ate leftovers
-came back to the office and did looked for my award prize and then played a Rick and Morty card game with the team
-came home and cleaned some more then went to Courtney's hotel where Ben picked is up and we ate thai food in Fremont and caught up
-they dropped me off and mum arrived and we went into cap hill to a mexican restaurant for drinks and catching up

09/08/16
-took a morning shower and then went into work for a team agreement meeting
-ate a hotdog from occidental park with the team while catching pokemon from the lures we put down
-went to a coders meeting where we discussed the problems and good things about the summer camp and talked about the next one
-went back to my desk and tried to do some more work and talked to mark about MOD stuff and talked to tony for a bit
-came home and cleaned for mum coming home and then went to capitol cider with Courtney at like 10pm and caught up with her

09/07/16
-podcasted and arrived at work for standup and then trying and failing to find anything about the MOD issue
-went to lunch with Merin and Yasha, looked at kitties and ate wayyy too much fish and chips
-came back and gossiped with Merin more and then had a weird heart attack blindness thing??
-faked working and then left at 4 with Merin, streetcar'd home and then met the wifi guy
-burned some brussel sprouts, cleaned the apartment, and watched netflix

09/06/16
-listened to a podcast on the way to work and gossiped with mark for a bit
-took notes on AWS stuff and ate leftovers while half-listening to the aws lecturer before playing smash
-ubered over to lake union with the tdp crew for wine on a boat in an empty lake
-went back to flying fish for a slightly less intense but still delicious happy hour with tequila and oyster (but actually only tequila) shots, more salmon sliders, and pineapple martinis
-came home pretty damn tipsy and talked to mum and dad and netflixed the night away

09/05/16
-woke up in the actually warm tent and ate tortillas for breakfast and took down the tents
-stopped in forks Washington for an overpriced finally non-burger lunch
-started the long drive around the peninsula and arrived at the hoh national forest for schlime and photoshoots and wearing moss crowns
-started out on the road again and drove through olympia and tacoma stopping to eat thai food in a mall
-dragged all of our smoky stinky crap back into the apartment, finally showered, and went straight to bed

09/04/16
-woke up after a sleep in and took down the tent and packed up the car
-started the drive to neah bay and then set up our new campsite by the beach
-ate a ton of snacks and went out to point flattery for a while for photoshoots with bears 
-went back into town to the only restaurant on the reservation and devoured a hamburger and then headed back to the campsite
-tried to make a good fire for ages and drank wine and played campfire games and then went to bed

09/03/16
-woke up early and dragged all the stuff into the car with kk and Patrick and took the ferry to Bainbridge to begin the drive to port Angeles
-arrived at the campsite and set up our tent then drove to hurricane ridge for pretty sights and pine trees then drove to port Angeles
-ate a super yummy burger and had a smoothie then drove to lake crescent for drone pics and then started driving to Sol Duc falls
-walked and talked to the falls and then sang Taylor Swift at the top of our lungs on the walk and drive back
-went to a grocery store for dinner supplies then back to make an okay fire, eat special chocolate, quesadillas, cream cheese mushrooms, and cookies before going to bed

09/02/16
-woke up earlier than usual and walked to a diner to have a huggee welcome breakfast with Tim and our managers
-went into work and gossiped for ages and pretended to work
-played smash during lunch and learned new moves before gossiping some more and going to a meeting
-gossiped more and took the streetcar home where me and nada then went to rei again and then little Woody's for a burger
-walked to target and shipped for more camping stuff and then was so pooped I just went straight to bed

09/01/16
-snoozed a bunch again listened to the moth podcast on the way to work
-fixed my silly "s" bug and got my code to work and then pair programmed with James for a bit
-watched and didn't listen to an aws presentation with tim and then grabbed sushi thanks to tdp
-came back and tried to work on more react tutorials and then went to REI with James where i bought a bunch of stuff for camping and then waited for nada to arrive
-spent 2.5 more hours in rei with nada looking over every aspect of the store and then finally made it home to pay bills and eat raspberries, salami, and cookies

08/31/16
-snoozed a hundred times and then dragged myself to work
-did some more react tutorials before helping James debug his story unsuccessfully
-grabbed lunch with Deepak, tim, and David at a teriyaki place then tried with mark to fix an environment issue
-went to the "picnic" on our floor and had a cider and some cookies, played smash and then left work early with some free sunflowers 
-cleaned up my room, made "fajitas", and netflixed

08/30/16
-had a conference call about recruiting in my apartment and then went into work at 9
-made some progress on the disclaimer and then had an environment issue
-went to lunch with the team at a hot pot place where i ate with chopsticks and consumed most likely undercooked food
-came back and had a quick meeting then started a tutorial for react and then went home just before four
-went home and then to the grocery store and then made yummy brussel sprouts for dinner and then skyped with JT and watched bachelor in paradise

08/29/2016
-dragged myself out of bed and walked to work
-caught up on emails, dug around the code base and then gave up for a bit
-went to lunch in the park with matt and James for a yummy burger then back to work for a dumb capz meeting
-fucked around all afternoon and then came home from work to continue fucking around and have pasta for dinner
-got the worst headache I can remember and suffered through it by watching rent

08/28/16
-slept in and showered and watched netflix
-aila picked up me and nada and we went to the mall to eat chowder and catch up
-walked over to the SAM to meet Deepak and looked at art together for a while
-walked to forever21 and bought some clothes and then walked up back home
-ate dinner at 8oz burger co with Matt, Aila, Chris and Nada and then headed back home for netflix and an early night in

08/27/16
-slept a ton and then was picked up by Ryan (who had bagels and lots of opinions) to go get Jon with nada to go furniture shopping
-stopped at a goodwill, vintage store, and a couple more consignments stores before shopping around in Ballard
-ate lunch at hi-life in Ballard with mansplaining and then to kerrys park for the view and then off to Jon's for more dull convos
-walked back home and hung out with nada and skyped with jt until me and nada decided we were gonna try edibles together
-went out to uncle ikes, got some chocolate and picked up Jon and matt where they came over, ate edibles, grabbed a huge ass pizza, watched game shows on the roof, giggled and twitched a shit ton, and had a good chill time

08/26/16
-woke up and had a nice hangover shower and walked to mohai with my hair wet and slightly nauseous 
-ate breakfast with the kiddos and then worked on the finishing touches of their app
-had pizza, a ton of sushi, egg rolls, ham and cheese, more sushi, and watched all the kids present their apps
-Lena and Shadia won an honorable mention and then we had some museum time where the mentors just sat around exhausted
-Natalie gave us a ride home and I went to target, goodwill, and Annapurna with Nada and finally got to catch up before going to bed nice and early

08/25/16
-walked to mohai and started working on our app which involved lots of me telling them what to do over and over again
-finished the basic parts of the app and sent the kids home for the day
-went to happy hour at a very nice seafood place with the coders team and ate a ton of expensive (500+ bucks) and over the top appetizers and had three margaritas 
-brought the gang back to the rooftop for white russians and finding out about eskimo brothers
-talked with KJ on my couch about life and aspirations until 2:30 in the morning

08/24/16
-morning showered and walked to mohai
-taught blah blah
-went to a sausage place and had two orders of french fries with aioli with James, Deepak, KJ
-ubered home with James and then cleaned the apartment
-watched mona lisa smile and had some wine

08/23/16
-walked to mohai again and had a bagel breakfast with lena and shadia 
-taught them how to make mole masher which they really liked to make and then had lunch together
-came back inside and started working on the virtual tour app which was long and boring for everyone and then said goodbye for the day
-took an uber to cap hill to poquitos with Deepak, Paarth, KJ and Natalie which was fun until I heard the news about uncle Robert and left to speak to dad
-back home i chilled out for a while and then watched bachelor in paradise with JT and then was so tired i went to bed before 11

08/22/16
-woke up and walked all the way over to mohai where I met my two kids, Lena and Shadia
-started to make some basic apps with them and get to know them
-ate lunch with the kids and tried to supervise a bunch of rowdy kids
-came back inside and programmed some more before going to the museum where we ran through as quickly as possible and lost shadia a few times
-walked way back home and got sweaty as heck, then watched bachelor in paradise with jt while eating grated cheese, then talked to nada and youval for a while

08/21/16
-slept in and woke up not sweaty for once
-cleaned up the apartment and watched a lot netflix
-talked to jt for ages on the phone as he drove back to austin
-went into cap hill to buy suction cups then to goodwill for a frame that i painted white 
-watched part of bachelor in paradise with JT and drank wine then went on chatroulette and talked to strangers for a while

08/20/16
-organized my apartment and finally hung up some art on my walls while sweating ridiculously without ac
-walked all the way down madison to a plant nursery where I perused for a while ad then decided on a new house plant
-walked all the way back up the hill in 90 degree heat holding a large plant and getting strange looks
-went to KJ's place for a bbq with work people where I got to know the new guy tim and then went to Matt, Jon, and Chris' place five minutes away
-drank wine around the fire and had a good time with old friends, held Jon's hand while he slept, cleaned his puke, and made it back home

08/19/16
-went into work and fucked around and went to a design thinking workshop
-went to lunch with Merin and KJ and gossiped and talked for ages over tamales
-went to a quick coders meeting and the fucked around for a while until happy hour with the James, Deepak, the crazy feminist Maddy (who was less crazy), Natalie and KJ in pioneer square
-traveled up to cap hill and went to a mezcal place for some drinks then to a fancy, expensive, wine bar place, and then finally to a fancy japanese place for fun cocktails and crazy shooters
-traveled deeper into cap hill to lindas where we had more drinks, got to know each other more, Natalie held my hand for a while(?), then went to Natalie and Maddy's place, where i got the hint about where their night was going and went home

08/18/16
-work which was really just talking to Merin a lot
-lunch with Merin and Yasha and gossiped and ate hotdogs
-talked with kj and Merin and pretended to work for the whole afternoon
-left work and street car'd home to watch netflix and make grilled cheese and try out my new rug
-drank wine and chilled in my classy new room

08/17/16
-woke up and went to work where i fucked around for a few hours trying to look busy
-went to lunch with Natalie and Deepak at rain shadow meats and then drove over to mohai with a few cap one people
-learned how to make another app and set up a bunch of tablets and computers
-went with a few coders people for a happy hour with yummy margs and appetizers and good convos with coworkers 
-came home and chilled for a while with netflix 

08/16/16
-woke up and went to work where me and matt awkwardly confronted Kevin about being shite-y, awkward
-wrote down a bunch of shit about errors and looked into booking my flights to austin for recruiting
-reheated some pasta and looked over the logs with kj and then fucked around for ages
-left work and took the streetcar home and went to the grocery store 
-made some burnt grilled cheese and watched tv and drank wine

08/15/16
-woke up and snoozed as many times as possible before going in to work
-got to work and managed to do nothing for very large amounts of time and found out that I can go to austin for a while!
-pair programmed with James and then went to berliner for lunch and talking to mum and Ellen on the phone
-came back to the office to do nothing again and that was pushed into error logs i know nothing about
-quickly abandoned work and came home for netflix, cereal for dinner, and wine and a quick skype with jt and tindering

08/14/16
-woke up super hot and sweaty in the no-ac apartment
-went to a garage sale in cal anderson park and to the farmers market with nada
-made ravioli for lunch and watched a bunch of netflix and looked at plants online
-watched more netflix, sweated more, and made cajun chicken pasta 
-skyped JT and watched rick and morty together and stayed up late talking

08/13/16
-woke up with Courtney and got doughnuts
-walked downtown with Nada to get some more furniture for the apartment from target, tjmaxx, etc
-chilled and sweated in the apartment before going to dinner with Courtney's family and getting wine drunk
-ubered back home and meet Nadas friend and his friends for sushi and crazy people
-hopped around bars for a bit and ended up back on the roof to chill

08/12/16
-went to work and worked with mark for ages trying to fix my environment
-made my first pull requests and then fucked around for a while
-went to lunch with the team at the waterfall garden and caught pokemon at our two lures for a long lunch
-came back to work and acted busy before leaving at four and walking home where i made dinner and then went to goodwill with nada to make more stained glass
-picked Courtney up from the train station and brought her back home for wine on the roof, catching up, and a sleepover

08/08/16
-woke up and went to work while Ellen got to sleep in lucky duck
-had a walkthrough of the project with Mark then went to lunch in occidental park with Ellen
-came back to work and tried to act busy for a while and then took the streetcar home
-went with Ellen to get an orca card and then to macciavelli's for a yummy pasta dinner, then back to mine where I dropped Ellen off at the streetcar and said goodbye and then skyped with JT for a while

08/03/16
-walked to work and then worked on my todo list app for a while
-played smash with James and Mark for a while and actually got a little better!
-ate leftovers for lunch and played more smash
-finished my todo list app and then pretended to work for the next couple of hours
-streetcar'ed home and called mum and Ellen for ages then made salmon and worked on the summer Europe trip video

08/02/16
-walked to work slightly chilly and fucked around until our fire(d)side chat that was boring and corporate 
-went back to work and tried to setup my VM and failed and then did some Js with James 
-went for thai food with Natalie and James for lunch and then back to the office for a boring planning meeting
-messed with Js for a while and then left early to get the streetcar home and catch up with dad
-got groceries and made Cajun pasta 

08/01/16
-woke up and walked to work where i sat in on my first stand up and gossiped about the announcements
-did nothing and continued to gossip with the team and then played smash bros for a while
-went to lunch with James at rain shadow meats and then went to a bar at 2pm with KJ, James, and Deepak and then to a fancy rooftop bar for a $20 drink and more gossip
-walked to nordstrom rack to buy hiking/running shoes and then to target for cleaning supplies and then all the way back up the hills to home
-called Shonagh and caught up with her, watched tv, skyped with jt really quick and watched more tv

07/31/16
-slept in and had crazy dreams about marrying jt and adopting more blind dogs
-went to Deepak and James place for brunches funches and some day drinking and sun burning
-drove out to golden gardens again to chill with my toes in the sand, eat pizza, and hang with the new gang
-started a fire as the sun went down and watched people get druuunk and other people spin and throw fire and scary angry feminists get angry and be sensitive
-took the slowest uber ever with Deepak and said scary feminist where she claimed being old > being young and then the uber driver said I could take his number and that i said no because i didn't want to look like a 'loose woman'

07/30/16
-woke up surprisingly not hung over! fucked around in the apt for a while and watched tv
-talked to Katie on the phone for a while and caught up with each others lives
-Nicole picked me up and we drove out to golden gardens to sit in the sun and people watch
-drove into bellevue to go to a sushi place with a conveyor belt and then went to bellevue park to pokemon hunt
-walked for ages around this park with hundreds of other people and joined in on some stampedes, then drove all the way back home with Nicole

07/29/16
-walked into work and started doing some javascript exercises then had coffee/lunch with Natalie at an Italian coffee shop and then went back to work to try out more javascript
-went to my own happy hour and had a few beers with some managers and tdp people
-went to Deepak and James' roof for more free drinks, then to Pono Ranch with Natalie, Deepak, James and some of their friends, jammed to some music, drank a marg, and then headed to a brewery for some meh cider and more conversation
-walked to a dispensary and was baffled then to a bar for quick whiskey shots, then to a Scottish pub for killing it at foosball, being called 'weapon x', trying to get free drinks by being Scottish and failing, and stupidly drinking gin
-took a lyft back to Deepak and James' place for relaxing, playing with a cat, eating toast and grilled cheese before taking a very talkative lyft home

07/28/16
-woke up and walked to work as is my new usual
-fucked around on my computer doing nothing and did expense reports
-went to lunch with KJ and Benji at a vietnamese place and then headed back to work to fuck around some more
-had a coffee meeting with Deepak which was only mildly uncomfortable and forced then came back for a 10-10 with Tony which was vague as always
-took the streetcar back home and made dinner out of crap in my fridge and watched tv with wine

07/27/16
-woke up and did the long walk to work 
-worked on trying to fix my proxy for like 3 hours and then managed to fuck it up so bad I lock myself out of my account and KJ had to come and help me for ages 
-went to a cap one coders training session where I learned how to make apps in app inventor 
-went back to my desk and tried to set up Ruby and failed and KJ came to my rescue again
-walked all the way home, made dinner and Skyped JT for bachelorette for ages 

07/26/16
-woke up and got ready for day two of grown up life
-walked in a little more casually and filled out CBTs all morning
-went to lunch with Deepak at a kebab place and heard some of the office gossip
-came back to the office for more fucking around, barely looking into JS, and then going to a meeting with people who I don't really know
-came home and made a small dinner and watched tv and netflix and drank wine with candles

07/25/16
-woke up and got ready for my very first day of work
-walked stressfully to the office and met with Tony for the first time and got coffee 
-was shown around the office and met a ton of people and then went to lunch with the other newish hires
-had the unofficial tour of the office and then was sent home for the day where I talked to Brittany on the phone and sweated my ass off
-went to qfc and made a grown up dinner and talked to mum, Ellen and jt about my day 

07/24/16
-woke up back in Seattle and did some grown up stuff with credit cards and banks
-went up to the roof and admired the mountains and wrote this out for a while
-walked downtown to the market and explored and then went to target to pass the time
-went to a strange pokemon go meetup at pikes place and then met Nicole to continue the pokewalk
-walked around for ages and had chipotle with Nicole before going back home for the night

07/23/16
-woke up bright and early with Kevin and got ready for the airport
-said goodbye to Kevin and went to the airport where my flight was late 
-had an exit row seat and fell asleep for a wee bit and read a little then arrived in Minneapolis where my flight was also delayed 
-somehow fell asleep through takeoff and then watched the big short on the long plane ride
-made it back to the apartment to make pasta for dinner and watch bachelorette with JT and catching up

07/22/16
-woken up with house keeping and was late and quickly got dressed and packed and ran downstairs 
-did a scavenger hunt around Richmond with Kevin, dan, and Daniel driving and was hot and sweaty and didn't really try
-made it back to the hotel for lunch, said goodbye to people going to McLean then went to Kevin dan and Daniel's apartment with Greg and then to target for a hundred years to buy nothing and then got a Wii u
-played some Wii and said goodbye to greg and then went to carytown for sushi where Daniel break danced in the streets and a drunk biker puked at us
-came back home showered and then drank beer and cocktails with the gang and their friends and played bs and slept on airmattress in their living room next to Kevin

07/21/16
-woke up and had breakfast with our line of business with Adan, Nathan, and greg
-won a spaghetti marshmallow competition and then went to watch Rob Alexander speak and then went to a hilarious happy hour with Greg, Kevin and dan and stood dangerously close to rob 
-came back to the hotel and then went over to Greg's room for some light making out and then headed out to a trailer park at a brewery to meet up with Kevin, Dan, and Daniel where we ate, drank and laughed like crazy 
-pregamed some more at their place then went to the tobacco company but weren't allowed in, Dan almost switched shirts with a homeless guy, we drank a ton and did shots (with Kim keno) , tried again to get into tobacco company, took care of a distraught drunk woman who just wanted love
-said goodbye to the gang and walked home with Greg and went back to his room for some hot rubbing and then ? and then scrambled back to my room at 4 and showered

07/20/16
-couldn't wake up Adan so caught the bus with Alex and talked Seattle 
-ate breakfast with the Chicago table and sat through hours of long boring talks
-ate lunch and flirted casually with Greg again and learned about capital one economics
-got the bus home with Greg and sat dangerously close and continued to flirt before splitting off and taking naps
-went to a seafood dinner with Adan, Greg, and some Chicago people for food and flirting and then played Pokemon go with Greg and Adan and was dragged aside and pulled up close for a secret kiss and then returned to playing pokemon while pretending it didn't happen ?

07/19/16
-woke up and early and grabbed Adan to go to more on boarding!
-sat for hours listening to talks and talking to greg and Dan in between 
-ate lunch then did an agile workshop with the gang and then headed back yo Richmond 
-went to the fine arts museum and had delicious food (which I nearly spat out from laughter on a few occasions) with Dan, Greg and Kevin 
-went to Dan and Kevin's, saw the glorious bathroom, drank more, then went to carry town for flirting with Greg, drunk birthday Adan, and then back to the hotel for drawing with Brent and Greg 

07/18/16
-woke up repeatedly last night and early in the morning thanks to a gin hangover 
-arrived at cap one for long boring speeches and meeting mostly really good people
-got my laptop, lost my phone, ate a shitty lunch, and learned next to nothing!
-came back home on the bus and went out to expensive dinner with some meh people 
-went on an Odyssey to get drinks then drank by the pool, got deetz on Seattle, played mushroom cup, and tried to flirt with Greg but was beaten to it by Adan lololol

07/17/16
-woke up hella early to go to the airport 
-flew from Seattle to Detroit are a breakfast "burrito" and then flew out to Richmond 
-landed in Richmond and met up with Adan again
-had drinks with the old intern gang and ate dinner at the opening reception 
-had more drinks and stupidly flirted with Xavier again before going to bed 

07/16/16
-slept in for the first time in ages 
-took a shower and made a tuna thingy for lunch 
-went out into capital hill and caught Pokemon in Cal Anderson park with a ton of other people
-walked up to volunteer park catching Pokemon along the way
-had leftovers for dinner and watched the bachelorette with JT and talked for a while

07/15/16
-attempted to hang up a bunch of art and reorganized my room
-finished game of thrones
-cleaned up the whole apartment
-made a teriyaki chicken for dinner
-got drunk with JT on skype and watched the bachelorette and then messed around on the webcam

07/14/16
-woke up early thanks to jet lag and caught up on tv/netflix for a while
-walked all the way to target, did some shopping, and then walked all the way back to the apartment
-cooled down then headed to cap hill for bagels and pokemon then to do my first round of grocery shopping
-played some more pokemon then walked to pikes market to get mac n cheese and gelato with aneesha and to catch up and have my first ever apartment guest
-watched the bachelorette with jt and drank wine on my lovely couch

07/13/16
-woke up early with mummy and then said a teary goodbye as she went back to austin
-ate breakfast and watched netflix in bed for what felt like the first time in ages
-took a warm bath and watched orange is the new black from the tub
-reheated pizza for lunch and watched netflix and set up my room some more
-skyped with jt where we watched the bachelorette together and talked for a while with some wine

07/12/16
-me and mummy woke up and went to eltana for the yummiest bagels!
-walked around cap hill and caught some pokemon before embarking on our journey to the space needle
-went to the chihuly glass gardens and explored there and then took the ride up to the top of the space need where we both felt a little bit ill
-walked back to first hill and got another crazy deal on a duvet from west elm and then went to dinner at ristorante machiavelli for yummy pasta and wine
-walked to boom again (this time already quite buzzed) for two rounds of cocktails and girl talk then back to the apartment for more drinks and talking to random neighbors on the roof

07/11/16
-mum woke me up early and moved in and walked around cap hull and explored
-went and shipped downtown at Ross and tjmaxx and then got a call about my furniture arriving and ran back to the apartment and got hot and sweaty 
-went back downtown, ate yummy grilled cheese then bought some awesome one of a kind custom tables and brought them home 
-walked to my work in pioneer square then went and had margaritas and lousy queso by the market
-went home and showered and then went to boom in capital hill for yummy cocktails and dinner and then to cupcake royale again and then home for wine on the roof

07/10/16
-woke up and drove to gas works park with mum and dad and caught Pokemon
-went to Pike place market, saw cool flowers, watched the euro finals in an Irish pub, and ate samosas and saw the gum wall
-had cupcake royale then went to seward park for a lovely walk
-had dinner in Columbia city with weird Unicorn people and delicious food
-said goodbye to daddy and then Skyped JT and then went to bed

07/09/16
-woke up for the first time in my new apartment on a mattress on the floor
-unpacked some more then mum and dad came over and we headed out to ikea
-found my new dresser and desk at ikea and then discovered a perfect condition couch for 200 dollars off and bought it!
-did a bit more shopping and saw mum and dad's airbnb and then took the dresser and desk home to build
-finished the furniture and ate pizza and stayed up waiting for my couch not to arrive grrr

07/08/16
-woke up very early to catch a 7am flight to Seattle
-arrived in Seattle and picked up the rental car then went to the apartment for the first time!
-after admiring the apartment we went off to Ikea where we completely stuffed the car with stuff
-stuffed the car even more with stuff from target, best buy and home depot then got five guys
-came back home and started to unpack and move in!

07/07/16
-woke up and drive up north to get fingerprinted 
-went to Ikea and North Lamar to pass the time with shopping
-had ramen with Alyssa and Jamie and then cupcakes from Amy's and caught up and freaked out about being grown ups 
-went over to JT's for some bachelorette (bye Chad) and then pterrys one last time and then messed around for the last time
-came home and did last minute packing and hung out with the family

07/06/16
-woke up at JT's and slept in while he went to class and then ?
-met up with Brittany for lunch at kebabalicious and caught up on her life and then said goodbye for a while
-came back home and went to holly's pool with Ellen and James and charlie
-helped mum get ready for my good bye party and sat around
-hosted a goodbye me party with the Scottish family and ate yummy barbecue and played pokemon go with the gang

07/05/16
-wrote up very early for my dentist appointment
-took James to his driving test where he passed and I got hot new booties!!
-came home then went to Starbucks with Shonagh and finally caught up
-went to JT's for bachelor and then ceviche and a shower
-best. night. ever.

07/04/16
-slept in and had a Marathon with JT :)
-went to torchys for queso and breakfast tacos
-watched the rest of the bachelorette and made brackets together 
-went home for a bit then back to JT's to watch more bachelorette 
-picked up a pizza and went to castle hill for the fireworks then to sonic and then more bachelorette and then finally drove back home

07/03/16
-woke up with JT, took a shower, broke a shower... 
-watched some Ricky and Morty and then went to flyrite for chicken
-tried to go to Barton springs but it was too busy then swam in JT's pool with mermaids and fishermans
-went to hopdoddys with the family and then got ice cream with Stephanie and her boyfriend 
-went to spiderhouse with JT and then watched the bachelorette and drank wine and then had fun with drunker than me JT 

07/02/16
-woke up really early thanks to jetlag with JT
-went back home to pack up my life into five suitcases 
-went to Flores for lunch with the family and ate way to much and started packing again
-saw the Swiss army man at the Alamo with the family 
-went to JT's and went to mangiries for pizza and then back to his where I fell asleep in his lap for ages then made it to bed for ?

07/01/16
-woke up and did grown up shit and sorted out my life
-went swimming at Holly's with Ellen and James and hung out with Charlie
-went to torchys with mum and Ellen and then preview shopping for Seattle
-went to JT's for a reunion and lots of drinking and swimming
-had a blast like the good old days

06/16/16
-woke up and went to granny mays with dad Ellen and James, then walked to the train station
-took the train into Glasgow and wandered around the city center and the uni for a while, saw the goma and hunterian collection
-ate lunch at a curry place on Ashton lane then went to little pub to watch the football
-went to a nardinis for a strawberry tart and then went to dinner with mum, Lorna and Amanda at a nice french restaurant 
-met up with dad and dad's friend Stephen for lots of wine and outspoken jokes and then the train and taxi back home to monkton

06/15/16
-woke up, showered, and then dad picked us up to go to largs
-walked around largs for a while, ate lunch in a small cafe, played with amusements and then had an ice cream
-went back to visit Robert who was awake this time and talking
-went to granny mays with dad to paint the fence
-went to Ayr for a lovely dinner with the Gordons and then back to grans for a while

06/14/16
-woke up, showered, and planned for the rest of our euro trip and drove with the family to Ayr to change out our money and had a greggs for lunch
-drove to the hospital to see Uncle Robert :'(
-tried to cheer up at Dean castle park where we saw pigs, deer, and goats
-went out to the ship inn with all the wyllies and had our farewell dinner
-signed my Seattle lease then found out that they're moving all tech out of Seattle, yay

06/13/16
-woke up hungover early in the morning 
-dad dropped us at Granny Jessie's for breakfast and a good shower
-Jayne picked us up and took us to silver burn where we didn't like any clothes and wandered up and down for ages
-had Frankie and Benny's for an okay dinner then met up with James, Andrew, and Matthew to watch the conjuring 2
-came back to granny Jessie's and played cards for a bit

06/12/16
-woke up and had breakfast and lunch at Granny Jessie's 
-went and picked up granny may and headed to the ceilidh 
-danced at the ceilidh for a while with Alan, Tommy, Stuart etc
-Went out for drinks with Andrew, Matthew, and Ellen
-drank some more and dad picked us up from the train station

06/11/16
-woke up early and packed up oscar and then drove the long way back to Glasgow 
-went Mugdock park with Lorna for a nice walk and then Lunch in the park
-went back to Lorna's for playing cards, eating Chinese, and drinking strongbow
-went back to granny Jessie's to read my Seattle lease
-was lectured about mold and then went to bed

06/10/16
-walked to Blair castle and did a tour and then collected pinecones in the gardens 
-started driving to loch Lomond and then stopped at the side of the road for sandwiches in oscar
-arrived at loch Lomond to tons of midges and met Alan, Tania, Matthew, and the babies then ran away to safety inside oscar
-went to dinner with the family and caught up and played with babies 
-ran back into oscar and hid away inside with wine and card games 

06/09/16
-woke up early and went to the tourist filled Urquhart castle and walked around
-had an okay toastie in nessieland and then drive to loch Morlich
-picked up pinecones and walked around the gorgeous loch
-felt sick and drove to Blair atholl and ate a bunch of snacks for dinner
-went to the hotel pub had some drinks then came back for some card games

06/08/16
-woke up and drive out to Glen Finnan monument and saw the viaduct 
-drove the. Single track road to salen we went to lunch in a nice hotel (pizzzaaaa)
-had an ice cream and looked in rock pools 
-went to tioram castle and breathed in clouds before driving up to Inverness
-drove to our campsite in Inverness and settled in then went to dinner and then applied for an apartment

05/28/16
-woke up and moved out of the shitty hostel we were staying in and hung out in Hyde park for a while before moving to our much nicer hostel
-checked in to the new hostel and went to tescos to pick up picnic supplies then went to Hyde park and had a picnic in the sun
-walking tour that we ditched to walk around on our own
-came back and then went to Hyde park for a while then walked around Paddington
-was gifted a bottle of wine by a crazy guy in the bunk below us then drank with him and a guy from Beirut who was cool, ended up becoming enemies with London guy and having weird drama??? Ate Yemen chicken and was told I was beautiful by an Irishman and a guy from Lebanon lol

05/24/16
-drove back up from south austin and went to lunch with Clint at Don food truck which tooook fooorevvverrrrrr
-JT picked me up and then I remembered all the shit I need so we went to target and then to CVS which toooook forevvveeerrrrr
-Went to whataburger because I was starving JT and being a meanie face then we swam in the pool for a bit and showeeerrreeeeeeeeedddddd ;) and then went to get a snocone
-went back to JT's to watch rick and morty and ya knooowwww 
-did some last minute trip stressing and made JT wait around again because i'm the worst and then grabbed last minute pterrys and then watched rick and morty and tried to fall asleep

05/23/16
-woke up and watched Rick and Morty with JT and messed around on the couch
-went with Alyssa to Amy's for our last Austin meetup
-dragged JT to the animal shelter to look at cute puppies n stuff
-went to the salty sow with Katie and Brittany for happy hour
-came home and packed and did last minute planning

05/22/16
-woke up and messed around with JT and he made me waffles
-went to the park and played frisbee with JT and then went into the pool for a bit
-watched Rick and Morty for a while before going to dinner with Ashleigh at magnolia cafe and saying goodbye for a while
-JT convinced Raj to go to dreamers to get me a ? lolololol
-used said ? for a while and had a blast

05/21/16
-woke up early again to get ready and then went to wholy bagel for graduation bagels
-went to the Erwin center and luckily met Alyssa and then went inside with her and Jaime and the ceremony was pretty uneventful, but I walked across the stage in cute ass shoes and GRADUATED!!!!
-Met up with mum and dad and took a bunch of teary eyed pics and saw Ashleigh at the fountain then went to ztejas with mum and dad for drinks and dessert then back home to chill for a while
-Katie picked me up and we perfectly timed our arrival to see the fireworks from the roof of the wrw and then went to Julia's party where I drank a lot of prossecco and hung out with Chloe and Katherine
-JT came to the party and took my very drunk self back to his place where we hung out for a while and I acted ridiculous

05/20/16
-woke up early to take senior pictures on campus with Ellen, ran around in a robe and took semi-awk pics
-met up with CHLOE HENRIOOOO and Ellen at mandola's and finally caught up with her
-got pedicures with mum and Ellen for graduation (echoing my 5th grade graduation pedicure)
-went to Jack Allen's kitchen for tons of appetizers, mango habanero margs, yummy food, and even a dessert!
-came home and wore my new graduation shoes, helped James with programming, and hung out with the family

05/19/16
-woke up early to get donuts then went back to bed
-JT dropped me off chez moi and then Alyssa brought over pterrys and we caught up
-went back to JT's where we hottubbed/swam for a bit
-Brittany picked me up and took me south to nxnw to meet up with Katie, where we caught up over beer and food
-came back home and hung out with mum and chatted for ages

05/18/16
-woke up had breakfast and felt kind of sick
-felt better then messed around on the ? and really tired myself out....
-got a peach and orange snocone with JT
-got amys with Kathleen
-made the world's cheesiest macaroni and cheese and then watched Rick and Morty

05/17/16
-slept in and then packed up my stuff
-ate five guys and went to the military store
-drove home and bought a new bag for Europe, looked at apartments, flights and helped James with Java
-JT picked me up and then we went to the poetry slam
-picked up a pizza, watched Troy and started to fall asleep, then talked for hours

05/16/16
-woke up at my parents place then drove back up, met JT, and thought about packing but then decided to take a shower and ?
-went to frisbee golf at zilker park and I sucked a lot
-went to home slice and had yummy yummy pizza and blew out a candle several times with laughter
-went over to Courtney's to hang out one last time and drink wine
-JT picked me up, we played halo, and ?

05/15/16
-woke up snuggled between Lily and JT
-drew some chalk roses in the kitchen while watching greys anatomy
-mum and Ellen came up to pack and paint the apartment
-finally booked our last hostel for Rome
-went over to JT's for salmon burgers and game of thrones and ? then drove down south in the rain to stay the night

05/14/16
-slept in til 1 then ? and then went back home
-started to pack up my room and move out while eating a milkshake from Amy's
-freaked out a lot about moving/Europe/life and ate dominos
-JT came over, we walked Lily, played oblivion and drank wine
-:)

05/13/16
-slept through an alarm and almost missed lilys haircut appointment and dropped Lily off and grabbed some donuts
-hiked down to the creek at violet crown trail and swam, fled from snakes and had a fucking blast then hiked back up in crazy humidity
-picked Lily up from down south then went home and hung with mum for a while
-went to the salt lick with Stas, JT, Raj and Raj's friends
-watched oceans eleven at your place and then ?

05/12/16
-got very little sleep but still had a good time
-went to heb to restock on food then back to JT's and layed on the couch for a while and relaxed then ya know 
-hopped in the pool for a little bit and then headed over to my apartment for a shower
-picked up a dominos pizza and went back to JT's for always sunny and pizza
-raj, Stas, Madeline and Sam came over and we had forties and watched weird weird videos

05/11/16
-woke up and decided to paint the kitchen with chalkboard paint
-walked Lily to the park with Ellen
-went south for book club, with sangria, chili, tacos and homemade ice cream
-came back up and waited for JT to finish OS and then went to his place
-Raj and Stas came over and we hottubbed until 3:30 and then they left and ?

05/10/16
-woke up and finally put away my laundry
-made cookies for JT and brought them over to him
-went home with Lily and hung out with mum and made salmon for dinner
-went to heb to get book club supplies and then for a walk with the dogs
-came back up and started planning Europe details

05/09/16
-slept in and snuggled with Lily for a while
-went for a hike to violet crown trail with the dogs and mum and Ellen
-went to cherrywood coffee shop with Nada to look at Seattle apartments and had more luck than last time
-walked with Stas to quacks and met up with Madeline
-watched a romcom with wine and popcorn and cucumbers

05/08/16
-accidentally slept in until 1pm
-Stas drove me, madeline, and Raj to the domain (very scary) and I was still unsuccessful at finding a grad dress
-came back home and ubered to campus for the wics end of year banquet 
-food was a little late but super delicious as always, clay pit catered in the GDC
-went back to Siena and Paige's place for lots of yummy wine, game of thrones, brownies and good conversation

05/07/16
-had a good time with JT in the morning
-went to kayaking with Kathleen and actually exercised!
-Picked up a snobeach with Kathleen and headed back home
-fucked around with Ellen for a while and then went to pick up pterrys :)
-went with JT to ernesto's party where we played cards against humanity for forever, sat in a "hot tub", watched people climb stop signs, and ?

05/06/16
-took Lily to her surgery bright and early then went back home to nap
-finished my last ever college paper and relaxed 
-hung out with my mumma then picked James up from school and went to get Lily!
-hung out with Lily at home for a bit and had dinner before going back north
-went to campus for the acm gaming night, played shitty werewolves and won, then went back to my place where we made chicken and JT stayed the night

05/05/16
-went to my last ever college class where I played sudoku the whole time
-came home and worked on my stupid consciousness paper for ages
-went to santa rita with Brittany and had the worst ever service and a blegh marg
-went to el chilito's for frozen-ish sangria instead and caught up 
-fucked around for a while doing nothing then went to JT's for hot tubbing then drove down south with lily late at night

05/04/16
-JT took me home and I got ready to go to my computational brain final
-coasted by on my brain final and then sat around in the WiCS office for ages
-booked Budapest airbnb, ate a panini, and hung out with JT
-presented my ios project to the class 
-went to JT's where we picked up dominos and watched shrek, showered, and ? and then came back home

05/03/16
-went to interaction design and worked on the gainz presentation
-hung out in the WiCS office and worked on the gainz presentation with Siena and booked flights with Stas!
-took Lily to the dentist and decided she needed two teeth removed
-went home for dad's birthday!! Went to satellite cafe and had drinks and pasta and dessert and then back home to open presents
-came back home and then went over to JT's ?

05/02/16
-actually managed to wake up on time and leave JT's place in a quick fashion
-messed around on Pinterest and went to computational brain where we did a practice final
-read my book outside on a surprisingly cold day and had bagels with JT at the gdc
-caught up with Alyssa (and she met JT!!) And went to ios for some pretty dull presentations
-worked on my paper and killed a very scary cockroach

05/01/16
-woke up and stayed in bed with JT until like 2 JT and made me super yummy quesadillas using leftover queso
-came home and gave Jiwon back her keys
-took Lily to central park and read more of my book
-made a basil tomato chicken pasta dinner with Ellen
-got pterrys milkshakes and went to JT's to watch game of thrones and then stayed the night

04/30/16
-came back to my place with JT to take lily out and have fun...
-went to torchy's for queso and breakfast tacos with JT
-worked on Gainz for a while and talked to Katie on the phone
-went to Nada's place for pregaming before going downtown to celebrate her 22nd, danced & drank with Aneesha, Frank, Jiwon, and Nada
-Got an uber ride home to JT's where we watched a little always sunny, showered, and then passed out together

04/29/16
-JT had to go to a 9am class so I went back to sleep for another two hours
-read that dumb stupid consciousness book for a while
-JT picked me up and we went to eat pizza at the top of the graffiti wall
-Hot tubbed solo for a little while and then invited the usual gang over for drinking and hot tubbing
-Got very very very wine drunk and partied hard with the gang

04/28/16
-bullshitted my way through my interaction design test and left after 13 minutes
-came back to the apartment and tried really hard to read through another chapter of my computational brain book
-took Lily down south with Ellen to get her checked out with Dara, looks like she'll need some teeth removed
-JT picked me up and we went to HEB to get quesadilla supplies, ate some of those and then went to Fuzzy's for incredibly cheap and sloppy margaritas
-drank some more at his place and then headed back to mine for a good night :)

04/27/16
-made JT skip class and state's in bed with him until 1:30
-showered with him and headed back to take Lily for a really slow unmoving walk
-"studied" for interaction design and listened to Lemonade for a while
-went to campus and caught up with Ashleigh and reminisced for a while
-went to the really long and dull ACM elections and then came back home for more "studying" + beyonce

04/26/16
-went to interaction design and gave a really half assed presentation
-picked up Kathleen and her friend and drove them to the airport
-read my book for the brain class REALLY slowly and went to momoko with Stas and Madeline for rice balls before they close forever
-went over to JT's for a Wedding Crashers + wine + :*
-kind of had a breakdown??? (moving + relationships + graduations = stressed Alison)

04/25/16
-ate breakfast chez JT and then headed back to the apartment
-tried really hard to read the first chapter of my computational brain book and failed
-made lemon chicken with Ellen for dinner
-showered then went to campus to work on our interaction design project
-came home late and watched Jane the virgin instead of practicing for the presentation

04/24/16
-stayed in bed until two with JT 
-went to torchys for breakfast tacos and queso
-came home and took Lily for a walk and then took a much needed nap
-went to campus to work on our stupid interaction design project and cried a little bit about leaving campus soon
-went to JT's to watch game of thrones and then stayed the night

04/23/16
-woke up early and went to the animal shelter with ACM got hella sweaty and covered in dog saliva/hair
-went to lunch at top notch with Raj, Stas, and Getz and then ice skated with acm, but mostly JT
-went to sno beach with JT and swam in his cold pool and then went to mandolas
-had Raj, Stas, Madeline, Getz, Eddie and Nikita over to JT's place for a night of drinking and finding out weird things about each other

04/22/16
-woke up early and said goodbye to JT and then went back to sleep
-had a phone call with Natalie from the Seattle office and found out some deetz and took Lily for a nice sunny walk
-walked with Brittany to Trudy's for margs and gossip and reminiscing
-crashed the family's dinner at Texas land and cattle and then went home to walk Sophie
-went to JT's place and played Xbox, did chatroulette and just hung out

04/21/16
-Went in the rain to interaction design and did nothing
-walked Lily in the sunshine and then worked on gainz for ages
-went to torchys with Alyssa and caught up over queso
-JT came over we got wine and watched always sunny
-went to Stas' place and watched guardians of the galaxy with Stas and Madeline and Eddie and Nikita and Raj then walked back to my place to sleep

04/20/16
-woke up and went to Shipley's for donuts
-took Lily out and then went south to walk Sophie
-worked on gainz for a while
-went to Mozart's with JT to work but the wifi was shit!
-went to magnolias for dinner 

04/19/16
-woke up with a delightful uti so I skipped interaction design and went to the doc and got some antibiotics and then picked up JT
-got tortilla soup at heb and came back to the apt and made it with JT
-took Lily out and then went with Ellen down south to see Sophie
-went to James steel drum concert at the one world theater and felt like exploding
-JT came over and we played left for dead then we went over to his place

04/18/16
-woke up and made JT late to class which turned out to be cancelled lol whoops
-got to wear my rainboots and rain coat woot and went to computational brain and mildly enjoyed myself?
-went down south and took Sophie for a walk and ate a bunch of snacks
-went to the wics bull session and elections then headed down south to try to pick up James but instead go to the wrong place and then just drive home in defeat
-went to pterrys with JT and then he came over and we watched it crowd

04/17/16
-woke up and spent some time with JT hhehehe
-came back to the apt and showered to go to a super mexican restaurant for lunch with Stephanie and tried my first ever torta
-became an actual couch potato and finished the rest of unbreakable kimmy schmidt and worked on go to hell
-made teriyaki chicken broccoli thingy for dinner with Ellen
-went to JT's to be nearly boiled in a hot tub, play Halo and be really really bad at it and then stay the night

04/16/16
-woke up and had a quick shower and then walked to JT's place with him to get his car and eat quesadillas 
-went for a hike at Emma Long park with Raj, Stas, Madeline, and Lily
-came back and showered and worked on the go to hell app
-went to dinner at the Silo with Kathleen and got to finally catch up
-went to JT's and played Dragon age for a while + drinks and then staying the night

04/15/16
-woke up and showered and slowly slowly finished my paper in between unbreakable kimmy schmidt
-pizza for lunch then snocones with Ellen and lily
-brick oven with aneesha and yummy lasagna
-walked Sophie and lily with mum and Ellen while dad fixed the dishwasher
-went to raj's place for cards against humanity with Stas, madeline, JT, Eddie and Nikita, then I dragged them to Amy's, and then we went up to a temple? and then me and JT came back to my place

04/14/16
-went to interaction design and played sudoku
-came home and went to the park in the sun with Ellen and chilly
-picked up cookie cake, got James the birthday boy and went to get snocones
-opened presents and went to the salt lick and ate cookie cake
-went to JT's to play dragon age

04/13/16
-spent the morning with JT ;)
-figured out a lot of hard stuff for my go to hell app
-started working on my brain paper and just felt clueless
-picked up dominos with Ellen and was way too excited
-went back to work on the paper

04/12/16
-went to interaction design and did nothing
-made fancy lemon chicken for lunch and walked Lily
-worked on go to hell and not the paper I need to finish
-had a huge huge fight with Ellen that included scratching, tears, a yummy pasta dish, and drinking nearly a bottle of wine
-went to JT's place for wine and stuff and matching shirts

04/11/16
-got the most sleep in ages, said bye to JT and showered
-went to computational brain and was bored
-came home cleaned then hit the mall with mum, returned some stuff and bought a sweater and presents for James
-went to heb with JT and then back to his to make dinner and chill out
-sleep alone for the first time in ages

04/10/16
-came home and showered
-caught up on TV and sat around for ages
-went to Jo's with Ellen and they didn't have my favorite sandwich anymore :(
-went to Mozart's with Nada and looked at apartments
-JT came over and we watched always sunny on the couch with wine and he stayed the night

04/09/16
-woke up and picked up Stas Madeline and Andy and started to drive to Hamilton pool then realized it was full and turned around and found a stained glass sale!
-went to the natural gardener and got a cactus that made JT bleed and then went to top golf and was really bad and JT was really good
-went to my lean in circle which was okay and then went shopping with Alyssa and didn't actually get anything
-went home for chili and then back here for a shower
-went to Stas' for a party of gossip circles and dancing then back to JT's with ya know

04/08/16
-JT had to leave early and I worked on my paper
-got pterrys with Ellen
-went to an awkward photo booth and then to snocones with JT and his bro
-finished the paper and went to via313 
-stayed at his place and played smash bros and smashed???

04/07/16
-woke up at JT's and ate strawberries
-came home, showered, took a nap
-went to the nell dale cream puff social thing
-went to mozarts with Alyssa and tyler
-hung out in central park with jt and then went to Stas' for wine and airplane and JT stayed the night

04/06/16
-went to WWW yoga where two other guys showed up
-went to the WWW oracle panel and had half a sandwich 
-met with my interaction design group for like 10 minutes
-waited for jt to finish his OS test then went to 24 diner for dinner 
-hit up HEB for strawberries and mixers then back to his for drinks and Spanish guitar you know the rest...
'''


output_json = {}

p1 = re.compile('\d{2}\/\d{2}\/\d{2}', flags=re.DOTALL)
results = p1.findall(sample_string)

for i in range(0, len(results)-1):
    things_pattern = "%s(.*?)%s" % (results[i].replace("/", "\/"), results[i+1].replace("/", "\/"))
    output_json[results[i]] = []
    notes = re.findall(things_pattern, sample_string, re.DOTALL)[0]
    for note in notes.split("\n"):
        output_json[results[i]].append(note[1:])
    while "" in output_json[results[i]]:
        output_json[results[i]].remove("");

print json.dumps(output_json, indent=4, sort_keys=True)

text_file = open("Output.txt", "w")
text_file.write(json.dumps(output_json, indent=4, sort_keys=True))
text_file.close()