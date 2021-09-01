import rpa
import pandas as pd
rpa.init(turbo_mode = True)
rpa.url("http://www.rpachallenge.com")
rpa.wait(2)
rpa.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
rpa.download("http://www.rpachallenge.com/assets/downloadFiles/challenge.xlsx", "challenge.xlsx")
df=pd.DataFrame(pd.read_excel("challenge.xlsx", sheet_name="Sheet1"))
for row in df.itertuples():
    rpa.type('//*[@ng-reflect-name="labelFirstName"]', row[1])
    rpa.type('//*[@ng-reflect-name="labelLastName"]', row[2])
    rpa.type('//*[@ng-reflect-name="labelCompanyName"]', row[3])
    rpa.type('//*[@ng-reflect-name="labelRole"]', row[4])
    rpa.type('//*[@ng-reflect-name="labelAddress"]', row[5])
    rpa.type('//*[@ng-reflect-name="labelEmail"]', row[6])
    rpa.type('//*[@ng-reflect-name="labelPhone"]', str(row[7]))
    rpa.click('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
    continue
rpa.wait(4)
rpa.close()