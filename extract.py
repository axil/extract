import sys,re,os

def untgz(a):
    base='.'.join(a)
    if not os.access(base,os.F_OK):
        os.mkdir(base)
    os.system('bsdtar xzvf "%s" -C "%s"' % (name, base))

def untbz2(a):
    base='.'.join(a)
    if not os.access(base,os.F_OK):
        os.mkdir(base)
    os.system('bsdtar xjvf "%s" -C "%s"' % (name, base))

def check(a,ext):
    if a[len(a)-1]==ext:
        a.pop()
        return True
    else:
        return False

#import pdb
#pdb.set_trace()
name = sys.argv[1]
a=re.split('\.', name)
#print name
#a=re.search('(.*)\.([^.]*)',name)
n=len(a)
if n>1:
#    (base,ext)=a.groups()
    if check(a,'rar'): 
        os.system('rar x -ad "%s"' % name)
    elif check(a,'zip'):
        base='.'.join(a)
        if not os.access(base,os.F_OK):
            os.mkdir(base)
        os.chdir(base)
        os.system('pkzip25 -ext -dir -nozip "../%s"' % name)
    elif check(a, 'tgz'):
        untgz(a)
    elif check(a,'gz'):
        if check(a,'tar'):
            untgz(a)
        else:
            os.system('gunzip %s' % name)
    elif check(a,'tbz2') or check(a,'bz2') and check(a,'tar'):
        untbz2(a)
    else:
        exit('unknown extension')
else:
    exit('no extension')

