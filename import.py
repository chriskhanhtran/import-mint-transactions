import os
import time
import urllib
import json

import pandas as pd

csv_name = 'import.csv'
account = '9195831'
tag1 = 'tag2120776'
tag2 = 'tag2120777'
tag3 = 'tag2120778'
cookie = 's_vi=[CS]v1|306E507D7A505B40-4000057BA548B1AC[CE]; s_ecid=MCMID%7C86119315603216739142127086571822453027; ivid_b=d4022ac0-f564-4956-a1e6-ac6bb1fb25cd; s_fid=3305CC92AAAB3764-03CB65588AC62D2A; ivid=1d5e4b7c-bdab-444e-9d90-02326d3e9bc5; did=SHOPPER2_733c187d54d9235c5a22248ab0925fc93a80cf7b5d7403e29dfab8cbc06e8af12a3a77eb4b16c389488c896d065984ff; da_lid=191EE75C9A72EA12C46EBB990C09E6EA79|0|0|0; mint.glogin=khanhtran96; mu=1; wa_login=1; _gcl_au=1.1.95529417.1625071961; aam_uuid=86330877239962026072146445007511207414; currentClientType=Mint; brandingOption=whitelabel; current-config-source=Back-end; userguid=E89C0BE18E3EDED0; aam_qbus=mesg1%3D16601478%3A16602502%3A16603107%3A17547636%3A17547749%3A17593783%3A17861345; tt_ipgeo=2783042644%7CUS%7CCA%7CY%7C37.425%7C-121.946%7C807%7C95134%7CSan%20Jose; ivid_p=1d5e4b7c-bdab-444e-9d90-02326d3e9bc5; tms_mint=18663:3:48876; visitCount=2|1628027535316; ROUTEID=.; AMCVS_969430F0543F253D0A4C98C6%40AdobeOrg=1; s_cc=true; qbn.uidp=192edeebb1032024f82bc81821ff16101ce; userIdentifier=13563577535553179; mintPN=4; _exp_mintPN=4; mintUserName=""; _transactionIframeLocation=undefined; __mintMoment_CK=; ius_session=94641B945498443EA9D94A617B9893EA; akid=gip104.109.156.22_gsip23.44.130.142_clip165.225.221.64_rclip23.208.27.75; ajs_user_id=%22192edeebb1032024f82bc81821ff16101ce%22; ajs_anonymous_id=%221d5e4b7c-bdab-444e-9d90-02326d3e9bc5%22; s_sq=%5B%5BB%5D%5D; mint.authid=13563577535553179; mint.gauthid=13563577535553179; mint.agentid=13563577535553179; mint.parentid=50000003; login.offering=Mint; qbn.authid=13563577535553179; qbn.gauthid=13563577535553179; qbn.agentid=13563577535553179; qbn.parentid=50000003; mint.ticket=V1-44-X0hg99surkm8rfjdbtm3un; mint.tkt=V1-44-X0hg99surkm8rfjdbtm3un; qbn.ticket=V1-44-X0hg99surkm8rfjdbtm3un; qbn.tkt=V1-44-X0hg99surkm8rfjdbtm3un; qbn.account_chooser=iVml-ml7pwbfX7UD6qMtXe9SFI0EX-v3jsE3bsmgnEtbUZ5tGhCWZMutC21_Ef2cEPHOI-seU1jgiOr0KHtay9agJnCJvsxXtnK6HTuvwcyG8Gj54EHF8vmTooHSzC26CZ0wDSMc9i9QcJgwJNsl9v04OnmtTLyGLJLLFthtEBR8M0SnEPGu9R411xJdfhWhORSr3fdeEeUYxkeQmq1McLb1ZgxGzDouSB8LDFEMjDs06HiXz-eWiA; mint.glogin_temp=khanhtran96; qbn.account_chooser_temp=%7B%22identifier%22%3A%22khanhtran96%22%2C%22offerings%22%3A%5B%7B%22offeringId%22%3A%22Intuit.ifs.mint%22%7D%5D%7D; ius_at=1628873484304; ADRUM=s=1628873484730&r=https%3A%2F%2Faccounts.intuit.com%2Findex.html%3F722397480; AMCV_969430F0543F253D0A4C98C6%40AdobeOrg=-637568504%7CMCIDTS%7C18853%7CMCMID%7C86119315603216739142127086571822453027%7CMCAAMLH-1629478286%7C7%7CMCAAMB-1629478286%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1628880686s%7CNONE%7CMCAID%7C306E507D7A505B40-4000057BA548B1AC%7CvVersion%7C5.1.1; MINTJSESSIONID=7B696EEA989D00CAF213FE519F98053B-n1; pseudonymID=192edeebb1032024f82bc81821ff16101ce; utag_main=v_id:017a5dd4d03e009bd19c3e6b8ab803073006506b00bd0$_sn:10$_se:5$_ss:0$_st:1628875290167$vapi_domain:intuit.com$ses_id:1628870970116%3Bexp-session$_pn:3%3Bexp-session; CONSENTMGR=dns:false%7Cconsent:true%7Cts:1628873490170; AWSALB=d24t3Xxr8UhGMulTPbW+Xap8twd8F8znlQLlbIp5zQgv2BKHtQ4O/Qxue5efSPSUle44eW85u8946fU0MVKwhGUGGDRkLSHpygiQPxKiK0xWojdBWVCkoCHHHP7b; AWSALBCORS=d24t3Xxr8UhGMulTPbW+Xap8twd8F8znlQLlbIp5zQgv2BKHtQ4O/Qxue5efSPSUle44eW85u8946fU0MVKwhGUGGDRkLSHpygiQPxKiK0xWojdBWVCkoCHHHP7b'
token = '25482548IDlDNWzk76p9bOBLiq8OBc0ctONXYhP2LuRYPmg'

def submit_transactions():
	df = pd.read_csv(csv_name)

	for idx, row in df.iterrows():
		print(f"processing row {idx + 1}/{len(df)}")
		print(row.to_dict())

		# Read data
		transaction_date = str(row['Transaction Date'])
		merchant = row['Description']
		catName = row['Category']
		amount = float(row['Amount'])
		note = row['Notes']

		# Process 'date'
		transaction_date = transaction_date.replace("/", "%2F").replace(".", "%2F").replace("-", "%2F")

		# Process 'merchant'
		merchant = urllib.parse.quote(merchant)

		# Process 'category'
		if len(catName) == 0: 
			catID = '20'
		else : 
			catID = str(category_to_id(catName))

		category = urllib.parse.quote(catName)

		# amount and expense
		is_expense = 'true' if amount > 0 else 'false'
		amount = str(amount * (-1))

		txnId = "9999999999"
		# prepare raw data
		raw_data = f'cashTxnType=on&mtCashSplit=on&mtCheckNo=&{tag1}=0&{tag2}=0&{tag3}=0&task=txnadd&txnId={txnId}' \
				f'&mtType=cash&mtAccount={account}&symbol=&note={note}&isInvestment=false&catId={catID}' \
				f'&category={category}&merchant={merchant}&date={transaction_date}&amount={amount}&mtIsExpense={is_expense}' \
				f'&mtCashSplitPref=1&token={token}'

		# CURL command
		curl_cmd = f"""curl 'https://mint.intuit.com/updateTransaction.xevent' \
			-H 'authority: mint.intuit.com' \
			-H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
			-H 'x-requested-with: XMLHttpRequest' \
			-H 'adrum: isAjax:true' \
			-H 'sec-ch-ua-mobile: ?0' \
			-H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36' \
			-H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
			-H 'accept: */*' \
			-H 'origin: https://mint.intuit.com' \
			-H 'sec-fetch-site: same-origin' \
			-H 'sec-fetch-mode: cors' \
			-H 'sec-fetch-dest: empty' \
			-H 'referer: https://mint.intuit.com/transaction.event' \
			-H 'accept-language: en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7' \
			-H 'cookie: {cookie}' \
			--data-raw '{raw_data}' \
			--compressed"""

		# submit command
		os.system(curl_cmd)
		print("\n")
		time.sleep(1)


def category_to_id(import_category):
	with open("category.json") as f:
		category_to_id_dict = json.loads(f.read())
	return category_to_id_dict.get(import_category, 20)


if __name__ == "__main__":
	submit_transactions()
