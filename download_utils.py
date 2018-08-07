

def download_file(url, file_path):
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get('content-length'))
    try:
        with open(file_path, 'wb', buffering=16*1024*1024) as f:
            if tqdm:
                bar = tqdm.tqdm_notebook(total=total_size, unit='B', unit_scale=True)
                bar.set_description(os.path.split(file_path)[-1])

            for chunk in r.iter_content(32 * 1024):
                f.write(chunk)
                if tqdm:
                    bar.update(len(chunk))

            if tqdm:
                bar.close()
            else:
                print("File {!r} successfully downloaded".format(file_path))
    except Exception:
        print("Download failed")
    finally:
        if os.path.getsize(file_path) != total_size:
            os.remove(file_path)
            print("Removed incomplete download")
            
def download_from_github(version, fn, target_dir):
    url = "https://github.com/hse-aml/intro-to-dl/releases/download/{0}/{1}".format(version, fn)
    file_path = os.path.join(target_dir, fn)
    download_file(url, file_path)


def sequential_downloader(version, fns, target_dir):
    os.makedirs(target_dir, exist_ok=True)
    for fn in fns:
        download_from_github(version, fn, target_dir)

