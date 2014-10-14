import csv
import lxml.html

url1='http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;opposition=6;orderby=start;'
url2 ='page='
url3 ='size=100;team=2;template=results;type=team;view=results'
url5 = ['http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;opposition=6;orderby=start;size=100;team=2;template=results;type=team;view=results']
for i in range(1,2):   #Mention the upper and lower limits
    url4 = url1 + url2 + str(i) + ';' + url3
    url5.append(url4)
data = open('ODI_ind_vs_aus.csv','wb',)
out = csv.writer(data)
out.writerow(('Team', 'Result', 'Toss', 'Bat','Opposition','Ground','Date'))
for page in url5:
    team = []
    result = []
    toss = []
    bat = []
    opp = []
    ground = []
    date = []

    content = lxml.html.parse(page)
    
    team = content.xpath('//tr[@class="data1"]/td[1]')
    result = content.xpath('//tr[@class="data1"]/td[2]')
    toss = content.xpath('//tr[@class="data1"]/td[5]')
    mins = content.xpath('//tr[@class="data1"]/td[3]')
    bfs = content.xpath('//tr[@class="data1"]/td[4]')
    fours = content.xpath('//tr[@class="data1"]/td[5]')
    sixes = content.xpath('//tr[@class="data1"]/td[6]')
    strike = content.xpath('//tr[@class="data1"]/td[7]')
    inns = content.xpath('//tr[@class="data1"]/td[8]')
    oppos = content.xpath('//tr[@class="data1"]/td[10]/a')

    batsmen = [bat.text for bat in bats]
    count = [c.tail for c in ct]
    rus = [r.text for r in run]
    mints = [mint.text for mint in mins]
    bface = [bfaced.text for bfaced in bfs]
    four = [fs.text for fs in fours]
    six = [s.text for s in sixes]
    str_rat = [srt.text for srt in strike]
    inngs = [inn.text for inn in inns]
    oppos = [opp.text for opp in oppos]

    bmen.extend(batsmen)
    country.extend(count)
    mins_crease.extend(mints)
    runs.extend(rus)
    balls_faced.extend(bface)
    fours_hit.extend(four)
    sixes_hit.extend(six)
    strike_rate.extend(str_rat)
    innings.extend(inngs)
    opposition.extend(oppos)

    zipped = zip(bmen,country,mins_crease,runs,balls_faced,fours_hit,sixes_hit,strike_rate,innings,opposition)
    for row in zipped:
        out.writerow(row)
        zipped = None
data.close()
