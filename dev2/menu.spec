# -*- mode: python -*-
a = Analysis(['menu.py'],
             pathex=['C:\\Users\\splee_000\\Documents\\Python Scripts\\game_dev\\dev2'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='menu.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
