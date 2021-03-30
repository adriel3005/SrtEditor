# -*- mode: python -*-

block_cipher = None


a = Analysis(['E:\\DAD SRT Video\\SrtGenerator\\src\\main\\python\\main.py'],
             pathex=['E:\\DAD SRT Video\\SrtGenerator\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\anaconda3\\envs\\srt\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['E:\\DAD SRT Video\\SrtGenerator\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='myapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , version='E:\\DAD SRT Video\\SrtGenerator\\target\\PyInstaller\\version_info.py', icon='E:\\DAD SRT Video\\SrtGenerator\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='myapp')
