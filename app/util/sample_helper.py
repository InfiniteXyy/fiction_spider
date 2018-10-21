from app.model.connection import my_db

books = my_db["books"]
if "chapters" not in my_db.list_collection_names():
    print("create collection books")
    my_db.create_collection("books")

BOOKS = [
    {"title": "剑灵同居日记", "author": "国王陛下", "rate": 5, "info": "第117章「仅供学习使用！仅供学习使用！」",
     "img_src": "http://yue07.sogoucdn.com/cdn/image/book/6840504077_1505815165607.jpg", "url": "jianling"},
    {"title": "逆天邪神", "author": "火星引力", "rate": 5, "info": "第117章「仅供学习使用！仅供学习使用！」",
     "img_src": "http://book.img.ireader.com/group6/M00/4C/57/CmQUN1Yva1aEF6ETAAAAALd7CA4139470213.jpg?v=38BPLxRI",
     "url": "xieshen"},
    {"title": "网游之修罗传说", "author": "火星引力", "rate": 4, "info": "第117章「仅供学习使用！仅供学习使用！」",
     "img_src": "http://pic.baike.soso.com/p/20100703/bki-20100703183017-2018209783.jpg", "url": "xiuluo"},
    {"title": "圣物星辰", "author": "乱世狂刀", "rate": 3, "info": "第117章「仅供学习使用！仅供学习使用！」",
     "img_src": "https://ss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/boxapp_novel/wh%3D267%2C357/sign=5d1d2a7e5b4e9258a6618eecaab5fd6b/023b5bb5c9ea15ce62ed2213bb003af33a87b2ad.jpg",
     "url": "shengwu"},
    {"title": "龙族", "author": "江南", "rate": 5, "info": "第117章「仅供学习使用！仅供学习使用！」",
     "img_src": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1539708719589&di"
                "=5e730e3963f3673a135ba756f80eb2e5&imgtype=0&src=http%3A%2F%2Fgss0.baidu.com%2F"
                "-fo3dSag_xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%2F77c6a7efce1b9d16ab1299d4f1deb48f8d5464a9.jpg",
     "url": "longzu"},
]

if __name__ == '__main__':
    for i in BOOKS:
        if not books.find_one({"title": i["title"]}):
            books.insert_one(i)
            print(i["title"], "插入")

        else:
            print(i["title"], "已存在")
