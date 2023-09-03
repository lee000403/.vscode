import numpy as np

def array_info(array):
    print(array)
    print("ndim : ", array.ndim) # 몇차원인지 int 정수로 알려준다.
    print("shape : ", array.shape) # 5개의 엘리먼트가 있다는 것을 알려준다.
    print("dtype : ", array.dtype) # 정수인지 알려준다.
    print("size : ", array.size) # 5개의 엘리먼트 개수를 알려준다.
    print("item size : ", array.itemsize) # 한개의 엘리먼트 바이트를 알려준다. (4 바이트인 것을 알려준다.)
    print("nbytes : ", array.nbytes) # 전체 바이트를 알려준다.
    print("strides : ", array.strides) # 다음 차원으로 넘어가는데 필요한 바이트를 알려준다.

a1 = np.array([1,2,3,4,5])
a2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
a3 = np.array([ [[1,2,3], [4,5,6], [7,8,9]],  # 3차원 배열
                [[1,2,3], [4,5,6], [7,8,9]],
                [[1,2,3], [4,5,6], [7,8,9]] ])
array_info(a3)
