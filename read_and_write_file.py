# 用內建程式open的method開啟特定的檔案。
# 選項1: file = open("my_file.txt")

# 選項2: 用with的寫法。
# with open("my_file.txt") as file:
#     contents = file.read() # 讀取檔案
#     print(contents) # 應該會印出 Hello, I'm Dawei.

# 如果用with開始檔案的時候，file.close就可以不啟用了。
# file.close()    # 關閉檔案，騰出電腦資源。

# R代表Read, W代表write, a代表attend
# 把mode改成a的時候，資料就不會被洗掉。
with open("my_file.txt", mode="a") as file:
    file.write("\n New text.") # 把原本在my_file.txt的資料洗掉。
    print(file)
    
# 如果要建立一個新的檔案的話，可以在mode的地方輸入w，就可以直接建立了。
# 記住，只有在沒有這個檔案的時候，輸入w時，才有效。
with open("new_testing_file.txt", mode="w") as file:
    file.write("Hello world.") # 輸入內容。
    # 這個時候，就會產生一個 new_testing_file.txt的檔案，在資料夾裡面。


