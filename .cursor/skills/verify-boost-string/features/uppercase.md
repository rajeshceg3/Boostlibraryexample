# Fixed-string uppercase CLI
## Sub-features
Boostalgorithm string uppercase, stdout and successful process exit.
## How to get to it (user POV)
Build hello_world.cpp with Boostheaders, then run compiled main. No input prompt, flags or configuration in product.
## Driving it with verify.py
Doctor dependency/source check, then drive forcebuilds the actual Makefile in a tempfile directory and invokes actual binary twice. Exact observed end state: HELLO, WORLD! followed by newline, no stderr, exit0. Temp binary disappears; proof remains.
## Gotchas
Shipped binary is Nix-loader-specific and not portable; rebuild source. Original Replit entrypoint named nonexistent main.cpp, corrected to actual hello_world.cpp. This is config-source correctness, not a tested Replit IDE session. Never clean/delete tracked main or caches. Missing local Boost/Clang is an environment prerequisite, not an app defect; runtime uses g++ override supported by Makefile.
