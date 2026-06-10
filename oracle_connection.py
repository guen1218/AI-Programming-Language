import oracledb

#데이터베이스 접속 정보 설정
dsn = "localhost:1521/FREE"
username = 'C##madang'
password = 'madang'
conflag = True # 접속상태 확인

try:
    print('데이터베이스 연결 준비')
    print(f'DSN: {dsn}')
    conn = oracledb.connect(user=username, password=password, dsn=dsn)
    print('데이터베이스 연결 성공')
    conflag = True
except Exception as e:
    print(f'연결 실패 {e}')
    print(f'oracle연결 중, username, password, dsn(서비스명) 확인 필요')
    conflag = False

if conflag:
    try:
        cursor = conn.cursor()
        sqlstring = 'select * from Book'
        cursor.execute(sqlstring)
        data = cursor.fetchall()

        print('='*50)
        print('테이블 조회 결과')
        print('='*50)
        print('bookid','bookname', 'publisher', 'price')
        for row in data:
            print(row[0],row[1],row[2],row[3])
        cursor.close()
        conn.close()
    except Exception as e:
        print(f'데이터 조회 중 문제 발생 {e}')