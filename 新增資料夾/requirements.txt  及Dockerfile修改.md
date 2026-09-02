**requirements.txt（會一直變動）**

為什麼不是寫死的：它記錄你專案需要的外掛工具。

變動時機：今天你只需要連線 MongoDB，所以寫 pymongo；明天主管叫你做網頁功能，你必須手動進去新增 flask 或 fastapi；後天要處理資料分析，又要加入 pandas。每次加新工具，這個清單就要跟著更新。



**Dockerfile（會跟著環境升級變動）**

為什麼不是寫死的：它是你的工廠藍圖。

變動時機：今天你用 Python 3.10，所以寫 FROM python:3.10-slim；明年公司升級系統，全面改用 Python 3.12，你就必須修改這張藍圖。或者專案需要多安裝其他系統套件時，也要回來修改它。



**核心觀念**

這三個檔案（app.py、requirements.txt、Dockerfile）都是由你親手編寫的「程式原始碼與設定」。它們只是固定在你的專案版本裡，不是不能改的密碼；當需求改變時，你隨時都可以打開它們進行修改。





**以下如何更改上面兩者:**



* 如果主管叫你「把程式改造成一個網頁 API」

假設你要加裝一個叫 Flask 的 Python 網頁套件，並讓這個 Docker 貨櫃可以對外開放網路埠（Port 5000）讓人連線。



**如何修改 requirements.txt** (直接換行加名字)

修改這個檔案最簡單，它就像是購物清單。你只需要用 VS Code 打開它，直接在最下面換行，填入新套件的名字和版本號即可。



**修改前:**

pymongo==4.6.1

dnspython==2.6.1

**修改後:**

pymongo==4.6.1

dnspython==2.6.1

flask==3.0.3



**如何修改 Dockerfile (通常只改第一行或最後面)**

修改這張藍圖時，你通常只需要調整「開頭的環境版本」或「對外開放的設定」。

以下是常用的修改指令：



**修改前:**

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD \["python", "app.py"]



**修改後（假設要升級 Python 版本，並開放 5000 網路孔）：**

\#1. 修改這裡 : 把3.10改成 3.12 (升級 PYTHON 版本)

FROM pyhon:3.12-slim



WORKDIR /app

COPY requirements.txt .

RUN pip install - -no-cache-dir -r requirements.txt

COPY app.py .



\#2. 新增這裡:告訴 Docker 這個貨櫃要打開 5000 號網頁通訊埠

EXPOSE 5000

CMD \["python", "app.py"]







**💡 記住這個大原則**

只要你動手修改了這兩個檔案的任何一個字，你的下一步動作一定是回到 CMD 輸入打包指令：

bashdocker build -t my-mongo-app .

因為如果不重新 build，Docker 就不會幫你安裝新寫進去的 flask 套件，貨櫃裡跑的也依然會是舊的複製品。













































