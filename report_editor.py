#일부 문자 바꾸어서 저장하기
from encodings import utf_8


while True:
  report=input("수정할 문서명을 입력하세요(-1 입력시 종료): ")

  if report=='-1': break
  
  report=report+".txt"
  print(f'문서명: {report}')

  with open(report, 'rt', encoding='cp949') as f1: 
    data=f1.read()
    print("기존문서")
    print('-'*100)
    print(data)
    print('\n')

    old=input('바꾸고 싶은 문자열을 입력하세요: ')
    new=input('바꿀 문자열을 입력하세요: ')
    print('\n')

  newdata=data.replace(old, new)
  print("수정된 문서")
  print('-'*100)
  print(newdata)
  print('\n')

  with open(report, 'wt', encoding='cp949') as f2:
    f2.write(newdata)
    print('\n')