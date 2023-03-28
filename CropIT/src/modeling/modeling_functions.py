def error_analysis(y_test, y_pred):
    """Generated true vs. predicted values and residual scatter plot for models
    Args:
        y_test (array): true values for y_test
        y_pred_test (array): predicted values of model for y_test
    """
    # calculate residuals
    residuals = y_test - y_pred
    # plot real vs. predicted values
    fig, ax = plt.subplots(1,2, figsize=(15, 5))
    plt.subplots_adjust(right=1)
    plt.suptitle('Error Analysis')
    ax[0].scatter(y_pred, y_test, color="blue", alpha=0.7)
    ax[0].plot([-400, 350], [-400, 350], color="#193251")
    ax[0].set_title("True vs. predicted values", fontsize=16)
    ax[0].set_xlabel("predicted values")
    ax[0].set_ylabel("true values")
    ax[0].set_xlim((y_pred.min()-5), (y_pred.max()+5))
    ax[0].set_ylim((y_test.min()-10), (y_test.max()+10))
    ax[1].scatter(y_pred, residuals, color="blue", alpha=0.7)
    ax[1].plot([-400, 350], [0,0], color="#193251")
    ax[1].set_title("Residual Scatter Plot", fontsize=16)
    ax[1].set_xlabel("predicted values")
    ax[1].set_ylabel("residuals")
    ax[1].set_xlim((y_pred.min()-5), (y_pred.max()+5))
    ax[1].set_ylim((residuals.min()-5), (residuals.max()+5));

def get_run_logdir():
    '''
    Function for creating a new folder for each run. Use prior to running the neural network models.
    Output is used in the get_callbacks function.
    Output:
    path to the directory
    '''
    now = datetime.now()
    run_id = now.strftime('%Y-%m-%d %H:%M:%S')
    return os.path.join(root_logdir, run_id)

# return [list of your callbacks]
def get_callbacks(name):
    '''
    Function to return a list of different stages of the training loop. Puts the name to the model.
    Arguments:
    name: enter the identifying name
    Output: 
    Directory for the TensorBoard.
    '''
    return tf.keras.callbacks.TensorBoard(run_logdir+name, histogram_freq=1)

def model_compile_and_fit(model, name, optimizer=None, max_epochs=EPOCHS):
    '''
    Function to compile and fit your neural network
    Arguments:
    model: previously defined model (i.e. tf.keras.Sequential())
    name: model name (for the get_callbacks function)
    optimizer: Default None, can use others i.e. adam etc.
    max_epochs: maximal number of cycles the training data set takes around the algorithm.
    Output:
    history of the model fit (can be used for plotting)
    '''
    # model.compile
    model.compile(optimizer = 'adam', loss = 'mae', metrics = ['mse'])
    
    # model.fit
    history = model.fit(X_tf_train, y_train, batch_size = BATCH_SIZE, validation_split=N_VAL, epochs = max_epochs, callbacks=get_callbacks(name))
    
    # return results
    return history
# plotting function for MSE
def plot_metric(history):
    '''
    Function for plotting the mean squared error (MSE) of a model
    Argument:
    history: Output of fitted model
    Output:
    plot of MSE per epoch
    '''
    plt.plot(history.history['mse'])
    plt.plot(history.history['val_mse'])
    plt.ylim([0, 20])
    plt.title('Model MSE')
    plt.ylabel('MSE')
    plt.xlabel('Epoch')
    plt.legend(['train', 'validation'], loc='upper right')
    plt.show()

# plotting function for loss
def plot_loss(history):
    '''
    Function for plotting the loss of a model
    Argument:
    history: Output of fitted model
    Output:
    plot of loss per epoch
    '''
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.ylim([0, 5])
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.legend()
    plt.grid(True)