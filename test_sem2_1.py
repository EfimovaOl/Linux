from sem import checkout
from sem import check_hash_crc32

folderin = "/home/user/tst"
folderout = "/home/user/out"
folderext = "/home/user/folder1"


#test1
def test_step1():
    assert checkout("cd {folderin}; 7z a {folderout}/arx2", "Everything is Ok"), "test1 FAIL"
#test2
def test_step2():
    assert checkout("cd {folderout}; 7z e arx2.7z -o{folderext} -y", "Everything is Ok"), "test2 FAIL"
#test3
def test_step3():
    assert checkout("cd {folderout}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"
#test4
def test_step4():
    assert checkout("cd {folderout}; 7z d arx2.7z", "Everything is Ok"), "test4 FAIL"
#test5
def test_step5():
    assert checkout("cd {folderin}; 7z u {folderout}/arx2.7z", "Everything is Ok"), "test5 FAIL"
#test6
def test_check_archive():
    res1 = checkout("cd {folderin}; 7z a {folderout}/arx2", "Everything is Ok")
    res2 = checkout("ls {folderout}", "arx2.7z")
    assert res1 and res2, "test_check_archive FAIL"

#test7
def test_nonemply_archive():
    assert checkout("cd {folderout}; 7z l arx2.7z", "2 files"), "test_check_archive FAIL"

#test8
def test_check_list_archive():
    res_tst1 = checkout("cd {folderout}; 7z l arx2.7z", "tst1")
    res_tst2 = checkout("cd {folderout}; 7z l arx2.7z", "tst2")
    assert res_tst1 and res_tst2, "test_check_list_archive FAIL"

def test_scheck_hash():
    hash_crc32 = check_hash_crc32("cd {folderout}; crc32 arx2.7z")
    res_upper = checkout("cd {folderout}; 7z h arx2.7z", hash_crc32.upper())
    res_lower = checkout("cd {folderout}; 7z h arx2.7z", hash_crc32.lower())
    assert res_upper or res_lower, "NO equal hash"
