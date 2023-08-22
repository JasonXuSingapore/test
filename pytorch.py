import torch
a = torch.ones(3)
a[1]
float(a[1])
a[2] = 2
a
# 使用.zeros是获取适当大小的数组的一种方法
points = torch.zeros(6)
# 用所需的值覆盖这些0
points[0] = 1.0
points[1] = 4.0
points[2] = 2.0
points[3] = 1.0
points[4] = 3.0
points[5] = 5.0
points = torch.tensor([1.0, 4.0, 2.0, 1.0, 3.0, 5.0])
points
float(points[0]),float(points[1])
points = torch.tensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
points.shape
points=torch.zeros(3,2)
points
points=torch.FloatTensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
points[0,1]
points[0]
points = torch.tensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
#points.storage()
points_storage = points.storage()
points_storage[0] = 2.0
points.storage()[1]
points
second_point = points[1]
#print(second_point)
second_point.storage_offset()## 获取新张量的存储偏移量
second_point.size()
second_point.shape
points.stride()
second_point.storage_offset()
second_point.stride()
points=torch.FloatTensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
second_point = points[1].clone()
second_point[0] = 10.0
points_t=points.t()#转置
points_t
id(points.storage()) == id(points_t.storage())
points.stride()
points_t.stride()
some_tensor = torch.ones(3, 4, 5)
print(some_tensor)
some_tensor.shape
some_tensor.stride()## 获取张量的步幅
some_tensor_t=some_tensor.transpose(0, 2)
print(some_tensor_t)
some_tensor_t.shape,some_tensor_t.stride()
points.is_contiguous(), points_t.is_contiguous()
points = torch.tensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
print(points)
points_t = points.t()
print(points_t)
points_t.storage()# 获取张量的底层数据存储
points_t.stride()
points_t_cont = points_t.contiguous()
points_t_cont
points_t_cont.stride()
points_t_cont.storage()#重构