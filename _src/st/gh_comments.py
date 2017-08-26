# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''base PyGithub/PyGithub: Typed interactions with the GitHub API v3
    https://github.com/PyGithub/PyGithub
grasp all comments from point repo.

core flow:
user->orig->repo->comments:
    -> path/line/comments -> data
        <- get_file_contents()
            -> .pkl save
            -> markdown
'''
__author__ = 'Zoom.Quiet'
__license__ = 'MIT@2017-03'
VERSION = "gh_comments v17.4.7.0009"

import os
import sys
import time
import base64
import cPickle as pickle

from github import Github

def main(usr, passwd, orig, repo):
    print usr, passwd, orig, repo
    gh = Github(usr, passwd)
    print gh
    _orig = gh.get_organization(orig)
    print _orig
    _repo = _orig.get_repo(repo)
    print _repo
    
    _comments = cc2dict(_repo)


def cc2dict(_repo):
    '''grasp gh repo all comments as dict
    base: CommitComment — PyGithub 1.25.2 documentation 
    http://pygithub.readthedocs.io/en/latest/github_objects/CommitComment.html
    {'path':{
        'line':[[commit_id,login,body]
                ,,,]
            ,,,
            }
        ,,,
        }
    '''
    _dict = {}
    _comments = _repo.get_comments()
    for c in _comments:
        _uname = ""
        if c.user.name:
            print c.user.name
            _uname = c.user.name
        else:
            print c.user.login
            _uname = c.user.login
        #print c.commit_id
        print c.created_at
        #print c.position
        print c.path,":",c.line
        print c.body
        #cc_key = "%s:%s"%(c.path, c.line)

        _item = [c.commit_id, _uname, c.created_at, c.body]

        if c.path not in _dict:
            _dict[c.path] = {}
            _dict[c.path][c.line] = []
        else:
            if c.line not in _dict[c.path]:
                _dict[c.path][c.line] = []

        _dict[c.path][c.line].append(_item)

    pickle.dump(_dict, open('%s_ccomments.pkl'%repo , 'wb'))
    print "dump data as %s"% '%s_ccomments.pkl'%repo
    print "gen. by {%s}"% VERSION
    return _dict


if __name__ == '__main__':
    if 5 != len(sys.argv) :
        print '''Usage:
$ gh2gc4_comments.py [user] [pass] [组织] [仓库]
    比如要提取: https://github.com/GC4WP/S08E01
    则是
$ gh2gc4_comments.py 用户 口令 GC4WP S08E01
        '''
    else:
        usr = sys.argv[1]
        passwd = sys.argv[2]
        orig = sys.argv[3]
        repo = sys.argv[4]
        main(usr, passwd, orig, repo)
