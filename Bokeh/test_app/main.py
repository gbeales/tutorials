# test_app

# system-level imports
import base64
import os

# 3rd-party module imports
import numpy as np
import imageio as img

# bokeh imports
from bokeh.io import show
from bokeh.layouts import column, row
from bokeh.models import (
    Button, CustomJS, FileInput,  ImageRGBA,
    ColumnDataSource, CDSView, IndexFilter, Slider
)
from bokeh.plotting import figure, curdoc

# create figure to show the image
img_fig = figure(
    x_range=(0, 10), y_range=(0, 10),
    plot_width=400, plot_height=400,
    toolbar_location='above',
    tools="hover, pan, reset, wheel_zoom, box_zoom")


input_test_img = img.imread("Bokeh//test_app//static//frame(30)_1.bmp")
input_test_img = np.ascontiguousarray(
            np.flipud(
                np.stack(
                (input_test_img[..., 0], input_test_img[...,1],
                    input_test_img[..., 2], np.ones_like(input_test_img[...,0])*255),
                axis=-1
                )
            ),
            dtype=np.uint8
        ).view(dtype=np.uint32).reshape((input_test_img.shape[0], input_test_img.shape[1]))


# create data sources
source = ColumnDataSource(
    data=dict(
        image=[input_test_img],
        start_x=[0], start_y=[0],
        width=[10], height=[10])
)
view = CDSView(source=source, filters=[IndexFilter([0])])
# view_callback_js = CustomJS(
#     args=dict(),
#     code="""
#         var filter = this[0]
#         console.log('filter_ind: value=' + filter.indices[0])
#     """
# )
# view.js_on_change('filters', view_callback_js)

# create plot
img_plot = img_fig.image_rgba(
    source=source, view=view,
    image='image',
    x='start_x', y='start_y',
    dw='width', dh='height',
    global_alpha=255
    )
# img_plot.js_on_change('view', view_callback_js)

# make image function
def add_image(img_loc, CDS: ColumnDataSource, filename: str):
    # import and format for ImageRGBA model
    with open(filename, "wb") as fh:
        fh.write(base64.urlsafe_b64decode(img_loc))

    input_img = img.imread(filename)
    os.remove(filename)
    input_img = np.ascontiguousarray(
        np.flipud(
            np.stack(
                (input_img[..., 0], input_img[...,1],
                    input_img[..., 2], np.ones_like(input_img[...,0])*255),
                axis=-1
                )
            ),
            dtype=np.uint8
    ).view(dtype=np.uint32).reshape((input_img.shape[0], input_img.shape[1]))

    # append to CDS 
    source.stream(new_data={
        'image': [input_img],
        'start_x': [0], 'start_y': [0],
        'width': [10], 'height': [10]
    })

# make the slider handler
def slider_handler(attr, old, new):
    # view.filters[0] = IndexFilter([new])
    # print(view.filters[0])
    img_plot.view = CDSView(source=source, filters=[IndexFilter([new])])

# make the handler itself
def file_handler(attr, old, new):
    add_image(new, source, filepicker.filename)
    ind = img_plot.view.filters[0].indices
    img_plot.view = CDSView(source=source, filters=[IndexFilter(ind)])
    # print(source.to_df().head())

# Make the file picker
filepicker = FileInput(
    accept="image/*",
    multiple=False)
filepicker.on_change('value', file_handler)

# Make the slider
slider = Slider(start=0, end=1, value=0, step=1, title="Image")
slider.on_change('value', slider_handler)
slider_handler_js = CustomJS(
    args=dict(source=source, view=img_plot.view, filter=img_plot.view.filters[0]),
    code="""
        console.log('range_slider: value=' + this.value, this.toString())
        filter.indices = [this.value]
        //console.log('filter_ind: value=' + filter.indices[0])
        source.change.emit()
        view.change.emit()
        filter.change.emit()
    """
    )
# slider.js_on_change("value", slider_handler_js)

left_col = column(img_fig, slider)
layout = row(left_col, filepicker)

curdoc().add_root(layout)