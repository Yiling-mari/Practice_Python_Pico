#預防crash&設定變數
try: 
    height = int(input("請輸入身高(公分):"))
    weight = int(input("請輸入體重(公斤):"))
except:
    print("輸入錯誤，請重新輸入")   
#計算BMI
else: 
    height /=100
    BMI = round(weight/height**2, 1)
    print(f"您的BMI值是{BMI}")            
    if BMI < 18.5:          #體重分析
        print ("您的體重過輕")
    elif BMI <= 24:
        print ("您的體重在正常範圍")
    elif BMI <= 27:
        print ("您的體重過重")
    elif BMI <= 30:
        print ("您的體重輕度肥胖")
    elif BMI <= 35:
        print ("您的體重重度肥胖")
    else:
        print ("請趕快減重!")

print("應用程式結束")