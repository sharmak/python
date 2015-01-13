def bold(fn):
    def wrap_fn(*args,**kwargs):
        return "<b> "  + fn(*args, **kwargs) + "</b>"
    def recompute(*args, **kwargs):
        import pdb;pdb.set_trace();
        return fn(*args, **kwargs)
    wrap_fn.recompute = recompute
    return wrap_fn
@bold
def hello():
    return "Hello"
class MyFoo(object):
    @classmethod
    @bold
    def test(cls):
        return "test"
print MyFoo.test()
print MyFoo.test.recompute(MyFoo)
