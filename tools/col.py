import zipfile
import zipfile


class Col:

    def compress(file_names):
        path = "./"
        compression = zipfile.ZIP_DEFLATED

        zf = zipfile.ZipFile("new file.zip", mode="w")
        try:
            for file_name in file_names:
                # Add file to the zip file
                # first parameter file to zip, second filename in zip
                zf.write(path + file_name, file_name, compress_type=compression)

        except FileNotFoundError:
            print("An error occurred")
        finally:
            zf.close()