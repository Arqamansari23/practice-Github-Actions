from src.maths_operation import add,sub



def test_add():
    assert add(1,2)==3
    assert add(2,3)==5

def test_sub():
    assert sub(2,1)==1
    assert sub(2,2)==0

    

