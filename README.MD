# COVID-19 UK Cases Capture

An unofficial repository for capturing daily updates in the COVID-19
cases, including: 
- daily figures published by [DHSC (gov.uk)](https://twitter.com/DHSCgovuk),
- daily updates on numbers across Upper Tier Local Authorities (UTLA)
from [the official dashboard](https://www.arcgis.com/apps/opsdashboard/index.html#/f94c3c90da5b4e9f9a0b19484dd4bb14);

**30 March Update:** looks like the official UK Dashboard now has a link to the historical
data of all cases including regions breakdown: https://fingertips.phe.org.uk/documents/Historic%20COVID-19%20Dashboard%20Data.xlsx

This is no doubt a great move, but I'll continue tracking daily updates here as well,
just in case.

## Motivation
The goal of the project is to capture the public information published
by the official UK bodies and represent it in a structured form
so that all the volunteers, tinkerers and enthusiasts would be able to
easily use it in their tools. This includes, but definitely not limited to: 
- graphs and charts,
- geo visualisations,
- statistics, forecasts & numeric models,
- Machine Learning and AI,
- retrospective analysis of the outbreak,
- Open Linked Data initiatives etc.

## Tooling
The repo includes some basic tooling to quickly scrape data from the UK official dashboard
(Chrome extension) and some various retrospective sources (assorted Python scripts).

A credit to [this guy](https://github.com/matheusrabelo/chrome-el-extractor) for
the inspiration to create a Chrome extension.

## Sources
### Department of Health and Social Care UK
https://twitter.com/DHSCgovuk

The DSHC Twitter seems to be one of the few reliable sources to get the number
of tested cases. The daily data update mainly includes numbers of cases:
total tested, confirmed positive & confirmed fatal.

**Note** that on 25th March the time snapshot for the number of fatal cases has been changed
from 09:00AM current day to 17:00 previous day.

### Total UK COVID-19 Cases Update
https://www.arcgis.com/apps/opsdashboard/index.html#/f94c3c90da5b4e9f9a0b19484dd4bb14

The official UK Dashboard that includes the breakdown by UTLA regions.

**Note** that the data on the dashboard consists of different and somewhat independent
parts which might be updated non-simultaneously, despite the fact that the date
in the header seemingly stands for the entire dashboard.

### Wikipedia - 2020 coronavirus pandemic in the United Kingdom
https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_Kingdom

This is an essential page kindly supported by many people who accumulate 
plenty of data from different sources. It also includes daily breakdowns
by NHS Regions (one of the reasons why it's not presented here).

The number of references & web links is also fantastically helpful.

### Archive.org
Helps in recovering historical data from dashboards and official websites.
For example, UTLA data from 7 March to 12 March has been recovered this way,
from gov.uk pages and the aforementioned dashboard.

### Various news websites
Regions data from 13 March to 17 March has been recovered from www.cambridge-news.co.uk.

Regions data from 19 March to 25 March has been collected from the widget published
on www.nwemail.co.uk.

Also, give some credit to this guy: https://docs.google.com/spreadsheets/d/1eTKeK9vRxgw0KhvKxPCaDrfaHnxQP-n9TsLzsEymviY/htmlview#
He's rigorously maintaining the spreadsheet for quite a while; I referring to it a few times
for cross-checking stats. 

## Related projects
A few links to other projects that also work hard on representing tracking data in the structured
way: 
- US COVID Tracking Project: https://covidtracking.com

Please reach me out if you know more of those.

## Known issues
- UTLA breakdown is missing for 18 March 2020.
- In UTLA breakdown, `date` attribute might have varying formats.
- Daily "recovered cases" information seems to be stale in the official sources.

## Ways to help & contribute
1. Most importantly. do use the data in your experiments and hacks!
Be creative, build graphs, viz, models etc to fight the nasty disease & prevent it spreading around.
1. Create more of structured data projects for your country. It's extremely hard to
emphasise more on how crucial it is to have data in the structured form so that
all the researchers, data scientists, analysts and developers could save our precious time
and concentrate on what's really important at the moment.
1. Raise issues if you've started using the data but figured out it's broken, incomplete
or inconsistent.
1. Fix issues from the list above. We want all the data to be clean & pristine.

I'm trying to update the numbers every day, so you could expect it's delayed for no more than 24h.
But please note we're all humans, even if self-isolated, and some unpredicted things might happen.
  
Feel free to get in touch via DM in Twitter if any questions ([@sainnr](https://twitter.com/sainnr)).
