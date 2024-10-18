import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df=None                    
data=None

# Sidebar layout
st.sidebar.title("EDA Explorer")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=['csv'])
st.sidebar.markdown("### Check characteristics")
check_attributes = st.sidebar.checkbox("Check attributes")
st.sidebar.markdown("### Print first n rows")
head = st.sidebar.checkbox("Head")
st.sidebar.markdown("### Print last n rows")
tail = st.sidebar.checkbox("Tail")
st.sidebar.markdown("### Select desired rows or columns")
slicing = st.sidebar.checkbox("Slicing")
sample = st.sidebar.checkbox("Sample")
filter_ = st.sidebar.checkbox("Filter")
queen = st.sidebar.checkbox("Queen")
take = st.sidebar.checkbox("Take")
truncate = st.sidebar.checkbox("Truncate")
st.sidebar.markdown("### Change dtypes for a column")
astype = st.sidebar.checkbox("astype")
select_dtypes = st.sidebar.checkbox("select_dtypes")
st.sidebar.markdown("### Check for missing values and handle it")
isna = st.sidebar.checkbox("ISNA")
bfill = st.sidebar.checkbox("bfill")
ffill = st.sidebar.checkbox("ffill")
replace = st.sidebar.checkbox("replace")
st.sidebar.markdown("### Apply aggregate functions")
agg = st.sidebar.checkbox("agg")
aggregate = st.sidebar.checkbox("aggregate")
st.sidebar.markdown("### Descriptive statistics and info")
describe = st.sidebar.checkbox("describe")
info = st.sidebar.checkbox("info")
st.sidebar.markdown("### Apply statistics")
mean = st.sidebar.checkbox("Mean")
median = st.sidebar.checkbox("Median")
mode = st.sidebar.checkbox("Mode")
var = st.sidebar.checkbox("Var")
covar = st.sidebar.checkbox("Covar")
std = st.sidebar.checkbox("Std")
st.sidebar.markdown("### Plot")
line_plot = st.sidebar.checkbox("Line Plot")
scatter_plot = st.sidebar.checkbox("Scatter Plot")
box_plot = st.sidebar.checkbox("Box Plot")
histogram = st.sidebar.checkbox("Histogram")
pie_chart = st.sidebar.checkbox("Pie Chart")
_3d_plot = st.sidebar.checkbox("3D Plot")
xkcd_mode = st.sidebar.checkbox("Activate XKCD Mode")
st.sidebar.markdown("### Perofrm binary operations")
add=st.sidebar.checkbox("add")
sub=st.sidebar.checkbox("sub")
mul=st.sidebar.checkbox("mul")
div=st.sidebar.checkbox("div")
truediv=st.sidebar.checkbox("truediv")
floordiv=st.sidebar.checkbox("floordiv")
mod=st.sidebar.checkbox("mod")
pow_=st.sidebar.checkbox("pow")
dot=st.sidebar.checkbox("dot")

st.title("EDA Explorer Dashboard")
col1,col2=st.columns([1,3])

count=1

def represent(data):
    if st.checkbox("Represent it in original form"):
        st.text(data)
    if st.checkbox("Represent it in tabular form"):
        st.table(data)
    if st.checkbox("Represent it in dynamic data frame form"):
        st.dataframe(data)
def Condition(data,df):
    Value=st.radio("Do yo want to continue with this data",["yes","No"],index=1)
    if Value == "Yes":
        df=data
        st.success("Your data is updated")
        st.ballons()
    if Value == "No":
        st.success("Don't Worry, Your Data Is Preserved")
        st.balloons()
    
    

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)

if check_attributes:
    with col1:
        index=st.checkbox("index")
        columns=st.checkbox("columns")
        dtypes=st.checkbox("dtypes")
        info=st.checkbox("infoo")
        select_dtypes=st.checkbox("select_dtypess")
        values=st.checkbox("values")
        axes=st.checkbox("axes")
        ndim=st.checkbox("ndim")
        size=st.checkbox("size")
        shape=st.checkbox("shape")
        memory_usage=st.checkbox("memory_usagee")
        empty=st.checkbox("empty")
        set_flags=st.checkbox("set_flags")
    with col2:
        if index:
            data=df.index
            represent(data)
        if columns:
            data=df.columns
            represent(data)
        if dtypes:
            data=df.dtypes
            represent(data)
        if info:
            data=df.info()
            represent(data)
        if select_dtypes:
            data=df.select_dtypes()
            represent(data)
        if values:
            data=df.values
            represent(data)
        if axes:
            data=df.axes
            represent(data)
        if ndim:
            data=df.ndim
            represent(data)
        if size:
            data=df.size
            represent(data)
        if shape:
            data=df.shape
            represent(data)
        if memory_usage:
            data=df.memory_usage()
            represent(data)
        if empty:
            data=df.empty
            represent(data)
        if set_flags:
            data=df.set_flags
            represent(data)
if head:
    n = st.slider("Number of rows to display", min_value=1, max_value=len(df), value=5)
    data=df.head(n)
    represent(data)
if tail:
    n = st.slider("Number of rows to display", min_value=1, max_value=len(df), value=5)
    data=df.tail(n)
    represent(data)
if slicing:
    a=b=None
    with col1:
        a=st.checkbox("Select rows and colums based on labels")
        b=st.checkbox("Select rows and colums based on indexes")
    if a:
        with col2:
            start_row=st.selectbox("Select the start row",df.index)
            end_row=st.selectbox("Select the end row",df.index)
            start_column=st.selectbox("Select the start column",df.columns)
            end_column=st.selectbox("Select the end column",df.columns)
            if start_row and end_row and start_column and end_column:
                data=df.loc[start_row:end_row,start_column:end_column]
                represent(data)
                Condition(data,df)
    if b:
        with col2:
            start_row=st.selectbox("Select the index for a start row",range(len(df.index)))
            end_row=st.selectbox("Select the index for a end row",range(len(df.index)))
            start_column=st.selectbox("Select the index for a start column",range(len(df.columns)))
            end_column=st.selectbox("Select the end column",range(len(df.columns)))
            if start_row and end_row and start_column and end_column:
                data=df.iloc[int(start_row):int(end_row),int(start_column):int(end_column)]
                represent(data)
                Condition(data,df)                         
if sample:
    number=fraction=replace=None
    with col1:
        number=st.number_input("Enter the number of samples do you want")
        fraction=st.number_input("Enter the fraction of samples do you need")
        replace=st.radio("Do you wat to include dulpicate rows in your output",["yes","No"],index=1)
    with col2:
        if number or fraction:
            if number and fraction:
                st.warnig("You can select either number of samples or fraction of samles")
            if number:
                if replace == "yes":
                    data=df.sample(n=int(number),replace=True)
                if replace == "No":
                    data=df.sample(n=int(number),replace=False)
            if fraction:
                if replace == "yes":
                    data=df.sample(frac=fraction,replace=True)
                if replace == "No":
                    data=df.sample(frac,relace=False)
            represent(data)
            Condition(data,df)
            

if filter_:
    with col1:
        axis=st.radio("Do you want to apply axis to columns",["yes","no"],index=1)
        like=st.text_input("Enter the pattern that you want to see in output")
        regex=st.text_input("Enter the valid expression to filter the data frame")
    with col2:
        if like or regex:
            if like and regex:
                st.warning("You can't apply both like and regex at once")
            if like:
                if axis=="yes":
                    data=df.filter(like=like,axis="columns")
                if axis=="no":
                    data=df.filter(like=like,axis="index")
            if regex:
                if axis=="no":
                    data=df.filter(regex=regex)
                if axis=="yes":
                    data=df.filter(regex=regex,axis="columns")
        represent(data)

if queen:
    with col1:
        axis=st.radio("Do you want to apply axis to columns",["yes","no"],index=1)
        exper=st.text_input("Enter the condition")
        if exper:
            if axis=="yes":
                data=df.query(cond=exper,axis=1)
            if axis=="no":
                data=df.query(cond=exper,axis=0)
    with col2:
        represent(data)
        Condition(data,df)
            
if take:
    with col1:
        axis=st.radio("Do you want to apply axis to columns",["yes","no"],index=1)
        indices=st.text_input("Enter the list of indices")
        values=indices.split(",")
        numeric=[x for x in values]
        for i in range(len(numeric)):
            numeric[i]=int(numeric[i])
        if indices:
            if axis=="yes":
                data=df.take(numeric,axis=1)
            if axis=="no":
                data=df.take(numeric)
    with col2:
        represent(data)
        Condition(data,df)
        

if truncate:
    with col1:
        axis=st.radio("Do you want to apply axis to columns",["yes","no"],index=1)
        before=st.text_input("Enter the index for the starting row/column that you wanted to include in the output(befor)")
        after=st.text_input("Enter the index for the last row/column that you wanted to include in the output(after)")
        if before and after:
            value1=int(before)
            value2=int(after)
            if axis=="yes":
                data=df.truncate(before=value1,after=value2,axis=1)
            if axis == "no":
                data=df.truncate(before=value1,after=value2)
    with col2:
        represent(data)
        Condition(data,df)
        
            

if astype:
    with col1:
        dictt={}
        columns=st.multiselect("select the columns that you want to change the dtype",df.columns)
        dtypes=st.multiselect("select the dtype that you want for the corresponding columns ",df.dtypes)
        if columns and dtypes:
            for i,j in columns,dtypes:
                dictt[i]=dtypes[j]
            data=df.astype(dictt)
    with col2:
        represent(data)
        Condition(data,df)
        

if select_dtypes:
    with col2:
        data=df.convert_dtypes()
        represent(data)
        Condition(data,df)
        
if isna:
    with col2:
        data=df.isna()
        represent(data)
        Condition(data,df)
        

if bfill:
    with col1:
        axis=st.radio("Do you want to apply it to the columns",["yes","no"],index=1)
        limit=st.text_input("Enter the limt values")
        if axis or limit:
            if axis and limit:
                if axis=="no":
                    data=df.bfill(limit=int(limit))
                if axis=="yes":
                    data=df.bfill(limit=int(limit),axis=1)
            if axis:
                if axis=="no":
                    data=df.bfill()
                if axis=="yes":
                    data=df.bfill(axis=1)
    with col2:
        represent(data)
        Condition(data,df)
            

if ffill:
    with col1:
        axis=st.radio("Do you want to apply it to the columns",["yes","no"],index=1)
        limit=st.text_input("Enter the limt values")
        if axis or limit:
            if axis and limit:
                if axis=="no":
                    data=df.ffill(limit=int(limit))
                if axis=="yes":
                    data=df.ffill(limit=int(limit),axis=1)
            if axis:
                if axis=="no":
                    data=df.ffill()
                if axis=="yes":
                    data=df.ffill(axis=1)
    with col2:
        represent(data)
        Condition(data,df)
        

if agg:
    with col1:
        new_list=[]
        column=st.multiselect("Select the columns that you want",df.columns)
        if column:
            columns=column
            for i in columns:
                value=st.text_input(f"Enter the list of functions that you wanted to apply on {i}")
                new_list.append(value.split(","))
            for i in range(len(columns)):
                dictt[columns[i]]=new_list[i]
            data=df.agg(dictt)
        with col2:
            represent(data)
            Condition(data,df)
           

if aggregate:
    with col1:
        new_list=[]
        column=st.multiselect("Select the columns that you want",df.columns)
        if column:
            columns=column
            for i in columns:
                value=st.text_input(f"Enter the list of functions that you wanted to apply on {i}")
                new_list.append(value.split(","))
            for i in range(len(columns)):
                dictt[columns[i]]=new_list[i]
            data=df.agg(dictt)
        with col2:
            represent(data)
            Condition(data,df)
        

if describe:
    with col2:
        data=df.describe()
        represent(data)
        

if info:
    data=df.info()
    with col2:
        represent(data)
        
if mean:
    with col1:
        axis=st.radio("Do you wan to apply it to columns",["yes","no"],index=1)
        dropna=st.radio("Do you want to drop nan values",["yes","no"],index=0)
        numeric_only=st.radio("Do you want to include numeric columns only",["yes","no"],index=1)
    with col2:
        if axis or dropna or ddof or numeric_only:
            if axis=="yes" or drop=="no"  or numeric_only=="yes":
                data=df.mean(axis=1,drop=False,numeric_only=True)
                repesent(data)
            else:
                data=df.mean()
                repesent(data)
    
        

if median:
    with col1:
        axis=st.radio("Do you wan to apply it to columns",["yes","no"],index=1)
        dropna=st.radio("Do you want to drop nan values",["yes","no"],index=0)
        numeric_only=st.radio("Do you want to include numeric columns only",["yes","no"],index=1)
    with col2:
        if axis or dropna or ddof or numeric_only:
            if axis=="yes" or drop=="no"  or numeric_only=="yes":
                data=df.median(axis=1,drop=False,numeric_only=True)
                repesent(data)
            else:
                data=df.median()
                repesent(data)
    
        

if mode:
    with col1:
        axis=st.radio("Do you wan to apply it to columns",["yes","no"],index=1)
        dropna=st.radio("Do you want to drop nan values",["yes","no"],index=0)
        numeric_only=st.radio("Do you want to include numeric columns only",["yes","no"],index=1)
    with col2:
        if axis or dropna or ddof or numeric_only:
            if axis=="yes" or dropna=="no"  or numeric_only=="yes":
                data=df.mode(axis=1,dropna=False,numeric_only=True)
                represent(data)
            else:
                data=df.mode()
                represent(data)
    

if var:
    with col1:
        axis=st.radio("Do you wan to apply it to columns",["yes","no"],index=1)
        skipna=st.radio("Do you want to include nan values",["yes","no"],index=1)
        ddof=st.number_input("Enter the ddof")
        numeric_only=st.radio("Do you want to include numeric columns only",["yes","no"],index=1)
    with col2:
        if axis or skipna or ddof or numeric_only:
            if axis=="yes" or skipna=="no"  or numeric_only=="yes":
                data=df.var(axis=1,skipna=False,ddof=ddof,numeric_only=True)
                repesent(data)
            else:
                data=df.var()
                repesent(data)
    
        

if covar:
    with col1:
        axis=st.radio("Do you wan to apply it to columns",["yes","no"],index=1)
        skipna=st.radio("Do you want to include nan values",["yes","no"],index=1)
        ddof=st.number_input("Enter the ddof")
        numeric_only=st.radio("Do you want to include numeric columns only",["yes","no"],index=1)
    with col2:
        if axis or skipna or ddof or numeric_only:
            if axis=="yes" or skipna=="no"  or numeric_only=="yes":
                data=df.cov(axis=1,skipna=False,ddof=ddof,numeric_only=True)
                repesent(data)
            else:
                data=df.cov()
                repesent(data)
    
        
if std:
    with col1:
        axis=st.radio("Do you wan to apply it to columns",["yes","no"],index=1)
        skipna=st.radio("Do you want to include nan values",["yes","no"],index=1)
        ddof=st.number_input("Enter the ddof")
        numeric_only=st.radio("Do you want to include numeric columns only",["yes","no"],index=1)
    with col2:
        if axis or skipna or ddof or numeric_only:
            if axis=="yes" or skipna=="no"  or numeric_only=="yes":
                data=df.std(axis=1,skipna=False,ddof=ddof,numeric_only=True)
                repesent(data)
            else:
                data=df.std()
                repesent(data)
colors = ['black', 'red', 'green', 'blue', 'purple', 'orange', 'yellow', 'brown', 'gray', 'pink']
weights = ['normal', 'bold', 'heavy', 'light', 'ultrabold', 'ultralight']
styles = ['normal', 'italic', 'oblique']
face_colors = ['white', 'lightgray', 'gray', 'lightblue', 'lightgreen', 'lightyellow']
edge_colors = ['black', 'red', 'green', 'blue', 'purple', 'orange']
box_styles = ['round', 'round4', 'roundtooth', 'square', 'pad=0.3', 'round,pad=0.5']
decorations = ['none', 'underline', 'overline', 'line-through', 'underline overline','underline line-through', 'overline line-through', 'underline overline line-through']    
        

if line_plot:
    with col1:
        column1 = st.selectbox("Enter the column for X-axis", df.columns)
        column2 = st.selectbox("Enter the column for Y-axis", df.columns)
        xlabel = st.text_input("Enter x label", "X-axis")
        ylabel = st.text_input("Enter y label", "Y-axis")
        title = st.text_input("Enter title", "Line Plot")
        select_marker = st.selectbox("Select the marker style", ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_'])
        line_style = st.selectbox("Select the line style", ['-', '--', '-.', ':'])
        st.subheader("Select the properties")
        components = st.radio("Select one to change the properties", ["title", "xlabel", "ylabel", "marker", "text"], index=1)
        plot = st.button("Plot")
    with col2:
        if column1 and column2:
            if xlabel:
                plt.xlabel(xlabel)
            if ylabel:
                plt.xlabel(ylabel)
            if title:
                plt.title(title)
            if select_marker:
                plt.plot.marker = select_marker
            if line_style:
                selectcolor = st.selectbox("Select line color", colors)
                if selectcolor:
                    plt.plot.linestyle = line_style
            if components:
                with col1:
                    color = st.selectbox("Select the color you want", colors)
                    weight = st.selectbox("Select the weight you want", weights)
                    style = st.selectbox("Select the style you want", styles)
                    decoration = st.selectbox("Select the decoration you want", decorations)
                    facecolor = st.selectbox("Select the facecolor you want", face_colors)
                    edgecolor = st.selectbox("Select the edgecolor you want", edge_colors)
                    boxstyle = st.selectbox("Select the boxstyle you want", box_styles)
                    mfc = st.selectbox("Select the mfc you want", colors)
                    mec = st.selectbox("Select the mec you want", colors)
                with col2:
                    if components == "text":
                        if color and weight and style:
                            plt.text(3, 4, "Sample Text", color=color, weight=weight, style=style)
                        if color and weight and style and decoration and facecolor and edgecolor and boxstyle:
                            plt.text(3, 4, "Sample Text", color=color, weight=weight, style=style)
                    if components == "xlabel":
                        if color and weight and style:
                            plt.xlabel(xlabel, color=color, weight=weight, style=style)
                        if color and weight and style and facecolor and edgecolor and boxstyle:
                            plt.xlabel(xlabel, color=color, weight=weight, style=style)
                    if components == "ylabel":
                        if color and weight and style:
                            plt.ylabel(ylabel, color=color, weight=weight, style=style)
                        if color and weight and style and facecolor and edgecolor and boxstyle:
                            plt.ylabel(ylabel, color=color, weight=weight, style=style)
                    if components == "marker":
                        if mfc:
                            plt.plot.mfc = mfc
                        if mec:
                            plt.plot.mec = mec
                    if components == "title":
                        if color and weight and style :
                            plt.title(title, color=color, weight=weight, style=style)
                        if color and weight and style and decoration and facecolor and edgecolor and boxstyle:
                            plt.title(title, color=color, weight=weight, style=style)
        if plot:
            with col2:
                plt.plot(df[column1], df[column2])
                st.pyplot()                         
if scatter_plot:
    with col1:
        column1 = st.selectbox("Enter the column for X-axis", df.columns)
        column2 = st.selectbox("Enter the column for Y-axis", df.columns)
        xlabel = st.text_input("Enter x label", "X-axis")
        ylabel = st.text_input("Enter y label", "Y-axis")
        title = st.text_input("Enter title", "Scatter Plot")
        select_marker = st.selectbox("Select the marker style", ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_'])
        line_style = st.selectbox("Select the marker edge style", ['-', '--', '-.', ':'])
    with col2:
        st.subheader("Select the properties")
        components = st.radio("Select one to change the properties", ["title", "xlabel", "ylabel", "marker", "text"], index=1)
        plot = st.button("Plot")
        if components:
            st.subheader(f"Adjust {components} properties")
            color = st.selectbox("Select the color you want", colors)
            weight = st.selectbox("Select the weight you want", weights)
            style = st.selectbox("Select the style you want", styles)
            decoration = st.selectbox("Select the decoration you want", decorations)
            facecolor = st.selectbox("Select the facecolor you want", face_colors)
            edgecolor = st.selectbox("Select the edgecolor you want", edge_colors)
            boxstyle = st.selectbox("Select the boxstyle you want", box_styles)
            mfc = st.selectbox("Select the mfc you want", colors)
            mec = st.selectbox("Select the mec you want", colors)
        if plot:
            with col2:
                plt.figure()            
                if components == "xlabel":
                    plt.xlabel(xlabel, color=color, weight=weight, style=style)
                elif components == "ylabel":
                    plt.ylabel(ylabel, color=color, weight=weight, style=style)
                elif components == "title":
                    plt.title(title, color=color, weight=weight, style=style)
                elif components == "text":
                    plt.text(3, 4, "Sample Text", color=color, weight=weight, style=style, decoration=decoration, bbox=dict(facecolor=facecolor, edgecolor=edgecolor, boxstyle=boxstyle))
                elif components == "marker":
                    plt.scatter(df[column1], df[column2], marker=select_marker, edgecolor=mec, facecolor=mfc, linestyle=line_style)
                st.pyplot()                    
if box_plot:
    with col1:
        column1 = st.selectbox("Select the column for Box Plot", df.columns)
        title = st.text_input("Enter title", "Box Plot")
        color = st.selectbox("Select the color for the box", colors)
        plot = st.button("Plot")
    with col2:
        if plot and column1:
            plt.figure()
            plt.boxplot(df[column1], patch_artist=True, boxprops=dict(facecolor=color))
            plt.title(title)
            st.pyplot()
if histogram:
    with col1:
        column1 = st.selectbox("Select the column for Histogram", df.columns)
        title = st.text_input("Enter title", "Histogram")
        color = st.selectbox("Select the color for bars", colors)
        plot = st.button("Plot")
    with col2:
        if plot and column1:
            plt.figure()
            plt.hist(df[column1], color=color, bins=20)
            plt.title(title)
            st.pyplot()
if pie_chart:
    with col1:
        column1 = st.selectbox("Select the column for Pie Chart", df.columns)
        title = st.text_input("Enter title", "Pie Chart")
        colors_pie = st.multiselect("Select colors for each section", colors)
        explode = st.checkbox("Explode slices")
        plot = st.button("Plot")
    with col2:
        if plot and column1:
            plt.figure()
            plt.pie(df[column1].value_counts(), labels=df[column1].unique(), autopct='%1.1f%%', colors=colors_pie, explode=explode)
            plt.title(title)
            st.pyplot()
if _3d_plot:
    st.write("Coming soon...")
if xkcd_mode:
    st.write("Coming soon...")

if add:
    with col1:
        axis=st.radio("Do you want to apply this to rows",["yes","no"],index=1)
        fillvalue=st.number_input("Enter the value for nan values",value=1)
        other=st.number_input("Enter the other value")
        with col2:
            if axis or fillvalue:
                if axis=="yes" and fillvalue:
                    data=df.add(axis=0,fill_value=fillvalue,other=str(other))
                if axis=="no" and fillvalue:
                    data=df.add(fill_value=fillvalue,other=str(other))
                represent(data)
                check(data)
if sub:
    with col1:
        axis=st.radio("Do you want to apply this to rows",["yes","no"],index=1)
        fillvalue=st.number_input("Enter the value for nan values",value=1)
        other=st.number_input("Enter the other value")
        with col2:
            if axis or fillvalue:
                if axis=="yes" and fillvalue:
                    data=df.sub(axis=0,fill_value=fillvalue,other=other)
                if axis=="no" and fillvalue:
                    data=df.sub(fill_value=fillvalue,other=other)
                represent(data)
if mul:
    with col1:
        axis=st.radio("Do you want to apply this to rows",["yes","no"],index=1)
        fillvalue=st.number_input("Enter the value for nan values",value=1)
        other=st.number_input("Enter the other value")
        with col2:
            if axis or fillvalue:
                if axis=="yes" and fillvalue:
                    data=df.mul(axis=0,fill_value=fillvalue,other=other)
                if axis=="no" and fillvalue:
                    data=df.mul(fill_value=fillvalue,other=other)
                represent(data)
if div:
    with col1:
        axis=st.radio("Do you want to apply this to rows",["yes","no"],index=1)
        fillvalue=st.number_input("Enter the value for nan values",value=1)
        other=st.number_input("Enter the other value")
        with col2:
            if axis or fillvalue:
                if axis=="yes" and fillvalue:
                    data=df.div(axis=0,fill_value=fillvalue,other=other)
                if axis=="no" and fillvalue:
                    data=df.div(fill_value=fillvalue,other=other)
                represent(data)
if truediv:
    with col1:
        axis=st.radio("Do you want to apply this to rows",["yes","no"],index=1)
        fillvalue=st.number_input("Enter the value for nan values",value=1)
        other=st.number_input("Enter the other value")
        with col2:
            if axis or fillvalue:
                if axis=="yes" and fillvalue:
                    data=df.truediv(axis=0,fill_value=fillvalue,other=other)
                if axis=="no" and fillvalue:
                    data=df.truediv(fill_value=fillvalue,other=other)
                represent(data)
if floordiv:
    with col1:
        axis=st.radio("Do you want to apply this to rows",["yes","no"],index=1)
        fillvalue=st.number_input("Enter the value for nan values",value=1)
        other=st.number_input("Enter the other value")
        with col2:
            if axis or fillvalue:
                if axis=="yes" and fillvalue:
                    data=df.floordiv(axis=0,fill_value=fillvalue,other=other)
                if axis=="no" and fillvalue:
                    data=df.floordiv(fill_value=fillvalue,other=other)
                represent(data)
if mod:
    with col1:
        axis=st.radio("Do you want to apply this to rows",["yes","no"],index=1)
        fillvalue=st.number_input("Enter the value for nan values",value=1)
        other=st.number_input("Enter the other value")
        with col2:
            if axis or fillvalue:
                if axis=="yes" and fillvalue:
                    data=df.mod(axis=0,fill_value=fillvalue,other=other)
                if axis=="no" and fillvalue:
                    data=df.mod(fill_value=fillvalue,other=other)
                represent(data)
if pow_:
    with col1:
        axis=st.radio("Do you want to apply this to rows",["yes","no"],index=1)
        fillvalue=st.number_input("Enter the value for nan values",value=1)
        other=st.number_input("Enter the other value")
        with col2:
            if axis or fillvalue:
                if axis=="yes" and fillvalue:
                    data=df.pow(axis=0,fill_value=fillvalue,other=other)
                if axis=="no" and fillvalue:
                    data=df.pow(fill_value=fillvalue,other=other)
                represent(data)
if dot:
    with col1:
        other=st.number_input("Enter the other value")
        with col2:
            data=df.dot(other=other)
            represent(data)




    
