import pytest

#def test_one():
#    data=[1,2,3]
#    assert data==[1,2,3]

#def test_two():
#    data=[1,2,3]
#    assert len(data)==3

@pytest.fixture
def data():
    return [1,2,3]

def test_three(data):
    #data=[1,2,3]
    assert 2 in data
    print(data)

    def test_four(data):
        #data=[1,2,3]
        print(data)
        assert len(data)==3






























