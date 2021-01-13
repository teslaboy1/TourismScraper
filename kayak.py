from bs4 import BeautifulSoup
import requests

url = 'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaKsBiAEBmAEJuAEHyAEM2AEB6AEB-AELiAIBqAIDuALe9ef_BcACAdICJDFlOTBiZWI1LTZmMzQtNDQwOS05MmVkLTEzMDI5ZDNiNmFhYdgCBuACAQ;sid=cf6dd6530ca264f43d7bbccc5b1d9bd3;checkin_monthday=22&checkin_year_month=2021-01&checkout_monthday=23&checkout_year_month=2021-01&dest_id=-1022136&dest_type=city&from_history=1&group_adults=2&group_children=0&highlighted_hotels=6181610&lsuihh=1&no_rooms=1&order=popularity&si=ad&si=ai&si=ci&si=co&si=di&si=la&si=re&;sh_position=1&dr_ps=ISR'

req = requests.get(url)

bsObj = BeautifulSoup(req.text,'lxml')

print(bsObj.find('div',attrs={'class' : 'sr_item  sr_item_new sr_item_default sr_property_block  sr_flex_layout       sr_item--highlighted   with_dates      '}))