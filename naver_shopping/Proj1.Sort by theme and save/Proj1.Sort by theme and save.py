<<<<<<< HEAD
import time
import pyexcel as px
import os
import sys

#작업시작
print("Process start")

#시작 시간 기록
start_time = time.time()

#시스템 명령어로부터 원본 데이터 경로를 불러옵니다 
directory = sys.argv[1]

#출력 데이터를 저장할 폴더를 지정합니다. 폴더가 없다면 생성합니다.
out_dir = "merged_" + directory
if out_dir not in os.listdir():
    os.mkdir(out_dir)

#입력 파일의 파일명 목록을 불러옵니다
input_files = os.listdir(directory)

#헤더를 저장할 빈 리스트를 만듭니다
HEADERS = []

#엑셀파일의 내용을 저장할 빈 리스트를 만듭니다
CONTENTS = []

#input_files에 저장된 파일명을 하나씩 불러옵니다
for filename in input_files:
    #".xlsx"가 없는 파일을 건너뜁니다.
    if ".xlsx" not in filename:
        continue

    #filename에 해당하는 엑셀파일을 file이란 리스트에 불러옵니다.
    file = px.get_array(file_name=directory + "/" + filename)

    #header에 file 리스트의 첫번째 열, 즉, filename 엑셀파일의 헤더를 저장합니다
    header = file[0]

    #content에 filename 엑셀파일의 데이터를 저장합니다
    content = file[1:]

    #헤더가 기존에 없던 것이라면 아래 IF문이 작동합니다.
    if header not in HEADERS:
        #header를 HEADER 리스트에 추가합니다.
        HEADERS.append(header)
        #header를 ?리스트의 한 항목으로서? CONTENTS 리스트에 추가합니다
        CONTENTS.append([header])

    #header가 HEADERS의 몇번째에 위치하는 지 확인합니다
    index = HEADERS.index(header)

    #리스트에 데이터 값을 쌓습니다.
    CONTENTS[index] += content

#CONTENTS의 길이만큼(=헤더 종류 수 만큼) FOR문을 반복합니다
for i in range(len(CONTENTS)):
    #리스트를 엑셀파일로 저장합니다
    px.save_as(array=CONTENTS[i], dest_file_name=out_dir + "/" + str(i) + "_merged_File.xlsx")

#작업 종료
print("Process Done")

#종료 및 작업 시간 출력
end_time = time.time()
print("The job took" + str(end_time - start_time) + " seconds.")
=======
import time
import pyexcel as px
import os
import sys

#작업시작
print("Process start")

#시작 시간 기록
start_time = time.time()

#시스템 명령어로부터 원본 데이터 경로를 불러옵니다 
directory = sys.argv[1]

#출력 데이터를 저장할 폴더를 지정합니다. 폴더가 없다면 생성합니다.
out_dir = "merged_" + directory
if out_dir not in os.listdir():
    os.mkdir(out_dir)

#입력 파일의 파일명 목록을 불러옵니다
input_files = os.listdir(directory)

#헤더를 저장할 빈 리스트를 만듭니다
HEADERS = []

#엑셀파일의 내용을 저장할 빈 리스트를 만듭니다
CONTENTS = []

#input_files에 저장된 파일명을 하나씩 불러옵니다
for filename in input_files:
    #".xlsx"가 없는 파일을 건너뜁니다.
    if ".xlsx" not in filename:
        continue

    #filename에 해당하는 엑셀파일을 file이란 리스트에 불러옵니다.
    file = px.get_array(file_name=directory + "/" + filename)

    #header에 file 리스트의 첫번째 열, 즉, filename 엑셀파일의 헤더를 저장합니다
    header = file[0]

    #content에 filename 엑셀파일의 데이터를 저장합니다
    content = file[1:]

    #헤더가 기존에 없던 것이라면 아래 IF문이 작동합니다.
    if header not in HEADERS:
        #header를 HEADER 리스트에 추가합니다.
        HEADERS.append(header)
        #header를 ?리스트의 한 항목으로서? CONTENTS 리스트에 추가합니다
        CONTENTS.append([header])

    #header가 HEADERS의 몇번째에 위치하는 지 확인합니다
    index = HEADERS.index(header)

    #리스트에 데이터 값을 쌓습니다.
    CONTENTS[index] += content

#CONTENTS의 길이만큼(=헤더 종류 수 만큼) FOR문을 반복합니다
for i in range(len(CONTENTS)):
    #리스트를 엑셀파일로 저장합니다
    px.save_as(array=CONTENTS[i], dest_file_name=out_dir + "/" + str(i) + "_merged_File.xlsx")

#작업 종료
print("Process Done")

#종료 및 작업 시간 출력
end_time = time.time()
print("The job took" + str(end_time - start_time) + " seconds.")
>>>>>>> dea8f04f47c7d0f4fea00419f12e57d5b8e1d4c1
