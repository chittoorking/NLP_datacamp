# We're almost ready to build a text classifier. But right now, all of our transcribed text data is in two lists, pre_purchase_text and post_purchase_text.

# To organize it better for building a text classifier as well as for future use, we'll put it together into a pandas DataFrame.

# To start we'll import pandas as pd then we'll create a post purchase dataframe, post_purchase_df using pd.DataFrame().

# We'll pass pd.DataFrame() a dictionary containing a "label" key with a value of "post_purchase" and a "text" key with a value of our post_purchase_text list.

# We'll do the same for pre_purchase_df except with pre_purchase_text.

# To have all the data in one place, we'll use pd.concat() and pass it the pre and post purchase DataFrames.

# Instructions
# Create post_purchase_df using the post_purchase_text list.
# Create pre_purchase_df using the pre_purchase_text list.
# Combine the two DataFrames using pd.concat().

import pandas as pd

# Make dataframes with the text
post_purchase_df = pd.DataFrame({"label": "post_purchase",
                                 "text": post_purchase_text})
pre_purchase_df = pd.DataFrame({"label": "pre_purchase",
                                "text": pre_purchase_text})

# Combine DataFrames
df = pd.concat([post_purchase_df, pre_purchase_df])

# Print the combined DataFrame
print(df.head())
