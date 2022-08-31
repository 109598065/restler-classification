論文工具說明
===

# 影片介紹

https://www.youtube.com/watch?v=npR4ejAYM6c&ab_channel=%E5%8C%97%E7%A7%91%E5%A4%A7-%E9%BB%83%E6%B3%93%E5%87%B1

# 檔案說明
```
Folder
└───restler
│   │   restler-modified.rar
│   │   restler-merged.rar
│
└   restler-classification.rar
```

- restler 資料夾: 內容為修改過後的 RESTler
    - restler-modified.rar 分類方法
    - restler-merged.rar 合併分類和序列的方法
- restler-classification.rar: 修改 Grammar 的程式

# 使用說明

- 環境: 安裝 [Python 3.8.2](https://www.python.org/downloads/) 和 [.NET 5.0](https://dotnet.microsoft.com/en-us/download/dotnet/5.0)。
- 修改基於 [RESTler 版本 8.6.0](https://github.com/microsoft/restler-fuzzer/tree/v8.6.0)

### 1. Build

建構 [修改後 RESTler](https://github.com/109598065/restler-modified) 的可執行檔案。

```=
cd D:\restler
python ./build-restler.py --dest_dir D:\restler_bin
```
### 2. Compile
編譯 Swagger 檔案，藉由 Swagger 檔案生成 Grammar。

於執行指令的資料夾下創建一個新的子資料夾 ```Compile```，其中編譯結果保存在該資料夾中。

```=
cd D:\demo-server-test
D:\restler_bin\restler\Restler.exe compile --api_spec D:\demo-server-test\swagger.json
```

### 3. Classification
使用 [RESTler Classification](https://github.com/109598065/restler-classification) 修改 Grammar 及設定。

切換至 RESTler Classification 資料夾對其進行設定。目前設定檔案放置於最外層的 execute.py 內。

```=
cd D:\restler-classification
python ./execute.py
```
### 4. Fuzz
使用 RESTler 執行模糊測試並生成結果報表。

時間設置5小時可成功執行大部分實驗

於執行指令的資料夾下創建一個新的子資料夾 ```Fuzz```，其中模糊測試結果保存在資料夾中。

```=
cd D:\demo-server-test
D:\restler_bin\restler\restler.exe fuzz --grammar_file D:\demo-server-test\Compile\grammar_classification.py --dictionary_file D:\demo-server-test\Compile\dict.json --settings D:\demo-server-test\Compile\engine_settings_classification.json --time_budget 5
```

# 結果說明
experiment 資料夾下有部分實驗的統計程式
```count.py: 實驗三統計狀態碼數量```
```http_status_code_coverage.py: 實驗三統計狀態碼覆蓋率```
