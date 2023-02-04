import os
import zipfile


class Col:

    @staticmethod
    def compress(file_names):
        path = os.getenv("PATH_FILE_ZIP")
        compression = zipfile.ZIP_DEFLATED
        zf = zipfile.ZipFile(os.getenv("ZIP_FILE_NAME"), mode="w")
        try:
            for file_name in file_names:
                zf.write(path + file_name, file_name, compress_type=compression)
            return 1
        except FileNotFoundError:
            print("An error occurred")
            return 0
        finally:
            zf.close()
