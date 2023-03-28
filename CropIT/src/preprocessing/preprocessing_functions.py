import pandas as pd
def column_rename(dataframe, old_colname, new_colname):
    ''' 
    rename a specific column in a dataframe. Enter the columnnames as strings.
    Arguments:
    dataframe: the dataframe with a column to be renamed
    old_colname: the column to be renamed
    new_colname: the name the column is supposed to have
    '''
    dataframe.rename(columns={old_colname: new_colname}, inplace=True)
    return dataframe

def drop_rows(dataframe, column, row_drop_list):
    ''' 
    Function to drop specific rows according to location. Prepare a list of row-conditions to be dropped beforehand.
    Arguments:
    dataframe: dataframe that needs to be modified
    columns: column which contains the instances to be dropped, enter as a string
    row_drop_list: list of instances to be dropped
    '''
    dataframe.drop(
        dataframe[
        dataframe[column]
        .isin(row_drop_list)]
        .index, 
        axis=0, 
        inplace=True)
    return dataframe

def drop_columns(dataframe, column_drop_list):
    ''' 
    Function to drop specific rows according to location. Prepare a list of row-conditions to be dropped beforehand.
    Arguments:
    dataframe: dataframe that needs to be modified
    columns: column which contains the instances to be dropped, enter as a string
    column_drop_list: list of instances to be dropped
    '''
    dataframe.drop(column_drop_list, axis=1, inplace=True)
    return dataframe

def merge_frames(dataframe_1, dataframe_2, merge_column, how='outer'):
    ''' 
    Function to merge two dataframes on a common column. Enter merge_column and how as a string.
    Arguments:
    dataframe_1: first dataframe to merge
    dataframe_2: second dataframe to merge
    merge_column: column on which to merge
    how: type of merge (outer, inner, left, etc.)
    Output:
    new dataframe called merge_frame
    '''
    merge_frame = dataframe_1.merge(dataframe_2,
                                  on=merge_column,
                                  how=how)
    return merge_frame

def make_datetime(dataframe, column):
    ''' 
    Function to turn object columns into datetime format. Enter column as a string.
    Arguments:
    dataframe: the dataframe containing the column to be turned into datetime format
    column: column to be changed to datetime format
    Output:
    dataframe containing column as new format
    '''
    dataframe[column] = pd.to_datetime(dataframe[column], yearfirst=True, format="%Y-%m-%d %H:%M:%S")
    return dataframe

def combine_datetime(dataframe, column_year, column_month, column_day, new_col):
    ''' 
    Function to compile separate year, month and day columns into one date column in datetime format. Enter columns as a string.
    Arguments:
    dataframe: the dataframe containing the column to be turned into datetime format
    column_year: column containing the year
    column_month: column containing the month
    column_day: column containing the day
    new_col: name of the new column
    Output:
    dataframe containing a new combined date column in the format year-month-day)
    '''
    dataframe[new_col] = pd.to_datetime(dict(year=dataframe[column_year],
                                       month=dataframe[column_month],
                                       day=dataframe[column_day]))
    return dataframe

def column_transform(dataframe, new_col, grouping, col_transform, how='mean', drop_old=True):
    ''' 
    Function to transform columns. It groups a dataframe according to given columns and calculates the mean values of given columns.
    how argument needs to be given as string. After transformation, the old columns are dropped. 
    If columns do not have a new name, drop_old must be set to False!
    Arguments:
    dataframe: dataframe with which to work
    new_col: list of new column names (if they do not need to be changed, the col_transform list can be given here as well)
    grouping: list of columns according to which the dataframe needs to be grouped for calculations
    col_transform: columns to be transformed
    how: method of transformation. Default is mean, can also be sum.
    drop_old: Default as true. Drops the old columns out of the dataframe. If set to False, it keeps them in.
    Output:
    Dataframe with transformed values.
    '''
    count_new_col = 0
    count_old_col = 0
    for col in new_col:
        if count_new_col <= len(new_col):
            dataframe[new_col[count_new_col]] = dataframe.groupby(grouping)[col_transform[count_old_col]].transform(how)
            if drop_old==True:
                dataframe.drop([col_transform[count_old_col]], axis=1, inplace=True)
            count_new_col += 1
            count_old_col += 1
    dataframe.reset_index(inplace=True)
    dataframe.drop(['index'], axis=1, inplace=True)
    return dataframe

def pivot_frame(dataframe, index, column, values):
    '''
    Function to pivot a dataframe and flatten newly generated columns. Enter index and column as string.
    Arguments:
    dataframe = dataframe to pivot
    index = column on which the dataframe is supposed to be pivoted
    column = column or list of columns to be retained
    values = (previously defined) list of columns which are supposed to be sorted according to column entry
    Output:
    pivoted dataframe with flattened columns.
    '''
    dataframe = pd.pivot_table(dataframe, index=index, columns=[column], values=values)
    # flatten the multi-index columns
    dataframe.columns = ['_'.join(col) for col in dataframe.columns.values]
    # flatten all columns to one level
    dataframe.reset_index(inplace=True)
    return dataframe