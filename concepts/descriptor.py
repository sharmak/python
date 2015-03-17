
# coding: utf-8

# In[8]:

class NoisyDescriptor(object):
    def __get__(self, obj, cls):
        print("Self %s" %str(self))
        print("Obj %s" %str(obj))
        print("Cls %s" %str(cls))
        # set the attribute des so that
        # next time when we acess the attribute *des*
        # we don't have to touch des
        setattr(obj, 'des', 'test')


# In[10]:

class Test(object):
    des = NoisyDescriptor()
    
t = Test()
print(t.__dict__)
print(Test.__dict__)
t.des
print(t.__dict__)
t.des


# In[17]:

def expensive_computation():
    print("Doing expensive computation")
    return (1,2,3)
class LazyProperty(object):
    def __init__(self, method):
        self.method  = method
    def __get__(self, obj, cls):
        value = expensive_computation()
        setattr(obj, self.method.__name__, value)
        return value

class MyLazyTest(object):
    def __init__(self):
        self._res = None
    @LazyProperty
    def res(self):
        return self._res
    
        
m = MyLazyTest()
print(m.res)
print(m.res)


# In[23]:

class SesitiveInfo(object):
    def __init__(self, info_name):
        self.info_name = info_name
    def password(self):
        return "abcd"
    def read(self):
        print("Calling sensitive info ")
        print("kishor sharma")
class Info(object):
    def __init__(self, info):
        self.info = info
        self.ses_info = SesitiveInfo("info")
    def get_info(self):
        passwd = raw_input('enter password')
        if passwd == self.ses_info.password():
            print("Access granted")
        else:
            raise ValueError("Permission Denied")
        return self.ses_info.read()
    
i = Info("test")
i.get_info()
    


# In[ ]:


