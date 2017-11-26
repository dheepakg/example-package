if __name__ == '__main__':
    from time import strftime, gmtime
    suffix = strftime('%d%B%Y_%H%M%S', gmtime())
    file_name = 'upload_'+str(suffix)+'.dgv'

    write_to_file(system_details(),'w','upload.txt')