#! python3
# backuptozip.py - copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os
def backupToZip(folder):
        # Backup the entire contents of "folder" into a Zip file.

        folder = os.path.abspath(folder) # make sure folder is absolute

        # figure out the filename this code should use based on
        # what files already exist.
        number = 1
        while True:
            zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
            if not os.path.exists(zipFilename):
                break
            number = number + 1

            # TODO: Create the ZIP file.

            # TODO: Walk the entire folder tree and compress the files in each
            # folder.
            for foldername, subfolders, filenames in os.walk(folder):
                print('Adding files in %s...' % (foldername))
                #add the current folder to the ZIP file.
                backupZip.write(foldername)
                #add all teh files in this folder to the ZIP file.
                for filename in filenames:
                    newBase = os.path.basename(folder) + '_'
                    if filename.startswith(newBase) and filename.endswith('.zip')
                        continue #don't backup the backup ZIP files
                    backupZip.write(os.path.join(foldername, filename))
            backupZip.close()
            print('Done.')

    backupToZip('C:\\Python27\\bacon_backup\\delicious')
