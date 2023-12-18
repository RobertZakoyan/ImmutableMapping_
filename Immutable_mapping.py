from collections.abc import Mapping, Sized, Iterable, Container


class ImmutableMapping(Mapping, Sized, Iterable, Container):
    def __init__(self,*args, **kwargs):
        self.data = dict(*args, **kwargs)

    def __contains__(self, key):
        if key in self.data:
            return True
        return False
    
    def __eq__(self, instance):
        if isinstance(instance, ImmutableMapping):
            return self.data == instance.data
        return False
    
    def __iter__(self):
        return iter(self.data)
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f'ImmutableMapping({self.data})'
    
    def keys(self):
        return self.data.keys()
    

    def values(self):
        return self.data.values()
    
    def items(self):
        return self.data.items()
    
    
if __name__ == "__main__":
    ImMap = ImmutableMapping([("Hello", "World")])
    try:
        ImMap["Hello"] = "Hajoxutyun"
    except:
        print("ImmutableMapping type is Immutable")