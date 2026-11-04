---
name: verify-boost-string
description: Build and drive Boostlibraryexample's actual C++ uppercase CLI in an isolated temporary directory, preserving the shipped binary and editor cache.
---
# Verify Boost string example
## Launch
Primary surface is hello_world.cpp: Boost to_upper on a fixed Hello, World! string, stdout then exit. No server/input/auth. Repo Makefile requires make and C++ compiler; Replit uses Clang+Boost from replit.nix. For a Linux host install/use available Boost headers and set BOOST_INCLUDE to the directory containing boost/. Runtime proof used g++ and unpacked Ubuntu libboost1.74-dev1.74.0-14ubuntu3 in /tmp; system package install not required. Header version/OS differs from Replit, so Replit launch is not certified. Existing tracked main has a Nix-specific dynamic loader and must not be treated as portable or overwritten by proof. All builds below use a unique tempfile directory and actual repo Makefile/source with explicit SRCS.
## Doctor
`python3 .cursor/skills/verify-boost-string/helpers/verify.py doctor --include /tmp/boost-verification-runtime/usr/include --out .verification-evidence/boost`
Replace include with actual Boost header directory. CXX defaults to g++ or honors environment override. Read-only compiler/make/header/source check; does not execute shipped binary.
## Drive
`python3 .cursor/skills/verify-boost-string/helpers/verify.py drive --include /tmp/boost-verification-runtime/usr/include --out .verification-evidence/boost`
Force builds the actual source through Makefile in an owned temp directory, invokes resulting CLI twice, asserts exact uppercase stdout/newline, exit0 and empty stderr. No generic mock/internal setter. Feature map in features/README.md.
## Evidence
out/doctor.json, drive.json and build.log survive cleanup. JSON records actual stdout/exit/compiler/header path. A doctor/build failure is not a runtime pass. No arbitrary Unicode, interactive input, benchmark, browser or wider Boost coverage claimed.
## Cleanup
No child/server persists. tempfile context removes only owned compiled output after success or failure. Source git status must remain identical during drive. Never run make clean in repo, remove tracked main/.ccls-cache or delete proof. Unknown mode fails before mutation.
## Helpers
Executable helpers/verify.py uses Python3stdlib, make, compiler and Boostheaders. No pip/network in helper. If dependencies are missing, report/install in a private runtime before retrying. Do not replace actual Boost with a stub. Use /maintain-verification-skill when source changes.
