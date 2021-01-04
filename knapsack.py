# knapsack.py
# A dynamic programming algorithm for the 0-1 knapsack problem and
# a greedy algorithm for the fractional knapsack problem

# A dynamic programming algorithm for the 0-1 knapsack problem.


# Python3 code for Dynamic Programming
# based solution for 0-1 Knapsack problem

# Prints the items which are put in a
# knapsack of capacity W

def knapSack(W, wt, val, n):
    list_of_item = []
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

    # stores the result of Knapsack
    res = K[n][W]
    print(res)

    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:

            # This item is included.
            list_of_item.append[i - 1]

            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]

        # Driver code
    return (list_of_item)


val = [0.00001711185795978930, 0.00124729160343982717, 0.05131953586193025579, 0.00113390145767256986,
       0.00003334617021901253, 0.01228548886266175866, 0.00001168762923283197, 0.02394094222852853268,
       0.00391453536228139349, 0.01486544152382072992, 0.00150922284016219107, 0.05645148944812328901,
       0.03186539410617148654, 0.09091568827109706985, 0.00007862852507161364, 0.00070406359331675651,
       0.00015322475135483228, 0.00200877560025587666, 0.00630439834630780981, 0.00058187073827831105,
       0.00001062511748439270, 0.02633503645138138630, 0.00036129594866117617, 0.00018540194913934711,
       0.00000798280802734237, 0.00093710864270460316, 0.00573127122391618987, 0.00243061847630961095,
       0.01798718424382308306, 0.00521024656719653624, 0.00267368032394057261, 0.00010465456687031777,
       0.00430598889850953345, 0.00008649137757877499, 0.01635198567620280499, 0.03505193351678864006,
       0.02896854009651952597, 0.00294104835633463013, 0.00323515319196809349, 0.04665412351084568393,
       0.00032845086241925107, 0.00077446995264843221, 0.00009514051533665250, 0.06209663839293562415,
       0.00002755881836282027, 0.00004882212781765627, 0.02176449293502593502, 0.00011512002355734955,
       0.00003668078724091380, 0.00007148047733783056, 0.00013929522850439298, 0.00000878108883007661,
       0.00029859169310841004, 0.00048088490766802565, 0.00923026961882926662, 0.01351403774892793314,
       0.00024676999430447104, 0.00003031470019910230, 0.00064005781210614218, 0.08265062570099733497,
       0.01015329658071219450, 0.00006498225212530050, 0.06830630223222917963, 0.00182615963659625157,
       0.00220965316028146454, 0.00005907477465936409, 0.00002277588294447956, 0.00022433635845861002,
       0.00002070534813134505, 0.01116862623878341586, 0.00137202076378380991, 0.00043716809788002325,
       0.00001555623450889936, 0.00001285639215611517, 0.00001882304375576823, 0.00052897339843482817,
       0.00001414203137172669, 0.00473658778836048670, 0.03855712686846749643, 0.00012663202591308451,
       0.01978590266820539484, 0.00000965919771308427, 0.00166014512417841020, 0.00085191694791327552,
       0.00027144699373491820, 0.00103081950697506359, 0.00762832199903245092, 0.00839115419893569740,
       0.00355866851116490301, 0.00005370434059942190, 0.00002505347123892752, 0.00020394214405328184,
       0.00000725709820667488, 0.00004034886596500518, 0.07513693245545211008, 0.04241283955531425370,
       0.00693483818093859183, 0.00016854722649031553, 0.00039742554352729383, 0.00004438375256150569]
wt = [0.00113390145767256964, 0.00839115419893569567, 0.02394094222852852574, 0.00124729160343982695,
      0.00137202076378380947, 0.00036129594866117612, 0.00000798280802734237, 0.04241283955531424676,
      0.00000725709820667488, 0.00003334617021901253, 0.01015329658071219276, 0.00355866851116490215,
      0.03505193351678862618, 0.00013929522850439295, 0.00001414203137172669, 0.00000878108883007661,
      0.00077446995264843211, 0.00085191694791327531, 0.07513693245545209620, 0.00693483818093859009,
      0.00004034886596500517, 0.00630439834630780807, 0.00006498225212530049, 0.00007862852507161361,
      0.00220965316028146411, 0.00762832199903244919, 0.00008649137757877498, 0.00002277588294447956,
      0.00009514051533665249, 0.00243061847630961052, 0.00002505347123892751, 0.01351403774892793140,
      0.00573127122391618900, 0.00048088490766802554, 0.00001062511748439270, 0.01486544152382072645,
      0.00473658778836048584, 0.00004438375256150568, 0.01978590266820539137, 0.00200877560025587622,
      0.00001555623450889936, 0.01228548886266175519, 0.06830630223222916575, 0.00020394214405328179,
      0.00923026961882926489, 0.00064005781210614207, 0.00010465456687031774, 0.00150922284016219064,
      0.00043716809788002314, 0.00003031470019910230, 0.06209663839293561027, 0.01116862623878341412,
      0.00024676999430447099, 0.08265062570099732109, 0.05645148944812327513, 0.00294104835633462970,
      0.00016854722649031547, 0.03855712686846748949, 0.00029859169310840993, 0.00039742554352729373,
      0.00004882212781765625, 0.00430598889850953258, 0.00267368032394057218, 0.05131953586193024192,
      0.02633503645138137936, 0.00323515319196809306, 0.00005907477465936408, 0.00002070534813134505,
      0.00166014512417840977, 0.03186539410617147960, 0.00002755881836282027, 0.00007148047733783054,
      0.00027144699373491814, 0.00015322475135483226, 0.00001711185795978930, 0.09091568827109705597,
      0.00011512002355734952, 0.00012663202591308448, 0.01798718424382307959, 0.00070406359331675640,
      0.00018540194913934706, 0.00052897339843482806, 0.00058187073827831095, 0.00032845086241925102,
      0.00000965919771308427, 0.00391453536228139262, 0.04665412351084567699, 0.00182615963659625113,
      0.00003668078724091379, 0.00001882304375576823, 0.00005370434059942189, 0.01635198567620280152,
      0.00022433635845860996, 0.02176449293502593155, 0.02896854009651952250, 0.00103081950697506337,
      0.00093710864270460294, 0.00001168762923283197, 0.00001285639215611517, 0.00521024656719653451]

for i in range(100):
    val[i] = int(val[i] / min(val))

W = int(0.1 / min(wt))
for i in range(100):
    wt[i] = int(wt[i] / min(wt))

n = len(val)

list_of_store = knapSack(W, wt, val, n)

print(list_of_store)

# K = [[0 for x in range(100)] for x in range(100)]
# def knapSack(W, wt, val, n):
#    #Table in bottom up manner
#    for i in range(100):
#       for w in range(100):
#          if i == 0 or w == 0:
#             K[i][w] = 0
#          elif wt[i-1] <= w:
#             K[i][w] = max(val[i-1] + K[i-1][w], K[i-1][w])
#          else:
#             K[i][w] = K[i-1][w]
#
#
#    res = K[99][99]
#    print(res)
#    #return K[99][99]
#    w = 99
#    for i in range(n, 0, -1):
#        if res <= 0:
#            break
#        if res == K[i - 1][w]:
#            continue
#        else:
#
#            # This item is included.
#            print(i-1)
#
#            # Since this weight is included
#            # its value is deducted
#            res = res - val[i - 1]
#            w = w - 1
#        #Main
#
# val = [0.00001711185795978930,0.00124729160343982717,0.05131953586193025579,0.00113390145767256986,0.00003334617021901253,0.01228548886266175866,0.00001168762923283197,0.02394094222852853268,0.00391453536228139349,0.01486544152382072992,0.00150922284016219107,0.05645148944812328901,0.03186539410617148654,0.09091568827109706985,0.00007862852507161364,0.00070406359331675651,0.00015322475135483228,0.00200877560025587666,0.00630439834630780981,0.00058187073827831105,0.00001062511748439270,0.02633503645138138630,0.00036129594866117617,0.00018540194913934711,0.00000798280802734237,0.00093710864270460316,0.00573127122391618987,0.00243061847630961095,0.01798718424382308306,0.00521024656719653624,0.00267368032394057261,0.00010465456687031777,0.00430598889850953345,0.00008649137757877499,0.01635198567620280499,0.03505193351678864006,0.02896854009651952597,0.00294104835633463013,0.00323515319196809349,0.04665412351084568393,0.00032845086241925107,0.00077446995264843221,0.00009514051533665250,0.06209663839293562415,0.00002755881836282027,0.00004882212781765627,0.02176449293502593502,0.00011512002355734955,0.00003668078724091380,0.00007148047733783056,0.00013929522850439298,0.00000878108883007661,0.00029859169310841004,0.00048088490766802565,0.00923026961882926662,0.01351403774892793314,0.00024676999430447104,0.00003031470019910230,0.00064005781210614218,0.08265062570099733497,0.01015329658071219450,0.00006498225212530050,0.06830630223222917963,0.00182615963659625157,0.00220965316028146454,0.00005907477465936409,0.00002277588294447956,0.00022433635845861002,0.00002070534813134505,0.01116862623878341586,0.00137202076378380991,0.00043716809788002325,0.00001555623450889936,0.00001285639215611517,0.00001882304375576823,0.00052897339843482817,0.00001414203137172669,0.00473658778836048670,0.03855712686846749643,0.00012663202591308451,0.01978590266820539484,0.00000965919771308427,0.00166014512417841020,0.00085191694791327552,0.00027144699373491820,0.00103081950697506359,0.00762832199903245092,0.00839115419893569740,0.00355866851116490301,0.00005370434059942190,0.00002505347123892752,0.00020394214405328184,0.00000725709820667488,0.00004034886596500518,0.07513693245545211008,0.04241283955531425370,0.00693483818093859183,0.00016854722649031553,0.00039742554352729383,0.00004438375256150569]
# wt = [0.00113390145767256964,0.00839115419893569567,0.02394094222852852574,0.00124729160343982695,0.00137202076378380947,0.00036129594866117612,0.00000798280802734237,0.04241283955531424676,0.00000725709820667488,0.00003334617021901253,0.01015329658071219276,0.00355866851116490215,0.03505193351678862618,0.00013929522850439295,0.00001414203137172669,0.00000878108883007661,0.00077446995264843211,0.00085191694791327531,0.07513693245545209620,0.00693483818093859009,0.00004034886596500517,0.00630439834630780807,0.00006498225212530049,0.00007862852507161361,0.00220965316028146411,0.00762832199903244919,0.00008649137757877498,0.00002277588294447956,0.00009514051533665249,0.00243061847630961052,0.00002505347123892751,0.01351403774892793140,0.00573127122391618900,0.00048088490766802554,0.00001062511748439270,0.01486544152382072645,0.00473658778836048584,0.00004438375256150568,0.01978590266820539137,0.00200877560025587622,0.00001555623450889936,0.01228548886266175519,0.06830630223222916575,0.00020394214405328179,0.00923026961882926489,0.00064005781210614207,0.00010465456687031774,0.00150922284016219064,0.00043716809788002314,0.00003031470019910230,0.06209663839293561027,0.01116862623878341412,0.00024676999430447099,0.08265062570099732109,0.05645148944812327513,0.00294104835633462970,0.00016854722649031547,0.03855712686846748949,0.00029859169310840993,0.00039742554352729373,0.00004882212781765625,0.00430598889850953258,0.00267368032394057218,0.05131953586193024192,0.02633503645138137936,0.00323515319196809306,0.00005907477465936408,0.00002070534813134505,0.00166014512417840977,0.03186539410617147960,0.00002755881836282027,0.00007148047733783054,0.00027144699373491814,0.00015322475135483226,0.00001711185795978930,0.09091568827109705597,0.00011512002355734952,0.00012663202591308448,0.01798718424382307959,0.00070406359331675640,0.00018540194913934706,0.00052897339843482806,0.00058187073827831095,0.00032845086241925102,0.00000965919771308427,0.00391453536228139262,0.04665412351084567699,0.00182615963659625113,0.00003668078724091379,0.00001882304375576823,0.00005370434059942189,0.01635198567620280152,0.00022433635845860996,0.02176449293502593155,0.02896854009651952250,0.00103081950697506337,0.00093710864270460294,0.00001168762923283197,0.00001285639215611517,0.00521024656719653451]
# W = 0.1
# n = len(val)
# print(knapSack(W, wt, val, n))
#