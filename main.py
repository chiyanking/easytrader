import easytrader

# from easytrader import server
#
# server.run(port=1430) # 默认端口为 1430



# //设置全局代理
# //http
# git config --global https.proxy http://127.0.0.1:7890
# //https
# git config --global https.proxy https://127.0.0.1:7890
# //使用socks5代理的 例如ss，ssr 1080是windows下ss的默认代理端口,mac下不同，或者有自定义的，根据自己的改
# git config --global http.proxy socks5://127.0.0.1:7890
# git config --global https.proxy socks5://127.0.0.1:7890
# 
# //只对github.com使用代理，其他仓库不走代理
# git config --global http.https://github.com.proxy socks5://127.0.0.1:7890
# git config --global https.https://github.com.proxy socks5://127.0.0.1:7890
# //取消github代理
# git config --global --unset http.https://github.com.proxy
# git config --global --unset https.https://github.com.proxy
# 
# //取消全局代理
# git config --global --unset http.proxy
# git config --global --unset https.proxy




user = easytrader.use('universal_client', host='10.50.20.232', port='1430', debug=True)
user.prepare(exe_path="D:\\同花顺软件\\同花顺\\xiadan.exe", user="029000028983", password="513071", comm_password="wk5131")
print(user.balance)
print(user.position)
user.buy("600016", price=0.30, amount=100)
user.cancel_all_entrusts()
user.auto_ipo()
