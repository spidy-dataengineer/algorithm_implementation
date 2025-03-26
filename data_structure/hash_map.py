hash_map = {} # 딕셔너리 자체가 해시맵과 거의 동일

# 키-값 추가
hash_map["apple"] = 5
hash_map["banana"] = 3

# 키 조회
print(hash_map.get("apple", 0))  # 5 (존재하지 않으면 기본값 0 반환)

# 키 삭제
del hash_map["banana"]

# 키 존재 여부 확인
print("banana" in hash_map)  # False
