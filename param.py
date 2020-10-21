#!/usr/bin/python
# -*- coding: utf-8 -*-

population_targets = {
    "2015": "http://www.pref.hokkaido.lg.jp/file.jsp?id=825833"
}

health_stat_report_targets = [
    {
        "name": "health_stat_report",
        "subname": "01-10",
        "type": "xlsx",
        "description": "北海道保健統計年報",
        "sheets": [
            "第1表 人口動態総覧，年次別",
            "第2表 人口動態総覧，都道府県別 ",
            "第3表 人口動態総覧（率），都道府県別",
            "第4表 人口動態総覧，年次・月別",
            "第5表 人口動態総覧，保健所",
            "第6表 人口動態総覧，支庁－市別",
            "第7表 人口動態総覧，保健所・市町村別",
            "第8表 人口動態総覧（率），保健所別",
            "第9表 人口動態総覧（率），支庁－市別",
            "第10表 人口動態総覧（率），保健所・市町村別"
        ],
        "urls":[
            {
                "year": "2008",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=70596",
                "url_redirected": "http://www.pref.hokkaido.lg.jp/hf/sum/grp/03/t001010-2.xls",
                "type": "xls"
            },
            {
                "year": "2009",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=435006",
                "url_redirected": "http://www.pref.hokkaido.lg.jp/hf/sum/t001010.xls",
                "type": "xls"
            },
            {
                "year": "2010",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=494361",
                "url_redirected": "http://www.pref.hokkaido.lg.jp/hf/sum/t001010-1.xls",
                "type": "xls"
            },
            {
                "year": "2011",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=620712",
                "type": "xlsx"
            },
            {
                "year": "2012",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=725951",
                "type": "xlsx"
            },
            {
                "year": "2013",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=880680",
                "type": "xlsx"
            },
            {
                "year": "2014",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=920632",
                "type": "xlsx"
            }
        ]
    },
    {
        "name": "health_stat_report",
        "subname": "21-24",
        "type": "xlsx",
        "description": "北海道保健統計年報",
        "sheets": [
            "第21表 死亡数，施設・市－郡部・年次別",
            "第22表 死亡数，月・年齢（5歳階級）別",
            "第23表 死亡割合（百分率），施設・市－郡部・年次別",
            "第24表 死亡数：年齢（5歳階級）・保健所・市町村別"
        ],
        "urls":[
            {
                "year": "2008",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=70649",
                "url_redirected": "http://www.pref.hokkaido.lg.jp/hf/sum/grp/03/t021024-2.xls",
                "type": "xls"
            },
            {
                "year": "2009",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=494377",  # このデータが欠損
                "type": "xls"
            },
            {
                "year": "2010",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=494377",
                "url_redirected": "http://www.pref.hokkaido.lg.jp/hf/sum/t021024-1.xls",
                "type": "xls"
            },
            {
                "year": "2011",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=620725",
                "url_redirected": "http://www.pref.hokkaido.lg.jp/hf/sum/T21-T24.xlsx",
                "type": "xlsx"
            },
            {
                "year": "2012",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=725999",
                "url_redirected": "http://www.pref.hokkaido.lg.jp/hf/sum/grp/03/2014-21-24.xlsx",
                "type": "xlsx"
            },
            {
                "year": "2013",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=846617",
                "url_redirected": "http://www.pref.hokkaido.lg.jp/hf/sum/25T21-24.xlsx",
                "type": "xlsx"
            }
        ]
    },
    {
        "name": "health_stat_report",
        "subname": "37-44",
        "type": "xlsx",
        "description": "北海道保健統計年報",
        "sheets": [
            "第37表 死亡数および死亡率（人口10万対），選択死因分類・保健所別",
            "第38表 死亡数および死亡率（人口10万対），選択死因分類・（総合）振興局－市",
            "第39表 死亡数，選択死因分類・保健所・市町村別",
            "第40表 死亡率（人口10万対），選択死因分類・保健所・市町村別",
            "第41表 死亡数，性・月・死因（死因簡単分類）別",
            "第42表 死亡数，性・年齢（5歳階級）・死因（死因簡単分類）別",
            "第43表 乳児死亡数，性・月・死因（乳児死因簡単分類）別",
            "第44表 感染症死亡数，性・死因（感染症分類）別"
        ],
        "urls":[
            {
                "year": "2008",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=70624",
                "type": "xls"
            },
            {
                "year": "2009",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=435027",
                "url_redirected": "http://www.pref.hokkaido.lg.jp/hf/sum/t037044-1.xls",
                "type": "xls"
            },
            {
                "year": "2010",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=494387",
                "url_redirected": "http://www.pref.hokkaido.lg.jp/hf/sum/t037044.xls",
                "type": "xls"
            },
            {
                "year": "2011",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=620734",
                "type": "xlsx"
            },
            {
                "year": "2012",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=726005",
                "type": "xlsx"
            },
            {
                "year": "2013",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=910379",
                "type": "xlsx"
            }
        ]
    },
    {
        "name": "health_stat_report",
        "subname": "59-64",
        "type": "xlsx",
        "description": "北海道保健統計年報",
        "sheets": [
            "第59表 医師数，業務の種類（従業地による）・年次別",
            "第60表 歯科医師数，業務の種類（従業地による）・年次別",
            "第61表 薬剤師数，業務の種類（従業地による）・年次別",
            "第62表 医師・歯科医師・薬剤師数，従業地による保健所",
            "第63表 医療施設従業医師数，診療科名（複数回答）・性・年次別",
            "第64表 医師・歯科医師・薬剤師数および率（人口10万対），従業地による保健所・市町村別"
        ],
        "urls":[
            {
                "year": "2008",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=70653",
                "type": "xls"
            },
            {
                "year": "2009",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=435034",
                "type": "xls"
            },
            {
                "year": "2010",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=495832",
                "type": "xls"
            },
            {
                "year": "2011",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=620762",
                "type": "xls"
            },
            {
                "year": "2012",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=726023",
                "type": "xls"
            },
            {
                "year": "2013",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=846599",
                "type": "xls"
            },
            {
                "year": "2014",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=920653",
                "type": "xls"
            }
        ]
    },
    {
        "name": "health_stat_report",
        "subname": "80-85",
        "type": "xlsx",
        "description": "北海道保健統計年報",
        "sheets": [
            "第80表 医療施設数および率（人口10万対），施設の種類・支庁－市別",
            "第81表 医療施設数および率（人口10万対），施設の種類・保健所・市町村別",
            "第82表 医療施設の病床数，施設の種類・支庁－市別",
            "第83表 医療施設の病床率（人口10万対），施設の種類・支庁－市別",
            "第84表 医療施設の病床数，施設の種類・保健所・市町村別",
            "第85表 医療施設の病床率（人口10万対），施設の種類・保健所・市町村別",
        ],
        "urls":[
            {
                "year": "2008",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=70643",
                "type": "xls"
            },
            {
                "year": "2009",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=435047",
                "type": "xls"
            },
            {
                "year": "2010",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=495840",
                "type": "xls"
            },
            {
                "year": "2011",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=671823",
                "type": "xls"
            },
            {
                "year": "2012",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=726506",
                "type": "xls"
            },
            {
                "year": "2013",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=846602",
                "type": "xls"
            },
            {
                "year": "2014",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=920642",
                "type": "xls"
            }
        ]
    },
]

tourism_stat_report_targets = [
    {
        "name": "tourism_stat_report",
        "subname": "",
        "type": "xlsx",
        "description": "北海道観光入込客数調査報告書",
        "targets": [
            # TODO 2000-2003
            {
                "year": "2004",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=85182",
                "type": "xls",
                "sheets": {
                    'monthly': '６'
                },

            },
            {
                "year": "2005",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=85130",
                "type": "xls",
                "sheets": {
                    'monthly': 'Ｐ６～４０'
                },

            },
            {
                "year": "2006",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=85122",
                "type": "xls",
                "sheets": {
                    'monthly': '6～31頁'
                },

            },
            {
                "year": "2007",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=85243",
                "type": "xls",
                "sheets": {
                    'monthly': '6～25頁'
                },
            },
            {
                "year": "2008",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=85066",
                "type": "xls",
                "sheets": {
                    'monthly': '6～25頁'
                },
            },
            {
                "year": "2009",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=85080",
                "type": "xls",
                "sheets": {
                    'monthly': '6～25頁'
                },
            },
            {
                "year": "2010",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=85073",
                "type": "xls",
                "sheets": {
                    'monthly': '6～28頁'
                },
            },
            {
                "year": "2011",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=539009",
                "type": "xls",
                "sheets": {
                    'monthly': '6～28頁'
                },
            },
            {
                "year": "2012",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=651449",
                "type": "xls",
                "sheets": {
                    'monthly': '6～28頁'
                },
            },
            {
                "year": "2013",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=747164",
                "type": "xls",
                "sheets": {
                    'monthly': '6～28頁'
                },
            },
            {
                "year": "2014",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=843639",
                "type": "xlsx",
                "sheets": {
                    'monthly': '6～28頁'
                },
            },
            {
                "year": "2015",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=943087",
                "type": "xlsx",
                "sheets": {
                    'monthly': '6～28頁'
                },
            },
            {
                "year": "2016",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=1038171",
                "type": "xlsx",
                "sheets": {
                    'monthly': '6～28頁'
                },
            },
            {
                "year": "2017",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=1137239",
                "type": "xls",
                "sheets": {
                    'monthly': '6～28頁'
                },
            },
            {
                "year": "2018",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=1230093",
                "type": "xlsx",
                "sheets": {
                    'monthly': '6～28頁'
                },
            },
            {
                "year": "2019",
                "url": "http://www.pref.hokkaido.lg.jp/file.jsp?id=1326718",
                "type": "xlsx",
                "sheets": {
                    'monthly': '6～28頁'
                },
            },
        ],
    }
]

communes = [
    "えりも町",
    "せたな町",
    "ニセコ町",
    "むかわ町",
    "愛別町",
    "旭川市",
    "芦別市",
    "安平町",
    "伊達市",
    "雨竜町",
    "浦臼町",
    "浦河町",
    "浦幌町",
    "猿払村",
    "遠軽町",
    "遠別町",
    "奥尻町",
    "乙部町",
    "音威子府村",
    "音更町",
    "下川町",
    "歌志内市",
    "芽室町",
    "岩見沢市",
    "岩内町",
    "喜茂別町",
    "共和町",
    "興部町",
    "倶知安町",
    "釧路市",
    "釧路町",
    "栗山町",
    "訓子府町",
    "恵庭市",
    "月形町",
    "剣淵町",
    "古平町",
    "厚岸町",
    "厚真町",
    "厚沢部町",
    "広尾町",
    "更別村",
    "江差町",
    "江別市",
    "黒松内町",
    "今金町",
    "根室市",
    "佐呂間町",
    "砂川市",
    "札幌市",
    "三笠市",
    "士別市",
    "士幌町",
    "枝幸町",
    "鹿追町",
    "鹿部町",
    "七飯町",
    "室蘭市",
    "斜里町",
    "寿都町",
    "初山別村",
    "小清水町",
    "小樽市",
    "小平町",
    "松前町",
    "沼田町",
    "上ノ国町",
    "上砂川町",
    "上士幌町",
    "上川町",
    "上富良野町",
    "新ひだか町",
    "新冠町",
    "新篠津村",
    "新十津川町",
    "新得町",
    "森町",
    "深川市",
    "真狩村",
    "仁木町",
    "清水町",
    "清里町",
    "西興部村",
    "石狩市",
    "積丹町",
    "赤井川村",
    "赤平市",
    "千歳市",
    "占冠村",
    "壮瞥町",
    "増毛町",
    "足寄町",
    "帯広市",
    "大空町",
    "大樹町",
    "鷹栖町",
    "滝上町",
    "滝川市",
    "知内町",
    "池田町",
    "稚内市",
    "置戸町",
    "秩父別町",
    "中札内村",
    "中川町",
    "中頓別町",
    "中標津町",
    "中富良野町",
    "長沼町",
    "長万部町",
    "津別町",
    "弟子屈町",
    "天塩町",
    "登別市",
    "島牧村",
    "東川町",
    "東神楽町",
    "当別町",
    "当麻町",
    "洞爺湖町",
    "苫小牧市",
    "苫前町",
    "奈井江町",
    "南富良野町",
    "南幌町",
    "日高町",
    "泊村",
    "白糠町",
    "白老町",
    "函館市",
    "八雲町",
    "比布町",
    "美唄市",
    "美瑛町",
    "美深町",
    "美幌町",
    "標茶町",
    "標津町",
    "浜中町",
    "浜頓別町",
    "富良野市",
    "平取町",
    "別海町",
    "豊浦町",
    "豊頃町",
    "豊富町",
    "北見市",
    "北広島市",
    "北斗市",
    "北竜町",
    "幌延町",
    "幌加内町",
    "本別町",
    "妹背牛町",
    "幕別町",
    "名寄市",
    "網走市",
    "木古内町",
    "紋別市",
    "湧別町",
    "由仁町",
    "雄武町",
    "夕張市",
    "余市町",
    "様似町",
    "羅臼町",
    "蘭越町",
    "利尻町",
    "利尻富士町",
    "陸別町",
    "留寿都村",
    "留萌市",
    "和寒町",
    "礼文町",
    "神恵内村",
    "福島町",
    "羽幌町",
    "鶴居村",
    "京極町",
]
