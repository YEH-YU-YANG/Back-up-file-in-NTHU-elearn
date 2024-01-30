- [Back-up-file-in-NTHU-elearn](#back-up-file-in-nthu-elearn)
  - [目標](#目標)
  - [限制](#限制)
  - [使用教學](#使用教學)
    - [第一步 : 確認Google版本](#第一步--確認google版本)
      - [右上角的三個圓點 -\> 設定](#右上角的三個圓點---設定)
      - [點集左下角的 "關於 Chrome"](#點集左下角的-關於-chrome)
      - [確認版本](#確認版本)
    - [第二步 : 下載對應版本 Driver](#第二步--下載對應版本-driver)
      - [Windows](#windows)
      - [Mac](#mac)
    - [第三步 : 找到登入 elearn 的 cookie](#第三步--找到登入-elearn-的-cookie)
      - [登入 elearn -\> 按下 `ctrl + shift + i` -\> 刷新頁面](#登入-elearn---按下-ctrl--shift--i---刷新頁面)
      - [找到 my 欄位 -\> 點擊 cookie -\> 找到 MoodleSessionM35 欄位的 value](#找到-my-欄位---點擊-cookie---找到-moodlesessionm35-欄位的-value)
    - [第四步 : 把 cookie 放入 env.json](#第四步--把-cookie-放入-envjson)
    - [第五步 : 執行.exe檔](#第五步--執行exe檔)
      - [直接點擊 `main.exe`](#直接點擊-mainexe)
      - [下載資訊](#下載資訊)
  - [查看結果](#查看結果)

# Back-up-file-in-NTHU-elearn

## 目標

![](Images/target_files.png)

下載歷屆繳交過的作業

## 限制

必須使用 **Google Chrome**

## 使用教學

### 第一步 : 確認Google版本

#### 右上角的三個圓點 -> 設定 
![](Images/google_version_1.png)

#### 點集左下角的 "關於 Chrome"
![](Images/google_version_2.png)

#### 確認版本
![](Images/google_version_3.png)

上圖顯示的版本為 **121.0.6167.86**。
代表目前的 **Google** 版本是 **121**。
> 只須關注版本號的前三位數字 !!

### 第二步 : 下載對應版本 Driver

#### Windows
| 版本                    | 文件大小 | 載點     |
|------------------------|-----------|--------------|
| Win64_ChromeDriver_v112 | 23.6 MB  | [**Win64_ChromeDriver_v112**][Win64_ChromeDriver_v112] |
| Win64_ChromeDriver_v113 | 23.6 MB  | [**Win64_ChromeDriver_v113**][Win64_ChromeDriver_v113] |
| Win64_ChromeDriver_v114 | 25.7 MB  | [**Win64_ChromeDriver_v113**][Win64_ChromeDriver_v113] |
| Win64_ChromeDriver_v121 | 24.9 MB  | [**Win64_ChromeDriver_v121**][Win64_ChromeDriver_v121] |

#### Mac
| 版本                    | 文件大小  |    載點     |
|-------------------------|----------|--------------|
| Mac64_ChromeDriver_v112 | 25.6 MB  | [**Mac64_ChromeDriver_v112**][Mac64_ChromeDriver_v112] |
| Mac64_ChromeDriver_v113 | 25.6 MB  | [**Mac64_ChromeDriver_v113**][Mac64_ChromeDriver_v113] |
| Mac64_ChromeDriver_v114 | 25.1 MB  | [**Mac64_ChromeDriver_v114**][Mac64_ChromeDriver_v114] |
| Mac64_ChromeDriver_v121 | 25   MB  | [**Mac64_ChromeDriver_v121**][Mac64_ChromeDriver_v121] |

> 記得"解壓縮"下載的檔案哦 !

### 第三步 : 找到登入 elearn 的 cookie

#### 登入 elearn -> 按下 `ctrl + shift + i` -> 刷新頁面
![](Images/elearn_login_1.png)

#### 找到 my 欄位 -> 點擊 cookie -> 找到 MoodleSessionM35 欄位的 value	
![](Images/elearn_login_2.png)

![](Images/elearn_login_3.png)

>(1) MoodleSessionM35 欄位的 value 為 a98xxxxxxxx。<br>
>(2) 不要外流這個 value。

### 第四步 : 把 cookie 放入 env.json

![](Images/env_1.png)
>(1) 記得放在 value 欄位的雙括號 `""` 裡面。 <br>
>(2) 記得存檔 !!

### 第五步 : 執行.exe檔

#### 直接點擊 `main.exe`
![](Images/main_exe_1.png)

#### 下載資訊
<img src="Images/result_1.png" width="70%" />

## 查看結果

下載完的檔案都在 `assignments` 資料夾裡面

![](Images/result_2.png)

![](Images/result_3.png)

![](Images/result_4.png)

![](Images/result_5.png)


[Mac64_ChromeDriver_v112]: https://github.com/YEH-YU-YANG/Back-up-file-in-NTHU-elearn/releases/download/v1.0-alpha/Mac64_ChromeDriver_v112.zip
[Mac64_ChromeDriver_v113]: https://github.com/YEH-YU-YANG/Back-up-file-in-NTHU-elearn/releases/download/v1.0-alpha/Mac64_ChromeDriver_v113.zip
[Mac64_ChromeDriver_v114]: https://github.com/YEH-YU-YANG/Back-up-file-in-NTHU-elearn/releases/download/v1.0-alpha/Mac64_ChromeDriver_v114.zip
[Mac64_ChromeDriver_v121]: https://github.com/YEH-YU-YANG/Back-up-file-in-NTHU-elearn/releases/download/v1.0-alpha/Mac64_ChromeDriver_v121.zip

[Win64_ChromeDriver_v112]: https://github.com/YEH-YU-YANG/Back-up-file-in-NTHU-elearn/releases/download/v1.0-alpha/Win64_ChromeDriver_v112.zip
[Win64_ChromeDriver_v113]: https://github.com/YEH-YU-YANG/Back-up-file-in-NTHU-elearn/releases/download/v1.0-alpha/Win64_ChromeDriver_v113.zip
[Win64_ChromeDriver_v114]: https://github.com/YEH-YU-YANG/Back-up-file-in-NTHU-elearn/releases/download/v1.0-alpha/Win64_ChromeDriver_v114.zip
[Win64_ChromeDriver_v121]: https://github.com/YEH-YU-YANG/Back-up-file-in-NTHU-elearn/releases/download/v1.0-alpha/Win64_ChromeDriver_v121.zip
