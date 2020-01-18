# starmocks

Implementing test functions with more than a few mocks quickly gets out of hand. `starmocks` allows you to reference all mocks by name, as a single parameter.

## Installing
```
pip install starmocks
```

## Usage

Just place the `starmocks` decorator after the mocks you want to group.


```python

from starmocks import starmocks


@mock.patch('myapp.module.myclass.mymethod')
@mock.patch('myapp.module.myfunction')
@mock.patch('myapp.module.requests.post')
@mock.patch('os.path.exists')
@starmocks
def test_this(mocks):
    mocks.exists.side_effect = lambda: True
    mocks.post.return_value = Response()
```
