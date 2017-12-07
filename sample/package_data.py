def write_to_file(contents,mode,filename):
    import os
    os.chdir(os.path.dirname(__file__))
    file = open(filename,mode)
    file.write(contents)
    file.flush()
def system_details():
    import platform
    from time import gmtime, strftime
    import datetime

    time_now = str(datetime.datetime.now())
    time_zone = strftime("%Z", gmtime())
    computer_name = platform.node()
    processor = platform.processor()
    chipset = platform.uname()[4]

    os_family = platform.system()
    os_version = platform.release()
    os_release = platform.platform()

    details = processor+'|'+chipset+'|'+os_family+'|'+os_version+'|'+os_release+'|'+computer_name+'|'+time_now+'|'+time_zone
    return(details)