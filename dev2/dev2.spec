# -*- mode: python -*-
a = Analysis(['dev2.py'],
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
          name='dev2.exe',
          icon='icon.ico'
          debug=False,
          strip=None,
          upx=True,
          console=True )
