# configuration for tenpay
TENPAY_PARTNER = "119879201"
TENPAY_KEY = "37b8cbaf90da9ffef761a91cf"
TENPAY_PAYMENT_URL = "https://gw.tenpay.com/gateway/pay.htm"

#exchange rate
RECHARGE_EXCHANGE_RATE = 1  # 1 indicates 1 Fen/balance
RECHARGE_FEE_RATE = 100   # 1 indicates 1 Fen/input_price_value, input as Yuan

http://gbk.sms.webchinese.cn/?Uid=smartbrandnew&Key=841092&smsMob=15257117182&smsText=000000

		print user.verifycode
		user.verifycode = random.randrange(000000,999999)
		user.save()
	        content = 'verifycode:' + str(user.verifycode)
	        utils.send_msg(data['phone'], content)