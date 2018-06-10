# coding=utf-8
import os
import shlex
from tempfile import gettempdir

from sh import inkscape, pdfseparate, convert


def extract_pages_from_pdf(input_filename):
    tmp_path = gettempdir()
    pdfseparate(input_filename, '{}/%d.pdf'.format(tmp_path))
    return [
        os.path.join(tmp_path, f) for f in os.listdir(tmp_path)
        if os.path.isfile(os.path.join(tmp_path, f)) and f.endswith('.pdf')
    ]


def extract_image_from_pdf(input_filename, output_dir, dpi=300):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    filename, _ = os.path.splitext(os.path.basename(input_filename))
    output_filename = os.path.join(output_dir, '{}.png'.format(filename))
    inkscape(shlex.split('''\
    -f {} --export-area-drawing --export-png={} --export-background=#FFFFFF --export-dpi={}
    '''.format(
        input_filename,
        output_filename,
        dpi,
    )))
    return output_filename


def add_border_to_image(input_filename, width=10):
    convert(shlex.split('{0}  -bordercolor White -border {1}x{1} {0}'.format(
        input_filename,
        width,
    )))
