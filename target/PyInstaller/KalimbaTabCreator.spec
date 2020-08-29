# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/Tardis_Database/Desktop/kalimba/src/main/python/main.py'],
             pathex=['/Users/Tardis_Database/Desktop/kalimba/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/Tardis_Database/Desktop/kalimba-venv/lib/python3.6/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/Users/Tardis_Database/Desktop/kalimba/target/PyInstaller/fbs_pyinstaller_hook.py'],
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
          name='KalimbaTabCreator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/Tardis_Database/Desktop/kalimba/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='KalimbaTabCreator')
app = BUNDLE(coll,
             name='KalimbaTabCreator.app',
             icon='/Users/Tardis_Database/Desktop/kalimba/target/Icon.icns',
             bundle_identifier='com.cyoung.kalimbatabcreator')
