import os
from glob import glob
import argsparse

class wiki(object):

    def __init__(self):
        docs_dir=self.docs_dir
        dirs=[]
        mds=[]
        for dirpath, dirnames, filenames in os.walk(docs_dir):
            for dir in dirnames:
                dirs.append(os.path.join(dirpath,dirnames))
            for file in filenames:
                if filenames[-3:] == '.md'
                    filenames.append(filenames)

    def make_dirs(self):
        for md in filenames:
            if md[:-3] not in dirs:
                os.mkdir(md[:-3])


    def make_mds(self):
        for dir in dirnames:
            if dir + '.md' not in mds:
                open ( dir + '.md', 'a').close()


if __name__ == "__main__":
    parser = argsparse.ArgumentParser(description="organizing function for wiki")
    parser.add_argument('-d', action="store",  dest="docs_dir"
                        default=os.path.join(os.getcwd(),"docs"),
                        required=True,type=str )

    args = parser.parse_args()
    wiki = wiki(args.docs_dir)
    wiki.make_dirs()
    wiki.make_mds()
