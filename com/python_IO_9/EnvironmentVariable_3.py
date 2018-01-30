# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
import os
print(os.environ)

# 输出 environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\admin\\AppData\\Roaming',
# 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (
# x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-UKQ7RTS',
# 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer',
# 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\admin', 'JAVA_HOME':
# 'C:\\Java\\jdk1.7.0_80', 'LOCALAPPDATA': 'C:\\Users\\admin\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-UKQ7RTS',
# 'MAVEN_HOME': 'D:\\maven\\maven3', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:\\Users\\admin\\OneDrive',
# 'OS': 'Windows_NT', 'PATH': 'F:\\python\\Scripts\\;F:\\python\\;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Windows
# \\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;D:\\mysql\\bin
# ;D:\\Git\\cmd;D:\\maven\\maven3\\bin;C:\\Java\\jdk1.7.0_80\\bin;D:\\sql\\bin', 'PATHEXT':
# '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW', 'PROCESSOR_ARCHITECTURE': 'AMD64',
# 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 42 Stepping 7, GenuineIntel', 'PROCESSOR_LEVEL': '6',
# 'PROCESSOR_REVISION': '2a07', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(
# X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH':
# 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\;C:\\Program Files\\Intel\\', 'PUBLIC':
# 'C:\\Users\\Public', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH':
# 'D:\\PycharmProjects\\studyPython', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:',
# 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\admin\\AppData\\Local\\Temp',
# 'TMP': 'C:\\Users\\admin\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-UKQ7RTS', 'USERDOMAIN_ROAMINGPROFILE':
# 'DESKTOP-UKQ7RTS', 'USERNAME': 'admin', 'USERPROFILE': 'C:\\Users\\admin', 'WINDIR': 'C:\\Windows'})

# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('JAVA_HOME'))  # 输出 C:\Java\jdk1.7.0_80






