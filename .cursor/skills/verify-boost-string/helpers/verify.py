#!/usr/bin/env python3
import argparse,json,os,pathlib,shutil,subprocess,tempfile
root=pathlib.Path(__file__).resolve().parents[4]
p=argparse.ArgumentParser();p.add_argument('mode',choices=['doctor','drive']);p.add_argument('--out',default='.verification-evidence/boost');p.add_argument('--include',default=os.environ.get('BOOST_INCLUDE',''));a=p.parse_args();out=pathlib.Path(a.out).resolve();out.mkdir(parents=True,exist_ok=True)
r={'mode':a.mode,'ok':False,'checks':[]};run=None
try:
 cxx=os.environ.get('CXX','g++');assert shutil.which(cxx),'Missing compiler '+cxx;assert shutil.which('make'),'Missing make'
 include=pathlib.Path(a.include) if a.include else pathlib.Path('/usr/include');assert (include/'boost/algorithm/string.hpp').is_file(),'Missing Boost headers: set BOOST_INCLUDE or --include to the directory containing boost/'
 assert (root/'hello_world.cpp').is_file() and (root/'Makefile').is_file(),'Wrong source';r['checks'].append({'doctor':'compiler/make/Boost headers/source found','compiler':cxx,'boost_include':str(include)})
 if a.mode=='drive':
  before=subprocess.run(['git','status','--porcelain'],cwd=root,text=True,capture_output=True,check=True).stdout
  with tempfile.TemporaryDirectory(prefix='boost-string-verify-') as td:
   command=['make','-B','-f',str(root/'Makefile'),'main','CXX='+cxx,'CXXFLAGS=-I'+str(include),'SRCS='+str(root/'hello_world.cpp'),'HEADERS=']
   build=subprocess.run(command,cwd=td,capture_output=True,text=True,timeout=30);(out/'build.log').write_text(build.stdout+build.stderr);assert build.returncode==0,'Build failed, see build.log'
   for n in range(2):
    run=subprocess.run([str(pathlib.Path(td)/'main')],capture_output=True,text=True,timeout=5);r['checks'].append({'run':n+1,'exit':run.returncode,'stdout':run.stdout,'stderr':run.stderr});assert run.returncode==0 and run.stdout=='HELLO, WORLD!\n' and run.stderr=='','Uppercase contract failed'
  after=subprocess.run(['git','status','--porcelain'],cwd=root,text=True,capture_output=True,check=True).stdout;assert before==after,'Verification changed tracked/untracked state';r['checks'].append({'cleanup':'owned temporary build removed; source git status unchanged'})
 r['ok']=True
except Exception as e:r['failure']=str(e)
(out/(a.mode+'.json')).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r));raise SystemExit(0 if r['ok'] else 1)
