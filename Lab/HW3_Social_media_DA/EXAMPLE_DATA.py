# File này chứa ví dụ dữ liệu mạng xã hội đơn giản
# Để test notebook, bạn có thể uncomment một trong các example dưới đây

## EXAMPLE 1: Mạng bạn bè đơn giản (20 người)
# Các cột: source, target (không có hướng)

"""
source,target
Alice,Bob
Alice,Charlie
Alice,David
Bob,Charlie
Bob,Eve
Charlie,David
Charlie,Frank
David,Eve
David,Grace
Eve,Frank
Eve,Henry
Frank,Grace
Frank,Ivy
Grace,Henry
Grace,Jack
Henry,Ivy
Henry,Kate
Ivy,Jack
Ivy,Laura
Jack,Kate
Kate,Laura
Laura,Alice
Laura,Bob
"""

## EXAMPLE 2: Mạng theo dõi (có hướng)
# follower -> followed

"""
source,target
User1,User2
User1,User3
User2,User3
User2,User4
User3,User4
User3,User5
User4,User5
User4,User6
User5,User6
User5,User1
User6,User1
User6,User2
"""

## EXAMPLE 3: Mạng cộng đồng (groups)

"""
source,target
Group_Tech,Group_AI
Group_Tech,Group_Programming
Group_AI,Group_ML
Group_AI,Group_DL
Group_ML,Group_DL
Group_ML,Group_DataScience
Group_DL,Group_CV
Group_DL,Group_NLP
Group_Programming,Group_Python
Group_Programming,Group_Java
Group_Python,Group_DataScience
Group_DataScience,Group_ML
"""

## EXAMPLE 4: Mạng tin nhắn (có trọng số)

"""
source,target,weight
User1,User2,10
User1,User3,5
User2,User3,15
User2,User4,8
User3,User4,12
User3,User5,7
User4,User5,20
User4,User6,6
User5,User6,18
User5,User1,9
"""

## Hướng dẫn sử dụng:
## 1. Copy một trong các example trên
## 2. Paste vào file mới (vd: my_network.csv)
## 3. Trong notebook, uncomment phần đọc file CSV:
##    edges_df = pd.read_csv('my_network.csv')
##    G = nx.from_pandas_edgelist(edges_df, source='source', target='target')

## Hoặc nếu có trọng số:
##    G = nx.from_pandas_edgelist(edges_df, source='source', target='target', 
##                                edge_attr='weight')

## Hoặc nếu có hướng:
##    G = nx.from_pandas_edgelist(edges_df, source='source', target='target', 
##                                create_using=nx.DiGraph())
