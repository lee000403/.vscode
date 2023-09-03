import numpy as np

# 배열 입출력
# np.save(): Numpy 배열 객체 1개를 파일에 저장, 파일종류: 바이너리
# np.saves() : Numpy 배열 객체 여러개를 파일에 저장 종류: 바이너리
# np.load() : 저장 파일로부터 객체 로딩

a2 = np.random.randint(1, 10, size=(5, 5))
print(a2)
np.save("a", a2) # 첫번째에는 파일명, 두번째는 저장하는 배열
# 저장한 파일을 보려면 ls로 확인

b2 = np.random.randint(1, 10, size=(5, 5))
print(b2)
np.savez("ab", a2, b2) # 여러개 배열 저장

npy = np.load("a.npy") # 파일 불러오기, 배열 하나는 .npy로 저장된다.
print(npy)

npz = np.load("ab.npz") 
print(npz.files) # filez 는 npz 안에 파일이 몇개 있는지 볼 수 있다.
print(npz['arr_0'])
print(npz['arr_1'])

# csv를 통한 savetxt, loadtxt 사용
print(a2)
np.savetxt("a.csv", a2, delimiter=',') # csv 는 구분자(delimiter) 꼭 사용

csv = np.loadtxt("a.csv", delimiter=",") # load 할 때도 구분자(delimiter) 꼭 사용
print(csv)

print(b2)
np.savetxt("b.csv", b2, delimiter=',', fmt="%.2e", header='c1, c2, c3, c4, c5')
csv = np.loadtxt("b.csv", delimiter=',')
print(csv)