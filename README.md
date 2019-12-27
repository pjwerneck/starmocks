# starmocks

Implementing test functions with more than a few mocks quickly gets out of hand. `starmocks` allows you to reference all mocks by name, as a single parameter.

```python
@mock.patch('myapp.module.myclass.mymethod')
@mock.patch('myapp.module.myfunction')
@mock.patch('myapp.module.requests.post')
@mock.patch('os.path.exists')
@starmocks
def test_this(mocks):
    mocks.exists.side_effect = lambda: True
    mocks.post.return_value = Response()
```
