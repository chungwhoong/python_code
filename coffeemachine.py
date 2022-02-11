coffee=10
price=300

while True:
  print("="*100)
  print("커피자동머신입니다.")
  print("커피가격: 300원")
  print(f'남은 커피: {coffee}')
  print("="*100)
  money=int(input("돈을 넣어주세요: "))
  if money>price:
    print(f'거스름돈 {money-price}원 받으세요. 커피가 곧 나옵니다.')
    coffee-=1

  elif money==price:
    print('커피가 곧 나옵니다.')
    coffee-=1
    
  else:
    print(f'잔돈이 부족합니다. 다시 {money}원 돌려드립니다.')
     
  if not coffee:
    print("모든 커피가 소진되었습니다. 죄송합니다.")
    break
  
  print(f'남은 수랑: {coffee}')