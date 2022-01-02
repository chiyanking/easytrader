import easytrader

# from easytrader import server
#
# server.run(port=1430) # 默认端口为 1430








user = easytrader.use('universal_client', host='10.50.20.232', port='1430', debug=True)
user.prepare(exe_path="D:\\同花顺软件\\同花顺\\xiadan.exe", user="029000028983", password="513071", comm_password="wk5131")
print(user.balance)
print(user.position)
user.buy("600016", price=0.30, amount=100)
user.cancel_all_entrusts()
user.auto_ipo()
