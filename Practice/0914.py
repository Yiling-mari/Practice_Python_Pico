while True:
    try: #預防crash&設定變數
        height = float(input("請輸入身高(公分):"))
        if height > 300:
            raise Exception("輸入身高不可超過300")  #手動raise Exception
        weight = float(input("請輸入體重(公斤):"))
        break
    except ValueError:       #except沒有限制幾個，但(多個)except&else只會執行其中一個
        print("輸入格式有誤，請重新輸入")
        continue
    except Exception as e:    #除了格式錯誤的其他所有錯誤都是exception(要在最後面，屬廣泛錯誤)
        print(f"錯誤訊息:{e}")   #e就是上面key的字
        continue
    else:    #計算BMI
        height /=100
        BMI = round(weight/height**2, 1)
        print(f"您的BMI值是{BMI}")            
        #體重分析    
        if BMI < 18.5:          
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

        play_again = input("還要繼續嗎?(y,n)")
        if play_again == "n":
            break

print("程式結束")