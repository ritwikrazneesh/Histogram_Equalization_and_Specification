#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


import rasterio
from rasterio.plot import show
import numpy as np
import pandas as pd
import math
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[3]:


def freq_calc( array, band ):
    pixels = array.shape[1]*array.shape[2]
    freq_array = [0]*256
    for i in range(0,array.shape[2]):
        for j in range(0, array.shape[1]):
            freq_array[ array[band][j][i] ] += 1/pixels
    return freq_array


# In[4]:


def upload_image():
    while True:
        try:
            # Prompt the user to enter the image path
            file_path = input("Please provide the path of the image: ")

            if file_path == "exit" :
                return None
            # Try opening the image directly from the file path
            tci = rasterio.open(file_path)
            #img.verify()  # Check if it's a valid image
            
            print("Image uploaded successfully!")
            #img = Image.open(file_path)  # Re-open to work with the image
            #img.show()  # Display the image
            return tci

        except (IOError, SyntaxError) as e:
            # If an error occurs, it means the file is not a valid image
            print("The file is not a valid image. Please try again.")


# In[5]:


tci = upload_image()


# 1 = Costal </br>
# 2 = Blue </br>
# 3 = Green </br>
# 4 = Red </br>
# 5 = NIR </br>
# 6 = SWIR1 </br>
# 7 = SWIR2 </br>
#  </br>
# RGB

# In[7]:


red = int( input("Which band to display as Red : ") )
green = int( input("Which band to display as Green : ") )
blue = int( input("Which band to display as Blue : ") )


# In[8]:


show((tci, [red, green, blue]), adjust='linear');


# In[9]:


high_img = upload_image()
show(high_img);


# In[10]:


t = tci.read([red, green, blue])
t = (t*(255/65535)).astype('uint8')
t2 = high_img.read([1,2,3])


# In[ ]:





# In[ ]:





# In[11]:


Red_freq = freq_calc( t, 0 );
Red_high_freq = freq_calc( t2, 0 );


# In[12]:


fig,ax = plt.subplots( ncols = 2, figsize = (15,5) )

ax[0].bar(range(0,256), Red_freq);
ax[1].bar(range(0,256), Red_high_freq);


# In[13]:


Red_cum_freq = [ Red_freq[0] ]
for i in range( 1, 256 ) :
    Red_cum_freq.append( Red_cum_freq[i-1]+Red_freq[i] )

Red_high_cum_freq = [ Red_high_freq[0] ]
for i in range( 1, 256 ) :
    Red_high_cum_freq.append( Red_high_cum_freq[i-1]+Red_high_freq[i] )


# In[14]:


fig,ax = plt.subplots( ncols = 2, figsize = (15,5) )

ax[0].bar(range(0,256), Red_cum_freq);
ax[1].bar(range(0,256), Red_high_cum_freq);


# In[15]:


i_low = 0
i_high = 0
Red_new_pixels = []

while i_low < 256 :
    if  i_high == 255 :
        Red_new_pixels.append(i_high)
        i_low += 1
    else :
        if ( ( Red_cum_freq[i_low] < Red_high_cum_freq[i_high+1] ) ) :
            Red_new_pixels.append(i_high)
            i_low += 1
        else :
            i_high += 1


# In[16]:


for i in range(0,t.shape[2]):
    for j in range( 0, t.shape[1] ):
        t[0][j][i] = Red_new_pixels[ t[0][j][i] ]


# In[17]:


Red_freq_new = freq_calc( t, 0 );


# In[18]:


fig,ax = plt.subplots( ncols = 2, figsize = (15,5) )
plt.title(f"Histogram of Band {red}")
ax[0].bar(range(0,256), Red_freq_new);
ax[1].bar(range(0,256), Red_high_freq);


# In[ ]:





# In[ ]:





# In[19]:


Green_freq = freq_calc( t, 1 );
Green_high_freq = freq_calc( t2, 1 );


# In[20]:


fig,ax = plt.subplots( ncols = 2, figsize = (15,5) )

ax[0].bar(range(0,256), Green_freq);
ax[1].bar(range(0,256), Green_high_freq);


# In[21]:


Green_cum_freq = [ Green_freq[0] ]
for i in range( 1, 256 ) :
    Green_cum_freq.append( Green_cum_freq[i-1]+Green_freq[i] )

Green_high_cum_freq = [ Green_high_freq[0] ]
for i in range( 1, 256 ) :
    Green_high_cum_freq.append( Green_high_cum_freq[i-1]+Green_high_freq[i] )


# In[22]:


fig,ax = plt.subplots( ncols = 2, figsize = (15,5) )

ax[0].bar(range(0,256), Green_cum_freq);
ax[1].bar(range(0,256), Green_high_cum_freq);


# In[23]:


i_low = 0
i_high = 0
Green_new_pixels = []

while i_low < 256 :
    if  i_high == 255 :
        Green_new_pixels.append(i_high)
        i_low += 1
    else :
        if ( ( Green_cum_freq[i_low] < Green_high_cum_freq[i_high+1] ) ) :
            Green_new_pixels.append(i_high)
            i_low += 1
        else :
            i_high += 1


# In[24]:


for i in range(0,t.shape[2]):
    for j in range( 0, t.shape[1] ):
        t[1][j][i] = Green_new_pixels[ t[1][j][i] ]


# In[25]:


Green_freq_new = freq_calc( t, 1 );


# In[26]:


fig,ax = plt.subplots( ncols = 2, figsize = (15,5) )

ax[0].bar(range(0,256), Green_freq_new);
ax[1].bar(range(0,256), Green_high_freq);


# In[ ]:





# In[ ]:





# In[27]:


Blue_freq = freq_calc( t, 2 );
Blue_high_freq = freq_calc( t2, 2 );


# In[28]:


fig,ax = plt.subplots( ncols = 2, figsize = (15,5) )

ax[0].bar(range(0,256), Blue_freq);
ax[1].bar(range(0,256), Blue_high_freq);


# In[29]:


Blue_cum_freq = [ Blue_freq[0] ]
for i in range( 1, 256 ) :
    Blue_cum_freq.append( Blue_cum_freq[i-1] + Blue_freq[i] )

Blue_high_cum_freq = [ Blue_high_freq[0] ]
for i in range( 1, 256 ) :
    Blue_high_cum_freq.append( Blue_high_cum_freq[i-1] + Blue_high_freq[i] )


# In[30]:


fig,ax = plt.subplots( ncols = 2, figsize = (15,5) )

ax[0].bar(range(0,256), Blue_cum_freq);
ax[1].bar(range(0,256), Blue_high_cum_freq);


# In[31]:


i_low = 0
i_high = 0
Blue_new_pixels = []

while i_low < 256 :
    if  i_high == 255 :
        Blue_new_pixels.append(i_high)
        i_low += 1
    else :
        if ( ( Blue_cum_freq[i_low] < Blue_high_cum_freq[i_high+1] ) ) :
            Blue_new_pixels.append(i_high)
            i_low += 1
        else :
            i_high += 1


# In[32]:


for i in range(0,t.shape[2]):
    for j in range( 0, t.shape[1] ):
        t[2][j][i] = Blue_new_pixels[ t[2][j][i] ]


# In[33]:


Blue_freq_new = freq_calc( t, 2 );


# In[34]:


fig,ax = plt.subplots( ncols = 2, figsize = (15,5) )

ax[0].bar(range(0,256), Blue_freq_new);
ax[1].bar(range(0,256), Blue_high_freq);


# In[ ]:





# -------
# </br></br></br></br>

# In[36]:


fig, ax = plt.subplots(figsize=(10, 10))
show((tci, [red, green, blue]), adjust='linear',ax=ax)
plt.show()


# In[37]:


fig, ax = plt.subplots(figsize=(10, 10))
show(t, adjust='linear', ax=ax)
plt.savefig("output_plot2.png", dpi=300, bbox_inches='tight')
plt.show()

