# 여기서부터 firebase 연결
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

# 공지 구분자는 '???'로 설정

# Firebase database 인증 및 앱 초기화
cred = credentials.Certificate("pleasedothat-f843e-firebase-adminsdk-fut4j-e7d1463897.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://pleasedothat-f843e-default-rtdb.firebaseio.com/'
})
# ref = db.reference() # 기본 위치 지정 realtime firebase
db = firestore.client() # firestore firebase settings

# 여기까지 파이어베이스 연결

# 텍스트 파일로 저장되어 있는 공지 정보를 firebase에 업로드
# 공지 번호와 제목이 포함된 파일
f = open("noti.txt", "rt")
 # 공지 세부 내용이 포함된 파일
con_f = open("noti_final.txt", "rt")

cnt = 0
noti = ""
noti_title = ""
content = ""

while True:
    # 공지 내용 담는 변수 초기화
    content = ""
    temp = f.readline()

    # 번호랑 제목만 업로드하는 코드
    if cnt % 2 == 0:
        noti = temp
        print(noti, end='')
        cnt = cnt + 1
    else:
        noti_title = temp
        print(noti_title, end='')
        cnt = cnt + 1

    if temp == "":
        break

    # 한 줄씩 읽어 내용을 넣는다.
    con_temp = con_f.readline()
    # 만약, 문장이 내용 구분자인 "---"로 시작한다면?
    if con_temp.startswith("???"):
        continue
    else:
        # 만약, 문장이 내용 구분자인 "---"로 시작하지 않는다면? (즉, 우리가 필요로하는 공지 세부 내용이라면?)
        while True:
            # 만약, 필요로하는 공지 세부 내용이 끝났음을 알리는 구분자가 읽힐 경우
            if (con_temp.startswith("???")):
                break
            else:
                # 아직 필요로하는 공지 세부 내용이 끝나지 않았다면, 
                # # 한 줄씩 읽어 내용을 넣는다.
                con_temp = con_f.readline()
                
                if (con_temp.startswith("???")):
                    continue
                # 기존의 content에 해당 한 줄을 추가한다.
                content += con_temp   

    # 일반 공지 게시판에 해당하는 내용일 경우 -> general
    doc_ref = db.collection(u'general').document(noti)
    doc_ref.set({
        # 해당 공지 번호에 해당하는 공지의 제목과 세부 정보 내용을 DB에 업로드
        u'title': noti_title,
        u'content':content,
    })

f.close()
con_f.close()