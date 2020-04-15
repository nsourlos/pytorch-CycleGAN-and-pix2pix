import os
import glob
from PIL import Image
import shutil


def rename_photos(photos_dir):

    f = open("./scripts/eval_cityscapes/original_names.txt", "r")
    names = f.readlines()

    photo_expr = photos_dir + "/*_fake_B.png"
    photo_paths = glob.glob(photo_expr)
    photo_paths = sorted(photo_paths)

    savedir = photo_paths[0].rsplit('/', 1)[0] + '/original_names'
    os.makedirs(savedir, exist_ok = True)

    for i, photo_path in enumerate(photo_paths):
        num = int(photo_path.rsplit('_', 2)[0].rsplit('/', 1)[-1])

        # photos
        savepath = os.path.join(savedir, names[num].rsplit('/', 1)[-1].rsplit('\n', 1)[0])
        shutil.copy(photo_path, savepath)

        if i % (len(photo_paths) // 10) == 0:
            print("%d / %d: last image saved at %s, " % (i, len(photo_paths), savepath))

    f.close()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--photos_dir', type=str, required=True,
                        help='Path to the Cityscapes test results directory.')
    opt = parser.parse_args()

    print('Renaming photos')
    rename_photos(opt.photos_dir)

    print('Done')
