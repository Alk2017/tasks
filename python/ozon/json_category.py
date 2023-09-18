import json
import functools

ID = 'id'
NAME = 'name'
PARENT = 'parent'
NEXT = 'next'


def insert(parent, cat):
    if cat[PARENT] == parent[ID]:
        parent[NEXT].append(dict(id=cat[ID], name=cat[NAME], next=[]))
    else:
        for ch in parent[NEXT]:
            insert(ch, cat)


def insert_by_id(id_dict, cat):
    if cat[ID] in id_dict.keys():
        cat[NEXT] = id_dict[cat[ID]]
    if len(cat[NEXT]) != 0:
        for subcat in cat[NEXT]:
            insert_by_id(id_dict, subcat)

def run():
    res = []
    for _ in range(int(input())):
    # for _ in range(1):
        js_line = ''
        for _ in range(int(input())):
        # for _ in range(1):
            js_line += input()
            # js_line += '''[
            #     {"id":566,"name":"all"},
            #     {"id":465,"name":"clothes","parent":435},
            #     {"id":768,"name":"shoes","parent":435},
            #     {"id":435,"name":"sneakers","parent":566}
            # ]'''
        js = json.loads(js_line)
        # size = len(js)
        id_dict = dict()
        head = None
        # actua_id = 0
        for cat in js:
            if PARENT not in cat.keys():
                head = cat
            else:
                if cat[PARENT] in id_dict.keys():
                    id_dict[cat[PARENT]].append(
                        dict(id=cat[ID], name=cat[NAME], next=[]))
                else:
                    id_dict[cat[PARENT]] = [
                        dict(id=cat[ID], name=cat[NAME], next=[])]
        insert_by_id(id_dict, head)
        res_c = head
        # js.sort(key=lambda c: (c[PARENT], c[ID]))
        # a = sorted(js, key=functools.cmp_to_key(comp))
        # for cat in js:
        #     if cat[PARENT] == -1:
        #         res_c[ID] = cat[ID]
        #         res_c[NAME] = cat[NAME]
        #         res_c[NEXT] = []
        #     else:
        #         insert(res_c, cat)
        res.append(res_c)
    print(json.dumps(res))


if __name__ == '__main__':
    run()
