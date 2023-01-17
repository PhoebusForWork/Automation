#### LD 3.0 automation testing

#### 程式碼規範
參照python PEP-8規範

原文：
https://peps.python.org/pep-0008/

中文版：
https://github.com/kernellmd/Knowledge/blob/master/Translation/PEP%208%20%E4%B8%AD%E6%96%87%E7%BF%BB%E8%AF%91.md

#### 程式碼結構
``` python
automation-testing
├── config               -- 設定檔
├── pylib                -- 內部函式庫
    ├── client_side        -- 前台共用函式庫
    ├── platform           -- 後台共用函式庫
├── resources            -- 測試案例
    ├── client_side        -- 前台測試案例
    ├── platform           -- 後台測試案例
    ├── upload_file        -- 測試上傳用檔案
├── testcase             -- 測試案例(實作層)
    ├── client_side        -- 前台測試案例(實作層)
    ├── platform           -- 後台測試案例(實作層)
├── utils                -- 三方共用函式庫

```