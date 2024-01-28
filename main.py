from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import json
import os
import re
import shutil

global driver

global download_path
download_path = os.path.join(os.getcwd(),"tmp")


def driver_setting():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)  #不自動關閉瀏覽器
    options.add_argument('--start-maximized') #瀏覽器視窗最大化

    prefs = {
        'profile.default_content_settings.popups': 0,
        'download.default_directory': download_path,
        'download.prompt_for_download': False,  # 禁用下载提示框
        'safebrowsing.enabled': True  # 打開安全瀏覽
    }
    options.add_experimental_option('prefs', prefs)

    # options.
    driver = webdriver.Chrome(options=options)
    return driver

def goto_grade_page():
    # 讀取檔案
    with open('env.json') as file:
        env = json.load(file)
    driver.get('https://elearn.nthu.edu.tw/my/')
    driver.add_cookie(env['cookie'])
    driver.refresh()
    driver.get("https://elearn.nthu.edu.tw/grade/report/overview/index.php")

def collect_class_urls():
    # 使用 WebDriverWait 等待表格出現
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "overview-grade"))
    )

    # 找到表格中的所有連結元素
    links = table.find_elements(By.XPATH, "//td[@class='cell c0']/a")

    # 提取所有連結的 href 屬性值
    urls = [link.get_attribute("href") for link in links]

    return urls

def collect_class_ids(urls):
    # 印出所有的 href 值
    ids=[]
    for url in urls:
        # 使用正規表達式匹配 URL 中的 id 數字
        match = re.search(r'id=(\d+)', url)

        if match:
            id_number = match.group(1)
            # print("從 URL 中取得的 id 數字:", id_number)
            ids.append(id_number)
        else:
            print("未找到 id 數字")

    return ids

def collect_homework_page(class_ids):

    ids = []

    base_url = 'https://elearn.nthu.edu.tw/mod/assign/index.php?id='
    for class_id in class_ids:
        url = base_url+class_id
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "maincontent"))
        )

        table = driver.find_elements(By.CLASS_NAME,'generaltable')
        if table:
            ids.append(class_id)


    return ids

def make_chinese_string(original_string):
    chinese_pattern = re.compile('[\u4e00-\u9fa5]+')
    chinese_matches = chinese_pattern.findall(original_string)

    # 將匹配到的中文字符列表合併成字串
    chinese_text = ''.join(chinese_matches)

    return chinese_text

def parse_and_format_date(date_string):
    # 使用正規表達式抓取年月日
    match = re.search(r'(\d{4})年 (\d{1,2})月 (\d{1,2})日', date_string)

    if match:
        year, month, day = match.groups()
        formatted_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        return formatted_date
    else:
        return None

def wait_for_download():

    # Wait for download
    while True:
        files = os.listdir(download_path)
        if len(files) >= 0 and not any('.crdownload' in name for name in files) and not any('.tmp' in name for name in files) :
            break
        for name in files:
            if name.endswith('.crdownload') or name.endswith('.tmp'):
                continue
            else:
                break

def make_directory(path,title):
    try:
      os.mkdir(path)
    except FileExistsError:
      print(f"目錄 '{title}' 已存在")

def download_branch_homeworks(url,destination_path, is_last):

    driver.get(url)

    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "generaltable"))
    )

    # 找到所有包含 target="_blank" 的連結元素
    links = table.find_elements(By.XPATH, ".//td[@class='cell c1 lastcol']//a[@target='_blank']")

    # 提取所有連結的 href 屬性值
    file_hrefs = [link.get_attribute("href") for link in links]

    file_names = [link.text for link in links]


    # 下載所有檔案
    for file_href, file_name in zip(file_hrefs,file_names):
        driver.get(file_href)
        if is_last:
            print(str(' ')*4 + '|-- ' + file_name)
        else:
            print('|' + str(' ')*3 + '|-- ' + file_name)

    wait_for_download()
    wait_for_download()
    wait_for_download()
    wait_for_download()
    wait_for_download()

    # 取得下載路徑中的所有文件
    files_to_move = os.listdir(download_path)

    if files_to_move:
        # 移動所有檔案到目標路徑
        for file_name in files_to_move:
            source_path = os.path.join(download_path, file_name)
            shutil.move(source_path, destination_path)

def download_homeworks(base_ids):
    
    #創建assignments資料夾
    make_directory(os.path.join(os.getcwd(),'assignments'), 'assignments')

    #創建tmp資料夾
    make_directory(os.path.join(os.getcwd(),'tmp'), 'tmp')


    base = 'https://elearn.nthu.edu.tw/mod/assign/index.php?id='
    for base_id in base_ids:
        
        print('')
        
        base_url = base + base_id
        driver.get(base_url)

        # 抓課程名稱
        subject_title= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'sitetitle'))
        )
        subject_title = make_chinese_string(subject_title.text)
        print(subject_title)

        # 抓各科作業連結
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "generaltable"))
        )

        # 找到表格中的所有連結元素
        cell_c1 = table.find_elements(By.XPATH, "//td[@class='cell c1']/a")
        branch_urls = [link.get_attribute("href") for link in cell_c1]

        # 找到各個作業名稱
        branch_titles = [link.text for link in cell_c1]

        # 找到各個作業死線
        cell_c2 = table.find_elements(By.XPATH, "//td[@class='cell c2']")
        temp_branch_deadlines = [link.text for link in cell_c2]

        branch_deadlines = []
        for topic in temp_branch_deadlines:
            str = parse_and_format_date(topic)
            branch_deadlines.append(str)

        #創科目資料夾
        subject_dir_path = os.path.join(os.getcwd(),'assignments',subject_title)
        make_directory(subject_dir_path,subject_title)

        for index, (branch_url, branch_deadline, branch_title) in enumerate(zip(branch_urls, branch_deadlines, branch_titles)):
            # 創各科作業資料夾
            if branch_deadline is None:
                branch_dir_path = os.path.join(subject_dir_path, branch_title)
                make_directory(branch_dir_path, branch_title)
            else:
                branch_dir_path = os.path.join(subject_dir_path, branch_deadline + ' ' + branch_title)
                make_directory(branch_dir_path, branch_deadline + ' ' + branch_title)

            print('|')
            print('|-- ' + branch_title)


            # Check if branch_url is the last element
            if index == len(branch_urls) - 1:
                last_url = True
            else:
                last_url = False

            # 下載該作業所有繳過的檔案
            download_branch_homeworks(branch_url, branch_dir_path, last_url)

        print('')

def remove_empty_directory():

    # tmp
    if os.path.exists(download_path):
        os.rmdir(download_path)

    # assignments
    path = os.path.join(os.getcwd(),'assignments')
    dirs = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    for dir in dirs:

        sub_path = os.path.join(path,dir)
        sub_dirs = [name for name in os.listdir(sub_path) if os.path.isdir(os.path.join(sub_path, name))]

        for sub_dir in sub_dirs:
            sub_sub_path = os.path.join(sub_path,sub_dir)
            number_of_subsubcontents = len(os.listdir(sub_sub_path))

            # 檢查資料夾是否為空
            if number_of_subsubcontents == 0:
                # 刪除資料夾
                os.rmdir(sub_sub_path)



        number_of_subcontents = len(os.listdir(os.path.join(path,dir)))
        # 檢查資料夾是否為空
        if number_of_subcontents == 0:
            # 刪除資料夾
            os.rmdir(sub_path)

def remove_useless_directory():
    directories_to_remove = []
    directories_to_remove.append(os.path.join(os.getcwd(),'assignments'))
    directories_to_remove.append(os.path.join(os.getcwd(),'tmp'))
    
    for directory_to_remove in directories_to_remove:
        if os.path.exists(directory_to_remove):
            shutil.rmtree(directory_to_remove)
            
def print_title(message):
    print('#'*30 + f' {message} ' + '#'*30)

    
if __name__ == '__main__':
    
    remove_useless_directory()
    print_title('開始下載')
    driver = driver_setting()
    goto_grade_page()
    class_urls = collect_class_urls()
    class_ids = collect_class_ids(class_urls)
    homework_pages = collect_homework_page(class_ids)
    download_homeworks(homework_pages)
    remove_empty_directory()
    driver.quit()
    print_title('結束下載')
    