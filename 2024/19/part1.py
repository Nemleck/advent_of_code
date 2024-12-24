import time, math

TOWELS = "buu, ubg, gub, wbwu, rrgrgg, urrwr, grwb, ubw, ubrbr, ubgb, gbw, rbrwgw, wbrr, brg, urugggr, wgbb, uwwu, urgg, wwwr, wrub, rbr, brgwb, gruwwb, rrwuwbu, rub, urwwgu, bbbw, wrr, uwr, grr, ggwrb, wbrwwbur, brbg, rubrg, urwbbru, brwww, bu, gugwww, rbww, buw, rurwgrug, rugwr, ruubww, bgbu, bgbw, wuu, burw, uuwb, rug, grw, bbrugwr, wurwbg, uurwu, bgu, ruu, bgrg, uguub, bgug, burubb, ubuugb, bbww, grbrr, gubbww, gwbgrwu, ggu, bubgurub, wguu, gww, wuuu, wbgb, bgrw, gug, rwwbw, uru, rwr, ubwr, uwb, bubwbwbw, gggwr, brr, gbrrg, rrww, gwg, uurubb, ruwwgrw, brgrru, gbgrwb, wbbwgg, wuwr, ruwuwbw, ggwrr, gbu, gwr, uur, wbgu, gbwgbgr, bbb, bubu, rwwggw, ruw, rbwuw, ugbbrwu, uurrgrg, bwwubwwg, gruu, ubgwu, rww, bur, ubwrg, wgb, gurbbr, rgbr, wuw, gbwuwru, rgwbrg, wbbr, wr, bgrrgb, wwb, urgwubww, bwurw, ur, rgbu, rrurw, ubbu, ubur, wrbwwr, uugww, grg, rwb, rgb, gguggu, rwgr, gurbubg, guwwr, wwbgb, grbgwruw, wug, bgb, rb, ruuubggr, www, wbgg, gguu, bbur, gbub, bwg, uuugbw, brb, brrrggu, buwu, rbrg, bg, bwgrbw, bwb, u, guw, gwrwur, brgb, wrru, ruugu, wrgrg, wbrb, rg, buwrr, ugr, uwru, bub, wbb, ubr, brrwr, wgbuu, bguu, bubw, ug, ugwg, wurbww, bwrbuwu, wwuwb, brbubg, wwub, g, brw, bbrwrgb, bgr, rbuwb, gwur, bggg, gbuu, wbu, rubw, bguug, bbw, wuguw, uwbwrgb, wwwub, wwbugg, gwubbb, rugwg, rgwwbru, ugbbubr, wrrgr, bubg, wwbwu, wbw, bbr, wbggugw, wurw, wwgwgr, burgr, wbgbu, wwwuuw, buguu, gwrugg, wwgugg, bburg, urwbu, rrug, ggb, ggbg, rguwbu, guru, wwr, ggurrw, brbbbubg, bbguuwgw, rru, ugwu, wbggr, rgrbww, rrubw, ubwurwg, gbr, rwrgw, wwguwbu, wggrr, wru, wrgbb, bgburwg, wruwwg, uuu, rugr, rwbw, bwwbr, bbbrgwu, br, ubb, bbu, urg, brbuggb, uw, rbug, wbbrgugb, rgu, uubgrrgw, bru, rwgbu, wrgw, gwb, bwbr, bgw, wgwg, wbgrwwg, wwwwgr, gg, gwgggu, ugwuu, gugur, gggbw, bwbwguu, uwbr, gw, wrgg, rugwbgg, uwg, urb, uwggb, urgggb, bbg, gwbr, uub, gbg, gwuu, buwrrw, rbu, wbbu, ru, rbbw, rgugrbwg, ggbgrw, ugrwwww, uwgbwu, wwbw, wurr, wrwrrr, rrw, rbb, rwrgr, bbwwg, rbg, bbbgrbrw, ruubwb, ubbg, gr, gwwbuuuw, bwgr, rrwwggu, bbuugb, guwwbg, rguw, rur, gwbbbbr, rbwr, wb, uuwrbb, uruwbrrr, bb, bbubu, gruguu, urr, bwbrb, rbru, ugu, ugg, rwbgu, rbbuug, uguw, grwbg, bbgrrr, gur, urw, gguwbb, rburuug, w, wg, ggw, wur, ubwuw, bwggugb, gwbu, wbrg, gbrgw, wrugur, rbgb, uwbrrubg, bbugugw, rwbgwur, ubwu, rw, wurwggr, gru, brur, gwbuw, uwu, gurbb, rgbgr, bgg, rggg, rrg, wbbg, wwu, wbr, uww, ggr, wbwgu, rrgu, rgw, rrwugrg, wgug, wrw, rbw, bug, bruuubrb, rubwurr, rwub, bbbru, rr, gwu, ubbgwg, gbww, wwrgrgg, wbg, rwu, ugurw, bubwg, wbubw, urwur, wgu, ubuuug, wubu, rrb, rrru, bwr, rbbubbru, gbwb, ggrruw, bww, uu, wu, wwuww, gwguwbb, ubu, uug, gubgr, rwggb, ubwug, wrg, r, wbwgwu, ww, gggw, rubrw, ugw, wgg, buguurwr, grb, bwur, wgr, uubb, wuwbwrb, urbwr, bw, ggg, bgrgr, buguwr, rbgbg, rrr, wgwbrr, rgg, rububg, bwu, ub, gbb, wub, uuw, wgw, bbub, wbggbb, wwwbgg, rgr, rbbbu, wuwb, grubu, rruwu, gubu, urwu, wrurg".split(", ")
WANTED = """wuuwwuwubwggbgggggwgurgwubwwrbwubgrbuubrwwgwgbbwugw
gwbwwrurbbgwuubwwugbrgrrwrgurgwgggubbugb
bugwwguwrbbgrbguguurbrrbwubbbrrwrgbguwrurbgwbg
bugwgguwrwbrggwugwgguwrwrwubrgwgwrububwrgugb
ruurguwurrwbgrrgwwbrrwgbrrbrbwwurwruuuuwbbbuwgggbugb
bgrurbguuurrgbgggrggrbgwbbwwguuggrwbwrgbgrrbugbgguwr
guggrwuugwrbbrwrubbbgwrrwruururgwubwwrbguugb
grugwgrgwrbuwwruurgwwwbrbrbwrurbbwrrubuwugb
gbwrgrgbubugggrwuwbugrrrrgurbbwbbgbggguwruwuubrurwrg
wuwbbgbrbruuubrbwwwugwbbwrugrwruwggwbbwbbuurbgr
rgbrbwugwrrgggbruuubruuubggrrrrgrbrgrwwrgrrgg
guwuggggurwbwugwgruwubwrubbuwbrwurwubugrburwuwbw
brbgwugbgggruwwugbwbguuugubwgrrrrruguwugubu
uggrbbbuwrggbgwbrbwggugwbrgrbwwwbrrbrbrwguwbbuugug
wurububrurruguubggbubbgwgwgguwbguubbwbwwwbrrubuuruuubbwgur""".split("\n")


max_towel_length = 0
for towel in TOWELS:
    if len(towel) > max_towel_length:
        max_towel_length = len(towel)

max_wanted_length = 0
max_wanted_towels_length = 0
wanted_towels = {}

for wanted in WANTED:
    if len(wanted) > max_wanted_length:
        max_wanted_length = len(wanted)
    
    wanted_towels[wanted] = []
    for towel in TOWELS:
        if towel in wanted:
            wanted_towels[wanted].append(towel)
    
    if len(wanted_towels[wanted]) > max_wanted_towels_length:
        max_wanted_towels_length = len(wanted_towels[wanted])


print(max_towel_length, max_wanted_length, max_wanted_towels_length)

n, k = len(TOWELS), max_wanted_length//max_towel_length
print("possibilities :", math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))