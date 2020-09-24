#%% Imports
from bokeh.io import show
from bokeh.models import Button, CustomJS, FileInput, layouts
# %%
# Make our button

# def button_clicked():
#     print("button clicked!")

button = Button(label='Run', button_type='primary')
button.js_on_click(CustomJS(
    code="console.log('button: click!', this.toString())"))
# button.on_event(button_clicked)

# show(button)
# %%
# Make the file picker
filepicker = FileInput(
    accept="image/*",
    multiple=True)


# %%
# Import image and make image plot
import imageio as img
from bokeh.models import ImageRGBA, ColumnDataSource, CDSView, IndexFilter
from bokeh.plotting import figure
import numpy as np

def prep_img(image):
    image = np.stack(
        (image[..., 0], image[..., 1], image[..., 2], np.ones_like(image[:,:,0])*255),
        axis=-1
        )
    return np.flipud(image)    # because Bokeh made poor choices


input_img = prep_img(
    img.imread("C:\\Users\\gbeales\\Downloads\\frame(0)_2.bmp")
    )
input_img2 = prep_img(
    img.imread("C:\\Users\\gbeales\\Downloads\\frame(0)_1.bmp")
    )
data = {
    'image': [input_img, input_img2],
    'start_x': [0, 0],
    'start_y': [0, 0],
    'width': [10, 10],
    'height': [10, 10]
    }
source = ColumnDataSource(data=data)
view = CDSView(source=source, filters=[IndexFilter([1])])
p = figure(
    plot_width=input_img.shape[1], plot_height=input_img.shape[0],
    x_range=(0, 10), y_range=(0, 10),
    tools="hover,pan,reset",
    toolbar_location='above')
p.image_rgba(source=source, image='image', x='start_x', y='start_y', dw='width', dh='height', view=view)

#%%

from bokeh.io import show
from bokeh.models import Slider

slider = Slider(start=0, end=2, value=1, step=1, title="Stuff")
slider.js_on_change("value", CustomJS(code="""
    console.log('slider: value=' + this.value, this.toString())
"""))

#%%

# Make layout & show
from bokeh.plotting import output_file
from bokeh.layouts import column

output_file('testout.html')

right_col = column([filepicker, button])
left_col = column([p, slider])
layout = layouts.GridBox( children=[
    (left_col, 0, 0),
    (right_col, 0, 1)
])

show(layout)
# %%
