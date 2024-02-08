import shutil

cnt = 529;

for k in range(78):
    for i in range(24):
        oldname = "{j}.jpeg".format(j = str(i + 1))
        name = "{j}.jpeg".format(j = str(cnt))
        shutil.copy(oldname, name)
        cnt = cnt + 1
