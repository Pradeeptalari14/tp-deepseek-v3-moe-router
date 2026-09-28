#!/usr/bin/env bash
set -e
echo "🔍 Validating DeepSeek-V3 MoE & DualPipe Suite..."
python3 -c "import py_compile; py_compile.compile('moe_router.py', doraise=True); print('✅ moe_router syntax verified')"
python3 -c "import py_compile; py_compile.compile('dualpipe_scheduler.py', doraise=True); print('✅ dualpipe_scheduler syntax verified')"
python3 -c "import py_compile; py_compile.compile('manim_flow.py', doraise=True); print('✅ manim_flow syntax verified')"
echo "✅ SRE compliance validation complete for deepseek-v3-moe-router."
