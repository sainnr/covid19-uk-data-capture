"""
Recovers data into a structured format from the Flourish JS graph.
A credit to https://www.nwemail.co.uk/news/18336733.uk-cases-coronavirus-area-by-area for collecting (or re-posting)
the data.
"""
import json

flourish_data_column_names = ["March 19", "March 20", "March 21", "March 22", "March 23", "March 24", "March 25"]

flourish_data = [{
        "image": "Ayrshire and Arran",
        "label": "Ayrshire and Arran",
        "values": ["12", "16", "21", "25", "34", "41", "57"]
    }, {
        "image": "Barking and Dagenham",
        "label": "Barking and Dagenham",
        "values": ["18", "21", "30", "35", "42", "45", "53"]
    }, {
        "image": "Barnet",
        "label": "Barnet",
        "values": ["28", "76", "81", "88", "94", "99", "100"]
    }, {
        "image": "Barnsley",
        "label": "Barnsley",
        "values": ["7", "7", "7", "10", "11", "15", "19"]
    }, {
        "image": "Bath and North East Somerset",
        "label": "Bath and North East Somerset",
        "values": ["4", "5", "11", "13", "16", "17", "20"]
    }, {"image": "Bedford", "label": "Bedford", "values": ["1", "1", "4", "4", "7", "7", "7"]}, {
        "image": "Bexley",
        "label": "Bexley",
        "values": ["22", "31", "37", "39", "43", "47", "59"]
    }, {
        "image": "Birmingham",
        "label": "Birmingham",
        "values": ["34", "54", "75", "91", "137", "187", "228"]
    }, {
        "image": "Blackburn with Darwen",
        "label": "Blackburn with Darwen",
        "values": ["1", "1", "1", "1", "1", "2", "3"]
    }, {"image": "Blackpool", "label": "Blackpool", "values": ["3", "5", "5", "6", "6", "8", "8"]}, {
        "image": "Bolton",
        "label": "Bolton",
        "values": ["9", "13", "15", "17", "18", "19", "21"]
    }, {
        "image": "Borders",
        "label": "Borders",
        "values": ["8", "9", "10", "11", "12", "12", "15"]
    }, {
        "image": "Bournemouth, Christchurch and Poole",
        "label": "Bournemouth, Christchurch and Poole",
        "values": ["9", "10", "11", "12", "13", "14", "15"]
    }, {
        "image": "Bracknell Forest",
        "label": "Bracknell Forest",
        "values": ["3", "3", "3", "3", "3", "3", "3"]
    }, {
        "image": "Bradford",
        "label": "Bradford",
        "values": ["7", "9", "10", "11", "13", "14", "16"]
    }, {
        "image": "Brent",
        "label": "Brent",
        "values": ["66", "75", "108", "128", "143", "170", "192"]
    }, {
        "image": "Brighton and Hove",
        "label": "Brighton and Hove",
        "values": ["12", "14", "17", "17", "17", "25", "25"]
    }, {
        "image": "Bristol, City of",
        "label": "Bristol, City of",
        "values": ["12", "13", "20", "23", "28", "37", "41"]
    }, {
        "image": "Bromley",
        "label": "Bromley",
        "values": ["40", "52", "63", "67", "76", "93", "125"]
    }, {
        "image": "Buckinghamshire",
        "label": "Buckinghamshire",
        "values": ["39", "39", "41", "44", "45", "50", "59"]
    }, {"image": "Bury", "label": "Bury", "values": ["8", "10", "11", "14", "15", "17", "23"]}, {
        "image": "Calderdale",
        "label": "Calderdale",
        "values": ["3", "5", "5", "5", "7", "7", "7"]
    }, {
        "image": "Cambridgeshire",
        "label": "Cambridgeshire",
        "values": ["15", "16", "17", "20", "30", "37", "41"]
    }, {
        "image": "Camden",
        "label": "Camden",
        "values": ["36", "46", "51", "53", "60", "64", "71"]
    }, {
        "image": "Central Bedfordshire",
        "label": "Central Bedfordshire",
        "values": ["7", "8", "11", "14", "19", "22", "24"]
    }, {
        "image": "Cheshire East",
        "label": "Cheshire East",
        "values": ["9", "9", "11", "18", "18", "25", "30"]
    }, {
        "image": "Cheshire West and Chester",
        "label": "Cheshire West and Chester",
        "values": ["7", "10", "10", "11", "16", "18", "18"]
    }, {
        "image": "Cornwall and Isles of Scilly",
        "label": "Cornwall and Isles of Scilly",
        "values": ["10", "16", "20", "20", "25", "30", "37"]
    }, {
        "image": "County Durham",
        "label": "County Durham",
        "values": ["5", "7", "11", "11", "14", "18", "25"]
    }, {
        "image": "Coventry",
        "label": "Coventry",
        "values": ["4", "7", "9", "14", "19", "24", "25"]
    }, {
        "image": "Croydon",
        "label": "Croydon",
        "values": ["49", "68", "81", "84", "85", "128", "163"]
    }, {
        "image": "Cumbria",
        "label": "Cumbria",
        "values": ["38", "52", "57", "79", "110", "129", "145"]
    }, {"image": "Darlington", "label": "Darlington", "values": ["2", "2", "3", "3", "3", "3", "4"]}, {
        "image": "Derby",
        "label": "Derby",
        "values": ["9", "12", "18", "23", "23", "37", "40"]
    }, {
        "image": "Derbyshire",
        "label": "Derbyshire",
        "values": ["40", "50", "64", "75", "82", "101", "110"]
    }, {
        "image": "Devon",
        "label": "Devon",
        "values": ["26", "30", "42", "43", "46", "48", "50"]
    }, {
        "image": "Doncaster",
        "label": "Doncaster",
        "values": ["2", "3", "5", "7", "9", "13", "15"]
    }, {"image": "Dorset", "label": "Dorset", "values": ["7", "7", "8", "11", "14", "15", "23"]}, {
        "image": "Dudley",
        "label": "Dudley",
        "values": ["11", "18", "19", "24", "26", "40", "51"]
    }, {
        "image": "Dumfries and Galloway",
        "label": "Dumfries and Galloway",
        "values": ["6", "10", "13", "16", "18", "26", "31"]
    }, {
        "image": "Ealing",
        "label": "Ealing",
        "values": ["53", "54", "80", "97", "106", "123", "136"]
    }, {
        "image": "East Riding of Yorkshire",
        "label": "East Riding of Yorkshire",
        "values": ["10", "15", "15", "15", "16", "16", "19"]
    }, {
        "image": "East Sussex",
        "label": "East Sussex",
        "values": ["8", "8", "8", "9", "11", "21", "22"]
    }, {
        "image": "Enfield",
        "label": "Enfield",
        "values": ["30", "48", "54", "68", "76", "84", "98"]
    }, {"image": "Essex", "label": "Essex", "values": ["31", "43", "45", "53", "67", "80", "88"]}, {
        "image": "Fife",
        "label": "Fife",
        "values": ["9", "12", "13", "16", "19", "25", "29"]
    }, {
        "image": "Forth Valley",
        "label": "Forth Valley",
        "values": ["17", "23", "27", "30", "40", "43", "59"]
    }, {
        "image": "Gateshead",
        "label": "Gateshead",
        "values": ["1", "1", "2", "3", "4", "5", "10"]
    }, {
        "image": "Gloucestershire",
        "label": "Gloucestershire",
        "values": ["15", "22", "27", "29", "32", "49", "57"]
    }, {
        "image": "Grampian",
        "label": "Grampian",
        "values": ["18", "19", "20", "23", "24", "24", "29"]
    }, {
        "image": "Greater Glasgow and Clyde",
        "label": "Greater Glasgow and Clyde",
        "values": ["71", "91", "110", "130", "152", "183", "221"]
    }, {
        "image": "Greenwich",
        "label": "Greenwich",
        "values": ["33", "41", "54", "61", "67", "77", "97"]
    }, {
        "image": "Hackney and City of London",
        "label": "Hackney and City of London",
        "values": ["32", "45", "52", "64", "72", "74", "85"]
    }, {
        "image": "Halton",
        "label": "Halton",
        "values": ["4", "5", "7", "7", "7", "8", "8"]
    }, {
        "image": "Hammersmith and Fulham",
        "label": "Hammersmith and Fulham",
        "values": ["28", "36", "45", "51", "58", "70", "80"]
    }, {
        "image": "Hampshire",
        "label": "Hampshire",
        "values": ["87", "107", "138", "156", "171", "207", "251"]
    }, {
        "image": "Haringey",
        "label": "Haringey",
        "values": ["32", "44", "51", "57", "64", "72", "76"]
    }, {
        "image": "Harrow",
        "label": "Harrow",
        "values": ["56", "60", "89", "103", "113", "134", "145"]
    }, {
        "image": "Hartlepool",
        "label": "Hartlepool",
        "values": ["2", "2", "2", "2", "3", "3", "3"]
    }, {
        "image": "Havering",
        "label": "Havering",
        "values": ["14", "19", "30", "35", "39", "44", "47"]
    }, {
        "image": "Herefordshire, County of",
        "label": "Herefordshire, County of",
        "values": ["3", "3", "7", "7", "7", "15", "15"]
    }, {
        "image": "Hertfordshire",
        "label": "Hertfordshire",
        "values": ["52", "61", "75", "92", "115", "139", "147"]
    }, {
        "image": "Highland",
        "label": "Highland",
        "values": ["6", "6", "8", "8", "12", "13", "22"]
    }, {
        "image": "Hillingdon",
        "label": "Hillingdon",
        "values": ["29", "34", "50", "63", "78", "85", "90"]
    }, {
        "image": "Hounslow",
        "label": "Hounslow",
        "values": ["29", "38", "52", "64", "73", "82", "90"]
    }, {
        "image": "Isle of Wight",
        "label": "Isle of Wight",
        "values": ["2", "2", "2", "2", "2", "3", "3"]
    }, {
        "image": "Islington",
        "label": "Islington",
        "values": ["35", "45", "48", "54", "59", "66", "70"]
    }, {
        "image": "Kensington and Chelsea",
        "label": "Kensington and Chelsea",
        "values": ["57", "66", "75", "81", "85", "91", "97"]
    }, {
        "image": "Kent",
        "label": "Kent",
        "values": ["25", "32", "45", "48", "64", "72", "96"]
    }, {
        "image": "Kingston upon Hull, City of",
        "label": "Kingston upon Hull, City of",
        "values": ["1", "1", "1", "1", "1", "1", "2"]
    }, {
        "image": "Kingston upon Thames",
        "label": "Kingston upon Thames",
        "values": ["14", "17", "22", "23", "23", "36", "37"]
    }, {
        "image": "Kirklees",
        "label": "Kirklees",
        "values": ["3", "6", "8", "11", "16", "17", "20"]
    }, {"image": "Knowsley", "label": "Knowsley", "values": ["3", "3", "4", "4", "5", "8", "9"]}, {
        "image": "Lambeth",
        "label": "Lambeth",
        "values": ["81", "103", "118", "127", "134", "188", "212"]
    }, {
        "image": "Lanarkshire",
        "label": "Lanarkshire",
        "values": ["33", "41", "49", "49", "58", "75", "87"]
    }, {
        "image": "Lancashire",
        "label": "Lancashire",
        "values": ["24", "26", "30", "44", "59", "71", "78"]
    }, {
        "image": "Leeds",
        "label": "Leeds",
        "values": ["15", "17", "20", "29", "35", "42", "53"]
    }, {
        "image": "Leicester",
        "label": "Leicester",
        "values": ["5", "11", "14", "19", "22", "24", "32"]
    }, {
        "image": "Leicestershire",
        "label": "Leicestershire",
        "values": ["17", "20", "29", "43", "53", "65", "80"]
    }, {
        "image": "Lewisham",
        "label": "Lewisham",
        "values": ["39", "47", "60", "67", "86", "97", "114"]
    }, {
        "image": "Lincolnshire",
        "label": "Lincolnshire",
        "values": ["7", "9", "9", "14", "20", "24", "31"]
    }, {
        "image": "Liverpool",
        "label": "Liverpool",
        "values": ["13", "14", "18", "22", "35", "41", "57"]
    }, {
        "image": "Lothian",
        "label": "Lothian",
        "values": ["35", "40", "44", "46", "59", "70", "88"]
    }, {"image": "Luton", "label": "Luton", "values": ["3", "4", "5", "8", "15", "19", "29"]}, {
        "image": "Manchester",
        "label": "Manchester",
        "values": ["21", "26", "28", "31", "37", "41", "45"]
    }, {"image": "Medway", "label": "Medway", "values": ["8", "11", "11", "11", "15", "19", "25"]}, {
        "image": "Merton",
        "label": "Merton",
        "values": ["39", "45", "56", "56", "57", "84", "98"]
    }, {
        "image": "Middlesbrough",
        "label": "Middlesbrough",
        "values": ["0", "0", "1", "1", "3", "7", "9"]
    }, {
        "image": "Milton Keynes",
        "label": "Milton Keynes",
        "values": ["5", "7", "7", "11", "17", "25", "29"]
    }, {
        "image": "Newcastle upon Tyne",
        "label": "Newcastle upon Tyne",
        "values": ["19", "21", "28", "34", "42", "49", "58"]
    }, {
        "image": "Newham",
        "label": "Newham",
        "values": ["32", "42", "51", "57", "70", "76", "77"]
    }, {
        "image": "Norfolk",
        "label": "Norfolk",
        "values": ["11", "17", "24", "34", "35", "42", "45"]
    }, {
        "image": "North East Lincolnshire",
        "label": "North East Lincolnshire",
        "values": ["0", "0", "0", "1", "1", "3", "3"]
    }, {
        "image": "North Lincolnshire",
        "label": "North Lincolnshire",
        "values": ["1", "1", "2", "2", "3", "5", "5"]
    }, {
        "image": "North Somerset",
        "label": "North Somerset",
        "values": ["4", "4", "5", "5", "7", "21", "21"]
    }, {
        "image": "North Tyneside",
        "label": "North Tyneside",
        "values": ["10", "12", "17", "18", "18", "20", "23"]
    }, {
        "image": "North Yorkshire",
        "label": "North Yorkshire",
        "values": ["13", "14", "16", "20", "24", "30", "45"]
    }, {
        "image": "Northamptonshire",
        "label": "Northamptonshire",
        "values": ["16", "17", "20", "21", "29", "37", "43"]
    }, {
        "image": "Northumberland",
        "label": "Northumberland",
        "values": ["6", "7", "10", "10", "10", "13", "19"]
    }, {
        "image": "Nottingham",
        "label": "Nottingham",
        "values": ["14", "22", "22", "34", "41", "49", "57"]
    }, {
        "image": "Nottinghamshire",
        "label": "Nottinghamshire",
        "values": ["29", "41", "45", "60", "71", "78", "92"]
    }, {
        "image": "Oldham",
        "label": "Oldham",
        "values": ["14", "14", "15", "23", "28", "34", "42"]
    }, {
        "image": "Oxfordshire",
        "label": "Oxfordshire",
        "values": ["34", "40", "44", "52", "63", "69", "86"]
    }, {
        "image": "Peterborough",
        "label": "Peterborough",
        "values": ["2", "2", "2", "2", "3", "6", "9"]
    }, {
        "image": "Plymouth",
        "label": "Plymouth",
        "values": ["7", "7", "11", "11", "11", "16", "21"]
    }, {
        "image": "Portsmouth",
        "label": "Portsmouth",
        "values": ["5", "13", "22", "25", "25", "29", "33"]
    }, {"image": "Reading", "label": "Reading", "values": ["7", "7", "7", "8", "8", "8", "9"]}, {
        "image": "Redbridge",
        "label": "Redbridge",
        "values": ["18", "27", "42", "45", "51", "57", "67"]
    }, {
        "image": "Redcar and Cleveland",
        "label": "Redcar and Cleveland",
        "values": ["1", "2", "3", "3", "3", "7", "10"]
    }, {
        "image": "Richmond upon Thames",
        "label": "Richmond upon Thames",
        "values": ["12", "16", "22", "25", "31", "36", "44"]
    }, {
        "image": "Rochdale",
        "label": "Rochdale",
        "values": ["9", "12", "13", "15", "19", "24", "29"]
    }, {
        "image": "Rotherham",
        "label": "Rotherham",
        "values": ["3", "4", "6", "9", "12", "16", "20"]
    }, {
        "image": "Salford",
        "label": "Salford",
        "values": ["9", "10", "12", "23", "25", "31", "47"]
    }, {
        "image": "Sandwell",
        "label": "Sandwell",
        "values": ["7", "11", "15", "20", "31", "47", "50"]
    }, {"image": "Sefton", "label": "Sefton", "values": ["6", "7", "7", "8", "10", "13", "20"]}, {
        "image": "Sheffield",
        "label": "Sheffield",
        "values": ["40", "48", "61", "82", "106", "130", "174"]
    }, {
        "image": "Shetland",
        "label": "Shetland",
        "values": ["24", "24", "24", "24", "24", "24", "24"]
    }, {
        "image": "Shropshire",
        "label": "Shropshire",
        "values": ["3", "3", "3", "3", "10", "27", "33"]
    }, {
        "image": "Slough",
        "label": "Slough",
        "values": ["17", "20", "21", "21", "22", "22", "22"]
    }, {
        "image": "Solihull",
        "label": "Solihull",
        "values": ["1", "3", "4", "4", "8", "12", "19"]
    }, {
        "image": "Somerset",
        "label": "Somerset",
        "values": ["10", "10", "12", "13", "15", "21", "22"]
    }, {
        "image": "South Gloucestershire",
        "label": "South Gloucestershire",
        "values": ["12", "13", "14", "17", "19", "19", "25"]
    }, {
        "image": "South Tyneside",
        "label": "South Tyneside",
        "values": ["2", "2", "5", "5", "6", "8", "9"]
    }, {
        "image": "Southampton",
        "label": "Southampton",
        "values": ["7", "7", "8", "11", "11", "24", "28"]
    }, {
        "image": "Southend-on-Sea",
        "label": "Southend-on-Sea",
        "values": ["4", "5", "8", "8", "8", "8", "9"]
    }, {
        "image": "Southwark",
        "label": "Southwark",
        "values": ["82", "110", "134", "139", "154", "181", "209"]
    }, {
        "image": "St. Helens",
        "label": "St. Helens",
        "values": ["2", "2", "3", "3", "6", "8", "16"]
    }, {
        "image": "Staffordshire",
        "label": "Staffordshire",
        "values": ["18", "25", "35", "41", "54", "76", "97"]
    }, {
        "image": "Stockport",
        "label": "Stockport",
        "values": ["13", "21", "24", "29", "36", "42", "45"]
    }, {
        "image": "Stockton-on-Tees",
        "label": "Stockton-on-Tees",
        "values": ["9", "9", "10", "11", "12", "12", "14"]
    }, {
        "image": "Stoke-on-Trent",
        "label": "Stoke-on-Trent",
        "values": ["2", "2", "2", "2", "4", "9", "12"]
    }, {
        "image": "Suffolk",
        "label": "Suffolk",
        "values": ["13", "13", "15", "18", "22", "28", "35"]
    }, {
        "image": "Sunderland",
        "label": "Sunderland",
        "values": ["4", "5", "11", "11", "13", "20", "25"]
    }, {
        "image": "Surrey",
        "label": "Surrey",
        "values": ["45", "57", "65", "68", "69", "110", "117"]
    }, {
        "image": "Sutton",
        "label": "Sutton",
        "values": ["14", "19", "23", "24", "24", "40", "45"]
    }, {"image": "Swindon", "label": "Swindon", "values": ["4", "5", "5", "6", "7", "7", "8"]}, {
        "image": "Tameside",
        "label": "Tameside",
        "values": ["14", "19", "21", "21", "27", "32", "35"]
    }, {
        "image": "Tayside",
        "label": "Tayside",
        "values": ["27", "31", "34", "38", "47", "48", "57"]
    }, {
        "image": "Telford and Wrekin",
        "label": "Telford and Wrekin",
        "values": ["0", "0", "0", "1", "3", "9", "12"]
    }, {
        "image": "Thurrock",
        "label": "Thurrock",
        "values": ["3", "6", "8", "10", "13", "15", "15"]
    }, {
        "image": "Torbay",
        "label": "Torbay",
        "values": ["8", "10", "10", "16", "17", "17", "18"]
    }, {
        "image": "Tower Hamlets",
        "label": "Tower Hamlets",
        "values": ["33", "43", "51", "57", "67", "70", "71"]
    }, {
        "image": "Trafford",
        "label": "Trafford",
        "values": ["13", "15", "19", "23", "28", "31", "40"]
    }, {
        "image": "Wakefield",
        "label": "Wakefield",
        "values": ["6", "6", "8", "10", "12", "13", "19"]
    }, {
        "image": "Walsall",
        "label": "Walsall",
        "values": ["16", "20", "28", "29", "37", "43", "60"]
    }, {
        "image": "Waltham Forest",
        "label": "Waltham Forest",
        "values": ["17", "23", "38", "50", "56", "61", "63"]
    }, {
        "image": "Wandsworth",
        "label": "Wandsworth",
        "values": ["75", "98", "107", "110", "113", "155", "184"]
    }, {
        "image": "Warrington",
        "label": "Warrington",
        "values": ["4", "4", "4", "4", "7", "8", "9"]
    }, {
        "image": "Warwickshire",
        "label": "Warwickshire",
        "values": ["11", "13", "17", "29", "35", "52", "59"]
    }, {
        "image": "West Berkshire",
        "label": "West Berkshire",
        "values": ["3", "6", "7", "8", "10", "12", "16"]
    }, {
        "image": "West Sussex",
        "label": "West Sussex",
        "values": ["16", "19", "27", "27", "28", "52", "57"]
    }, {
        "image": "Westminster",
        "label": "Westminster",
        "values": ["78", "99", "110", "117", "134", "143", "152"]
    }, {"image": "Wigan", "label": "Wigan", "values": ["4", "6", "9", "9", "9", "11", "14"]}, {
        "image": "Wiltshire",
        "label": "Wiltshire",
        "values": ["12", "17", "20", "23", "28", "34", "39"]
    }, {
        "image": "Windsor and Maidenhead",
        "label": "Windsor and Maidenhead",
        "values": ["13", "13", "13", "13", "13", "13", "13"]
    }, {
        "image": "Wirral",
        "label": "Wirral",
        "values": ["8", "9", "10", "10", "12", "15", "16"]
    }, {
        "image": "Wokingham",
        "label": "Wokingham",
        "values": ["9", "12", "13", "13", "13", "13", "13"]
    }, {
        "image": "Wolverhampton",
        "label": "Wolverhampton",
        "values": ["28", "39", "45", "52", "69", "81", "98"]
    }, {
        "image": "Worcestershire",
        "label": "Worcestershire",
        "values": ["8", "10", "12", "19", "28", "38", "55"]
    }, {"image": "York", "label": "York", "values": ["5", "6", "8", "10", "10", "11", "14"]}]

source = "Source: Flourish widget data at www.nwemail.co.uk. Note: includes Scotland & England combined."

if __name__ == "__main__":
    for i in range(0, len(flourish_data_column_names)):
        [m, d] = flourish_data_column_names[i].split(" ")
        date = "{} {} 2020".format(d, m)
        entries = len(flourish_data)
        res = {"meta": {"date": date, "description": source, "entries": entries}, "data": {}}
        sum = 0
        for utla in flourish_data:
            reg = utla["image"]
            val = int(utla["values"][i])
            res["data"][reg] = val
            sum += val

        res["meta"]["total"] = sum

        with open("../by_utla/2020-03-{}.json".format(d), 'w') as out:
            json.dump(res, out)